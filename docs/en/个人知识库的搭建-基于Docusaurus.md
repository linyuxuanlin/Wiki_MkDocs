# Building a Personal Knowledge Base - Using Docusaurus

Continuing from the previous article, [**Why You Need a Knowledge Base**](https://wiki-power.com/%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BD%A0%E9%9C%80%E8%A6%81%E4%B8%80%E4%B8%AA%E7%9F%A5%E8%AF%86%E5%BA%93), this article will provide a detailed guide on setting up a knowledge base using the Docusaurus framework.

Before we dive into this article, please ensure that you are prepared with:

- Access to the internet
- Flexibility to adapt
- Some basic knowledge of English

## Configuring Your Local Environment

### Installing Node.js

Visit the [**Node.js official website**](https://nodejs.org/zh-cn/) to download and install Node.js.

### Setting up VS Code

We will use VS Code as our local editor for modifying the website framework and writing articles.

First, download and install VS Code from the [**VS Code official website**](https://code.visualstudio.com/).

After installing the software, you can optionally install the following two plugins:

- [**Chinese (Simplified) Language Pack**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans): This plugin will localize the VS Code interface into Chinese.
- [**Markdown All in One**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): This plugin provides enhanced support for Markdown syntax.

Once you have installed the plugins, you may need to restart VS Code as prompted.

For more detailed configuration instructions, you can refer to this article on [**VS Code Productivity Guide - Environment Setup**](https://wiki-power.com/VSCode%E7%94%9F%E4%BA%A7%E5%8A%9B%E6%8C%87%E5%8D%97-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE).

### Installing the Docusaurus Framework

Navigate to the directory where you want to create your website project.

For example, if you want to create a knowledge base project in a folder named "wiki" on your D drive, open VS Code, go to `File` > `Open Folder`, select your D drive, and choose the "wiki" folder.

Initialize your website using npx:

```shell
npx @docusaurus/init@latest init [name] [template]
```

For instance, if your website project folder is named "wiki," replace `[name]` with "wiki," and according to the [**official documentation**](https://v2.docusaurus.io/docs/installation#scaffold-project-website), you can replace `[template]` with "classic" as the website template theme. Therefore, the command you would execute is:

```shell
npx @docusaurus/init@latest init wiki classic
```

Inside VS Code, open the terminal using the shortcut `Ctrl` + <code>`</code>, paste the command above, and press Enter. Be patient as it loads.

Once the loading is complete, switch to the website's folder directory in the terminal:

```shell
cd [name]
```

Replace `[name]` with the name of your website project folder, such as "wiki," which we used in the previous step.

Next, run the following command:

```shell
npm run start
```

This will deploy the website locally. After the deployment process is complete, it will automatically open the website in your browser at [**localhost:3000**](localhost:3000). If everything goes smoothly, you will see that the website has been successfully generated.

## Deploying the Website to the Cloud

In the previous step, we successfully generated the website, but it is currently only deployed locally and inaccessible from the internet. We need to deploy the website to a cloud server so that other users can access it from anywhere on the internet.

### Register a GitHub Account

Go to the [**GitHub official website**](https://github.com/join) and register for a GitHub account.

### Install Git

Download Git software from the [**official Git website**](https://git-scm.com/downloads) and complete the installation.

Restart VS Code, open the terminal, and paste the following commands to initialize Git:

```shell
git config --global user.name "username"
git config --global user.email "email@example.com"
```

Replace `"username"` with your Git commit username, which is recommended to be the same as the username you just registered on GitHub. For example, I replaced it with `linyuxuanlin`. Similarly, replace `"email@example.com"` with the email you used for your GitHub registration.

For more detailed configuration instructions, you can refer to this [**Git Learning Notes**](https://wiki-power.com/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0) article.

### Configure the Project Repository in VS Code

To be able to push to the GitHub server in the next steps, we need to configure the project's Git repository within VS Code and upload it to GitHub.

In VS Code, use the shortcut `Ctrl` + `Shift` + `G` to switch to the source code management interface, initialize the project's Git repository, and make the initial commit.

Then, use the shortcut `Ctrl` + `Alt` + `S` to push the local Git repository to GitHub (follow the prompts to log in to your GitHub account).

### Deploy the Website to the Vercel Cloud

The functionality of Vercel is similar to GitHub Action + GitHub Pages, which provides automatic continuous deployment and static website hosting. We choose Vercel because the static websites generated by Vercel tend to load faster for users in China compared to GitHub Pages.

First, visit the [**Vercel GitHub login page**](https://github.com/login?client_id=Iv1.9d7d662ea00b8481&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3DIv1.9d7d662ea00b8481%26scope%3Dread%253Auser%252Cuser%253Aemail%26state%3DFdx6thivZ89LeAihPfRiiYf9), and use your GitHub account to register for a Vercel account.

After completing the registration, click on "New Project" on the website, and import the corresponding repository from GitHub (for example, the "wiki" repository we created earlier). You may need to log in to GitHub again as prompted. Once imported, simply click "Next" and the website will be deployed quickly.

## Summary

In this article, we've achieved both local and cloud deployment of a knowledge base based on Docusaurus. If you encounter any issues during this process, feel free to reach out to me on [**WeChat**](https://wiki-power.com/WeChat) for feedback. In the next article (to be updated), I will provide a detailed explanation of personalized configuration.

## References and Acknowledgments

- [Docs·Docusaurus](https://v2.docusaurus.io/docs/)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.