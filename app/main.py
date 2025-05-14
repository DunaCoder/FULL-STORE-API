from fastapi import FastAPI, HTTPException
import json
from typing import List, Optional
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os


app = FastAPI()

# Obtener la ruta absoluta de la carpeta "imagenes"
imagenes_dir = Path(__file__).parent.parent / "imagenes"  # Si main.py está en app/

# Montar la carpeta de imágenes
app.mount("/imagenes", StaticFiles(directory=imagenes_dir), name="imagenes")

# Obtener el directorio actual del archivo
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "db.json")

with open(db_path, "r", encoding='utf-8') as f:
    data = json.load(f)
    db = data["productos"]  # <-- Extraer solo los productos

class Item(BaseModel):
    nombre: str
    precio: float
    descripcion: Optional[str] = None
    caracteristicas: List[str] = []
    stock: int
    categoria: str
    imagen: str

class ItemResponse(Item):
    id: int

@app.get("/productos/", response_model=List[ItemResponse])
def obtener_productos():
    return db

@app.get("/productos/{producto_id}", response_model=ItemResponse)
def obtener_producto(producto_id: int):
    for producto in db:
        if producto["id"] == producto_id:
            return producto
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.post("/productos/", response_model=ItemResponse)
def crear_producto(item: Item):
    # Generar nuevo ID
    nuevo_id = max(p["id"] for p in db) + 1 if db else 1
    nuevo_producto = {**item.dict(), "id": nuevo_id}
    
    db.append(nuevo_producto)
    guardar_datos()
    return nuevo_producto

@app.put("/productos/{producto_id}", response_model=ItemResponse)
def editar_producto(producto_id: int, item: Item):
    for i, producto in enumerate(db):
        if producto["id"] == producto_id:
            # Mantener el ID original y actualizar otros campos
            db[i] = {**item.dict(), "id": producto_id}
            guardar_datos()
            return db[i]
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):
    global db
    initial_length = len(db)
    db = [p for p in db if p["id"] != producto_id]
    
    if len(db) == initial_length:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    guardar_datos()
    return {"message": "Producto eliminado"}

def guardar_datos():
    with open(db_path, "w") as f:  # <-- Usa la ruta absoluta
        json.dump(db, f, indent=4, ensure_ascii=False)
# {
#     "nombre": "Producto X",
#     "precio": 28.99,
#     "descripcion": "Un producto propio"
# }