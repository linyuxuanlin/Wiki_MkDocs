---
id: 基于docsify搭建个人Wiki
title: 基于 docsify 搭建个人 Wiki
---


## 背景

笔者一直都有撰写博客的传统，自 2015 年以来，历经 Wordpress, Hexo, Jekyll, Bitcron ,GitBook 等博客工具，甚至尝试用 GitHub issues 直接撰写文章，效果始终不理想。而最近发现的 docsify 博客工具，辅以一系列非常规操作，似乎是博客撰写的最终归宿。

## 搭建 Wiki 的意义

假设你自古以来是本博客的读者，你会发现笔者每更换一次博客平台，都会重复念叨这个问题。

### 为什么我们需要一个博客

1. 防止遗忘
2. 体系化归纳知识
3. 用输出倒逼输入

好记性不如烂笔头，知识需要归纳、总结、沉淀。而输出总是比输入难的，在这个过程中，也加深了对知识的掌握和理解。这是一个反刍，咀嚼和表达的过程。知识经历了这个过程，才能真正被我们所吸收。

![学习保持率金字塔图](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200128214300.png)

### 什么是独立博客

独立博客的特征：

- 数据自由
- 样式自由

举个例子：

- **非独立平台**：知乎、简书、CSDN、公众号、博客园等
- **独立博客**：数据部署在自己服务器上 / 托管在开源代码仓库上。我的网站就算是独立博客。

独立博客的弊端：

- 有一定的门槛
- 流量获取渠道缺失

独立博客的优势：

- 数据完全由自己掌握
- 样式完全由自己定义

虽然优势看上去平平无奇，但重要性显而易见。当我们在非独立平台上写作时，这几个问题可能时时困扰着你：

1. 我辛辛苦苦写的回答怎么就被折叠了呢？我的文章怎么就被 `政治敏感` 了呢？
2. 怎么会有如此多的广告，污染我的文章版面？
3. 我的读者大多是躲在被窝里阅读的，我想加一个暗色模式，保护读者的眼睛，平台却没有这个功能？（微信公众号）
4. 我想介绍一个不错的网站，却不允许我引用外部链接？（微信公众号）
5. 我想换个平台，可我的文章数据该如何完全导出呢？

至于独立博客，则不存在以上的问题，数据牢牢掌握在自己手中。只要你妥善保管好数据（异地备份、托管于 GitHub、甚至把字刻在石头上），即使平台倒闭、天荒地老、太阳系被二向化，你辛辛苦苦写的文章都不会丢失。  
而至于门槛，虽然我们提倡自己动手，丰衣足食，但有了各路大神先行踩坑，总结出来的解决方案对零基础小白来说，门槛几乎为零。

总会有一些人，需要的是一个安静、内向与创作的互联网。

### Wiki 与 Blog 形式之争

关于这个问题，笔者先前用的是 Blog 的形式，可以参考一下之前的站点（如果它还活着）：https://yxrct.com/  
而现在这个站点，采用的是 Wiki 的形式。于我个人而言，Wiki 更有利于构建知识体系，本篇教程也着重于此。

引用之前写过的文字：

> Blog 的形式，更类似于微信公众号，是一种信息流，时效性比较强，而且也不便于修改和归档，而我们知道，知识是要不断反刍，时而翻阅的，信息流给读者带来了便利，却不利于作者自身的提高。
>
> Wiki 的形式则像档案库。侧边栏目录分出不同的类别，以及所包含的文章。这样简洁明晰的结构很方便检索，也更像是在翻阅一本书的不同章节。
>
> 更多的时候，博客作为一个比较正式的对外展示载体，一些琐碎而不可或缺的知识不适合单独成文，而体系化的知识，却又从这些零散的知识点积累而来，这时，用 Wiki 就很合适了。
>
> 积土成山，风雨兴焉；积水成渊，蛟龙生焉。从某些角度来说，Blog 锋芒毕现，Wiki 厚积薄发。

## docsify 的优势

- 不会将 `.md` 转成 `.html` 文件，所有转换工作都是在运行时进行
- 容易使用并且轻量 (~19kB gzipped)
- 主题样式简洁且可自定义
- 丰富的插件及 API 支持
- 可部署在服务器上，也可托管于 GitHub / Coding Pages

选择 docsify，笔者主要是看中这几点：

1. 可以搭建 Wiki 形式的网站
2. 可托管在 GitHub Pages, 免费且数据永不丢失
3. 主题样式清爽
4. 丰富且实用的插件

## 准备工作

工欲善其事，必先利其器。
本篇教程虽然面向零基础，但有些技能还是需要读者具备的：

1. 英语不能太差
2. Markdown 语法：我们用它来写文章，它有什么优势以及怎么用，请自行了解
3. 善用搜索引擎（最好是 Google）：难道你愿意接受百度上少得可怜的中文结果，并接受广告轰炸吗？
4. Git / GitHub 基本使用：下文将会普及
5. （非必须）前端语言（HTML / CSS / Javascript），基本的命令行操作

