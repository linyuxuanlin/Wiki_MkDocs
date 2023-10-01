# ESXi Initialization Guide

VMware ESXi is a virtual machine manager that can be installed directly on bare metal. This tutorial is based on ESXi 8 and is still in draft stage.

You can follow this tutorial to get started: [**"Pitfalls of Soft Routers" Part 2: Essential Knowledge and Nanny-Level Installation Process for ESXi 8.0 Virtual Machines**](https://post.smzdm.com/p/a8x6o5on/p3/?sort_tab=hot/#comments)

When you reach the section "5. Modify the Default Space of ESXi," use the following method to modify the default space size of ESXi.

### Reduce VMFSL Usage

Within 5 seconds of clicking "Install System," press `Shift` + `O` and enter `cdromBoot runweasel systemMediaSize=min` to configure virtual memory to the minimum value. For more information, refer to the official documentation [**ESXi System Storage Overview**](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.install.doc/GUID-474D003B-C6FB-465D-BC1B-5FD30F8E2209.html?hWord=N4IghgNiBcIM4E84BcCmBbAsqgJgSzAGU8AvVEAXyA#esxi-70-system-storage-links-2).

### Installing Windows 11 Virtual Machines

Windows 11 has strict system requirements, and during installation, you may encounter the message "This PC can't run Windows 11." This is usually due to TPM checks, which can be bypassed using the following method:

1. On the virtual machine initialization page, enable "Windows Virtualization-based Security."
2. On the "Now Installing" page after entering the Windows virtual machine, press `Shift` + `F10` to open a cmd window (if the cmd interface does not appear, it may be due to keyboard issues with the laptop, so try using an external keyboard).
3. Enter "regedit" to open the registry editor. Under the path `HKEY_LOCAL_MACHINE\SYSTEM\Setup`, create two 32-bit DWORD values:
   - `BypassTPMCheck`, with a value of hexadecimal `1`.
   - `BypassSecureBootCheck`, with a value of hexadecimal `1`.

If installation still cannot be completed, you can try checking other conditions. It may be that some requirements are not met, such as a CPU with a frequency of 1GHz or higher, a disk space of 64GB or more, and a memory of 4GB or more. For specific details, please refer to the [System requirements](https://www.microsoft.com/en-us/windows/windows-11-specifications?r=1).

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.