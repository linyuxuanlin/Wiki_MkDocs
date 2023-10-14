`![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/` -> `![](https://f004.backblazeb2.com/file/wiki-media/` (zh)


`![](https://img.wiki-power.com/d/wiki-media/`

## draft

```
<div
  class="altium-ecad-viewer"
  data-project-src="https://github.com/linyuxuanlin/Collection_of_Motor_Driver_Design/raw/main/DC_Motor/IR2104S/IR2104S.SchDoc"
  style="
    border-radius: 0px 0px 4px 4px;
    height: 500px;
    border-style: solid;
    border-width: 1px;
    overflow: hidden;
    max-width: 1280px;
    max-height: 700px;
    box-sizing: border-box;
  "
>在线预览项目</div>
```

todo:

- post time
- index page of groups
- speed up page loading

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