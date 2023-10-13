# استخدام Graphviz لرسم الرسوم البيانية

طريقة لرسم الرسوم البيانية باستخدام الشفرة.

## الخلفية

[Graphviz](http://www.graphviz.org/) شيء جيد ، يمكن استخدامه لرسم الرسوم البيانية. يوجد فرق أساسي بينه وبين Visio: يتم إنشاء الرسم البياني في Graphviz بطريقة **تخطيط تلقائي** ، ولا يلزم تعديل مواقع العناصر يدويًا. عندما يكون الشبكة العلاقية معقدة ، يمكن تحقيق **تقليل أدنى لتداخل الخطوط** باستخدام التخطيط التلقائي.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/Graphviz.png)

## التثبيت

اكتشفت محررًا عبر الإنترنت جيدًا: \[GraphvizOnline\]\([http://dreampuf.github.io/GraphvizOnline/\#digraph graph_name { ](http://dreampuf.github.io/GraphvizOnline/#digraph%20graph_name%20{%20) %20%20A-&gt;B[label%3D"العلاقة"\]%20 }\) يدعم العرض الفوري ، وتصدير `.png` و `.svg` وغيرها من الأشكال.

تثبيت على macOS: `brew install graphviz`

## عملية الرسم

1. إنشاء `xxx.dot`
2. تحرير مستند `.dot`
3. التبديل إلى الدليل الذي يحتوي على الملف ، ثم التصدير: `dot xxx.dot -T png -o xxx.png`

## بناء الجملة البسيطة

```
graph graph_name {
  A--B[label="العلاقة"]
}
```

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20190201140244.png)

## استنتاج

التخطيط التلقائي هو جوهر Graphviz. بالمقارنة مع الطريقة التي استخدمتها سابقًا لإنشاء الشرائح باستخدام Markdown ، تقوم هذه الأدوات بتوحيد المحتوى ، مما يتيح للأشخاص التركيز **أكثر على المحتوى بدلاً من الشكل والتخطيط**.

## المراجع والشكر

- [دليل Graphviz البسيط](https://blog.zengrong.net/post/2294.html)
- [رسم الرسوم البيانية باستخدام dot](http://www.graphviz.org/pdf/dotguide.pdf)
- [تثبيت ودليل المبتدئين لـ Graphviz على Windows](https://blog.csdn.net/lanchunhui/article/details/49472949)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.