# How to Batch Pull Git Repository Updates

When there are many repositories, it can become cumbersome to pull them one by one manually. With the method described in this article, you can perform batch pull operations on Git repositories.

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
root_dir="【path to directory containing multiple repositories】"
getdir $root_dir
```

2. Replace `【path to directory containing multiple repositories】` with your own path, for example `C:\repos`.
3. Run the command:

```shell
sh pull-master.sh
or
./pull-master.sh
```

Or double-click `pull-master.sh` to run it.

## Scheduled Execution

1. Search for and open `Task Scheduler`.
2. Click `Create Task`.
   1. Fill in the name on the `General` tab.
   2. Set the schedule on the `Triggers` tab.
   3. Create a new action on the `Actions` tab, fill in the `Program/script` (e.g. `F:\pull-master.sh`), add arguments (e.g. `pull-master.sh`), and set the `Start in` (e.g. `F:\`).
3. Test run, and if there are no issues, it can be left to run. (If it fails, refer to [**Pull-Git-Repo.xml**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Pull-Git-Repo.xml))

## Deployment on Synology NAS

1. Place the script (e.g. `github-pull.sh`) in any path on the NAS.
2. Modify the path of `root_dir` in `github-pull.sh`, for example, I changed it to `"/volume1/projects"`, which is where you put your Git repositories.
3. `Control Panel` - `Task Scheduler` - `Create` - `User-defined script`, configure the scheduled run time and the command to run the script (e.g. `bash /volume1/stash/permanent/github-pull.sh`).
4. Output results can be configured in `Settings`. After selecting the task, click `Run` to test the run, and open the configured output path to view the results.

If you need to enter your password every time, you can enter the following command (user home directory must be enabled in advance):

```shell
git config –global credential.helper store
```

This will generate a text file locally that records your username and password.  
The next time you are prompted for your password, you only need to enter it once, and you won't have to enter it again in the future.

## References and Acknowledgements

- [Batch git pull script](https://www.jianshu.com/p/42e8da5eb0af)
- [Git batch pull_shell script -- batch pull latest master code from multiple code repositories](https://blog.csdn.net/weixin_39618730/article/details/113024998)
- [Scheduled execution of shell scripts on Windows](https://blog.csdn.net/qq_40463753/article/details/84976977)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.