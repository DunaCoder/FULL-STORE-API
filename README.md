## Cómo Poner en Marcha la API

Sigue estos sencillos pasos para clonar el repositorio, instalar las dependencias y ejecutar la API en tu máquina local.

### 1\. Clonar el Repositorio

Primero, clona este repositorio a tu máquina local usando Git:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
```

Una vez clonado, navega al directorio de tu proyecto:

```bash
cd nombre_de_tu_repositorio
```

### 2\. Instalar Dependencias

Se recomienda usar un **entorno virtual** para gestionar las dependencias del proyecto. Si no tienes uno, puedes crearlo y activarlo así:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual (Windows)
.\venv\Scripts\activate

# Activar el entorno virtual (macOS/Linux)
source venv/bin/activate
```

Con el entorno virtual activado, instala todas las dependencias necesarias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3\. Ejecutar la API

Con las dependencias instaladas y el entorno virtual activado, puedes iniciar la API usando Uvicorn:

```bash
uvicorn app.app:app --reload
```

El parámetro `--reload` hará que el servidor se reinicie automáticamente cada vez que hagas cambios en el código, lo cual es muy útil durante el desarrollo.

### 4\. Acceder a la API

Si todo se ejecutó correctamente, la API estará disponible en tu navegador o en tu cliente API favorito (como Postman o Insomnia) en la siguiente dirección:

[enlace sospechoso eliminado]

Al acceder a esta URL, deberías ver el siguiente mensaje de bienvenida:

```json
{"message": "Bienvenido a la API de productos"}
```

-----

## Rutas Principales de la API

Aquí te dejamos las rutas principales que puedes utilizar:

  * **`GET /productos/`**: Obtiene una lista de todos los productos disponibles.
  * **`GET /productos/{id}`**: Obtiene los detalles de un producto específico. Por ejemplo, `http://127.0.0.1:8000/productos/3` para el producto con ID 3.
  * **`GET /proveedores/`**: Obtiene una lista de todos los proveedores.
  * **`GET /productos/proveedor/{id_proveedor}`**: Obtiene los productos asociados a un proveedor específico.
  * **`POST /productos/`**: Crea un nuevo producto (requiere un cuerpo de solicitud JSON).
  * **`PUT /productos/{id}`**: Actualiza un producto existente (requiere un cuerpo de solicitud JSON).
  * **`DELETE /productos/{id}`**: Elimina un producto específico.
