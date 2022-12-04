---
id: Linux学习笔记-用户操作
title: Linux 学习笔记 - 用户操作
---

## 基本操作

### 添加用户

```shell
useradd -m 用户名
```

### 设置密码  

```shell
passwd 用户名
```

### 删除用户

```shell
userdel  -r  用户名
```

### 删除用户目录

```shell
rm -rf 用户名
```

### 切换当前用户

```shell
su 用户名
```

## 参考与致谢

- [linux 创建用户、设置密码](https://blog.csdn.net/li_101357/article/details/69367457)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

