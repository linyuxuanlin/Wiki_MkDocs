# Homelab - أداة ضغط الصور عالية الجودة TinyPNG-docker

![صورة](https://img.wiki-power.com/d/wiki-media/img/20230416163137.png)

TinyPNG-docker هو أداة تستخدم واجهة برمجة تطبيقات TinyPNG لضغط الصور عالية الجودة، حيث يمكنها ضغط صور WEBP وJPEG وPNG تلقائيًا في المسار الذي تحدده، ثم تخزين الصور المضغوطة في المسار الذي ترغب فيه. هذا يمكن أن يقلل بشكل فعال من استخدام عرض النطاق الترددي للموقع، ويقلل من حركة المرور وزمن التحميل. إذا كان ذلك غير كافٍ، فهذا تطبيق Docker الذي قمت بتطويره باستخدام ChatGPT.

## النشر (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` واستبدل `${DIR}` بالمجلد المحلي الخاص بك (مثل `/DATA/AppData`) واستبدل `${API}` بمفتاح TinyPNG الخاص بك:

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

قبل استخدام هذا حاوية Docker، يجب عليك التسجيل أولاً على موقع TinyPNG وطلب مفتاح واجهة برمجة تطبيقات (API).

استخدامه بسيط، قم بنسخ الصور التي ترغب في ضغطها إلى المجلد `${DIR}/tinypng/input` وستجد الصور المضغوطة في المجلد `${DIR}/tinypng/output`.

إذا كانت الحاوية غير قادرة على العمل بشكل صحيح، يمكنك استخدام الخطوات التالية لتحديد المشكلة:

1. تأكد من أن المسارات المحددة في ملف `compose.yaml` للمجلدات "input" و "output" صحيحة.

2. تحقق من حساب TinyPNG الخاص بك للتأكد مما إذا كان قد تم الوصول إلى الحد الأقصى لعدد مرات الضغط المسموح به بواسطة مفتاح واجهة برمجة تطبيقات (API).

3. تحقق من أن مجلد "input" يحتوي على ملفات الصور بالتنسيق الصحيح (WebP، PNG، JPEG). يرجى ملاحظة أن هذه الحاوية ستقوم بفحص وضغط الصور فقط عند حدوث حدث "created"، لذا إذا كانت الصور موجودة بالفعل، يجب نقلها يدويًا إلى مجلد "input".

4. تحقق من أن جودة الصور المضغوطة ليست أقل من إعدادات الضغط التي تم تعيينها في واجهة برمجة تطبيقات (API)، حيث قد تؤدي جودة ضغط الصور إلى فشل فك تشفير الواجهة.

5. جرب استخدام أداة ضغط TinyPNG الرسمية المتاحة على موقعهم على الإنترنت لضغط الصور يدويًا واكتشاف المشكلة بالإضافة إلى مخرجات تصحيح الأخطاء في واجهة السطر لتحديد المشكلة بشكل أفضل.

---

## عملية تطوير صور Docker

### التحضير

1. إذا لم تقم بتسجيل حساب Docker Hub بعد، فعليك أولاً إنشاء حساب على Docker Hub.

2. قم بتسجيل الدخول إلى Docker Hub:

```shell
docker login
```

اتبع التعليمات وقم بإدخال اسم المستخدم وكلمة المرور لتسجيل الدخول إلى Docker Hub.

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

ثم، قم بإنشاء ملف `main.py` في نفس المجلد:


```markdown
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

هنا يتم استيراد المكتبات الضرورية في Python أولاً: tinify، os، time، sys، watchdog. ثم يتم تعريف فئة تسمى MyHandler ترث من FileSystemEventHandler في watchdog. تحتوي هذه الفئة على وظيفة تسمى on_created، والتي ستُستدعى عندما يتم إنشاء ملف جديد في المجلد المستهدف. تقوم وظيفة on_created بالحصول على مسار الصورة المصدر وتقوم بضغطها ثم حفظها في المسار المستهدف. أخيرًا، تبدأ المراقبة لمجلد الإدخال وعندما يتم اكتشاف ملف جديد في المجلد المستهدف، سيتم تنفيذ عملية الضغط تلقائيًا وسيتم حفظ الصورة المضغوطة في المجلد المستهدف.

### بناء الحاوية

قم بتنفيذ الأمر التالي في نفس المجلد الذي يحتوي على ملف Dockerfile لبناء الحاوية:

```shell
docker build -t tinypng-docker .
```

حيث "tingpng-docker" هو اسم الصورة التي ستتم بناؤها، والنقطة "." تشير إلى موقع ملف Dockerfile.

### إعطاء الصورة علامة

استخدم الأمر التالي لإعطاء الصورة علامة:

```shell
docker tag <image-name> <dockerhub-username>/<repository-name>:<tag>
```

مثال:

```shell
docker tag tinypng-docker linyuxuanlin/tinypng-docker:latest
```
```

```markdown
### رفع صورة إلى Docker Hub

استخدم الأمر التالي لرفع الصورة إلى Docker Hub:

```shell
docker push <اسم-مستخدم-DockerHub>/<اسم-المستودع>:<وسم>
```

مثال:

```shell
docker push linyuxuanlin/tinypng-docker:latest
```

### استحضار الصورة

بعد الانتهاء من الرفع، يمكن للآخرين استحضار الصورة باستخدام الأمر التالي:

```shell
docker pull linyuxuanlin/tinypng-docker:latest
```

## المراجع والشكر

- [وثائق Homelab لأداة ضغط الصور TinyPNG-docker](to_be_replace[3])
- [مستودع GitHub](https://github.com/linyuxuanlin/Dockerfiles/tree/main/tinypng-docker)
- [Docker Hub](https://hub.docker.com/r/linyuxuanlin/tinypng-docker)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```

**ملاحظة:** يُفضل استبدال الروابط المحددة `> عنوان النص: <https://wiki-power.com/>` و `> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.` بالروابط الفعلية وفقًا للمحتوى الأصلي.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.