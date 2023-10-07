# VS Code Productivity Guide - Jupyter Notebook

Create efficient productivity tools with VS Code.

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323155728.png)

Jupyter Notebook is a powerful tool that allows us to write, run, view output, visualize data, and view results in a document environment. In short, with it, writing documents containing code is much more convenient.

In the previous article, we completed the basic setup of VS Code. In this article, I will provide a detailed explanation of Jupyter with VS Code.

## Environment Configuration

As we all know, Jupyter Notebooks depend on the Python environment.  
To confirm whether you have a Python environment, type **Python: Select Interpreter** in the VS Code command panel (`Ctrl + Shift + P`). If you see a Python version that you can select, then there is no problem.

If you do not have a Python environment, you can install it using the following method:

1. Download the latest version of the installation package from the [**Python official website**](https://www.python.org/) (preferably the `web-based installer` version).

After configuring the local Python environment, we also need to install the [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python) plugin in VS Code. In a recent update, Jupyter Notebooks have been included in this plugin, so there is no need to install it separately.

## Creating a Notebook

After the environment is configured, we can create a blank Jupyter notebook (`.ipynb` file) by typing **Python: Create Blank New Jupyter** in the VS Code command panel (`Ctrl + Shift + P`). Test it as shown in the figure below:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323153020.png)

As you can see, the code runs normally.

## Basic Operations

Jupyter Notebook uses **code cells** to create, edit, and run code.

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323153717.png)

### Adding Code Cells

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323153850.png)

### Running a Single Code Cell

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323153939.png)

### Running Multiple Code Cells

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154005.png)

### Moving Code Cells

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154059.png)

### Deleting Code Cells

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154148.png)

### Switching Between Code and Markdown



### Chart Viewer

With the chart viewer, you can easily view the charts output by your code and export them in various image formats:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154555.png)

### Data and Variable Viewer

The type, quantity, and value of variables can be viewed in real-time through the variable viewer:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154758.png)

You can also browse more specific data through the data viewer:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154832.png)

## References and Acknowledgements

- [Working with Jupyter Notebooks in Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)
- [VS Code Python 全新发布！Jupyter Notebook 原生支持终于来了！](https://zhuanlan.zhihu.com/p/85445777)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.