# Method for Enabling Virtualization on MSI Motherboards

## Restart and Enter BIOS

```cmd
shutdown.exe /r /o
```

After the restart, click on `Troubleshoot` - `Advanced options` - `UEFI Firmware Settings` to access the motherboard BIOS.

## Locate the Relevant Setting

1. Press `F7` to access advanced options.
2. Navigate to `OC` - `CPU Features`.
3. Locate `SVM Mode / Intel Virtualization` (varies depending on your CPU).

## Modify the Setting

Change `Disabled` to `Enabled`.

## Save and Exit

Press `F10` to save and exit.

## References and Acknowledgments

- [How to Access BIOS?](https://zhuanlan.zhihu.com/p/34223088)
- [Method to Enable VT on MSI Computers and Motherboards](http://mumu.163.com/20181108/25905_784199.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.