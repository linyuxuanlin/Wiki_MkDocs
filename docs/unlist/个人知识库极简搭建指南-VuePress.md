---
id: 个人知识库极简搭建指南-VuePress
title: 个人知识库极简搭建指南 - VuePress
---

我们所用到的技术栈：

- 框架：VuePress
- 托管及自动编译：GitHub
- 部署：Vercel

为了让不想折腾的小伙伴，能够快速搭起一个知识库，所以这篇教程顺时而生。  
至于某些详细步骤的操作，后续会慢慢补充完善，理解万岁！搭建知识库也就啪那一下，很快的！

## 第一步：配置域名

咱上 GoGaddy / 腾讯云 / 阿里云买个自己的域名，咱 **假设** 你买的域名是 `xx.com` , 记住它。  
（国内买的一般要提交实名信息，按着提示操作就行了）

修改域名解析：

| 主机记录 | 记录类型 |      记录值      | TTL（秒） |
| :------: | :------: | :--------------: | :-------: |
|    @     |  CNAME   | `alias.zeit.co.` |    600    |

没提到的项视为默认。

## 第二步：克隆仓库

（这里以我的知识库作为模板）打开链接：[**linyuxuanlin/Wiki-book**](https://github.com/linyuxuanlin/Wiki-book)  
将仓库克隆到本地。咱 **假设** 你的仓库名字为 `xxx/Wiki-book`（其中 `xxx` 是你的 GitHub 用户名），记住它。

## 第三步：修改变量

在克隆下来的仓库内，全局搜索以下变量，并把它们改掉：

- `wiki-power.com`：替换为你的自定义域名 `xx.com`
- `linyuxuanlin/Wiki-book`：替换为你的 GitHub 用户名和仓库名 `xxx/Wiki-book`
  - （如果仓库名称不为 `Wiki-book`，则需全局搜索并修改对应的仓库名）
- `master`：替换为 `main`.

## 第四步：配置部署

本来可以直接部署在 GitHub Pages 的，由于某些不可描述的原因，国内网络访问可能出问题，所以这里我们借助第三方部署工具 Vercel.

点开 [**vercel.com**](https://vercel.com/) , 直接使用 GitHub 账户完成注册。  
完成之后，在个人主页点击 `Import Project（导入项目）` 按钮，把 GitHub 仓库的 **完整链接** 粘贴进去：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20201122232933.jpg)

接下来提示 `Please select the directory（请选择目录）` ，直接点 `Continue` 继续就行。

在接下来的页面，我们只需在 `OUTPUT DIRECTORY（输出目录）` 处，填入 `docs/.vuepress/dist` 即可：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20201122235715.jpg)

在提示 **部署成功** 后，我们点击页面右上角的 `Settings（设置）` , 切换到 `Domains（域名）` 栏目，在输入框内填写你买的域名 `xx.com` ，点击 `Add（添加）`。

然后我们切换到 `Git（没得翻译）` 栏目，滚轮下滑到 `Production Branch（生产分支）`，选择 `Custom` , 填写 `gh-pages` , 如下图：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20201122232843.jpg)

点击 `Save` 保存。

## 胜利在望！

在本地仓库随便做点改动（注意：Commit message 不要少于 4 个英文字符），`Push` 到 GitHub（目的是生成一次 Commit 让 GitHub Action 重新编译到 gh-pages 分支，再让 Vercel 完成重新部署。

等泡一杯茶的时间，访问你买的域名 `xx.com` , 如果你能够顺利看到这个画面：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20201122233838.jpg)

恭喜你！拥有了一个属于自己的知识库！

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

