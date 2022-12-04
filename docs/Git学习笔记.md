---
id: Git学习笔记
title: Git 学习笔记
---

## 安装与配置

下载安装包：[**git-scm.com/downloads**](https://git-scm.com/downloads)

配置：

```shell
git config --global user.name "username"
git config --global user.email "email@example.com"
```

## 基础语句

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200216204934.png)

### 基本流程

1. 切换到指定的路径下：`cd git-learning`
2. 初始化 Git 仓库：`git init`
3. 将已存在 / 新增的文件，由 **工作区** 转移至 **暂存区** ：
   - `git add .` ：添加工作区的所有文件
   - `git add xxx.xx` ：添加单个文件
4. 提交更新至 **暂存区分支** ：`git commit -m "description"`
5. 切换至某一个版本：`git reset --hard commit_id`

### 常用语句

- 查看修改（仅文件在工作区时可以使用）：`git diff`
- 查看仓库状态：`git status`
- 查看提交历史（按照提交顺序）：`git log` ，按 `q` 退出
- 查看命令历史（所有提交记录）：`git reflog`

## 远程仓库

### 本地项目远程化

适用于本地已有项目文件的情况。

1. 创建 SSH Key：`ssh-keygen -t rsa -C "youremail@example.com"`
   - 更换为你的邮箱，一路回车即可
2. 点开 GitHub [**个人设置 - SSH and GPG keys**](https://github.com/settings/keys)，添加新的 SSH key
   - Title 任意，Key 为 `id_rsa.pub` 文件中的内容
3. 在 GitHub 新建仓库，不要勾选 `Initialize this repository with a README`
   - 如果不小心初始化了仓库，则要先 pull 下来：`git pull origin master`
4. 复制 SSH 地址（示例：`git@github.com:linyuxuanlin/git-learning.git`），在本地 Git 仓库下运行命令：`git remote add origin git@server-name:user/repo-name.git`
5. 将本地内容推送到远程仓库：`git push -u origin master`
   - 在出现提示信息时输入 `yes` 并回车继续
   - 由于远程库是空的，我们第一次推送 master 分支时，加上了 `-u` 参数，Git 不但会把本地的 master 分支内容推送的远程新的 master 分支，还会把本地的 master 分支和远程的 master 分支关联起来，在以后的推送或者拉取时就可以简化命令
6. 未来每一次提交：`git push origin master`

### 远程项目本地化

适用于从零开始，或基于别人的项目开发的情况。

1. 将远程仓库克隆下来：`git clone git@server-name:user/repo-name.git`

## 分支管理

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200217195056.png)

> 分支就是科幻电影里面的平行宇宙，当你正在电脑前努力学习 Git 的时候，另一个你正在另一个平行宇宙里努力学习 SVN。  
> 如果两个平行宇宙互不干扰，那对现在的你也没啥影响。不过，在某个时间点，两个平行宇宙合并了，结果，你既学会了 Git 又学会了 SVN!
>
> 分支在实际中有什么用呢？假设你准备开发一个新功能，但是需要两周才能完成，第一周你写了 50% 的代码，如果立刻提交，由于代码还没写完，不完整的代码库会导致别人不能干活了。如果等代码全部写完再一次提交，又存在丢失每天进度的巨大风险。  
> 现在有了分支，就不用怕了。你创建了一个属于你自己的分支，别人看不到，还继续在原来的分支上正常工作，而你在自己的分支上干活，想提交就提交，直到开发完毕后，再一次性合并到原来的分支上，这样，既安全，又不影响别人工作。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200217202649.png)

1. 创建并切换至新分支：`git switch -c branch_name`
   - `-c` 代表创建并切换分支
2. 查看当前分支：`git branch`
3. 将新分支内容合并到 master 上：`git merge branch_name`
   - 先切换到待合并的分支，再使用合并命令（示例：先切换到 master，再执行以上命令）
   - 当 Git 无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成
   - 解决冲突就是把 Git 合并失败的文件手动编辑为我们希望的内容，再提交
4. 删除某个分支：`git branch -d dev`
5. 禁用 Fast forward 合并分支：`git merge --no-ff -m "commit text" branch_name`
   - 因为本次合并要创建一个新的 commit，所以加上 `-m` 参数，把 commit 描述写进去
   - Fast forward 模式下，删除分支后，会丢掉分支信息

## GitHub 漫游指南

借助 GitHub 平台，我们可以发现丰富多彩的开源项目，并于全世界的开发者一起搭建开源世界。  
当我们发现了一个优秀的开源项目，可以先 Fork 到自己的 GitHub 账户下（这样才拥有读写权限），然后再通过 SSH 克隆到本地进行开发。  
开发完成后，可以在 GitHub 上发起一个 pull request，如果原项目所有者觉得你的修改合适，那么将并入原有的开源项目中。

### GitHub CLI

GitHub CLI 是 GitHub 的命令行工具，将 pull requests，issues 等功能搬到命令行使用。  
下载地址：[**cli.github.com**](https://cli.github.com/)  
GitHub CLI 目前正处于 Beta 版本，值得一试。

## 参考与致谢

- [Git 教程 - 廖雪峰](https://www.liaoxuefeng.com/wiki/896043488029600)
- [实际项目中如何使用 Git 做分支管理](https://blog.csdn.net/ShuSheng0007/article/details/80791849)
- [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
- [git-cheatsheet.pdf](https://github.com/linyuxuanlin/File-host/blob/main/software-development/git-cheatsheet.pdf)
- [Pro Git](https://git-scm.com/book/zh/v2)
- [GitHub CLI - Manual](https://cli.github.com/manual/)
- [20 多张精美图带你进入 Git 大门](https://mp.weixin.qq.com/s/oTtMQFEI9J5ymqt6SQ0PFg)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

