# إزالة إدارة Chrome (Edge) من قِبَل المؤسسة

## الخطوات

1. اضغط على `Win` + `R` ، ثم اكتب `regedit` لفتح محرر التسجيل.
2. ابحث عن المسارات التالية واحذفها:

Chrome:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome
HKEY_CURRENT_USER\SOFTWARE\Policies\Google\Chrome
```

Edge:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge
HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Edge
```

## المراجع والشكر

- [Works! Fix Chrome (or Edge) is Managed by your Organization (in 3 steps!)](https://www.joshualowcock.com/guide/fix-chrome-is-managed-by-your-organization-in-3-steps/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.