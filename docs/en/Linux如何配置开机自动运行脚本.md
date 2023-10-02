# How to Configure Automatic Script Execution on Linux Startup

## For Systems Using SysV init

Note: The following method is applicable for Linux distributions using SysV init (such as Ubuntu 18.04 and newer versions, or Debian). For distributions using Systemd (such as Ubuntu 18.04 and newer versions), please use the `systemctl` method to manage startup services.

Suppose we need to automatically execute the script `xxx.sh` on startup. First, create a startup script in the `/etc/init.d` directory, for example, named `autorun.sh`:

```shell
sudo nano /etc/init.d/autorun.sh
```

Add the script you need to automatically execute on startup:

```bash title="autorun.sh"
#!/bin/bash
/path/to/xxx.sh  # Modify to the specific path
```

Add the `autorun.sh` script to the system's startup services:

```shell
sudo update-rc.d autorun.sh defaults
```

Set the `autorun.sh` script to start on boot:

```shell
sudo update-rc.d autorun.sh enable
```

This way, the `autorun.sh` script will automatically run after restarting.

## For Systems Using Systemd

If your Linux distribution uses Systemd as the startup manager (such as Ubuntu 18.04 and newer versions), you can use the `systemctl` command to set up automatic startup.

Suppose we need to automatically execute the script `xxx.sh` on startup. First, create a Unit file that describes the service you want to auto-start, such as `autorun.service`:

```shell
sudo nano /etc/systemd/system/autorun.service
```

In the Unit file, define the configuration of your service. Here is an example:

```service title="autorun.service"
[Unit]
Description=My Service
After=network.target
[Service]
ExecStart=/path/to/xxx.sh
[Install]
WantedBy=default.target
```

The parameters in the above code are:

- `Description`: describes your service.
- `After`: specifies which other services your service should start after. For example, `network.target` means your service should start after the network service.
- `ExecStart`: specifies the path to the script or command you want to execute.
- `WantedBy`: specifies the target your service should be started with. `default.target` means your service should start when the default target starts.

Save and close the file, then run the following command to reload the systemd configuration:

```shell
sudo systemctl daemon-reload
```

Enable your service with the following command:

```shell
sudo systemctl enable autorun.service
```

Finally, start your service with the following command:

```shell
sudo systemctl start autorun.service
```

Now your service is set to run automatically on system startup. You can restart the system to verify that the service starts properly.

---

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.