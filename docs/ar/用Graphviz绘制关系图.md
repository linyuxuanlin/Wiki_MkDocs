# استخدام Graphviz لرسم الرسوم البيانية

طريقة لرسم الرسوم البيانية باستخدام الشفرة.

## الخلفية

[Graphviz](http://www.graphviz.org/) هو أداة رائعة يمكن استخدامها لرسم الرسوم البيانية. يوجد فرق أساسي بينه وبين Visio: يقوم Graphviz بتوليد الرسوم البيانية بشكل **تلقائي**، ولا يتطلب تعديل يدوي لمواضع العناصر. عندما يكون الشبكة العلاقية معقدة، يمكن استخدام التخطيط التلقائي لتقليل **تداخل الروابط**.

![](https://media.wiki-power.com/img/Graphviz.png)

## التثبيت

اكتشفت أداة تحرير عبر الإنترنت رائعة: \[GraphvizOnline\]\([http://dreampuf.github.io/GraphvizOnline/\#digraph graph_name { ](http://dreampuf.github.io/GraphvizOnline/#digraph%20graph_name%20{%20) %20%20A-&gt;B\[label%3D"العلاقة"\]%20 }\) تدعم العرض الفوري، وتصدير بتنسيقات `.png` و `.svg` وغيرها.

لتثبيته على نظام macOS: `brew install graphviz`

## عملية الرسم

1. قم بإنشاء `xxx.dot` جديدة
2. قم بتحرير مستند `.dot`
3. انتقل إلى المجلد الذي يحتوي على الملف، وقم بالتصدير: `dot xxx.dot -T png -o xxx.png`

## بناء الجملة البسيطة

```
graph graph_name {
  A--B[label="الربط"]
}
```

![](https://media.wiki-power.com/img/20190201140244.png)

## الاستنتاج

التخطيط التلقائي هو جوهر Graphviz. بالمقارنة مع استخدامي السابق لصيغة Markdown لإنشاء العروض التقديمية، هذه الأدوات تقوم بتوحيد المحتوى وتسمح للشخص بالتركيز **أكثر على المحتوى وليس الشكل والتخطيط**.

## المراجع والشكر

- [دليل بسيط لـ Graphviz](https://blog.zengrong.net/post/2294.html)
- [رسم الرسوم البيانية باستخدام dot](http://www.graphviz.org/pdf/dotguide.pdf)
- [تثبيت ودليل مبتدئين لـ Graphviz على نظام Windows](https://blog.csdn.net/lanchunhui/article/details/49472949)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
