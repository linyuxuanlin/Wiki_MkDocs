# Git Study Notes

## Installation and Configuration

Download installation package: [**git-scm.com/downloads**](https://git-scm.com/downloads)

Configuration:

```shell
git config --global user.name "username"
git config --global user.email "email@example.com"
```

## Basic Statements

![](https://img.wiki-power.com/d/wiki-media/img/20200216204934.png)

### Basic Process

1. Switch to the specified path: `cd git-learning`
2. Initialize Git repository: `git init`
3. Transfer existing/new files from **working directory** to **staging area**:
   - `git add .`: Add all files in the working directory
   - `git add xxx.xx`: Add a single file
4. Commit updates to **staging branch**: `git commit -m "description"`
5. Switch to a specific version: `git reset --hard commit_id`

### Common Statements

- View changes (only available when the file is in the working directory): `git diff`
- View repository status: `git status`
- View commit history (in order of submission): `git log`, press `q` to exit
- View command history (all commit records): `git reflog`

## Remote Repository

### Local Project Remote

Applicable to cases where local project files already exist.

1. Create SSH Key: `ssh-keygen -t rsa -C "youremail@example.com"`
   - Replace with your email, press Enter all the way
2. Click on GitHub [**Personal Settings - SSH and GPG keys**](https://github.com/settings/keys), and add a new SSH key
   - Title can be anything, Key is the content in the `id_rsa.pub` file
3. Create a new repository on GitHub, do not check `Initialize this repository with a README`
   - If you accidentally initialized the repository, you need to pull it down first: `git pull origin master`
4. Copy the SSH address (example: `git@github.com:linyuxuanlin/git-learning.git`) and run the command in the local Git repository: `git remote add origin git@server-name:user/repo-name.git`
5. Push the local content to the remote repository: `git push -u origin master`
   - Enter `yes` and press Enter to continue when prompted
   - Since the remote repository is empty, we added the `-u` parameter when pushing the master branch for the first time. Git will not only push the contents of the local master branch to the new remote master branch, but also associate the local master branch with the remote master branch, making it easier to push or pull in the future.
6. For every future submission: `git push origin master`

### Localizing a Remote Project

Suitable for starting from scratch or developing based on someone else's project.

1. Clone the remote repository: `git clone git@server-name:user/repo-name.git`

## Branch Management

![](https://img.wiki-power.com/d/wiki-media/img/20200217195056.png)

A branch is like a parallel universe in a science fiction movie. While you are working hard to learn Git in front of your computer, another you is working hard to learn SVN in another parallel universe. If the two parallel universes do not interfere with each other, it doesn't affect you now. However, at some point in time, the two parallel universes merge, and as a result, you have learned both Git and SVN!

What is the practical use of branches? Suppose you are ready to develop a new feature, but it will take two weeks to complete. In the first week, you wrote 50% of the code. If you submit it immediately, the incomplete code library will prevent others from working. If you wait until all the code is written before submitting, there is a huge risk of losing progress every day.

Now with branches, you don't have to worry. You create a branch that belongs to you, which others cannot see, and they continue to work on the original branch. You work on your own branch and submit it whenever you want. When the development is complete, you merge it into the original branch at once. This way, it is both safe and does not affect the work of others.

1. Create and switch to a new branch: `git switch -c branch_name`
   - `-c` means create and switch branches
2. View the current branch: `git branch`
3. Merge the content of the new branch into master: `git merge branch_name`
   - Switch to the branch to be merged first, and then use the merge command (example: switch to master first, then execute the above command)
   - When Git cannot automatically merge branches, conflicts must be resolved first. After resolving the conflict, submit it and complete the merge.
   - Resolving conflicts means manually editing the files that Git failed to merge to the content we want, and then submitting them.
4. Delete a branch: `git branch -d dev`
5. Disable Fast forward merge: `git merge --no-ff -m "commit text" branch_name`
   - Because this merge creates a new commit, the `-m` parameter is added to write the commit description.
   - In Fast forward mode, when the branch is deleted, the branch information will be lost.

## GitHub Roaming Guide

With the help of the GitHub platform, we can discover a variety of open source projects and build an open source world with developers from all over the world.
When we discover an excellent open source project, we can first fork it to our own GitHub account (so that we have read and write permissions), and then clone it to our local computer for development using SSH.
After development is complete, we can initiate a pull request on GitHub. If the original project owner thinks your changes are appropriate, they will be merged into the existing open source project.

### GitHub CLI

GitHub CLI is a command-line tool for GitHub that brings pull requests, issues, and other features to the command line.
Download link: [**cli.github.com**](https://cli.github.com/)
GitHub CLI is currently in beta and worth a try.

## References and Acknowledgments

- [Git Tutorial - Liao Xuefeng](https://www.liaoxuefeng.com/wiki/896043488029600)
- [How to Use Git for Branch Management in Real Projects](https://blog.csdn.net/ShuSheng0007/article/details/80791849)
- [A Successful Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
- [git-cheatsheet.pdf](https://github.com/linyuxuanlin/File-host/blob/main/software-development/git-cheatsheet.pdf)
- [Pro Git](https://git-scm.com/book/zh/v2)
- [GitHub CLI - Manual](https://cli.github.com/manual/)
- [More than 20 Beautiful Pictures Take You into the Door of Git](https://mp.weixin.qq.com/s/oTtMQFEI9J5ymqt6SQ0PFg)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
