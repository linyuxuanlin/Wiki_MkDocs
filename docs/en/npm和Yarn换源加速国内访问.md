# Speeding up npm and Yarn access in China by changing the source

## Background

The default source addresses for npm and Yarn are located overseas, resulting in slow access speeds in China.  
Use the following command to check the current mirror source:

```shell
yarn config get registry
```

## Solution

Use the software cgr to quickly switch the mirror source for npm and Yarn.

### Install cgr

```shell
npm install -g cgr
```

### List the available mirror sources

```
cgr ls
```

### Select a mirror source to switch to (Taobao)

```
cgr use taobao
```

### Test access speed

```
cgr test taobao
```

## References and Acknowledgments

- [yarn 国内加速，修改镜像源](https://learnku.com/articles/15976/yarn-accelerate-and-modify-mirror-source-in-china)
- [cgr -- change registry | yarn & npm registry manager](https://www.npmjs.com/package/cgr)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.