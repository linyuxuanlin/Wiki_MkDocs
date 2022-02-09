---
id: 如何批量拉取Git仓库更新
title: 如何批量拉取 Git 仓库更新
---

仓库一多，逐个手动拉取就会变得很麻烦。使用本文的方法，可以对 Git 仓库进行批量拉取操作。

## 步骤

1. 新建脚本文件 `pull-master.sh`，并将以下代码粘贴进去：

```shell title="pull-master.sh"
#!/bin/bash

function showMsg()
 {
   echo -e "\033[32m$1\033[0m"
 }

function getdir(){
    for element in `ls $1`
    do
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then
            cd $1"/"$element
            showMsg 'git pull '$element
            git pull
        else
            echo $dir_or_file
        fi
    done
}
root_dir="【包含多个仓库的路径】"
getdir $root_dir
```

2. 将 `【包含多个仓库的路径】` 替换为你的路径，比如我的是 `C:\repos`。
3. 运行命令：

```shell
sh pull-master.sh
或
./pull-master.sh
```

或直接双击 `pull-master.sh` 运行

## 定时执行

1. 搜索并打开 `任务计划程序`
2. 点击 `创建任务`
   1. 在 `常规` 标签页内填写名称
   2. 在 `触发器` 标签页内设置周期
   3. 在 `操作` 标签页内新建操作，填写 `程序或脚本`（例如 `F:\pull-master.sh`），添加参数（例如 `pull-master.sh`），起始于（例如 `F:\`）
3. 测试运行，如果没问题即可。（如不成功可参考 [**Pull-Git-Repo.xml**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Pull-Git-Repo.xml)）

## 在群晖 NAS 上部署

1. 将脚本（比如我是 `github-pull.sh`）放在 NAS 上任意路径
2. 修改 `github-pull.sh` 内 `root_dir` 的路径，比如我改为 `"/volume1/projects"`，也就是你放 Git 仓库的地方
3. `控制面板` - `任务计划` - `新增` - `计划的任务` - `用户定义的脚本`，在 `计划` 和 `任务设置` 标签页配置周期运行时间，和运行脚本的命令（比如 `bash /volume1/stash/permanent/github-pull.sh`）
4. 可在 `设置` 内配置输出结果，后选择任务，点击 `运行`，可测试运行，可打开配置的输出路径看运行结果

如果每次都需要输入密码，可以输入以下命令（需提前开启用户家目录）：

```shell
git config –global credential.helper store
```

这会在本地生成一个文本，上边记录账号和密码。  
接下来遇到要输入密码时，只需再输入一次，以后就不用重新输入了。

## 参考与致谢

- [批量 git pull 小脚本](https://www.jianshu.com/p/42e8da5eb0af)
- [git 批量 pull_shell 脚本 -- 多个代码库批量 pull 最新 master 代码](https://blog.csdn.net/weixin_39618730/article/details/113024998)
- [Windows 定时执行 shell 脚本](https://blog.csdn.net/qq_40463753/article/details/84976977)
