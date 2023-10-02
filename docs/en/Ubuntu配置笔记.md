# Ubuntu Configuration Notes

## Dual System Time Issue

After installing dual systems, there may be a time issue (Windows and Ubuntu time not synchronized), which can be solved using the following command:

```shell
timedatectl set-local-rtc 1 --adjust-system-clock
```

## Software Installation

1. Chrome
2. VS Code
3. [**Qv2ray**](https://qv2ray.net/)
4. Git
   - `sudo apt install git`
   - `git config --global user.name "John Doe"`
   - `git config --global user.email johndoe@example.com`

## Tips

### View Hidden Files

Use shortcut key: `Ctrl` + `H`

### Open Terminal

Use shortcut key: `Ctrl` + `Alt` + `T`

### Commands

Note: `<xx>` means required, `(xx)` means optional

- cd
  - Change working directory
  - `cd <directory path>`
- pwd
  - View current absolute path
  - `pwd`
- mkdir
  - Create directory
  - `mkdir (option) <directory name>`
- ls
  - List contents of directory
  - `ls (option) (directory name)`
- touch
  - Change file/directory time
  - `touch (option) <file name>`
- mv
  - Cut
  - `mv (option) (source file/directory) <destination file/directory>`
- cp
  - Copy
  - `cp (option) (source file/directory name) <destination file/directory name>`
- rm
  - Delete
  - `rm (option) <file/directory name>`

## References and Acknowledgments

- [ROS Installation Tutorial](https://mp.weixin.qq.com/s?__biz=MzU4Mzc1NDA5Mw==&mid=2247486645&idx=1&sn=8ba442af57060b4d608d4c24d4307921&chksm=fda504b7cad28da11a2dd782b60dce466d53ad8e260f161b1e47f24423cc1e9f9aabc486c7f3&mpshare=1&scene=1&srcid=1125YhpxcX5as5se6rsek2IS&sharer_sharetime=1606233866320&sharer_shareid=57baeb2b96d0cff9b17ac2c15b36602b&key=a402d93e91746f46ae3228f3f1014e2c74a235c331168642475573a82dabce23902b3593a2a240439e9e37cd9b2ceaeab2b3b2130d952ee61260b30c6cad24ab3f1907dd57abfae9934d0c9487ddc4364b41261c6fb7277d94de784fa9718f9f60712a15b25f505ab7105346330f16f4b659970a5143e8aa882da96dc76c0100&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_CN&exportkey=A0ZOktA1B68GOdT4vmLQPxA%3D&pass_ticket=b2tffRx7FG4vxDxfZxW7b9rGQf%2FK8YGbZtslM9VWUgnItoiwUPJYOD8ciwJbwx%2BC&wx_header=0)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.