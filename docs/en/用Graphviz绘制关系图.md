# Drawing Relationship Diagrams with Graphviz

A way to draw relationship diagrams using code.

## Background

[Graphviz](http://www.graphviz.org/) is a great tool for drawing relationship diagrams. It has a fundamental difference from Visio: Graphviz generates graphs with **automatic layout**, eliminating the need for manual adjustment of element positions. When a relationship network becomes complex, automatic layout can minimize **crossing lines**.

![](https://media.wiki-power.com/img/Graphviz.png)

## Installation

I found a useful online editor: [GraphvizOnline](http://dreampuf.github.io/GraphvizOnline/#digraph%20graph_name%20{%20%20A-%3EB%5Blabel%3D%22relationship%22%5D%20%20}) which supports real-time rendering and exporting to formats such as `.png` and `.svg`.

For macOS installation: `brew install graphviz`

## Drawing Process

1. Create a new `xxx.dot` file.
2. Edit the `.dot` document.
3. Switch to the directory where the file is located, and export it: `dot xxx.dot -T png -o xxx.png`

## Simple Syntax

```
graph graph_name {
  A--B[label="relationship"]
}
```

![](https://media.wiki-power.com/img/20190201140244.png)

## Summary

Automatic layout is the essence of Graphviz. Similar to how I used Markdown syntax to directly generate slides, these tools standardize content, allowing people to focus more on the **content itself rather than the form and layout**.

## References and Acknowledgements

- [Graphviz Simple Tutorial](https://blog.zengrong.net/post/2294.html)
- [Drawing graphs with dot](http://www.graphviz.org/pdf/dotguide.pdf)
- [Graphviz Installation and Beginner's Tutorial for Windows](https://blog.csdn.net/lanchunhui/article/details/49472949)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
