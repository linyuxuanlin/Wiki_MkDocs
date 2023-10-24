# تغليف التطبيق كحاوية Docker

تغليف التطبيق كحاوية Docker يمكن أن يسهل عملية النشر والإدارة. فيما يلي مثال يوضح كيفية تغليف تطبيق Python كحاوية Docker وتنفيذه باستخدام Docker Compose.

## القالب الأساسي

لتحويل التطبيق إلى حاوية Docker ، يجب التأكد من تثبيت Docker أولاً. ثم ، يجب إنشاء ملفين في دليل تطبيق Python الأساسي: `Dockerfile` و `compose.yaml` ، ويجب أن يحتوي كلاهما تقريبًا على المحتوى التالي:

```Dockerfile title="Dockerfile"
# تعيين الصورة الأساسية لـ Python كصورة رسمية ، يمكن تخصيص الإصدار
FROM python:3.9

# تعيين دليل العمل إلى /app
WORKDIR /app

# نسخ ملفات الاعتمادات لتطبيق Python
COPY requirements.txt .

# تثبيت اعتمادات التطبيق
RUN pip install --no-cache-dir -r requirements.txt

# نسخ ملفات التطبيق ، نسخها من الدليل الحالي إلى داخل الحاوية
COPY . .

# تعيين الأمر الافتراضي للتنفيذ
CMD ["python", "app.py"]
```

```yaml title="compose.yaml"
version: "3"
services:
  app:
    build: .
```

في ملف `compose.yaml` هذا ، قمنا بتعريف خدمة تسمى `app` . باستخدام التعليمة `build: .` ، ستستخدم ملف `Dockerfile` في نفس الدليل لبناء الصورة. يمكنك بناء وتشغيل هذا التطبيق عن طريق تنفيذ `docker compose up` في دليل `compose.yaml`.

## مثال: تغليف تطبيق Python بسيط كحاوية Docker

فيما يلي مثال بسيط لتطبيق Hello World:

هذا هو مثال لتطبيق Python يقوم بطباعة "Hello World" على صفحة الويب:

```python title="app.py"
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
```

إذا قمنا بنشر تطبيق Python بالطريقة التقليدية دون استخدام الحاويات ، فسيكون علينا تثبيت الاعتمادات أولاً ، وقد يحدث أخطاء في بعض الحالات التي تتطلب تثبيت حزمة بناء ، وقد يكون هناك نقص في الملفات الرأسية اللازمة. عندما نقوم بتغليفه كحاوية Docker ، يمكننا تجاهل الاختلافات في البيئة ؛ حتى إذا لم يكن الجهاز المضيف متصلاً بالإنترنت ، فإنه يمكننا فقط نسخ الصورة لإكمال عملية النشر. يوضح الخطوات التالية كيفية تغليفه كحاوية Docker ونشره باستخدام Docker Compose.

أولاً ، قم بإنشاء ملف يسمى `Dockerfile` واملأه بالمحتوى التالي:

```Dockerfile title="Dockerfile"
# تعيين الصورة الأساسية لـ Python
FROM python:3.9

# نسخ ملفات التطبيق
COPY . /app

# تعيين دليل العمل
WORKDIR /app

# تثبيت الاعتمادات
RUN pip install flask

# فتح منفذ 8000 للوصول إليه
EXPOSE 8000

# تشغيل التطبيق
CMD python ./app.py
```

ثم ، قم بإنشاء ملف يسمى `compose.yaml` في نفس الدليل وانسخ المحتوى التالي إليه:

```yaml title="compose.yaml"
version: "3"
services:
  helloworld-flask:
    build: .
    ports:
      - "8099:8000" # يمكن تخصيص المنفذ 8099
```

الآن ، يمكنك فتح الطرفية والانتقال إلى الدليل الذي يحتوي على ملفي `Dockerfile` و `compose.yaml` ، وتشغيل الأمر التالي لتشغيل التطبيق:

```shell
docker compose up
```

Docker سيقوم ببناء الصورة وتشغيل الحاوية. يمكنك الوصول إلى Hello World عن طريق زيارة <http://localhost:8099>. من خلال الخطوات المذكورة أعلاه ، يمكنك تحويل تطبيق Python البسيط إلى حاوية ونشره باستخدام Docker Compose.

## المراجع والشكر

- [تحويل التطبيق إلى حاوية](https://docs.docker.com/get-started/02_our_app/)
- [تحويل تطبيق Python إلى حاوية في 3 دقائق](https://cloud.tencent.com/developer/article/1752513)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.