# Remove Chrome (Edge) Managed by Organization

## Steps

1. Press `Win` + `R`, type `regedit` to open the Registry Editor.
2. Find and delete the following directories:

For Chrome:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome
HKEY_CURRENT_USER\SOFTWARE\Policies\Google\Chrome
```

For Edge:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge
HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Edge
```

## References and Acknowledgements

- [Works! Fix Chrome (or Edge) is Managed by your Organization (in 3 steps!)](https://www.joshualowcock.com/guide/fix-chrome-is-managed-by-your-organization-in-3-steps/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.