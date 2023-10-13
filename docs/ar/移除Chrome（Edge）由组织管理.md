# إزالة إدارة Chrome (Edge) من قبل المؤسسة

## الخطوات

1. `Win` + `R` ، أدخل `regedit` لفتح التسجيل
2. العثور على المسارات التالية وحذفها

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

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.