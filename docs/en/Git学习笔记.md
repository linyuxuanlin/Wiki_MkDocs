# Git Learning Notes

## Installation and Configuration

Download the installation package: [**git-scm.com/downloads**](https://git-scm.com/downloads)

Configuration:

```shell
git config --global user.name "username"
git config --global user.email "email@example.com"
```

## Basic Commands

![](https://img.wiki-power.com/d/wiki-media/img/20200216204934.png)

### Basic Workflow

1. Change to the specified directory: `cd git-learning`
2. Initialize the Git repository: `git init`
3. Transfer existing or newly added files from the **working directory** to the **staging area**:
   - `git add .`: Add all files from the working directory
   - `git add xxx.xx`: Add a single file
4. Commit updates to the **staging branch**: `git commit -m "description"`
5. Switch to a specific version: `git reset --hard commit_id`

### Common Commands

- View changes (only when files are in the working directory): `git diff`
- Check repository status: `git status`
- View commit history (in chronological order): `git log`, press `q` to exit
- View command history (all commit records): `git reflog`

## Remote Repositories

### Making a Local Project Remote

Applicable when you already have local project files.

1. Create an SSH Key: `ssh-keygen -t rsa -C "youremail@example.com"`
   - Replace it with your email and press Enter throughout the process.
2. Open GitHub [**Settings - SSH and GPG keys**](https://github.com/settings/keys), and add a new SSH key.
   - Title can be anything, and the key is the content from the `id_rsa.pub` file.
3. Create a new repository on GitHub, do not select "Initialize this repository with a README."
   - If the repository was accidentally initialized, pull it first: `git pull origin master`
4. Copy the SSH URL (e.g., `git@github.com:linyuxuanlin/git-learning.git`) and run the following command in your local Git repository: `git remote add origin git@server-name:user/repo-name.git`
5. Push the local content to the remote repository: `git push -u origin master`
   - When prompted, type `yes` and press Enter to continue.
   - Since the remote repository is empty, when we push the master branch for the first time, we use the `-u` option to associate the local and remote master branches for future simplification of commands.
6. For all future commits: `git push origin master`

### Making a Remote Project Local

Applicable when starting from scratch or developing based on someone else's project.

1. Clone the remote repository: `git clone git@server-name:user/repo-name.git`

## Branch Management

![](https://img.wiki-power.com/d/wiki-media/img/20200217195056.png)

Branches are like parallel universes in a science fiction movie. While you're diligently learning Git in front of your computer, another you is striving to master SVN in a different parallel universe. If these two parallel universes don't interfere with each other, it doesn't affect your current self. However, at some point, these two universes merge, and the result is that you've learned both Git and SVN!

But what's the practical use of branches? Imagine you're about to develop a new feature that will take two weeks to complete. In the first week, you've written 50% of the code. If you were to commit it immediately, the incomplete codebase would prevent others from working effectively. On the other hand, if you wait until all the code is done before submitting, there's a significant risk of losing daily progress.

Now, with branches, you don't have to worry. You create your own branch, invisible to others, and they can continue working on the original branch. Meanwhile, you work on your branch, submitting whenever you want. Once the development is complete, you can merge it into the original branch in one go. This approach is both secure and non-disruptive to others.

![Branching](https://img.wiki-power.com/d/wiki-media/img/20200217202649.png)

1. Create and switch to a new branch: `git switch -c branch_name`
   - `-c` stands for creating and switching branches.
2. View the current branch: `git branch`
3. Merge the content of the new branch into master: `git merge branch_name`
   - First, switch to the branch to be merged, then use the merge command (e.g., switch to master first, then execute the above command).
   - When Git cannot automatically merge the branches, you must resolve conflicts first. After resolving conflicts, you can commit, and the merge is complete.
   - Resolving conflicts involves manually editing the files that Git failed to merge to match the desired content before committing.
4. Delete a branch: `git branch -d dev`
5. Disable Fast Forward when merging a branch: `git merge --no-ff -m "commit text" branch_name`
   - Since this merge creates a new commit, use the `-m` parameter to add the commit message.
   - In Fast Forward mode, branch information is lost when the branch is deleted.

## GitHub Roaming Guide

With the help of the GitHub platform, we can discover a diverse world of open-source projects and collaborate with developers from around the globe to build an open-source community. When we come across an outstanding open-source project, we can first fork it to our GitHub account (to gain read-write permissions), then clone it locally using SSH for development. Once the development is complete, you can initiate a pull request on GitHub. If the original project owner deems your changes appropriate, they will merge them into the existing open-source project.

### GitHub CLI

GitHub CLI is a command-line tool provided by GitHub that brings the functionality of pull requests, issues, and more to the command line. You can download it from [**cli.github.com**](https://cli.github.com/). GitHub CLI is currently in beta, but it's worth a try.

## References and Acknowledgments

- [Git Tutorial by Liao Xuefeng](https://www.liaoxuefeng.com/wiki/896043488029600)
- [How to Use Git for Branch Management in Real Projects](https://blog.csdn.net/ShuSheng0007/article/details/80791849)
- [A Guide to a Successful Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
- [git-cheatsheet.pdf](https://github.com/linyuxuanlin/File-host/blob/main/software-development/git-cheatsheet.pdf)
- [Pro Git](https://git-scm.com/book/zh/v2)
- [GitHub CLI Manual](https://cli.github.com/manual/)
- [Explore the World of Git with Over 20 Beautiful Illustrations](https://mp.weixin.qq.com/s/oTtMQFEI9J5ymqt6SQ0PFg)

[to_be_replaced[1]]
[to_be_replaced[2]]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.