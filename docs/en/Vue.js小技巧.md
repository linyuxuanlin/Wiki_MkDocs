# Vue.js Tips

## Removing `#` from URL

**Problem**: When using Vue.js to build a project, the URL may contain `#`, which affects the appearance.

**Solution**:

1. Search for the `const router = new VueRouter({})` function globally in the project.
2. Add the statement `mode: 'history'` inside the function.

## Reference and Acknowledgement

- [How to remove # from Vue project --- History mode](https://www.cnblogs.com/zhuzhenwei918/p/6892066.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.