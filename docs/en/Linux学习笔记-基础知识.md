# Linux Study Notes - Basic Knowledge

## Connecting to a Remote Host

To connect to a remote host, you can use SSH:

```shell
ssh user@IP
```

## Root Directory Structure

![Root Directory Structure](https://media.wiki-power.com/img/20211009094302.png)

| Directory   | Contents                                                                                                                                                                                                       |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bin         | This directory contains binary (executable) files for system commands, such as 'cat,' 'cp,' and 'mkdir.'                                                                                                       |
| boot        | It holds the necessary content for the system's boot process, like the boot manager 'grub2.'                                                                                                                   |
| dev         | This directory contains all device files, such as sound cards, hard drives, and optical drives.                                                                                                                |
| etc         | Abbreviation for "etcetera," this is where the main configuration files for the system are stored.                                                                                                             |
| home        | The directory where user home directory data is stored.                                                                                                                                                        |
| lib         | This is the library directory where the necessary library files for commands in the 'sbin' and 'bin' directories are kept to avoid duplication.                                                                |
| lib32/lib64 | These directories store binary function libraries, supporting both 32-bit and 64-bit systems.                                                                                                                  |
| lost+found  | In EXT3/4 systems, when the system crashes or shuts down unexpectedly, some fragment files are generated in this directory. The 'fsck' tool checks this directory on system startup and repairs damaged files. |
| media       | This directory is used for mounting devices like CDs, floppy disks, and DVDs.                                                                                                                                  |
| mnt         | Similar to 'media,' this directory is used for temporarily mounting storage devices.                                                                                                                           |
| opt         | It's the directory for storing third-party software installations.                                                                                                                                             |
| proc        | This directory is for storing process and kernel information and does not consume hard disk space.                                                                                                             |
| root        | The home directory for the 'root' user.                                                                                                                                                                        |
| run         | This is a temporary file system that stores information since the system started. Files in this directory should be deleted or cleared when the system is rebooted.                                            |
| sbin        | Abbreviation for "system bin," it stores commands used by the 'root' user, such as the formatting command 'mkfs.'                                                                                              |
| srv         | It contains data files required by some network services.                                                                                                                                                      |
| sys         | Similar to the 'proc' directory, it is used to record information related to the CPU and system hardware.                                                                                                      |
| tmp         | This directory is for storing temporary files generated during program execution.                                                                                                                              |
| usr         | It's the directory where the system stores programs, similar to the 'Program Files' folder in Windows.                                                                                                         |
| var         | It is the directory for files that change frequently, such as system log files.                                                                                                                                |

## File Types

In Linux, everything is a file.

Common file extensions are as follows:

- Extensions like .tar, .tar.gz, .tgz, .zip, .tar.bz indicate compressed files, typically created using commands like tar, gzip, zip, etc. The extension within a compressed file usually signifies the compression format used for easy selection of the appropriate extraction command.

- .sh represents shell script files, which are programs developed using shell scripting.

- .pl represents Perl language files, which are programs developed using the Perl language.

- .py represents Python language files, which are programs developed using the Python language.

- .html, .htm, .php, .jsp, .do represent web language files.

- .conf represents configuration files for system services.

- .rpm represents RPM installation package files.

Files mainly fall into the following types:

### Regular Files

These include text files, binary files, and so on.

### Executable Files

These encompass scripts and applications that the system can load and run, similar to bat scripts and exe program files in Windows.

### Link Files

Link files can be hard links or symbolic links:

- Hard links are different aliases for the same file.

- Symbolic links are akin to Windows shortcuts and are actually special files. In symbolic links, the file is, in reality, a text file containing the location information of another file.

### Directory Files

In Linux, directories are also files.

### Device Files

Hardware devices are also treated as files. By opening the corresponding device files, you can initialize devices, and in some cases, control hardware by reading and writing to device files.

## Users and File Permissions

### User Permissions

Linux is a multi-user operating system, and the user with full control over all resources on the system, including managing other users and the computer itself, is called the root user. In Linux, each user has a specific number called UID to identify a system user. The root user has a UID of 0. You can use the `id` command to view the UID of the current user. A user can belong to multiple GIDs (groups) to acquire different file permissions.

### File Permissions

Linux file attributes consist of read, write, and execute permissions (allowing a file to be loaded into memory and executed by the operating system).

File permissions can be modified using the `chmod` command.

## Command Line

### Terminal Prompt

When you open a terminal, you'll see a prompt like this:

```shell
power@Linuxbook:~$
```

This indicates that the current user is "power," the hostname is "Linuxbook," "~" represents the home directory (i.e., `/home/power`), and "$" is the command prompt for a regular user. If you were a superuser, it would be "#" instead.

### Commands

The basic format of a command is as follows (the last two parts are optional):

```shell
command [-options] [argument]
```

You can use the Tab key for auto-completion, and during command execution, you can terminate it with Ctrl + C.

- command: The name of the command, such as `cd`, `ls`, and so on.

- -options: Additional options for the command, e.g., `ls -l`. The command performs different operations depending on the specific options.

- argument: Command parameters, such as `/home` in `cd /home`.

Commonly used commands include:

```markdown
- `ls`: List directories and file names

  - `-a`: Display hidden files (those with names starting with `.`)
  - `-l`: List detailed information including file type, permissions, owner, and file size
  - `-t`: List files in order of their creation time
  - `-A`: Similar to `-a`, but exclude `.` and `..` (current and parent directories)
  - `-R`: If there are files in the directory, it will also list the files in that directory, making it a recursive display.

- `cd`: Change directory

  - Special paths
    - `~`: Home directory of the current user
    - `/`: Root directory
    - `.`: Current directory
    - `..`: Parent directory
    - `-`: Switch to the directory of the last `cd` command.

- `pwd`: Display the current directory.

- `mkdir`: Create a directory

  - `-p`: Create directories if they do not exist.

- `rmdir`: Remove an empty directory.

- `touch`: Create a file.

- `cp`: Copy files or directories.

- `rm`: Remove files or directories

  - `-r`: Delete directories, including their subdirectories and files.
  - `-f`: Force removal.

- `mv`: Move files and directories or rename them.

- `cat`: View the contents of a file.

- `echo`: Output content to the terminal.

- Output redirection to a file: Save the output of a command to a file.

  - `command > filename`: Create the file if it doesn't exist, or overwrite it if it does.
  - `command >> filename`: Create the file if it doesn't exist, or append to the end if it does.

- `sudo`: Switch user do. Use it before a command that requires root permissions to execute the command as the root user. If a command fails under a regular user due to lack of permissions, you can use `sudo !!` to re-run the last command with elevated privileges.

- `clear`: Clear the terminal screen.

- `reboot` / `poweroff`: Restart or shut down the system.

## Package Management

Package management is essentially the process of installing software using commands. In the Linux operating system, the two most common package types are deb and rpm.

## References and Acknowledgments

- [Linux Tutorial](https://www.runoob.com/linux/linux-tutorial.html)
- [i.MX Linux Development Guide by Embedfire](https://doc.embedfire.com/linux/imx6/base/en/latest/index.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
```

Please note that the original markdown format has been preserved in the translation.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
