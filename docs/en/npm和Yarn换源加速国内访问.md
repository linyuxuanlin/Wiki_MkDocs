# Accelerating Access to npm and Yarn in China by Changing the Source

## Background

By default, npm and Yarn use overseas source addresses, resulting in slow access in China.  
You can check the current mirror source being used with the following command:

```shell
yarn config get registry
```

## Solution

Utilize the cgr software to quickly switch between mirror sources for npm and Yarn.

### Installing cgr

```shell
npm install -g cgr
```

### Listing currently available mirror sources

```
cgr ls
```

### Selecting a mirror source to switch to (e.g., Taobao)

```
cgr use taobao
```

### Testing access speed

```
cgr test taobao
```

## References and Acknowledgments

- [Yarn Acceleration in China: Modifying Mirror Sources](https://learnku.com/articles/15976/yarn-accelerate-and-modify-mirror-source-in-china)
- [cgr - Change Registry: Yarn & npm Registry Manager](https://www.npmjs.com/package/cgr)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.