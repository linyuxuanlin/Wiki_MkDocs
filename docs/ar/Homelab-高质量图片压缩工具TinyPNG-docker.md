# Homelab - أداة ضغط الصور عالية الجودة TinyPNG-docker

TinyPNG-docker هي أداة تستخدم API TinyPNG لضغط الصور عالية الجودة، ويمكنها ضغط صور WEBP و JPEG و PNG تلقائيًا في المسار المحدد وإخراجها في المسار الذي تريده. يمكنها تقليل استخدام عرض النطاق الترددي والمرور ووقت التحميل للموقع بشكل فعال. بالمناسبة، هذا هو تطبيق Docker الذي قمت بتطويره باستخدام ChatGPT.

## التنصيب (Docker Compose)

أولاً، قم بإنشاء `compose.yaml` واستبدل `${DIR}` بالمسار المحلي (مثل `/DATA/AppData`) و `${API}` بمفتاح TinyPNG الخاص بك:

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

## شرح التكوين

قبل استخدام هذا الحاوية Docker، يجب عليك التسجيل في موقع TinyPNG وطلب مفتاح API.

الاستخدام سهل، قم بنسخ الصور التي تريد ضغطها إلى مجلد `${DIR}/tinypng/input` وستجد الصور المضغوطة في مجلد `${DIR}/tinypng/output`.

إذا لم تعمل الحاوية بشكل صحيح، يمكنك استخدام الخطوات التالية لإصلاح المشكلة:

1. تأكد من أن مسار المجلد المحدد في ملف `compose.yaml` صحيح.
2. تحقق من حساب TinyPNG الخاص بك وتأكد من عدم تجاوز الحد الأقصى لعدد مرات الضغط المسموح بها لمفتاح API.
3. تحقق من مجلد `input` وتأكد من وجود ملفات الصور بالتنسيق الصحيح (WebP و PNG و JPEG). يرجى ملاحظة أن هذه الحاوية ستقوم بالكشف عن الأحداث `created` فقط وضغطها، لذلك إذا كان الملف موجودًا بالفعل، فيجب نقله يدويًا إلى مجلد `input`.
4. تحقق من أن جودة الصور المضغوطة لا تزيد عن إعدادات ضغط API، وذلك لتجنب فشل فك تشفير API (على سبيل المثال، إذا تم ضغط الصورة قبل الضغط).
5. جرب استخدام أداة ضغط API المقدمة من موقع tinify يدويًا، وقم بتحميل الصورة المضغوطة لتحديد موقع المشكلة بدقة، ويمكنك أيضًا استخدام معلومات التصحيح في وحدة التحكم لتحديد المشكلة.

---

## عملية تطوير صورة Docker

### الإعداد

1. إذا لم تكن قد سجلت حسابًا في Docker Hub بعد، فيجب عليك إنشاء حساب على Docker Hub.

2. تسجيل الدخول إلى Docker Hub:

```shell
docker login
```

اتبع التعليمات لإدخال اسم المستخدم وكلمة المرور وتسجيل الدخول إلى Docker Hub.

### إنشاء الحاوية

أنشئ ملف `Dockerfile`:

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

أنشئ `main.py` في نفس المسار:

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

هنا يتم استيراد المكتبات اللازمة للعملية: tinify، os، time، sys، watchdog. ثم يتم تعريف فئة تسمى MyHandler والتي ترث من FileSystemEventHandler. تحتوي هذه الفئة على دالة تسمى on_created والتي يتم استدعاؤها عند اكتشاف ملف جديد في المجلد المحدد. تقوم دالة on_created بالحصول على مسار الصورة الأصلية وضغطها وحفظها في المسار المحدد للملف المضغوط. ثم يتم بدء مراقبة المجلد المحدد وعند اكتشاف ملف جديد فيه، يتم تنفيذ عملية الضغط تلقائيًا وحفظ الصورة المضغوطة في المجلد المحدد للملفات المضغوطة.

### تجميع الحاوية

يتم تجميع الحاوية باستخدام الأمر التالي في نفس مسار `Dockerfile`:

```shell
docker build -t tinypng-docker .
```

حيث `tingpng-docker` هو اسم الصورة التي سيتم إنشاؤها، و `.` هو مسار `Dockerfile`.

### وضع علامة على الصورة

يتم وضع علامة على الصورة باستخدام الأمر التالي:

```shell
docker tag <image-name> <dockerhub-username>/<repository-name>:<tag>
```

على سبيل المثال:

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

- [Homelab-%E9%AB%98%E8%B4%A8%E9%87%8F%E5%9B%BE%E7%89%87%E5%8E%8B%E7%BC%A9%E5%B7%A5%E5%85%B7TinyPNG-docker](](https://wiki-power.com/ar/)
- [GitHub repo](https://github.com/linyuxuanlin/Dockerfiles/tree/main/tinypng-docker)
- [Docker Hub](https://hub.docker.com/r/linyuxuanlin/tinypng-docker)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.