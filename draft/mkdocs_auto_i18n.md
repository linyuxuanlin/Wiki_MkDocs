# mkdocs_auto_i18n

https://pypi.org/project/mkdocs-auto-i18n

---

## index.py

这个插件会在 mkdocs 的预处理阶段（on_pre_build 事件）中遍历 docs 目录下的所有.md 文件，并翻译为指定语言。翻译后的文件将被储存在相应的语言文件夹下（例如 docs/en、docs/zh 等）。然后，插件会将翻译后的文件添加到 mkdocs 的 Page 对象中，以便在浏览文章的时候允许用户切换语言。

当用户访问一个页面时，插件会根据页面的 URL 确定当前语言，并将当前语言的翻译文件路径替换为原始文件路径。这样，当用户切换语言时，mkdocs 会自动加载相应语言的文件。

请注意，为了使用 OpenAI API 进行翻译，您需要在插件配置中设置 OpenAI API Key。此外，插件还支持自定义每个语言的文件夹名称和最大翻译长度。

---

要发布这个插件，您可以将它上传到 Python Package Index (PyPI)上，让用户可以使用 pip 命令安装。以下是发布插件的步骤：

1. 创建一个名为`mkdocs-translation-plugin`的 Python 包，并将插件代码放在其中。确保包中包含一个名为`setup.py`的文件和一个名为`README.md`的说明文件。

2. 在 PyPI 上注册一个账号，并使用`twine`工具将包上传到 PyPI 上。您可以使用以下命令安装`twine`工具：

   ```
   pip install twine
   ```

   然后，使用以下命令将包上传到 PyPI：

   ```
   python setup.py sdist
   twine upload dist/*
   ```

   这将会上传一个源代码分发包到 PyPI 上。

3. 现在，其他用户就可以使用以下命令安装您的插件：

   ```
   pip install mkdocs_auto_i18n
   ```

   安装完成后，用户就可以在他们的 mkdocs.yaml 配置文件中使用这个插件了。

在 mkdocs.yaml 中配置这个插件的方法如下：

```
plugins:
  - translation:
      api_key: YOUR_OPENAI_API_KEY
      max_length: 1000
      languages:
        en: en
        zh: zh
```

在这个配置中，插件名称是`translation`，并且需要设置 OpenAI API Key、最大翻译长度和每个语言对应的文件夹名称。在这个例子中，我们为英语和中文分别指定了一个文件夹名称（`en`和`zh`）。

---

## setup.py

这个 setup.py 文件中包含了以下元数据：

- name: 包的名称。
- version: 包的版本号。
- description: 包的简短描述。
- long_description: 包的详细描述，通常是一个 README 文件。
- long_description_content_type: long_description 的类型，通常是 text/markdown。
- author: 包的作者。
- author_email: 作者的电子邮件地址。
- url: 包的主页。
- packages: 包含要包含在分发包中的 Python 包的列表。
- install_requires: 包的依赖项列表。
- classifiers: 包的分类列表，用于 PyPI 搜索。

```python
## from setuptools import setup, find_packages

setup(
    name="mkdocs-auto-i18n",
    version="0.1.0",
    description="A plugin for MkDocs that automatically translates documentation pages and allows users to switch languages.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Power Lin",
    author_email="linyuxuanlin@outlook.com",
    url="https://github.com/linyuxuanlin/mkdocs-auto-i18n",
    packages=find_packages(),
    install_requires=[
        "mkdocs>=1.1",
        "openai>=0.11.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)
```

---

PyPi 使用 API 令牌进行身份验证:
https://www.fournoas.com/posts/authentication-on-pypi-using-api-token-instead-of-password/

---