## 快速部署

如果你不想折腾，只想好好写文章，那么以下是捷径：

1. 下载软件：[**GitHub Desktop**](https://desktop.github.com/)
2. 在 GitHub 上注册一个账户：https://github.com/
3. 直接搬走我网站的样式
   1. 打开 https://github.com/linyuxuanlin/Wiki
   2. 点击右上角 `Fork` 按钮，待页面刷新后继续
   3. 点击右上角小齿轮图标的 `Settings` 按钮，将 `Repository name` 从 `Wiki` 改为 `你的 GitHub 用户名。github.io`（如果忘了刚刚设置的用户名，可以看看页面左上角），然后点击 `Rename` 按钮，待页面刷新后继续
   4. 点击绿色按钮 `Clone or download`, 然后选择 `Open in Desktop`
   5. 在  GitHub Desktop  弹出的窗口内更改  `Local Path`，选择你想保存的路径，点击确认
4. 打开文件 `你保存的路径/index.html`（找个适合自己的编辑器例如 VScode），利用 `Ctrl + H` 搜索替换：
   1. 搜索 `Power's Wiki`（包括下方的 `Power\'s Wiki`），改为你自己网站的名字（注意如果 Wiki 标题 `'s` ，需要加转义字符 `\'s`）
   2. 删除 `你保存的路径/CNAME` 文件
   3. 其他设置项的更改稍后再说
5. 保存文档，打开 GitHub Desktop, 可以看到有修改记录。我们在下方的 `Summary` 一栏里填写本次提交的摘要（填什么都行），点击最下方蓝色按钮 `Commit to master`，然后点击右边蓝色按钮 `Push origin`，等待提交完成
6. 我们回到刚才打开的网页，点击右上角小齿轮图标的 `Settings` 按钮，滚动页面找到 `GitHub Pages` 栏目，如果没问题的话，可以看到提示 `Your site is ready to be published at https://xxx.github.io/.`，点击链接就可以访问你的网站了

## 写文章的流程

1. 直接在相应目录创建 `文章标题。md`（参照我网站的目录结构），用 Markdown 写作
2. 在 `siderbar.md` 内更新这篇文章的路径
3. 在 GitHub Desktop 软件内进行 Commit & Push 操作，文章更新完成

## 拓展

### 文档

- [**docsify 官方文档（中文）**](https://docsify.js.org/#/zh-cn/)：有问题多看官方文档
- [**docsify-themeable**](https://jhildenbiddle.github.io/docsify-themeable/#/)：一个主题插件

### 工具

- [**docsify-cli**](https://docsify.js.org/#/zh-cn/quickstart)（推荐使用）：用于本地预览文档网站

### 常用插件

- **全文搜索**：已默认配置并开启，详见文档
- **谷歌统计**：已默认配置并开启，需修改 `track id` ，详见文档
- **Gitalk**：墙内可用且评论不受审查。已默认配置并开启，需以下操作：
  1. 打开链接 [**Register a new OAuth application**](https://github.com/settings/applications/new)
  2. 填写信息。`Application name` ,`Homepage URL` 与 `Authorization callback URL` 都填写 `你的用户名。github.io`, 然后点击注册
  3. 记下生成的 `clientID` 和 `clientSecret`
  4. 打开 `index.html`, 搜索并更新 `clientID` 与 `clientSecret`, `repo` 的参数改为 `你的用户名。github.io`, `owner` 与 `admin` 内相应字符改为 `你的用户名`.（注意冒号后保留一空格，且标点符号为英文字符）
  5. Commit & Push

### 图床

网站图片的解决方案参考 [**Github+jsDelivr+PicGo 打造稳定快速、高效免费图床**](https://www.itrhx.com/2019/08/01/A27-image-hosting/).

## 总结

与其临渊羡鱼，不如退而结网。  
写作，是为了更好地思考。

## 参考与致谢

- [docsify 官方文档（中文）](https://docsify.js.org/#/zh-cn/)
- [docsify-themeable](https://jhildenbiddle.github.io/docsify-themeable/#/)
- [处理 Gitalk 中由于文章 URL 过长导致的 Validation Failed (422)](<https://priesttomb.github.io/%E6%97%A5%E5%B8%B8/2018/02/12/%E5%A4%84%E7%90%86Gitalk%E4%B8%AD%E7%94%B1%E4%BA%8E%E6%96%87%E7%AB%A0URL%E8%BF%87%E9%95%BF%E5%AF%BC%E8%87%B4%E7%9A%84Validation-Failed(422)/>)
- [Github+jsDelivr+PicGo 打造稳定快速、高效免费图床](https://www.itrhx.com/2019/08/01/A27-image-hosting/)
- [教育杂想](https://bug-hunter.baklib.com/unclassified/863b)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

