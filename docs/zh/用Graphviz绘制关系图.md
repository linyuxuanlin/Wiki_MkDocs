# 用 Graphviz 绘制关系图

一种用代码绘制关系图的方式。

## 背景

[Graphviz](http://www.graphviz.org/) 是个好东西，可用来绘制关系图。与 Visio 有一个本质上的差异： Graphviz 生成图是**自动布局**的，不需要手动调整元素的位置。当一个关系网络比较复杂时，用自动布局可实现**最小化连线交叉**。

![](https://img.wiki-power.com/d/wiki-media/img/Graphviz.png)

## 安装

发现一个很好用的在线编辑器：\[GraphvizOnline\]\([http://dreampuf.github.io/GraphvizOnline/\#digraph graph_name { ](http://dreampuf.github.io/GraphvizOnline/#digraph%20graph_name%20{%20) %20%20A-&gt;B\[label%3D"关系"\]%20 }\) 支持即时渲染，导出 `.png` 与 `.svg` 等格式。

macOS 安装：`brew install graphviz`

## 作图流程

1. 新建 `xxx.dot`
2. 编辑 `.dot` 文档
3. 切换到所在目录，导出：`dot xxx.dot -T png -o xxx.png`

## 简易语法

```
graph graph_name {
  A--B[label="连接关系"]
}
```

![](https://img.wiki-power.com/d/wiki-media/img/20190201140244.png)

## 总结

自动布局是 Graphviz 的精髓。类比我之前用 Markdown 语法直接生成幻灯片，这些工具把内容标准化，让人能够**更加注重于内容，而非形式与布局**。

## 参考与致谢

- [Graphviz 简易教程](https://blog.zengrong.net/post/2294.html)
- [Drawing graphs with dot](http://www.graphviz.org/pdf/dotguide.pdf)
- [Windows 下 Graphviz 安装及入门教程](https://blog.csdn.net/lanchunhui/article/details/49472949)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

``` mermaid
graph TD
    start(开始) -->|检查marker_force_translate| A{marker_force_translate in md_content?}
    A -->|包含| B{marker_written_in_en in md_content?}
    B -->|包含| C{翻译为除英文之外的语言}
    C -->|翻译| D{输出结果}
    B -->|不包含| E{翻译为所有语言}
    E -->|翻译| F{输出结果}
    A -->|不包含| G{filename in exclude_list?}
    G -->|在| H{不进行翻译}
    G -->|不在| I{filename in processed_list_content?}
    I -->|在| J{不进行翻译}
    I -->|不在| K{marker_written_in_en in md_content?}
    K -->|包含| L{翻译为除英文之外的语言}
    L -->|翻译| M{输出结果}
    K -->|不包含| N{翻译为所有语言}
    N -->|翻译| O{输出结果}
    D -->|结束| end(结束)
    F -->|结束| end
    H -->|结束| end
    J -->|结束| end
    M -->|结束| end
    O -->|结束| end
```