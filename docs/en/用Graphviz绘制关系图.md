# Drawing Relationship Diagrams with Graphviz

A way to draw relationship diagrams using code.

## Background

[Graphviz](http://www.graphviz.org/) is a great tool for drawing relationship diagrams. It has a fundamental difference from Visio: Graphviz generates graphs that are **automatically laid out**, without the need for manual adjustment of element positions. When a relationship network is complex, automatic layout can achieve **minimization of line crossings**.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/Graphviz.png)

## Installation

I found a very useful online editor: \[GraphvizOnline\]\([http://dreampuf.github.io/GraphvizOnline/\#digraph graph_name { ](http://dreampuf.github.io/GraphvizOnline/#digraph%20graph_name%20{%20) %20%20A-&gt;B\[label%3D"relationship"\]%20 }\) which supports real-time rendering and export to formats such as `.png` and `.svg`.

macOS installation: `brew install graphviz`

## Drawing Process

1. Create `xxx.dot`
2. Edit the `.dot` document
3. Switch to the directory and export: `dot xxx.dot -T png -o xxx.png`

## Simple Syntax

```
graph graph_name {
  A--B[label="relationship"]
}
```

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20190201140244.png)

## Conclusion

Automatic layout is the essence of Graphviz. Similar to how I previously used Markdown syntax to directly generate slides, these tools standardize content, allowing people to focus more on **content rather than form and layout**.

## References and Acknowledgments

- [Graphviz Simple Tutorial](https://blog.zengrong.net/post/2294.html)
- [Drawing graphs with dot](http://www.graphviz.org/pdf/dotguide.pdf)
- [Graphviz Installation and Getting Started Tutorial for Windows](https://blog.csdn.net/lanchunhui/article/details/49472949)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
