---
id: Vue.js小技巧
title: Vue.js 小技巧
---

## 去除 url 中的 `#`

**问题**：使用 Vue.js 搭建的项目，url 中会包含 `#`，影响观感。

**解决方法**：

1. 在项目中全局搜索 `const router = new VueRouter({})` 函数
2. 在函数内添加语句：`mode: 'history'`

## 参考与致谢

- [如何去除 vue 项目中的 # --- History 模式](https://www.cnblogs.com/zhuzhenwei918/p/6892066.html)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

