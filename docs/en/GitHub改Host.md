# Changing GitHub Host

## Issue

Error: `curl: (7) Failed to connect to raw.githubusercontent.com port 443: Connection refused`

## Cause

DNS contamination in China.

## Solution

Add the following entries to your local host file:

```markdown
199.232.68.133 raw.githubusercontent.com
199.232.68.133 user-images.githubusercontent.com
199.232.68.133 avatars2.githubusercontent.com
199.232.68.133 avatars1.githubusercontent.com
```

Host file paths:

- Windows: `C:\Windows\System32\drivers\etc`
- Linux: `/etc/hosts`

Here are steps for Linux:

1. Open a terminal.
2. Enter the command: `vi /etc/hosts`
3. Press `A` to switch to edit mode.
4. Add the above host directives at the end.
5. Press `Esc` to exit edit mode, then type `:wq` to save and exit.

## Extension

To find the IP of a domain, you can use [**IPAddress**](https://www.ipaddress.com/).

## References and Acknowledgments

- [Adding Hosts to Speed Up GitHub Access](https://yangshun.win/blogs/2b7abf4f/#%E4%BF%AE%E6%94%B9-host)

> Article by: **Power Lin**
> Original Source: <https://wiki-power.com>
> Copyright Notice: This article is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Please provide attribution when reposting.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.