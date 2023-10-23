# How to Configure Automatic Startup of Scripts on Linux

## Applicable to Systems Using SysV Init

Note: The following method is suitable for Linux distributions that use SysV init (such as Ubuntu 18.04 and newer versions, or Debian). For distributions using Systemd (e.g., Ubuntu 18.04 and newer versions), use the `systemctl` method to manage startup services.

Suppose the script you want to run automatically at boot is `xxx.sh`. First, create a startup script in the `/etc/init.d` directory, and name it, for example, `autorun.sh`:

```shell
sudo nano /etc/init.d/autorun.sh
```

Add the script you want to run automatically at boot:

```bash title="autorun.sh"
#!/bin/bash
/path/to/xxx.sh  # Change to the actual path
```

Add the `autorun.sh` script to the system's startup services:

```shell
sudo update-rc.d autorun.sh defaults
```

Set the `autorun.sh` script to start at boot:

```shell
sudo update-rc.d autorun.sh enable
```

This way, after a reboot, the `autorun.sh` script will run automatically.

## Applicable to Systems Using Systemd

If your Linux distribution uses Systemd as the init system (e.g., Ubuntu 18.04 and newer versions), you can use the `systemctl` command to set up automatic startup.

Suppose the script you want to run automatically at boot is `xxx.sh`. First, create a Unit file that describes the service you want to autostart, such as `autorun.service`:

```shell
sudo nano /etc/systemd/system/autorun.service
```

In the Unit file, define the configuration for your service. Here's an example:

```service title="autorun.service"
[Unit]
Description=My Service
After=network.target
[Service]
ExecStart=/path/to/xxx.sh
[Install]
WantedBy=default.target
```

The parameters in the file are as follows:

- `Description`: Describe your service.
- `After`: Specify when your service should start in relation to other services. For example, `network.target` means your service starts after the network service.
- `ExecStart`: Specify the path to the script or command you want to execute.
- `WantedBy`: Specify the target at which your service should start. `default.target` means your service starts when the default target is activated.

Save and close the file, then run the following command to reload the systemd configuration:

```shell
sudo systemctl daemon-reload
```

Enable your service with this command:

```shell
sudo systemctl enable autorun.service
```

Finally, start your service with this command:

```shell
sudo systemctl start autorun.service
```

Now, your service is set to run automatically at system startup. You can restart your system to verify if the service starts correctly.

---

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.