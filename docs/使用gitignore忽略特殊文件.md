---
id: 使用gitignore忽略特殊文件
title: 使用 gitignore 忽略特殊文件
---

有些文件我们不想纳入 Git 版本管理，也不希望它们总出现在未跟踪列表，例如 node_modules、一些开发依赖、编译日志等等。

这时，我们可以创建一个 `.gitignore` 文件，列出需要忽略的清单。

## 规范

- 空行或者以注释符号 `#` 开头的行会被忽略
- 标准的glob模式匹配
- 匹配模式最后跟反斜杠（/）说明要忽略的是目录
- 要忽略指定模式以外的文件和目录，可以在模式前加上 `!` 取反

## 示例

```gitignore
# 此行为注释，将被 Git 忽略

# 忽略所有 .a 格式的文件
*.a

# 不忽略 lib.a
!lib.a

# 忽略根目录下的 TODO 文件
/TODO

# 忽略 build 文件夹
build/

# 忽略 doc 目录下的所有 txt 文件（不包含次级目录）
doc/*.txt

# 忽略doc目录下的所有 txt 文件（包含所有次级目录）
doc/**/*.txt
```

## 参考与致谢 

- [zxhfighter/git-ignore.md](https://gist.github.com/zxhfighter/6320b9a08698bb8703ee)
- [github/gitignore](https://github.com/github/gitignore)
