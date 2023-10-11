# Building a Password Manager (Synology Docker) with Bitwarden

Note: Due to the renaming of the bitwarden_rs image and the incompatibility of the Bitwarden official browser extension with older versions, which prevents login, please replace `bitwardenrs/server` with `vaultwardenrs/server` in the following text and ensure that the version is not lower than 1.27.0!

This article introduces how to deploy the cross-platform password management server Bitwarden on your own Synology with Docker for private use.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503221838.png)

Currently, there are various password manager solutions, such as 1Password, Lastpass, KeePass, and Bitwarden, each with its own advantages and disadvantages. My requirements are multi-device synchronization, open-source self-deployment, automatic filling, and a beautiful interface. Therefore, I chose to deploy the Bitwarden service on my own Synology.

## Deploying on Synology Docker

### Create a folder to store data

Create a folder to store Bitwarden data (e.g. `docker/bitwarden`) under the `docker` directory.

### Download the image and configure the container

Open the Synology Docker Suite, download the `bitwardenrs/server` image, double-click to start, check `Enable auto-restart`, and then enter `Advanced Settings`.

On the `Volume` page, configure the mounted folder, click `Add Folder`, select the local `docker/bitwarden` path, and fill in the mounting path as `/data` (which cannot be changed by default):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503211711.png)

On the `Port Settings` page, manually set the local port corresponding to container port 80 (e.g. I set it to `8003`):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503211759.png)

After completing the configuration, start the container. Enter the Synology local IP:8003, and we can see the Bitwarden login page. However, when we create an account and log in, we will see the following prompt:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503212146.png)

This is because the Docker container itself does not provide https port configuration, and Bitwarden can only log in through https (SSL encryption to prevent man-in-the-middle attacks). Therefore, we must use Synology's built-in reverse proxy service to access the internal http port through https. For specific tutorials, please refer to the article [**Implementing HTTPS Access with Synology's Built-in Reverse Proxy**](https://wiki-power.com/en/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE).

## Multi-device Usage

You can download various versions of the Bitwarden client from the Bitwarden official [**download page**](https://bitwarden.com/download/).

### Desktop Client

It is recommended to use the browser extension [**Bitwarden - Free Password Manager**](https://chrome.google.com/webstore/detail/bitwarden-free-password-m/nngceckbapebfimnlniiiahkandclblb) directly.

When logging in, click the small gear icon in the upper left corner to enter the settings:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503215149.png)

In the "Self-hosted Environment", fill in the Synology NAS IP: external port in the "Server URL" to log in normally.

If needed, you can also download the desktop client to use.

### Mobile

Simply download the Bitwarden App from the AppStore or various app stores. You also need to configure the self-hosted environment on the login page, which is the same as the desktop version.

## Backup Password Database

There are two ways to backup the Bitwarden database:

1. Select "Export Password Library" on the web or client.
2. Directly backup the "data" folder.

## References and Acknowledgments

- [Synology NAS Advanced Services - Deploying Bitwarden Cross-Platform Password Manager with Docker](https://www.ioiox.com/archives/70.html)
- [Using Synology to Build a Third-Party Bitwarden Password Server](https://ppgg.in/blog/10271.html#comment-8463)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
