# Empaquetar una aplicación como contenedor Docker

Empaquetar una aplicación como contenedor Docker puede facilitar su implementación y gestión. A continuación, se muestra un ejemplo de cómo empaquetar una aplicación Python como contenedor Docker y ejecutarla utilizando Docker Compose.

## Plantilla básica

Para contenerizar una aplicación, primero asegúrate de tener Docker instalado. Luego, en el directorio raíz de tu aplicación Python, crea estos dos archivos: `Dockerfile` y `compose.yaml`, que contendrán lo siguiente:

```Dockerfile title="Dockerfile"
# Establecer la imagen base como la imagen oficial de Python, la versión puede ser personalizada
FROM python:3.9

# Establecer el directorio de trabajo como /app
WORKDIR /app

# Copiar los archivos de dependencias de la aplicación Python
COPY requirements.txt .

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los archivos de la aplicación, desde el directorio actual al directorio dentro del contenedor
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

En el archivo `compose.yaml`, se define un servicio llamado `app`. Con la instrucción `build: .`, se utilizará el archivo `Dockerfile` en el directorio actual para construir la imagen. Ejecuta `docker compose up` en el directorio de `compose.yaml` para construir y ejecutar la aplicación.

## Ejemplo: Empaquetar una aplicación Python simple como contenedor Docker

A continuación, se muestra un ejemplo de una aplicación Hello World simple que imprime "Hello World" en una página web:

```python title="app.py"
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
```

Si implementamos la aplicación Python de manera convencional, sin contenerizarla, necesitamos instalar las dependencias primero. Para algunas dependencias que requieren la compilación de paquetes, esto puede dar problemas en entornos de Windows, donde pueden faltar archivos de encabezado necesarios. Si la contenerizamos como Docker, podemos ignorar las diferencias de entorno; incluso si el host no está conectado a Internet, solo necesitamos copiar la imagen para implementarla. Los siguientes pasos muestran cómo contenerizarla y implementarla con Docker Compose.

Primero, crea un archivo llamado `Dockerfile` y escribe lo siguiente:

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

Luego, en el mismo directorio, crea un archivo llamado `compose.yaml` y copia lo siguiente:

```yaml title="compose.yaml"
version: "3"
services:
  helloworld-flask:
    build: .
    ports:
      - "8099:8000" # El puerto 8099 se puede personalizar
```

Ahora, abre la terminal, ve al directorio que contiene los archivos `Dockerfile` y `compose.yaml`, y ejecuta el siguiente comando para iniciar la aplicación:

```shell
docker compose up
```

Docker construirá la imagen y lanzará el contenedor. Acceda a <http://localhost:8099> para ver los caracteres de Hello World. Con estos pasos, se puede contenerizar una aplicación Python simple y desplegarla utilizando Docker Compose.

## Referencias y agradecimientos

- [Contenerizar una aplicación](https://docs.docker.com/get-started/02_our_app/)
- [Contenerizar una aplicación Python en 3 minutos](https://cloud.tencent.com/developer/article/1752513)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.