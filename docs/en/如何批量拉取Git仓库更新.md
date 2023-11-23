# How to Batch Pull Git Repository Updates

When there are many repositories, it can become tedious to manually pull each one. By using the method described in this article, you can perform batch pull operations on Git repositories.

## Steps

1. Create a script file named `pull-master.sh` and paste the following code into it:

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
root_dir="[to_be_replace[Path containing multiple repositories]]"
getdir $root_dir
```

2. Replace `[to_be_replace[Path containing multiple repositories]]` with your own path, for example, `C:\repos`.
3. Run the command:

```shell
sh pull-master.sh
or
./pull-master.sh
```

or double-click `pull-master.sh` to run it.

## Scheduled Execution

1. Search for and open `Task Scheduler`.
2. Click `Create Task`.
   1. Fill in the name on the `General` tab.
   2. Set the schedule on the `Triggers` tab.
   3. Create a new action on the `Actions` tab, fill in the `Program/script` (e.g., `F:\pull-master.sh`), add arguments (e.g., `pull-master.sh`), and start in (e.g., `F:\`).
3. Test run the task. If there are no issues, it should work. (If it doesn't work, you can refer to [**Pull-Git-Repo.xml**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Pull-Git-Repo.xml))

## Deployment on Synology NAS

1. Place the script (e.g., `github-pull.sh`) in any path on the NAS.
2. Modify the path of `root_dir` in `github-pull.sh`, for example, change it to `"/volume1/projects"`, which is where you store your Git repositories.
3. Go to `Control Panel` - `Task Scheduler` - `Create` - `Scheduled Task` - `User-defined script`. Configure the schedule and command to run the script (e.g., `bash /volume1/stash/permanent/github-pull.sh`).
4. In `Settings`, configure the output result. Then select the task, click `Run` to test the execution, and open the configured output path to view the results.

If you are prompted to enter a password every time, you can enter the following command (user home directory needs to be enabled in advance):

```shell
git config –global credential.helper store
```

This will generate a text file locally that stores the account and password.  
The next time you are prompted for a password, you only need to enter it once and you won't need to enter it again in the future.

## References and Acknowledgements

- [批量 git pull 小脚本](https://www.jianshu.com/p/42e8da5eb0af)
- [git 批量 pull_shell 脚本 -- 多个代码库批量 pull 最新 master 代码](https://blog.csdn.net/weixin_39618730/article/details/113024998)
- [Windows 定时执行 shell 脚本](https://blog.csdn.net/qq_40463753/article/details/84976977)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.