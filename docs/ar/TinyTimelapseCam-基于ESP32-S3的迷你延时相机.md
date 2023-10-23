# TinyTimelapseCam - كاميرا تايم لابس صغيرة على أساس ESP32-S3

هذه هي كاميرا تايم لابس صغيرة على أساس ESP32-S3، يمكنك استخدامها لالتقاط حركة السحب النهارية، أو تغيير النجوم طوال الليل، ويمكن أيضًا استخدامها لالتقاط مجموعات متنوعة من الناس على شوارع المدينة.

## نصب الكاميرا الشبكية

يرجى الرجوع إلى الفصل [**استخدام الكاميرا**](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12) للقيام بالتثبيت، لن نعيد شرحها هنا.

## اختبار استدعاء البث باستخدام Python

```py title="StreamViewer.py"
# استدعاء مكتبة OpenCV
import cv2

# تعريف عنوان الكاميرا
camera_url = "http://192.168.31.203:81/stream"

# إنشاء كائن VideoCapture
cap = cv2.VideoCapture(camera_url)

# التحقق مما إذا كانت الكاميرا مفتوحة بنجاح
if not cap.isOpened():
    print("تعذّر الاتصال بالكاميرا. الرجاء التحقق من عنوان الكاميرا أو اتصال الشبكة.")
    exit()

while True:
    # قراءة الإطار
    ret, frame = cap.read()

    # التحقق مما إذا تم قراءة الإطار بنجاح
    if not ret:
        print("تعذّر الحصول على الإطار.")
        break

    # عرض الإطار المعاين
    cv2.imshow('معاينة الكاميرا', frame)

    # الضغط على مفتاح 'q' للخروج من وضع المعاينة
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# تحرير الموارد
cap.release()
cv2.destroyAllWindows()
```

من الجدير بالذكر أن عنوان البث يتم تكوينه عبر إضافة ":81/stream" إلى عنوان الآي بي الأصلي. يمكن أيضًا نسخ عنوان البث من الشاشة الحية المعروضة على صفحة الويب.

## كاميرا التايم لابس

إذا كان اختبار البث السابق ناجحًا، يمكنك الآن تجربة برنامج كاميرا التايم لابس كما يلي:

```py title="TimelapseCam.py"
import cv2
import numpy as np
import time
import os

nframes = 500  # عدد الصور الملتقطة
interval = 0.00001  # الفاصل الزمني (ثواني)

# يجب تغييره إلى عنوان الآي بي الخاص بـ ESP32 الخاص بك
cap = cv2.VideoCapture('http://192.168.31.203:81/stream')

print("تم تشغيل كاميرا التايم لابس")
for i in range(nframes):
    # التقاط الإطار
    ret, img = cap.read()
    # حفظ ملف الصورة
    if img is None:
        print("تعذّر الحصول على الصورة")
    else:
        cv2.imwrite('temp_destination/photos/img_' +
                    str(i + 1000).zfill(4) + '.png', img)
    # انتظار فترة زمنية
    time.sleep(interval)
    print("رقم الصورة:", i)
```

```markdown
# تعريف مسار مجلد الصور
photos_path = "temp_destination/photos/"
# إذا لم يكن المجلد موجودًا ، قم بإنشاء المجلد
os.makedirs(photos_path, exist_ok=True)
# الحصول على قائمة أسماء ملفات الصور
photos = os.listdir(photos_path)
# فرز الصور وفقًا للاسم
photos.sort()
# إنشاء كائن كتابة الفيديو
video = cv2.VideoWriter("temp_destination/video.avi",
                        cv2.VideoWriter_fourcc(*"MJPG"), 100, (1280, 720))

# تصفح الصور
for photo in photos:
    # قراءة الصورة كصورة
    image = cv2.imread(photos_path + photo)
    # ضبط حجم الصورة ليتناسب مع حجم إطار الفيديو
    image = cv2.resize(image, (1280, 720))
    # كتابة الصورة إلى الفيديو
    video.write(image)

# إطلاق كائن كتابة الفيديو
video.release()
print("تم إنتاج فيديو التصوير البطيء بنجاح")
```

بعد تشغيل البرنامج، يمكنك العثور على الفيديو الذي تم إنشاؤه في مجلد `temp_destination`. يمكنك أيضًا تعديل معاملات `nframes` و `interval` لجعل الكاميرا بالتصوير البطيء مناسبة لسيناريوهات التصوير المختلفة.

## إرشادات وحلول للمشكلات الشائعة

- إذا كان بإمكانك عرض الصور في المتصفح عبر الإنترنت ولكن لا يمكنك الالتقاط محليًا، فهذا يمكن أن يكون بسبب أنه يمكن فتح اتصال بالكاميرا في نفس الوقت فقط. يُفضل إغلاق المتصفح إذا كنت ترغب في استخدام الالتقاط المحلي.
- إذا كنت تخطط لتسجيل فيديو طوال اليوم، يمكنك تشغيل البرنامج على خادم ذي استهلاك منخفض للطاقة أو هاتف قديم. هذا سيساعد في توفير الطاقة وعدم الحاجة لتشغيل الكمبيوتر طوال الوقت.

## مراجع وشكر

- [مثال ESP32-CAM Python stream OpenCV](https://www.hackster.io/onedeadmatch/esp32-cam-python-stream-opencv-example-1cc205)
- [كيفية إنشاء كاميرا أمان مباشرة مع UNIHIKER & FireBeetle 2 ESP32S3](https://www.hackster.io/pradeeplogu0/live-security-camera-with-unihiker-firebeetle-2-esp32s3-5d478e)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```


> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.