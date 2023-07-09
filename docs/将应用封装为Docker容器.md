---
id: 将应用封装为Docker容器
title: 将应用封装为 Docker 容器
---

将应用封装为 Docker 容器，可以更加方便地部署管理。下面是一个示例，演示了如何将一个 Python 应用封装为 Docker 容器，并使用 Docker Compose 的方式执行。

## 基本模板

将应用 Docker 容器化，首先需要确保 Docker 已经安装。接着，需要在你的 Python 应用程序根目录下，创建这两个文件：`Dockerfile` 和 `compose.yaml`，它们大致会包含以下内容：

```Dockerfile title="Dockerfile"
# 设置基础镜像为 Python 官方镜像，版本可自定义
FROM python:3.9

# 设置工作目录为 /app
WORKDIR /app

# 复制 Python 应用程序的依赖文件
COPY requirements.txt .

# 安装应用程序依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用程序文件，从当前目录拷贝进容器内的目录
COPY . .

# 设置默认执行命令
CMD ["python", "app.py"]
```

```yaml title="compose.yaml"
version: "3"
services:
  app:
    build: .
```

在这个 `compose.yaml` 文件中，我们定义了一个服务名为 `app` 的服务。通过 `build: .` 指令，它将使用当前目录下的 `Dockerfile` 文件来构建镜像。在 `compose.yaml` 的目录下执行 `docker compose up`，即可构建并启动这个应用。

## 实例：一个简单的 TODO 应用

以下是一个简单的 Todo 应用示例，详细讲解将一个 python 应用 Docker 容器化，并用 Docker Compose 部署的流程。

这是应用的 Python 文件：

```python title="app.py"
from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []

# 获取所有的 Todo 项
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# 添加一个新的 Todo 项
@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.get_json()
    todos.append(todo)
    return jsonify({'message': 'Todo added successfully'})

# 删除指定索引的 Todo 项
@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    if index < len(todos):
        todos.pop(index)
        return jsonify({'message': 'Todo deleted successfully'})
    else:
        return jsonify({'error': 'Todo not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

接下来，将这个 Todo 应用容器化，并使用 Docker Compose 进行部署。首先，创建一个名为`Dockerfile`的文件，将以下内容复制到其中：

```Dockerfile title="Dockerfile"
# 设置基础镜像为Python官方镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制应用程序文件
COPY . .

# 安装依赖
RUN pip install --no-cache-dir flask

# 设置环境变量
ENV FLASK_APP=app.py

# 启动应用程序
CMD flask run --host=0.0.0.0 --port=8000
```

然后，在同一目录下创建一个名为`compose.yaml`的文件，将以下内容复制到其中：

```yaml
version: "3"
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 8000:8000
```

现在，你可以打开终端，进入包含 `Dockerfile` 和 `compose.yaml` 文件的目录，并运行以下命令来启动应用程序：

```shell
docker compose up
```

Docker 将会构建镜像并启动容器。你可以通过访问 <http://localhost:8000> 在本地浏览器中访问 Todo 应用程序。

通过以上步骤，可以将一个简单的 Todo 应用容器化，并使用 Docker Compose 进行部署。
