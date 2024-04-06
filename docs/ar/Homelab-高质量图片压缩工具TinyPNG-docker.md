# Homelab - أداة ضغط صور عالية الجودة TinyPNG-docker

![](https://media.wiki-power.com/img/20230416163137.png)

TinyPNG-docker هي أداة تستخدم واجهة برمجة التطبيقات (API) لـ TinyPNG لضغط الصور عالية الجودة. يمكنها ضغط صور WEBP وJPEG وPNG في المسار المحدد تلقائيًا ، ثم إخراجها في المسار الذي تريده. يمكنها تقليل استخدام عرض النطاق الترددي وحجم البيانات ووقت التحميل للموقع بشكل فعال. بالمناسبة ، هذا هو تطبيق Docker الذي طورته باستخدام ChatGPT.

## التنصيب (Docker Compose)

أولاً ، قم بإنشاء `compose.yaml` واستبدل `${DIR}` بالمسار المحلي (مثل `/DATA/AppData`) ؛ استبدل `${API}` بمفتاح TinyPNG الخاص بك:

```yaml title="compose.yaml"
version: "3"
services:
  tinypng-docker:
    image: linyuxuanlin/tinypng-docker
    environment:
      - TINYPNG_API_KEY=${API}
      - INPUT_DIR=/app/input
      - OUTPUT_DIR=/app/output
    volumes:
      - ${DIR}/tinypng-docker/input:/app/input
      - ${DIR}/tinypng-docker/output:/app/output
```

## تعليمات التكوين

قبل استخدام هذا الحاوية Docker ، يجب أن تقوم بتسجيل حساب على موقع TinyPNG وطلب مفتاح API.

الاستخدام بسيط ، قم بنسخ الصور التي ترغب في ضغطها في مجلد `${DIR}/tinypng/input` ، وستجد الصور المضغوطة في مجلد `${DIR}/tinypng/output`.

إذا لم يتمكن الحاوية من العمل بشكل صحيح ، يمكنك استبعاد الأسباب التالية:

1. تأكد من أن مسار المجلد المحدد في ملف `compose.yaml` صحيح للمجلدين `input` و `output`.
2. تحقق من حساب TinyPNG الخاص بك لمعرفة ما إذا كان قد تم الوصول إلى الحد الأقصى لعدد ضغطات المفتاح الخاص بك.
3. تحقق مما إذا كان مجلد `input` يحتوي على ملفات صور بتنسيق صحيح (WebP و PNG و JPEG). لاحظ أن هذه الحاوية ستقوم بفحص وضغط الصور فقط عند حدوث حدث `created` ، لذا إذا كان الملف موجودًا بالفعل ، فيجب نقله يدويًا إلى المجلد `input`.
4. تحقق مما إذا كانت الصور المضغوطة تفقد جودتها بشكل أكبر من إعدادات ضغط API ، مما يمكن أن يؤدي إلى فشل فك تشفير API (على سبيل المثال ، إذا تم ضغط الصورة قبل الضغط الأولي).
5. جرب استخدام أداة ضغط الصور المقدمة من موقع tinify يدويًا ، وقم بتحميل الصور المضغوطة لتحديد مكان المشكلة بشكل أفضل ، وفي الوقت نفسه ، يمكنك تحديد موقع المشكلة من خلال إخراج معلومات التصحيح في وحدة التحكم.

---

## عملية تطوير صور Docker

### الإعداد

1. إذا لم تكن قد سجلت حسابًا على Docker Hub بعد ، فيجب عليك إنشاء حساب على Docker Hub أولاً.

2. تسجيل الدخول إلى Docker Hub:

```shell
docker login
```

اتبع التعليمات وأدخل اسم المستخدم وكلمة المرور لتسجيل الدخول إلى Docker Hub.

### إنشاء الحاوية

قم بإنشاء ملف `Dockerfile`:

```Dockerfile title="Dockerfile"
FROM python:3.8-slim-buster

RUN pip install tinify watchdog

WORKDIR /app

COPY . /app

ENV TINYPNG_API_KEY=<your_tinypng_api_key>
ENV INPUT_DIR=/app/input
ENV OUTPUT_DIR=/app/output

CMD ["python", "main.py"]
```

قم بإنشاء `main.py` في نفس المسار:

```py title="main.py"
import tinify
import os
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print("Received created event - %s." % event.src_path)
            source_path = event.src_path
            output_path = os.path.join(os.environ['OUTPUT_DIR'], os.path.basename(source_path))
            compress_image(source_path, output_path)

def compress_image(source_path, output_path):
    tinify.key = os.environ['TINYPNG_API_KEY']
    source = tinify.from_file(source_path)
    source.to_file(output_path)
    print(f"{source_path} compressed and saved to {output_path}")

if __name__ == "__main__":
    print("Watching for new images...")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.environ['INPUT_DIR'], recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

أولاً، يتم استيراد المكتبات اللازمة للغة Python: tinify، os، time، sys، watchdog. ثم يتم تعريف فئة تسمى MyHandler ترث من FileSystemEventHandler في watchdog.events. تحتوي هذه الفئة على دالة تسمى on_created تُستدعى عند اكتشاف إنشاء ملف جديد في المجلد المحدد. تقوم دالة on_created بالحصول على مسار الصورة الأصلية وتقوم بضغطها وحفظها في المسار المحدد. أخيرًا، يتم البدء في مراقبة المجلد المحدد، وعند اكتشاف ملف جديد في المجلد، يتم تنفيذ عملية الضغط تلقائيًا وحفظ الصورة المضغوطة في المجلد المحدد.

### بناء الحاوية

قم بتنفيذ الأمر التالي في نفس مسار `Dockerfile` لبناء الحاوية:

```shell
docker build -t tinypng-docker .
```

حيث `tingpng-docker` هو اسم الصورة التي سيتم بناؤها، و `.` هو المسار الذي يحتوي على ملف `Dockerfile`.

### وضع علامة على الصورة

استخدم الأمر التالي لوضع علامة على الصورة:

```shell
docker tag <image-name> <dockerhub-username>/<repository-name>:<tag>
```

مثال:

```shell
docker tag tinypng-docker linyuxuanlin/tinypng-docker:latest
```

### رفع الصورة إلى Docker Hub

استخدم الأمر التالي لرفع الصورة إلى Docker Hub:

```shell
docker push <dockerhub-username>/<repository-name>:<tag>
```

على سبيل المثال:

```shell
docker push linyuxuanlin/tinypng-docker:latest
```

### سحب الصورة

بعد الرفع، يمكن للآخرين سحب الصورة باستخدام الأمر التالي:

```shell
docker pull linyuxuanlin/tinypng-docker:latest
```

## المراجع والشكر

- [الوثائق](https://wiki-power.com/Homelab-%E9%AB%98%E8%B4%A8%E9%87%8F%E5%9B%BE%E7%89%87%E5%8E%8B%E7%BC%A9%E5%B7%A5%E5%85%B7TinyPNG-docker)
- [مستودع GitHub](https://github.com/linyuxuanlin/Dockerfiles/tree/main/tinypng-docker)
- [Docker Hub](https://hub.docker.com/r/linyuxuanlin/tinypng-docker)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
