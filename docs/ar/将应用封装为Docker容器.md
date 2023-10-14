# تغليف التطبيق كحاوية Docker

تغليف التطبيق كحاوية Docker يمكن أن يسهل إدارته ونشره بشكل أفضل. فيما يلي مثال يوضح كيفية تغليف تطبيق Python كحاوية Docker وتشغيله باستخدام Docker Compose.

## القالب الأساسي

لتحويل التطبيق إلى حاوية Docker ، يجب التأكد من تثبيت Docker أولاً. ثم ، يجب إنشاء ملفين في دليل تطبيق Python الخاص بك: `Dockerfile` و `compose.yaml` ، والتي ستحتوي على ما يلي:

```Dockerfile title="Dockerfile"
# تعيين الصورة الأساسية لصورة Python الرسمية ، يمكن تخصيص الإصدار
FROM python:3.9

# تعيين دليل العمل إلى /app
WORKDIR /app

# نسخ ملفات الاعتماديات لتطبيق Python
COPY requirements.txt .

# تثبيت الاعتماديات للتطبيق
RUN pip install --no-cache-dir -r requirements.txt

# نسخ ملفات التطبيق ، من الدليل الحالي إلى الدليل داخل الحاوية
COPY . .

# تعيين الأمر الافتراضي للتشغيل
CMD ["python", "app.py"]
```

```yaml title="compose.yaml"
version: "3"
services:
  app:
    build: .
```

في ملف `compose.yaml` هذا ، قمنا بتعريف خدمة تسمى `app`. باستخدام التعليمة `build: .` ، سيتم استخدام ملف `Dockerfile` في الدليل الحالي لبناء الصورة. يمكن بناء التطبيق باستخدام `docker compose up` في دليل `compose.yaml`.

## مثال: تغليف تطبيق Python بسيط كحاوية Docker

فيما يلي مثال بسيط على تطبيق Hello World:

هذا هو تطبيق Python بسيط يستخدم Flask لطباعة Hello World على صفحة الويب:

```python title="app.py"
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
```

إذا قمنا بنشر تطبيق Python بشكل عادي دون استخدام الحاويات ، فسيتعين علينا تثبيت الاعتماديات أولاً ، وقد يتعذر ذلك في بعض الحالات ، وخاصةً في بيئة Windows. إذا قمنا بتغليفه كحاوية Docker ، يمكننا تجاهل الفروق في البيئة. حتى إذا لم يتم توصيل الجهاز المضيف بالإنترنت ، يمكننا نسخ الصورة وإكمال النشر. يوضح الخطوات التالية كيفية تحويله إلى حاوية Docker ونشره باستخدام Docker Compose.

أولاً ، قم بإنشاء ملف يسمى `Dockerfile` وأضف المحتويات التالية:

```Dockerfile title="Dockerfile"
# تعيين الصورة الأساسية لصورة Python الرسمية
FROM python:3.9

# نسخ ملفات التطبيق
COPY . /app

# تعيين دليل العمل
WORKDIR /app

# تثبيت الاعتماديات
RUN pip install flask

# فتح منفذ 8000 للوصول
EXPOSE 8000

# تشغيل التطبيق
CMD python ./app.py
```

ثم ، في نفس الدليل ، قم بإنشاء ملف يسمى `compose.yaml` وأضف المحتويات التالية:

```yaml title="compose.yaml"
version: "3"
services:
  helloworld-flask:
    build: .
    ports:
      - "8099:8000" # يمكن تخصيص المنفذ 8099
```

الآن ، يمكنك فتح الطرفية والانتقال إلى الدليل الذي يحتوي على ملفي `Dockerfile` و `compose.yaml` وتشغيل الأمر التالي لتشغيل التطبيق:

```shell
docker compose up
```

# Docker سيقوم ببناء الصورة وتشغيل الحاوية. يمكنك الوصول إلى http://localhost:8099 لرؤية حرف Hello World. باستخدام الخطوات المذكورة أعلاه ، يمكن تحويل تطبيق Python البسيط إلى حاوية ونشره باستخدام Docker Compose.

## المراجع والشكر

- [تحويل التطبيق إلى حاوية](https://docs.docker.com/get-started/02_our_app/)
- [تحويل تطبيق Python إلى حاوية في 3 دقائق](https://cloud.tencent.com/developer/article/1752513)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.