# Building an RSS Generator with RSSHub on Synology Docker

Deploy RSSHub on Synology Docker to generate RSS feeds for all kinds of content.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504105215.png)

## Deployment on Synology Docker

Open Synology Docker, download the `diygod/rsshub` image, double-click to start, check "Enable auto-restart", and then go to "Advanced Settings".

On the "Port Settings" page, manually set the local port corresponding to container port 1200 (e.g. I set it to `8004`):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504085806.png)

After completing the configuration, start the container. If you can see the RSSHub page by entering Synology local IP:8004, the installation is successful.

## Usage

For detailed usage, please refer to the [**RSSHub official documentation**](https://docs.rsshub.app/).

As a simple example, in the official documentation, the method for generating "Now Playing Movies" on Douban is as follows:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504104630.png)

Therefore, using `yourdomain/douban/movie/playing` can generate your own RSS feed on your server.

It is recommended to use Synology's built-in reverse proxy to achieve HTTPS encrypted access. For specific tutorials, please refer to the article [**Implementing HTTPS Access with Synology's Built-in Reverse Proxy**](https://wiki-power.com/en/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE).

## Automatic Detection of Routes with RSSHub Radar

[**RSSHub Radar**](https://github.com/DIYgod/RSSHub-Radar) is a browser extension that helps you quickly discover and subscribe to RSS and RSSHub on the current website.

Fill in the custom address on its settings page to use it.

## References and Acknowledgments

- [RSSHub official documentation](https://docs.rsshub.app/)
- [Install RSSHub in Synology using Docker](https://immwind.com/use-docker-install-rsshub-in-synology)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.