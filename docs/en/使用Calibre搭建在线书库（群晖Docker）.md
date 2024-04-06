# Building an Online Book Library with Calibre (Synology Docker)

Learn how to set up an online book library using Calibre-web (Docker) on your Synology NAS.

![Image](https://media.wiki-power.com/img/20210429125418.png)

Compared to the traditional method of using folders, book library management systems like Calibre, which are open source, offer a wide range of features, including online reading, downloading, format conversion, email delivery, and removing duplicate books. Calibre-web is a Docker image based on Calibre, making it convenient to deploy a book library on servers like Synology.

## Creating the Initial Folder

First, create a folder for your library resources. I created a shared folder named `book` directly in the root directory of the disk:

![Image](https://media.wiki-power.com/img/20210429214028.png)

Correspondingly, create a folder named `calibre-web` within the `docker` folder. This folder is specifically for storing the configuration files for the Docker image.

## Creating a Container

Open Synology's Docker package, search for `johngong/calibre-web` in the registry, and double-click to download. Initialize the container and navigate to the advanced settings.

On the "Volume" page, add mapped folders with mount paths `/library` and `/config`:

![Image](https://media.wiki-power.com/img/20210429214908.png)

On the "Port Settings" page, add port mapping, primarily mapping the internal container's `8083` port to an external port, such as `5004`.

![Image](https://media.wiki-power.com/img/20210429215121.png)

Next, create and start the container.

## Running a Test

Open your Synology's local IP address followed by `:5004` to access the management interface. The default credentials are `admin` for both the username and password.

Please note that the book upload function is not enabled by default. You need to click on "Admin" in the top right corner, then go to "Basic Configuration" > "Enable Upload" to enable book uploads.

![Image](https://media.wiki-power.com/img/20210429215628.png)

## Enabling HTTPS

### Using Synology's Built-In Reverse Proxy (Recommended)

For detailed instructions, you can refer to the article [**Setting Up HTTPS Access with Synology's Built-In Reverse Proxy**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE).

### Directly Adding Certificate Method

Copy a duplicate of the certificate and key files you obtained to the `docker/calibre-web/` directory.

Then, within Calibre-web, go to "Admin" > "Basic Configuration" > "Server Configuration" and configure the paths for the SSL certificate and key files (e.g., mine are `/config/wiki-power.com.cer` and `/config/wiki-power.com.key`). Afterward, click "Save."

This will enable HTTPS access.

## References and Acknowledgments

- [Installing the Calibre-web Book Management System on Synology Docker](https://www.chrno.cn/index.php/docker/15.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
