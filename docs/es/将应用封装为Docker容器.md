# Empaquetar la aplicación como un contenedor Docker

Empaquetar la aplicación como un contenedor Docker facilita su implementación y gestión. A continuación se muestra un ejemplo que demuestra cómo empaquetar una aplicación Python como un contenedor Docker y ejecutarla utilizando Docker Compose.

## Plantilla básica

Para contenerizar una aplicación, primero asegúrese de tener Docker instalado. Luego, cree dos archivos en el directorio raíz de su aplicación Python: `Dockerfile` y `compose.yaml`. Estos archivos contendrán aproximadamente lo siguiente:

```Dockerfile title="Dockerfile"
# Establecer la imagen base como la imagen oficial de Python, la versión puede personalizarse
FROM python:3.9

# Establecer el directorio de trabajo como /app
WORKDIR /app

# Copiar los archivos de dependencias de la aplicación Python
COPY requirements.txt .

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los archivos de la aplicación desde el directorio actual al directorio dentro del contenedor
COPY . .

# Establecer el comando de ejecución predeterminado
CMD ["python", "app.py"]
```

```yaml title="compose.yaml"
version: "3"
services:
  app:
    build: .
```

En el archivo `compose.yaml`, se define un servicio llamado `app`. Mediante la instrucción `build: .`, se utiliza el archivo `Dockerfile` en el directorio `compose.yaml` para construir la imagen. Ejecute `docker compose up` en el directorio donde se encuentra `compose.yaml` para construir y ejecutar la aplicación.

## Ejemplo: Empaquetar una aplicación Python simple como un contenedor Docker

A continuación se muestra un ejemplo de una aplicación simple de "Hola Mundo" en Python que imprime "Hello World" en una página web:

```python title="app.py"
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
```

Si implementamos la aplicación Python de manera convencional, sin utilizar contenedores, tendríamos que instalar las dependencias primero. Para algunas dependencias que requieren compilación e instalación, esto puede generar errores, especialmente en entornos Windows, donde pueden faltar archivos de encabezado necesarios. Sin embargo, si la empaquetamos como un contenedor Docker, podemos ignorar las diferencias de entorno. Incluso si el host no tiene conexión a Internet, solo necesitamos copiar la imagen para implementarla. A continuación, se muestran los pasos para contenerizarla y implementarla utilizando Docker Compose.

Primero, cree un archivo llamado `Dockerfile` y agregue el siguiente contenido:

```Dockerfile title="Dockerfile"
# Establecer la imagen base como la imagen oficial de Python
FROM python:3.9

# Copiar los archivos de la aplicación
COPY . /app

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias
RUN pip install flask

# Exponer el puerto 8000 para acceder a la aplicación
EXPOSE 8000

# Iniciar la aplicación
CMD python ./app.py
```

Luego, en el mismo directorio, cree un archivo llamado `compose.yaml` y copie el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  helloworld-flask:
    build: .
    ports:
      - "8099:8000" # El puerto 8099 se puede personalizar
```

Ahora, abra una terminal, vaya al directorio que contiene los archivos `Dockerfile` y `compose.yaml`, y ejecute el siguiente comando para iniciar la aplicación:

```shell
docker compose up
```

Docker construirá la imagen y lanzará el contenedor. Puedes acceder a `http://localhost:8099` para ver el mensaje "Hello World". Siguiendo estos pasos, puedes contenerizar una aplicación simple de Python y desplegarla utilizando Docker Compose.

## Referencias y Agradecimientos

- [Containerizar una aplicación](https://docs.docker.com/get-started/02_our_app/)
- [Contenerizar una aplicación de Python en 3 minutos](https://cloud.tencent.com/developer/article/1752513)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.