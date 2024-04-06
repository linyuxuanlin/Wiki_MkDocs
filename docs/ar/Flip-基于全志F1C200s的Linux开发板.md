```markdown
# Flip - لوحة تطوير Linux مبنية على معالج Allwinner F1C200s

![صورة](https://media.wiki-power.com/img/20220527234815.jpeg)

![صورة](https://media.wiki-power.com/img/20220527234855.jpeg)

مستودع المشروع: [**linyuxuanlin/Flip**](https://github.com/linyuxuanlin/Flip)

معاينة المشروع عبر الإنترنت:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Flip/raw/main/Hardware/Flip_V0.1.zip"
  ></div>
</div>

معالجات F1C100s/F1C200s مبنية على الهندسة المعمارية ARM9 ومعبأة بنفس الشكل. الفرق الرئيسي بينهما هو أن معالج F1C100S يأتي مع ذاكرة داخلية DDR1 سعة 32 ميجابايت، بينما معالج F1C200S يأتي مع ذاكرة سعة 64 ميجابايت.

بالإضافة إلى ذلك، يتضمن هذا الرقاقة واجهات أخرى مفيدة مثل USB OTG، UART، SPI، TWI، TP، SD/MMC، و CSI.

## المعلومات الأساسية

المعلومات الأساسية لمعالج F1C200s هي كالتالي:

- هندسة معمارية المعالج ARM9 بسرعة 400 ميجاهرتز
- ذاكرة داخلية بسعة 64 ميجابايت من نوع DDR1
- دعم SD2.0 و eMMC 4.41
- فك تشفير الفيديو بصيغ H.264/MPEG1 بدقة 1920x1080@30 إطارًا في الثانية، وترميز الفيديو بصيغة MJPEG بدقة 1280x720@30 إطارًا في الثانية
- واجهات صوتية، تحتوي على 2 مخرجات DAC ومدخل ADC واحد. الـ DAC يدعم سرعات تصل إلى 192 كيلوهرتز، والـ ADC يدعم سرعات تصل إلى 48 كيلوهرتز
- واجهة I2S/PCM واحدة
- واجهة عرض RGB تدعم دقة تصل إلى 1280x720@60 إطارًا في الثانية
- مخرج تلفزيون CVBS مع دعم للمعايير NTSC/PAL
- منفذ USB OTG
- دعم SDIO
- مستقبل الأشعة تحت الحمراء (IR)
- 3 واجهات TWI
- 2 واجهات SPI
- 3 منافذ UART
- نظام تشغيل Melis أو Linux SDK
- معبأة بحجم QFN88 بقياس 10 ملم x 10 ملم

هنا نجد مخطط الهندسة المعمارية لمعالج F1C200s:

![صورة](https://media.wiki-power.com/img/20220422152227.png)

وهذا هو رسم تخطيطي للاستخدام النموذجي:

![صورة](https://media.wiki-power.com/img/20220513232027.png)

تعريف المنافذ:

![صورة](https://media.wiki-power.com/img/20220422153239.png)

## المراجع والشكر

- [مذكرات دراسة Allwinner F1C100S/F1C200S](https://blog.csdn.net/p1279030826/article/details/113370239)
- [peng-zhihui/Planck-Pi](https://github.com/peng-zhihui/Planck-Pi)
- [Linux الخاصة بالمبتدئين - الجزء 1: رسم مخطط الدوائر وتصميم اللوحة](https://www.cnblogs.com/twzy/p/14714651.html)
- [MangoPi](https://mangopi.cc/f1c200s)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

## تصميم الوحدات المختلفة
```

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
