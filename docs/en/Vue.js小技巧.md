# Vue.js Tips

## Removing the `#` from the URL

**Issue**: When using Vue.js to build a project, the URL may contain a `#`, which affects the overall appearance.

**Solution**:

1. In your project, perform a global search for the `const router = new VueRouter({})` function.
2. Inside the function, add the statement: `mode: 'history'`

## References and Acknowledgments

- [How to Remove the # in a Vue Project - History Mode](https://www.cnblogs.com/zhuzhenwei918/p/6892066.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.