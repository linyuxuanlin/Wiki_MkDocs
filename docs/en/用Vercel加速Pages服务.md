# Speed up Pages service with Vercel

Recently, my blog (hosted on GitHub Pages) was blocked. This was a big problem because most of my audience is from China. Typically, the solutions to this issue are either buying a server or migrating to OSS. However, these methods are complex and expensive. Luckily, I came across this amazing tool called Vercel, which allows me to happily write my blog again.

## Advantages of Vercel

- Free custom domain with HTTPS support
- Provides Serverless service
- Offers Google Cloud and AWS nodes, including Hong Kong and Taiwan nodes for decent speed in China
- Free quota of 20 GB, which is sufficient
- No limit on the number of sites and Serverless APIs
- Serverless supports Node.js, Go, Python, and Ruby
- Supports now.sh CLI, GitHub, GitLab, and Bitbucket for importing and deploying

## Usage

Since the configuration steps are not complicated, I will provide a brief explanation in text form.

1. Log in directly with your GitHub account
2. Import your site (directly import from GitHub Repo)
3. Configure deployment settings (leave it empty for VuePress platform)
4. Configure output directory (for VuePress, it is `docs/.vuepress/dist`)
5. Set the production branch as `gh-pages` in the settings
6. Bind your domain

## Note

Make sure to write a commit message with more than 1 character, otherwise it will not be deployed.

## References and Acknowledgements

- [Vercel](https://vercel.com/)
- [ZEIT (Vercel) now.sh Free Deployment for Blog Websites, Supports Serverless Python Go Node.js](https://wivwiv.com/post/zeit-use-guide/)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.