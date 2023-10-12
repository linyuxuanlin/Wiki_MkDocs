# TinyTimelapseCam - كاميرا تأخير صغيرة بناءً على ESP32-S3

هذه هي كاميرا تأخير صغيرة بناءً على ESP32-S3 ، يمكنك استخدامها لالتقاط تحركات الغيوم النهارية وحركة النجوم طوال الليل ، كما يمكن استخدامها لالتقاط مجموعة متنوعة من الناس في شوارع المدينة.

## نشر كاميرا الويب

يرجى الرجوع إلى الفصل [**استخدام الكاميرا**](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12) للقيام بالنشر ، لا يتم تكراره هنا.

## اختبار استدعاء التدفق باستخدام Python

```py title="StreamViewer.py"
# استدعاء مكتبة OpenCV
import cv2

# تعريف عنوان الكاميرا
camera_url = "http://192.168.31.203:81/stream"

# إنشاء كائن VideoCapture
cap = cv2.VideoCapture(camera_url)

# التحقق من أن الكاميرا تم فتحها بنجاح
if not cap.isOpened():
    print("لا يمكن الاتصال بالكاميرا. يرجى التحقق من عنوان الكاميرا أو الاتصال بالشبكة.")
    exit()

while True:
    # قراءة الإطار
    ret, frame = cap.read()

    # التحقق من نجاح قراءة الإطار
    if not ret:
        print("لا يمكن الحصول على الإطار.")
        break

    # عرض الصورة المعاينة
    cv2.imshow('Camera Preview', frame)

    # الضغط على مفتاح 'q' للخروج من العرض المعاينة
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# إطلاق الموارد
cap.release()
cv2.destroyAllWindows()
```

يجب ملاحظة أن عنوان التدفق هو عنوان IP الأصلي ، بالإضافة إلى اللاحقة `:81/stream`. يمكنك أيضًا النقر بزر الماوس الأيمن على الصورة المعروضة في الويب ونسخ عنوان التدفق.

## كاميرا التأخير

إذا نجح اختبار التدفق السابق ، فيمكنك تجربة برنامج كاميرا التأخير التالي:

```py title="TimelapseCam.py"
import cv2
import numpy as np
import time
import os

nframes = 500  # عدد الصور الملتقطة
interval = 0.00001  # الفاصل الزمني (ثانية)

# يجب تغييرها إلى عنوان IP الخاص بـ ESP32 الخاص بك
cap = cv2.VideoCapture('http://192.168.31.203:81/stream')

print("تم تشغيل كاميرا التأخير")
for i in range(nframes):
    # التقاط إطار الصورة
    ret, img = cap.read()
    # حفظ ملف الصورة
    if img is None:
        print("لا يمكن الحصول على الصورة")
    else:
        cv2.imwrite('temp_destination/photos/img_' +
                    str(i + 1000).zfill(4) + '.png', img)
    # الانتظار لبعض الوقت
    time.sleep(interval)
    print("رقم الصورة:", i)

# تعريف مسار مجلد الصور
photos_path = "temp_destination/photos/"
# إذا لم يكن المجلد موجودًا ، فأنشئ المجلد
os.makedirs(photos_path, exist_ok=True)
# الحصول على قائمة أسماء ملفات الصور
photos = os.listdir(photos_path)
# فرز الصور حسب الاسم
photos.sort()
# إنشاء كائن كتابة الفيديو
video = cv2.VideoWriter("temp_destination/video.avi",
                        cv2.VideoWriter_fourcc(*"MJPG"), 100, (1280, 720))

# تصفح الصور
for photo in photos:
    # اقرأ الصورة كصورة
    image = cv2.imread(photos_path + photo)
    # ضبط حجم الصورة لتناسب حجم إطار الفيديو
    image = cv2.resize(image, (1280, 720))
    # كتابة الصورة في الفيديو
    video.write(image)

# إطلاق كائن كتابة الفيديو
video.release()
print("تم إنشاء فيديو التصوير البطيء")

بعد تشغيل البرنامج ، يمكنك العثور على الفيديو الذي تم إنشاؤه في مجلد "temp_destination". يمكنك أيضًا تعديل معلمات "nframes" و "interval" لجعل الكاميرا البطيئة تناسب مشاهد التصوير المختلفة.

## الأسئلة الشائعة والاقتراحات

- إذا كان بإمكان الويب عرض الصورة بشكل حي ، ولكن لا يمكنك الحصول على بث الفيديو على الجهاز المحلي ، فهذا يعود إلى أنه يمكن فتح بث واحد في نفس الوقت ، يرجى إغلاق الصفحة الإلكترونية.
- إذا كنت تخطط لتصوير فيديو طوال اليوم ، فيمكنك تشغيل برنامج Python على خادم منخفض الطاقة أو هاتف محمول قديم ، حتى لا تحتاج إلى تشغيل الكمبيوتر طوال الوقت.

## المراجع والشكر

- [ESP32-CAM Python stream OpenCV Example](https://www.hackster.io/onedeadmatch/esp32-cam-python-stream-opencv-example-1cc205)
- [Live Security Camera with UNIHIKER & FireBeetle 2 ESP32S3](https://www.hackster.io/pradeeplogu0/live-security-camera-with-unihiker-firebeetle-2-esp32s3-5d478e)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.