# Automatically Updating Containers on Synology Docker with Watchtower

Automatically update containers on Synology Docker using Watchtower.

## Downloading the Image in Synology Docker Application

Open the Synology Docker package and download the `containrrr/watchtower` image.

## Configuring Watchtower in Task Scheduler

Navigate to Synology's `Control Panel` - `Task Scheduler` - `Create` - `Scheduled Task` - `User-defined script`. Then, fill in the configuration as shown in the images below:

![Configuration Image 1](https://media.wiki-power.com/img/202301092319956.png)

![Configuration Image 2](https://media.wiki-power.com/img/202301092321592.png)

The script in question is as follows:

```shell
docker run --rm --name watchtower -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --cleanup --run-once calibre-web freshrss code-server
```

Please note that the last part of the script, "calibre-web freshrss code-server," represents the names of the containers to be updated. You should replace these with the names of the containers you wish to update, or leave it blank to update all containers.

Save and execute the script to achieve batch scheduled updates of Docker containers.

## References and Acknowledgments

- [How to Gracefully Update Synology Docker Containers with a Single Command - Watchtower Tutorial](https://post.smzdm.com/p/awzggnqp/)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
