# GitHub Change Host

## Problem

Error: `curl: (7) Failed to connect to raw.githubusercontent.com port 443: Connection refused`

## Cause

DNS pollution in China.

## Solution

Add the following lines to the host file on your local machine:

```
199.232.68.133 raw.githubusercontent.com
199.232.68.133 user-images.githubusercontent.com
199.232.68.133 avatars2.githubusercontent.com
199.232.68.133 avatars1.githubusercontent.com
```

Host path:

- Windows: `C:\Windows\System32\drivers\etc`
- Linux: `/etc/hosts`

Here's how to do it on Linux:

1. Open the terminal
2. Enter the command: `vi /etc/hosts`
3. Press `A` to switch to edit mode
4. Add the above lines of Host pointing to the end
5. Press `Esc` to exit edit mode, and press `:wq` to save and exit

## Extension

### Query IP of Domain Name

Use [**IPAddress**](https://www.ipaddress.com/)

## Reference and Acknowledgement

- [Adding Host to Speed Up Access to Github](https://yangshun.win/blogs/2b7abf4f/#%E4%BF%AE%E6%94%B9-host)

> Article author: **Power Lin**
> Original address: <https://wiki-power.com>
> Copyright statement: The article is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Please indicate the source when reprinting.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.