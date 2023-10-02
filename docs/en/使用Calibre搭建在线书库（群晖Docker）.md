# Building an Online Book Library with Calibre (Synology Docker)

How to build an online book library using calibre-web (Docker) on a Synology NAS.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429125418.png)

Compared to the traditional method of using folders, book library management methods represented by open-source Calibre can provide richer features such as online reading, downloading, format conversion, email pushing, and removing duplicate books. Calibre-web is a Docker image based on Calibre, which allows us to easily deploy the book library on servers like Synology.

## Creating the Initial Folder

First, create a book library resource folder. Here, I directly created a shared folder named `book` in the root directory of the disk:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429214028.png)

Correspondingly, create a folder named `calibre-web` in the `docker` folder, specifically for storing the configuration files of the Docker image.

## Creating the Container

Open Synology's Docker suite, search for `johngong/calibre-web` in the registry, double-click to download, and initialize the container. Click on advanced settings.

On the `Volume` page, add mapped folders, and the mounting paths are `/library` and `/config` respectively:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429214908.png)

On the `Port Settings` page, add port mapping, mainly mapping the internal `8083` port of the container. Here, I chose `5004`.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429215121.png)

Then, create and start the container.

## Running the Test

Open the Synology internal IP:5004 to open the management interface. The default account is `admin`, and the password is `admin123`.

It should be noted that book upload function is not enabled by default. You need to click on `Admin` - `Edit Basic Configuration` - `Enable Upload` in order to enable book upload function.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429215628.png)

## Enabling HTTPS

### Using Synology's Built-in Reverse Proxy (Recommended)

For specific instructions, please refer to the article [**Implementing HTTPS Access with Synology's Built-in Reverse Proxy**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE)

### Directly Adding Certificate Method

Copy the obtained certificate and key files to the `docker/calibre-web/` directory.

Then, in calibre-web, click on `Admin` - `Edit Basic Configuration` - `Server Configuration`, and configure the path of the SSL certificate and key files (for example, mine is `/config/wiki-power.com.cer` and `/config/wiki-power.com.key`), and then click on Save.

This will enable HTTPS access.

## References and Acknowledgments

- [Synology Docker Installation of Calibre-web Book Management System](https://www.chrno.cn/index.php/docker/15.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.