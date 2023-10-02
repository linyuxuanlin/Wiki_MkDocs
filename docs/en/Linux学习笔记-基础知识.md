# Linux Study Notes - Basics

## Connecting to a Remote Host

Use ssh:

```shell
ssh user@IP
```

## Root Directory Structure

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211009094302.png)

| Directory   | Contents                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| bin         | Binary files for system commands such as cat, cp, and mkdir.                                                                             |
| boot        | Contains files needed for the boot process, such as the boot manager grub2.                                                               |
| dev         | Directory for all device files (e.g. sound card, hard drive, CD-ROM).                                                                     |
| etc         | Etcetera, contains main system configuration files.                                                                                      |
| home        | Directory for storing user home directory data.                                                                                           |
| lib         | Library, contains library files needed for commands in sbin and bin directories to avoid duplication.                                   |
| lib32/lib64 | Contains binary function libraries that support 32/64-bit.                                                                               |
| lost+found  | In EXT3/4 systems, when the system crashes or shuts down unexpectedly, some fragment files will be generated in this directory. The fcsk tool will check this directory and repair damaged files. |
| media       | Used to mount devices such as CDs, floppy disks, and DVDs.                                                                                |
| mnt         | Same as media, used to temporarily mount storage devices.                                                                                 |
| opt         | Directory for installing third-party software.                                                                                            |
| proc        | Directory for storing process and kernel information, does not occupy hard disk space.                                                   |
| root        | Home directory for the root user.                                                                                                        |
| run         | A temporary file system that stores information since system startup. These files should be deleted or cleared when the system restarts. |
| sbin        | System bin, contains commands used by the root user, such as the formatting command mkfs.                                               |
| srv         | Data files required for some network services.                                                                                            |
| sys         | Same as proc directory, used to record CPU and system hardware information.                                                               |
| tmp         | Directory for storing temporary files generated during program execution.                                                                 |
| usr         | Directory for storing system programs, similar to the "Program Files" folder in Windows.                                                 |
| var         | Directory for storing files that frequently change, such as system log files.                                                            |

## File Types

In Linux, everything is a file.

Common file extensions are as follows:

- .tar, .tar.gz, .tgz, .zip, .tar.bz indicate compressed files, created using commands such as tar, gzip, zip, etc. The suffix in the compressed file usually indicates the compression format used, making it easy to choose the appropriate command for decompression.
- .sh indicates shell script files, developed using shell language.
- .pl indicates Perl language files, developed using Perl language.
- .py indicates Python language files, developed using Python language.
- .html, .htm, .php, .jsp, .do indicate web language files.
- .conf indicates system service configuration files.
- .rpm indicates RPM installation package files.

Files mainly have the following types:

### Regular Files

Text files, binary files, etc.

### Executable Files

Including scripts and applications, these files can be loaded and run by the system, similar to bat script and exe program files in Windows.

### Link Files

Link files are divided into hard links and symbolic links:

- Hard links refer to different aliases of the same file.
- Symbolic links are similar to Windows shortcuts. It is actually a special file. In symbolic links, the file is actually a text file that contains the location information of another file.

### Directory Files

In Linux, directories are also files.

### Device Files

Hardware devices are also files. By opening the corresponding device file, the device can be initialized, and some devices can also be controlled by reading and writing device files.

## Users and File Permissions

### User Permissions

Linux is a multi-user operating system, and the user who has access to all resources of other users and the computer is called the root account. In Linux, each user has a specific number - UID, used to identify a system user. The UID of the root account is labeled as 0. We can use the `id` command to view the UID value of the current user. A user can belong to multiple GIDs (groups) to obtain different file permissions.

### File Permissions

Linux file attributes are divided into read permission, write permission, and execute permission (files that can be loaded into memory and executed by the operating system).

File permissions can be modified using the `chmod` command.

## Command Line

### Terminal Prompt

When we open the terminal, a prompt like the following appears:

```bash
[user@hostname ~]$
```

- `user` is the current user's username.
- `hostname` is the name of the computer.
- `~` indicates the current working directory.
- `$` is the command prompt.

```shell
power@Linuxbook:~$
```

This represents the current user as "power", the hostname as "Linuxbook", "~" represents the current directory as the home directory (i.e. "/home/power"), and "$" is the command prompt, indicating that this is a regular user. If it is a superuser, it will be "#" instead.

### Commands

The basic format of a command (with the last two items being optional):

```shell
command [-options] [argument]
```

You can use the "Tab" key for auto-completion, and use "Ctrl" + "C" to terminate the command execution.

- command: the name of the command, such as "cd", "ls", etc.
- -options: additional options for the command, such as "ls -l". The command will perform different operations based on the specific options.
- argument: command parameter, such as "/home" in "cd /home".

Commonly used commands include:

- `ls`: List directory contents
  - `-a`: Show hidden files (files starting with `.`)
  - `-l`: List detailed information about file types, permissions, owners, file sizes, etc.
  - `-t`: List files in order of creation time
  - `-A`: Same as `-a`, but does not list `.` and `..` (current and parent directories)
  - `-R`: Recursively list files in subdirectories if there are any
- `cd`: Change directory
  - Special paths
    - `~`: Current user's home directory
    - `/`: Root directory
    - `.`: Current directory
    - `..`: Parent directory
    - `-`: Change to the directory used in the previous `cd` command
- `pwd`: Print working directory
- `mkdir`: Make directory
  - `-p`: Create directories that do not exist in the specified path
- `rmdir`: Remove an empty directory
- `touch`: Create a file
- `cp`: Copy files or directories
- `rm`: Remove files or directories
  - `-r`: Remove directories and their contents recursively
  - `-f`: Force removal without prompting for confirmation
- `mv`: Move files or directories, or rename files or directories
- `cat`: View file contents
- `echo`: Print text to the terminal
- Output redirection to a file: Save the output of a command to a file
  - `command > filename`: Create or overwrite the file with the command output
  - `command >> filename`: Append the command output to the end of the file
- `sudo`: Switch user do. Use `sudo` before a command that requires root privileges to execute the command as the root user. If the command fails due to lack of permissions as a regular user, use `sudo !!` to re-execute the previous command with root privileges.
- `clear`: Clear the terminal screen
- `reboot`/`poweroff`: Restart or shut down the system

## Package Management

Package management is the use of commands to install software. In Linux operating systems, the two most common package types are deb and rpm.

## References and Acknowledgments

- [Linux Tutorial](https://www.runoob.com/linux/linux-tutorial.html)
- [[Wildfire] i.MX Linux Development Practical Guide](https://doc.embedfire.com/linux/imx6/base/en/latest/index.html)

Sorry, there is no Chinese article provided to be translated. Please provide the article and I will be happy to assist you.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.