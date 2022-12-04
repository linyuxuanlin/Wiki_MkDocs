---
id: 删除GitHub仓库中某个文件夹
title: 删除 GitHub 仓库中某个文件夹
---

## 问题来源

在本地仓库上传到 GitHub 时，忘记忽略某个文件夹，直接 push 到远程仓库了。  
如何在保留本地文件夹的同时，删除 GitHub 仓库中的文件夹？

## 解决方法

```shell
git pull origin master        # 先将远程仓库里面的项目拉取下来
dir                           # 查看有哪些文件夹
git rm -r --cached target     # 删除名字为 target 的文件夹
git commit -m '删除了 target'  # 添加操作说明并提交
```

## 参考与致谢

- [删除 GitHub 中某个文件夹](https://blog.csdn.net/wudinaniya/article/details/77508229)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

