# ESXi Initialization Guide

VMware ESXi is a virtual machine manager that can be installed directly on bare metal. This tutorial is based on ESXi 8 and is still in the draft stage.

You can start by following this tutorial: [**'Troubleshooting Guide for Soft Routers,' Part Two: Essential Information and Step-by-Step Installation Process for ESXi 8.0**](https://post.smzdm.com/p/a8x6o5on/p3/?sort_tab=hot/#comments)

When you reach the part titled `5. Modify ESXi's Default Space` in the tutorial, use the following method to adjust the default space size of ESXi.

### Reducing VMFSL Usage

Within 5 seconds of selecting the system installation, press `Shift` + `O`, and enter `cdromBoot runweasel systemMediaSize=min` to configure virtual memory to its minimum value. For more details, you can refer to the official documentation [**ESXi System Storage Overview**](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.install.doc/GUID-474D003B-C6FB-465D-BC1B-5FD30F8E2209.html?hWord=N4IghgNiBcIM4E84BcCmBbAsqgJgSzAGU8AvVEAXyA#esxi-70-system-storage-links-2).

### Installation of Windows 11 Virtual Machine

Windows 11 has strict system requirements, and during installation, you may encounter the message, "This PC can't run Windows 11." Typically, this issue arises from TPM checks and can be bypassed using the following steps:

1. On the virtual machine's initialization page, enable "Windows-based Virtualization Security."
2. After entering the Windows virtual machine and reaching the "Now Install" page, press the keyboard shortcut `Shift` + `F10` to launch the Command Prompt (if the cmd window does not appear, it may be due to laptop keyboard layout issues, so you can try using an external keyboard).
3. Type `regedit` to open the registry editor. Under the path `HKEY_LOCAL_MACHINE\SYSTEM\Setup`, create two 32-bit DWORD values:
   - `BypassTPMCheck` with a hexadecimal value of `1`.
   - `BypassSecureBootCheck` with a hexadecimal value of `1`.

If you still encounter installation issues, you can try checking for other requirements. This could include factors like a CPU clock speed of 1GHz or higher, more than 64GB of disk space, and a minimum of 4GB of RAM. For more specific details, please refer to [**System requirements**](https://www.microsoft.com/en-us/windows/windows-11-specifications?r=1).

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.