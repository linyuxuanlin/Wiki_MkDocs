# Building a Personal Knowledge Base - Based on Docusaurus

Continuing from the previous article [**Why You Need a Knowledge Base**](https://wiki-power.com/en/%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BD%A0%E9%9C%80%E8%A6%81%E4%B8%80%E4%B8%AA%E7%9F%A5%E8%AF%86%E5%BA%93), this article will provide a detailed explanation on building a knowledge base based on the Docusaurus framework.

Before we begin, please ensure that you are prepared with:

- Access to a VPN
- Adaptability
- Basic knowledge of English

## Configuring the Local Environment

### Installing Node.js

Visit the [**Node.js website**](https://nodejs.org/en/) to download and install Node.js.

### Installing and Configuring VS Code

We will use VS Code as our local editor for modifying the website framework and writing articles.

First, download and install VS Code from the [**VS Code website**](https://code.visualstudio.com/).

After installing the software, we can choose to install the following two plugins:

- [**Chinese (Simplified) Language Pack**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans): Localizes the VS Code interface to Simplified Chinese
- [**Markdown All in One**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): Provides additional support for Markdown syntax

After installing the plugins, you may need to restart VS Code as prompted.

For more detailed configuration instructions, refer to [**VS Code Productivity Guide - Environment Configuration**](https://wiki-power.com/en/VSCode%E7%94%9F%E4%BA%A7%E5%8A%9B%E6%8C%87%E5%8D%97-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) (in Chinese).

### Installing the Docusaurus Framework

Navigate to the directory where you want to create the website project.

For example, if I want to create a folder named `wiki` on my D drive as the project for this knowledge base, I would select `File` - `Open Folder` in VS Code, click on the D drive, and select the `wiki` folder.

Initialize the website using npx:

```shell
npx @docusaurus/init@latest init [name] [template]
```

For example, if my website project folder is named `wiki`, I would replace `[name]` with `wiki`. According to the [**official documentation**](https://v2.docusaurus.io/docs/installation#scaffold-project-website), `[template]` refers to the theme of the website template, and we can replace it with `classic`. Therefore, the command we would execute is:

```shell
npx @docusaurus/init@latest init wiki classic
```

In VS Code, use the shortcut `Ctrl` + <code>`</code> to open the terminal, paste the above command, and hit enter. Wait patiently for the loading to complete.

Once loading is complete, use the following command in the terminal to navigate to the website folder directory:

```shell
cd [name]
```

Replace `[name]` with the name of your website project folder, for example, `wiki` in our previous step.

Next, execute the following command:

```shell
npm run start
```

This will deploy the website locally. Once the deployment process is complete, it will automatically open the website in your browser at [**localhost:3000**](localhost:3000). If everything goes smoothly, you should see that the website has been successfully generated.

## Deploying the Website to the Cloud

In the previous step, we successfully generated a website, but it was only deployed locally and could not be accessed from the internet. We need to deploy the website to a cloud server so that other users can access it from the internet.

### Register a GitHub account

Register a GitHub account on the [**GitHub website**](https://github.com/join).

### Install Git

Download Git software from the [**Git website**](https://git-scm.com/downloads) and complete the installation.

Restart VS Code, call up the terminal, and paste the following command to initialize Git:

```shell
git config --global user.name "username"
git config --global user.email "email@example.com"
```

Here, replace `"username"` with your Git commit username, which is recommended to be the same as the account name just registered on GitHub. For example, I replaced it with `linyuxuanlin`. `"email@example.com"` should also be replaced with the email registered on GitHub.

For more detailed configuration instructions, refer to this article on [**Git Learning Notes**](https://wiki-power.com/en/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0).

### Configure the project repository in VS Code

In order to push to the GitHub server later, we need to configure the project Git repository in VS Code and upload it to GitHub.

Use the shortcut `Ctrl` + `Shift` + `G` in VS Code to switch to the source code management interface, initialize the project Git repository, and make the first commit.

Then, use the shortcut `Ctrl` + `Alt` + `S` to push the local Git repository to GitHub (log in to the GitHub account as prompted).

### Deploy the website on Vercel cloud

The function of Vercel here is equivalent to GitHub Action + GitHub Pages, that is, automatic continuous deployment + static website display. Vercel is chosen because the static website it generates is much faster than GitHub Pages when accessed in China.

First, directly access the [**Vercel GitHub login page**](https://github.com/login?client_id=Iv1.9d7d662ea00b8481&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3DIv1.9d7d662ea00b8481%26scope%3Dread%253Auser%252Cuser%253Aemail%26state%3DFdx6thivZ89LeAihPfRiiYf9), and register a Vercel account with your GitHub account.

After completing this, click `New Project` on the webpage, import the corresponding repository on GitHub (such as the `wiki` repository we previously created), and you may need to log in to GitHub again as prompted. After importing, click `Next` all the way to continue, and the website can be deployed successfully soon.

## Summary

In this article, we have achieved local and cloud deployment of a knowledge base based on Docusaurus. If you encounter any problems during the process, you can contact me for feedback on [**WeChat**](https://wiki-power.com/en/WeChat). In the next article [to be updated], I will provide a detailed explanation of personalized configuration.

## References and Acknowledgments

- [Docs·Docusaurus](https://v2.docusaurus.io/docs/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.