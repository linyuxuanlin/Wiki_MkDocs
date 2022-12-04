---
id: 用Vercel加速Pages服务
title: 用 Vercel 加速 Pages 服务
---

前一段时间，我的博客（托管在 GitHub Pages）被墙了。因为受众大多是国内用户，所以问题很大。  
一般来说，解决方法只有买服务器 / 迁移到 OSS. 但方法都偏复杂，也费钱。
恰巧碰上了这个神器 Vercel. 于是又可以愉快地写博客了。

## Vercel 的优势

- 免费自定义域名，支持 HTTPS
- 提供 Serverless 服务
- 提供 Google Cloud 与 AWS 节点，有香港与台湾节点，国内访问速度还可以
- 免费额度有 20 GB，够用
- 不限站点与 Serverless API 数量
- Serverless 支持 Node.js，Go，Python，Ruby
- 支持 now.sh CLI，GitHub，GitLab，Bitbucket 导入 / 部署

## 用法

因配置步骤不复杂，所以只以文字进行简要的说明。

1. 用 GitHub 账号直接登录
2. 导入站点（直接导入 GitHub Repo）
3. 配置部署指令（VuePress 平台可放空）
4. 配置输出路径（VuePress 是 `docs/.vuepress/dist`）
5. 要在设置里面把生产分支设为 `gh-pages`
6. 绑定域名

## 注意

每次 commit message 要写超过 1 个字符，否则不会部署。

## 参考与致谢

- [Vercel](https://vercel.com/)
- [ZEIT (Vercel) now.sh 免费部署博客网站，支持 Serverless Python Go Node.js](https://wivwiv.com/post/zeit-use-guide/)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

