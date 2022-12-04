---
id: VSCode生产力指南-JupyterNotebook
title: VS Code 生产力指南 - Jupyter Notebook
---

用 VS Code 打造高效率的生产力工具。


![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323155728.png)

Jupyter Notebook 是一个很强大的工具，它允许我们在一个文档环境内编写、运行代码、查看输出、将数据可视化并查看结果……总之，有了它，我们写含代码的文档就方便多了。

在上一篇文章中，我们完成了 VS Code 基本环境的搭建。这篇文章我将对 Jupyter with VS Code 进行详细讲解。

## 环境配置

众所周知，Jupyter Notebooks 依赖 Python 环境。  
为了确认你是否拥有 Python 环境，在 VS Code 命令面板（`Ctrl + Shift + P`）内键入 **Python: Select Interpreter**，如果看到有可以选择的 Python 版本，那就没问题。

如果没有 Python 环境，可以通过以下方法安装：

1. 在 [**Python 官网**](https://www.python.org/) 下载最新版本安装包（尽量选择 `web-based installer` 版本）


配置完本地 Python 环境后，我们还需要在 VS Code 内安装 [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 插件。在近期的一次更新中，Jupyter Notebooks 已经被包含在这个插件内，不用再单独安装了。

## 创建笔记本

环境配置完成后，我们可以在 VS Code 命令面板（`Ctrl + Shift + P`）输入 **Python: Create Blank New Jupyter** 创建一个空白的 Jupyter 笔记本（`.ipynb` 文件）。如下图简单测试一下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323153020.png)

可以看到，代码正常运行。

## 基本操作

Jupyter Notebook 使用 **代码单元（code cells）** 的形式来创建、编辑和运行代码。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323153717.png)

### 添加 code cells

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323153850.png)

### 运行单个 code cell

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323153939.png)

### 运行多个 code cells

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323154005.png)

### 移动 code cell

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323154059.png)

### 删除 code cell

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323154148.png)

### 在代码与 Markdown 之间切换

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323154242.png)

### 图表查看器

通过图表查看器，你可以轻松查看代码输出的图表，也可以将图标导出各种格式的图片：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323154555.png)

### 数据与变量查看器

变量的类型、数量与值可以通过变量查看器实时查看：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323154758.png)

也可以通过数据查看器浏览更具体的数据：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200323154832.png)



## 参考与致谢

- [Working with Jupyter Notebooks in Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)
- [VS Code Python 全新发布！Jupyter Notebook 原生支持终于来了！](https://zhuanlan.zhihu.com/p/85445777)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

