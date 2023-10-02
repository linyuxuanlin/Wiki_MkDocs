# Embedded Linux - Basic Knowledge

## Common Commands

- View CPU information: `cat /proc/cpuinfo`
- View kernel version: `cat /proc/version`
- View memory usage: `cat /proc/meminfo`
  - You can also use the `free` command to get a simple understanding of memory usage
- View FLASH storage usage: `cat /proc/partitions`
- View task processes: `top`
- View supported file systems: `cat /proc/filesystems` (nodev means no need to mount block devices)
- View CPU frequency: `cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq`

## Linux Drivers

The role of drivers on Linux is to establish a mapping relationship between hardware devices and Linux files.

For example, when controlling LED lights and buttons, we don't need to know their specific hardware connections. We just need to know which file represents which device, and then we can manipulate similar devices in the same way through files.

## References and Acknowledgments

- [[Wildfire] i.MX Linux Development Practical Guide](https://doc.embedfire.com/linux/imx6/base/zh/latest/index.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.