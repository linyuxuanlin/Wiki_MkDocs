# Setting Up an RSS Generator with RSSHub on Synology Docker

Deploy RSSHub service on Synology Docker to generate RSS subscription sources for various peculiar content.

![RSSHub](https://media.wiki-power.com/img/20210504105215.png)

## Deployment on Synology Docker

Open the Synology Docker Package, download the `diygod/rsshub` image, double-click to start, select "Enable auto-restart," and then access "Advanced Settings."

On the "Port Settings" page, manually set the local port corresponding to container port 1200 (e.g., I set it as `8004`):

![Port Settings](https://media.wiki-power.com/img/20210504085806.png)

After completing the configuration, start the container. Enter your Synology's local IP:8004, and if you can see the RSSHub page, consider the installation successful.

## Usage Instructions

For detailed usage instructions, please refer to the [**RSSHub Official Documentation**](https://docs.rsshub.app/).

As a simple example, in the official documentation, you can find the method to generate the RSS feed for "Now Playing Movies" on Douban as follows:

![RSS Generation](https://media.wiki-power.com/img/20210504104630.png)

So, you can use `your_domain/douban/movie/playing` to generate RSS feeds using your own server.

It's recommended to use Synology's built-in reverse proxy to implement HTTPS encryption. You can find a specific tutorial in the article [**Enabling HTTPS Access with Synology's Built-In Reverse Proxy**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE).

## Automatic Detection of Routes with RSSHub Radar

[**RSSHub Radar**](https://github.com/DIYgod/RSSHub-Radar) is a browser extension that helps you quickly discover and subscribe to RSS feeds from current websites and RSSHub.

You can use it by entering custom addresses in its settings.

## References and Acknowledgments

- [RSSHub Official Documentation](https://docs.rsshub.app/)
- [Installing RSSHub on Synology with Docker](https://immwind.com/use-docker-install-rsshub-in-synology)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
