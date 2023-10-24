# Packaging the Application as a Docker Container

Packaging the application as a Docker container makes it easier to deploy and manage. Here is an example that demonstrates how to package a Python application as a Docker container and execute it using Docker Compose.

## Basic Template

To containerize the application with Docker, make sure Docker is installed first. Then, create these two files in the root directory of your Python application: `Dockerfile` and `compose.yaml`. They will roughly contain the following content:

```Dockerfile title="Dockerfile"
# Set the base image to the official Python image, version can be customized
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the dependencies file of the Python application
COPY requirements.txt .

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files from the current directory to the directory inside the container
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

In this `compose.yaml` file, we define a service named `app`. With the `build: .` instruction, it will use the `Dockerfile` file in the current directory to build the image. Run `docker compose up` in the directory where `compose.yaml` is located to build and start the application.

## Example: Packaging a Simple Python Application as a Docker Container

Here is an example of a simple Hello World application:

This is a sample Python application that prints Hello World on a webpage:

```python title="app.py"
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
```

If we deploy a Python application using the conventional method without containerization, we need to install dependencies first. For some packages that require compilation, errors may occur, especially in a Windows environment, and necessary header files may be missing. By packaging it as a Docker container, we can ignore the differences in environments. Even if the host machine is not connected to the internet, we only need to copy the image to complete the deployment. The following steps demonstrate how to containerize it with Docker and deploy it using Docker Compose.

First, create a file named `Dockerfile` and fill it with the following content:

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

Then, create a file named `compose.yaml` in the same directory and copy the following content into it:

```yaml title="compose.yaml"
version: "3"
services:
  helloworld-flask:
    build: .
    ports:
      - "8099:8000" # Port 8099 can be customized
```

Now, you can open the terminal, navigate to the directory that contains the `Dockerfile` and `compose.yaml` files, and run the following command to start the application:

```shell
docker compose up
```

Docker will build the image and start the container. Accessing <http://localhost:8099> will display the characters "Hello World". By following the steps above, a simple Python application can be containerized and deployed using Docker Compose.

## References and Acknowledgements

- [Containerize an application](https://docs.docker.com/get-started/02_our_app/)
- [Containerize a Python application in 3 minutes](https://cloud.tencent.com/developer/article/1752513)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.