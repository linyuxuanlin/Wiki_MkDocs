---
id: npm和Yarn换源加速国内访问
title: npm 和 Yarn 换源加速国内访问
---

## 背景

npm 和 Yarn 默认源地址在国外，国内访问速度慢。  
以下命令查看当前使用的镜像源：

```shell
yarn config get registry
```

## 解决方法

使用软件 cgr 快速切换 npm 和 Yarn 的镜像源。

### 安装 cgr

```shell
npm install -g cgr
```

### 列出当前可用的镜像源

```
cgr ls
```

### 选择一个镜像源进行切换（淘宝）

```
cgr use taobao
```

### 测试访问速度

```
cgr test taobao
```

## 参考与致谢

- [yarn 国内加速，修改镜像源](https://learnku.com/articles/15976/yarn-accelerate-and-modify-mirror-source-in-china)
- [cgr -- change registry | yarn & npm registry manager](https://www.npmjs.com/package/cgr)




> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

