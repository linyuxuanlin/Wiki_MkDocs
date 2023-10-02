# Accelerating Pages Service with Vercel

Recently, my blog (hosted on GitHub Pages) was blocked in China, which was a big problem since most of my audience is from there. Typically, the only solutions are to buy a server or migrate to OSS, but both options are complicated and expensive. Luckily, I discovered the amazing tool Vercel, which allowed me to continue writing my blog with ease.

## Advantages of Vercel

- Free custom domain with HTTPS support
- Provides Serverless services
- Offers Google Cloud and AWS nodes, with Hong Kong and Taiwan nodes for faster access in China
- Free quota of 20 GB, which is sufficient
- No limit on the number of sites or Serverless APIs
- Serverless supports Node.js, Go, Python, and Ruby
- Supports now.sh CLI, GitHub, GitLab, and Bitbucket import/deployment

## Usage

Since the configuration steps are not complicated, I will provide a brief explanation in text only.

1. Log in directly with your GitHub account
2. Import your site (directly from your GitHub Repo)
3. Configure the deployment command (can be left blank for VuePress platform)
4. Configure the output path (for VuePress, it is `docs/.vuepress/dist`)
5. Set the production branch to `gh-pages` in the settings
6. Bind your domain name

## Note

Make sure to write a commit message with more than one character, otherwise it will not be deployed.

## References and Acknowledgments

- [Vercel](https://vercel.com/)
- [ZEIT (Vercel) now.sh Free Deployment of Blog Websites, Supporting Serverless Python Go Node.js](https://wivwiv.com/post/zeit-use-guide/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.