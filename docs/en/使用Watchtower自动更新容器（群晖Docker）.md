# Automatically Updating Containers with Watchtower (Synology Docker)

Use Watchtower to automatically update containers on Synology Docker.

## Download the Image in Synology Docker Applications

Open Synology Docker Suite and download the `containrrr/watchtower` image.

## Configure Watchtower in Task Scheduler

Open Synology's `Control Panel` - `Task Scheduler` - `Create` - `Scheduled Task` - `User-defined script`, and then fill in the configuration according to the following pictures:

![](https://f004.backblazeb2.com/file/wiki-media/img/202301092319956.png)

![](https://f004.backblazeb2.com/file/wiki-media/img/202301092321592.png)

The script is as follows:

```shell
docker run --rm --name watchtower -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --cleanup --run-once calibre-web freshrss code-server
```

Note that the last part of the script `calibre-web freshrss code-server` is the name of the container that needs to be updated. Replace it with the name of the container you want to update, or leave it blank to update all containers.

Save and run the script to achieve batch scheduled updates of Docker containers.

## Reference and Acknowledgement

- [How to Use Watchtower to Update Synology Docker Containers with One Command](https://post.smzdm.com/p/awzggnqp/)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.