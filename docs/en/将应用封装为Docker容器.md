# Packaging Applications as Docker Containers

Packaging applications as Docker containers can make deployment and management more convenient. Here is an example that demonstrates how to package a Python application as a Docker container and execute it using Docker Compose.

## Basic Template

To containerize an application with Docker, you first need to ensure that Docker is installed. Then, you need to create these two files in the root directory of your Python application: `Dockerfile` and `compose.yaml`, which will roughly contain the following:

```Dockerfile title="Dockerfile"
# Set the base image to the official Python image, version can be customized
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the dependency files of the Python application
COPY requirements.txt .

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files, copy from the current directory to the directory inside the container
COPY . .

# Set the default command to execute
CMD ["python", "app.py"]
```

```yaml title="compose.yaml"
version: "3"
services:
  app:
    build: .
```

In this `compose.yaml` file, we define a service named `app`. With the `build: .` instruction, it will use the `Dockerfile` file in the current directory to build the image. Run `docker compose up` in the directory of `compose.yaml` to build and start the application.

## Example: Packaging a Simple Python Application as a Docker Container

Here is a simple Hello World application example, a Python application that prints Hello World on a webpage:

```python title="app.py"
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
```

If we deploy the Python application using the normal process without containerization, we need to install dependencies first. For some packages that need to be compiled and installed, errors may occur in the Windows environment, and necessary header files may be missing. If we package it as a Docker container, we can ignore the differences in the environment. Even if the host machine is not connected to the network, we only need to copy the image to complete the deployment. The following steps show how to containerize it with Docker and deploy it with Docker Compose.

First, create a file named `Dockerfile` and fill in the following:

```Dockerfile title="Dockerfile"
# Set the base image to the official Python image
FROM python:3.9

# Copy the application files
COPY . /app

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install flask

# Expose port 8000 for access
EXPOSE 8000

# Start the application
CMD python ./app.py
```

Then, create a file named `compose.yaml` in the same directory and copy the following content:

```yaml title="compose.yaml"
version: "3"
services:
  helloworld-flask:
    build: .
    ports:
      - "8099:8000" # Port 8099 can be customized
```

Now, you can open the terminal, go to the directory containing the `Dockerfile` and `compose.yaml` files, and run the following command to start the application:

```shell
docker compose up
```

Docker will build an image and start a container. Accessing <http://localhost:8099> will display the characters "Hello World". By following these steps, a simple Python application can be containerized and deployed using Docker Compose.

## References and Acknowledgements

- [Containerize an application](https://docs.docker.com/get-started/02_our_app/)
- [Containerize a Python application in 3 minutes](https://cloud.tencent.com/developer/article/1752513)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.