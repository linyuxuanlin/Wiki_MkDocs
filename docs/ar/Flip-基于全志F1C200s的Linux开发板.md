# Flip - لوحة تطوير لينكس مبنية على معالج F1C200s من Allwinner

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527234815.jpeg)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527234855.jpeg)

مستودع المشروع: [**linyuxuanlin/Flip**](https://github.com/linyuxuanlin/Flip)

معاينة المشروع عبر الإنترنت:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Flip/raw/main/Hardware/Flip_V0.1.zip"
  ></div>
</div>

يعتمد F1C100s/F1C200s على بنية ARM9 CPU، وتكون التغليف متطابقًا، والفرق هو أن F1C100S يحتوي على ذاكرة DDR1 داخلية بسعة 32 ميجابايت، بينما يحتوي F1C200S على 64 ميجابايت.

بالإضافة إلى ذلك، يتضمن هذا الشريحة وحدات الإدخال والإخراج العامة مثل USB OTG و UART و SPI و TWI و TP و SD/MMC و CSI.

## المعلومات الأساسية

تتضمن المعلومات الأساسية لـ F1C200s ما يلي:

- بنية ARM9 CPU بسرعة 400 ميجاهرتز
- ذاكرة SIP DDR1 بسعة 64 ميجابايت
- SD2.0، eMMC 4.41
- فك تشفير الفيديو H.264/MPEG1 بدقة 1920x1080 بمعدل 30 إطارًا في الثانية، وترميز MJPEG بدقة 1280x720 بمعدل 30 إطارًا في الثانية
- صوت، 2xDAC و 1xADC، DAC يصل إلى 192kHz، ADC يصل إلى 48kHz
- واجهة I2S/PCM واحدة
- واجهة عرض RGB تصل إلى 1280x720 بمعدل 60 إطارًا في الثانية
- مخرج TV CVBS، يدعم NTSC/PAL
- USB OTG
- SDIO
- IR
- 3 x TWI
- 2 x SPI
- 3 x UART
- نظام التشغيل Melis أو Linux SDK
- الحزمة QFN88، 10 مم × 10 مم

مخطط بنية نظام F1C200s:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220422152227.png)

رسم توضيحي للتطبيقات النموذجية:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220513232027.png)

تعريفات Pin:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220422153239.png)

## المراجع والشكر

- [【目录】全志 F1C100S/F1C200S 学习笔记](https://blog.csdn.net/p1279030826/article/details/113370239)
- [peng-zhihui/Planck-Pi](https://github.com/peng-zhihui/Planck-Pi)
- [小白自制 Linux 开发板 一. 瞎抄原理图与乱画 PCB](https://www.cnblogs.com/twzy/p/14714651.html)
- [MangoPi](https://mangopi.cc/f1c200s)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

## تصميم كل وحدة

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
