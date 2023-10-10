# Docker Compose - أداة ترتيب الصور الخاصة بـ Docker

![](https://f004.backblazeb2.com/file/wiki-media/img/20210117130925.jpg)

Docker Compose هي أداة ترتيب الصور الخاصة بـ Docker. يوصى باستخدام Docker Compose كطريقة افتراضية لفتح Docker ، لأنها لا تسمح فقط بتكوين ونشر الصور بسهولة ، بل تسمح أيضًا بتكوين خدمات الصور المتعددة بسهولة ، وحتى تمييز ترتيب تشغيلها ، وهو ما لا يتوفر في طريقة الفتح باستخدام الأوامر.

على الرغم من أن فكرة Docker هي الفصل بين العمليات (عملية واحدة لكل صورة) وزيادة قابلية إعادة الاستخدام وعدم تضمين خدمات متعددة في صورة واحدة ، إلا أن هناك بعض التطبيقات التي تتطلب تشغيل خدمات متعددة في نفس الوقت. على سبيل المثال ، تحتاج تطبيقات الويب النموذجية على الأقل إلى تعاون بين الخادم وقاعدة البيانات. وبالتالي ، ستحتاج إلى نشر حاويات اثنين على حدة ، وحتى بعض الخدمات تحتاج إلى تشغيلها بترتيب محدد. وبالتالي ، سيكون الصور المطلوبة وخطوات التشغيل معقدة للغاية.

يضع Docker Compose جميع الصور المطلوبة (جميع خصائص الخدمات والحاويات المطلوبة وتكوين الشبكة وتعليقات التخزين) والترتيب في ملف YAML واحد. يمكنك تشغيل حاويات وفقًا للطريقة والخطوات التي تحتاجها دون الحاجة إلى التحكم اليدوي في كل حاوية. فيما يلي مثال على Docker Compose لنشر خدمة ويب:

```yaml title="compose.yaml"
version: "3"
services:
  web:
    image: beginor/geoserver:2.11.1
    container_name: geoserver-web
    hostname: geoserver-web
    ports:
      - 8080:8080
    volumes:
      - ./web/data_dir:/geoserver/data_dir
      - ./web/logs:/geoserver/logs
    restart: unless-stopped
    links:
      - database:database
  database:
    image: beginor/postgis:9.3
    container_name: postgis
    hostname: postgis
    ports:
      - 5432:5432
    volumes:
      - ./database/data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: 1q2w3e4R
    restart: unless-stopped
```

في هذا الملف YAML ، تم تعريف وتشغيل مثيلين لـ `web` و `database`.

## تثبيت وتكوين Docker Compose

يعتمد Docker Compose على Docker Engine ، لذلك يرجى التأكد من تثبيت بيئة Docker Engine أولاً. إذا لم تكن قد قمت بالتثبيت بعد ، فيمكنك الرجوع إلى الدرس السابق: [**مفاهيم Docker الأساسية**](https://wiki-power.com/ar/Docker%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) ، وتثبيت بيئة Docker Engine.

إذا كنت تستخدم عميل سطح المكتب Windows / MacOS / Linux ، فلا حاجة لتثبيت Docker Compose بشكل منفصل ، لأنه مضمن بالفعل. فيما يلي طريقة تثبيت Docker Compose في بيئة Linux Docker Engine.

بالنسبة لـ Ubuntu و Debian ، استخدم الأمر التالي لتثبيت Docker Compose:

```shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

بالنسبة لإصدارات RPM من Linux (مثل CentOS) ، استخدم الأمر التالي لتثبيت Docker Compose:

```shell
sudo yum update
sudo yum install docker-compose-plugin
```

بعد الانتهاء ، استخدم الأمر التالي للتحقق من نجاح التثبيت:

```shell
docker compose version
```

## كيفية استخدام Docker Compose

عادةً ما نقوم بإنشاء ملف `compose.yaml` (الإصدارات القديمة تسمى `docker-compose.yml` وهي متوافقة أيضًا) ونضعه في مجلد يحمل اسم التطبيق، مثل `web/compose.yaml`.

لتشغيل هذا البرنامج، يمكنك ببساطة تنفيذ الأمر `docker compose up` في هذا المجلد لتشغيل الخدمات وفقًا لتكوين الملف YAML. (يمكنك تشغيله في الخلفية باستخدام الخيار `-d`)

لإيقاف تشغيل تطبيق الحاويات، يمكنك استخدام الأمر `docker compose down`.

## كتابة ملف Docker Compose

الطريقة الافتراضية لاستخدام Docker Compose هي إنشاء ملف بتنسيق YAML وتسميته افتراضيًا `compose.yaml`. يتضمن المثال التالي قالبًا يحتوي على جميع المعلمات المتاحة (ولكن ليس من الضروري استخدامها جميعًا):

```yaml title="compose.yaml"
version: "3"

services:
  service1:
    build:
      context: .
      dockerfile: Dockerfile
    image: your-image1
    command: ["python", "app.py"]
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
    networks:
      - your-network
    environment:
      - ENV_VARIABLE=value
    depends_on:
      - db

  db:
    image: mysql:5.7
    environment:
      - MYSQL_ROOT_PASSWORD=yourpassword
    volumes:
      - db-data:/var/lib/mysql

networks:
  your-network:

volumes:
  your-volume:
  db-data:
```

عادةً ما يتضمن ملف `compose.yaml` المعلمات التالية:

- **version**: يستخدم لعرض معلومات إصدار ملف compose. يرتبط بإصدار Docker Engine وقد يحتوي على ميزات جديدة أو بناء جديد للصياغة. يرجى الرجوع إلى الوثائق الرسمية [**Compose file versions and upgrading**](https://docs.docker.com/compose/compose-file/compose-versioning/).
- **services**: يحدد الخدمات (الحاويات) الموجودة في ملف compose. كل خدمة هي حاوية مستقلة ويمكن تحديد صورتها وتعيين مخرجات البورت والمتغيرات البيئية وغيرها.
- **container_name**: اسم الحاوية، ليس إلزاميًا ولكن لا يمكن تكرار الأسماء.
- **networks**: يحدد تكوين الشبكة بين الخدمات. يمكن إنشاء شبكة مخصصة وتوصيل الخدمات بها لتحقيق الاتصال بين الحاويات.
- **volumes**: يحدد تكوين توصيل الأقراص للحاويات. يمكن توصيل مجلدات أو ملفات الحاويات بمجلدات أو ملفات المضيف لتحقيق الاستدامة والمشاركة. يعادل خيار `-v` في Docker CLI.
- **environment** (أو `env_file`): يحدد اسم ومسار ملف المتغيرات البيئية للحاوية ويحدد تحميل المتغيرات البيئية من هذا الملف. يمكن تجاهله إذا لم يتم تكوين المتغيرات البيئية. إذا كانت المتغيرات البيئية في المجلد الحالي واسمها `.env` ، فيمكن تجاهلها. يعادل خيار `-e` في Docker CLI.
- **build**: يستخدم لتشغيل الحاوية باستخدام الصورة المنشأة. يحدد مسار ملف Dockerfile.
- **image**: يحدد الصورة التي تستخدمها الحاوية. يمكن استخدام صورة من مستودع الصور العام أو تحديد ملف Dockerfile المحلي.
- **ports**: يحدد تعيين البورت بين الحاوية والمضيف ويمكن تحديد بروتوكول التعيين (TCP أو UDP). يعادل خيار `-p` في Docker CLI.
- **depends_on**: يحدد العلاقات الوظيفية بين الخدمات. يمكن تحديد اسم واحد أو أكثر للخدمات التي يعتمد عليها الخدمة الحالية للبدء.
- **restart**: يحدد استراتيجية إعادة تشغيل الحاوية. يمكن تعيينها إلى `no` (لا يتم إعادة التشغيل تلقائيًا) أو `always` (يتم إعادة التشغيل تلقائيًا دائمًا) أو `unless-stopped` (يتم إعادة التشغيل تلقائيًا ما لم يتم إيقاف الحاوية يدويًا) أو `on-failure` (يتم إعادة التشغيل فقط في حالة الفشل). يعادل خيار `--restart` في Docker CLI.
- **command**: يحدد الأمر الذي يتم تشغيله عند بدء الحاوية ويمكن استخدامه لتغيير الأمر الافتراضي لصورة الحاوية.
- **volumes_from**: يحدد الحاوية التي توفر الأقراص التي يتم توصيلها للحاوية.

## بعض أوامر Docker Compose الشائعة

هذه بعض الأوامر الشائعة لإدارة وتشغيل الخدمات المحددة في ملف `compose.yaml`:



- `docker compose up`: يقوم ببناء الصور المحددة في compose ويشغل الحاويات. إذا لزم الأمر ، فسيقوم ببناء الصور تلقائيًا (إذا تم تغيير Dockerfile) ، ثم يشغل جميع الخدمات المحددة. إذا كنت تريد تشغيلها في الخلفية ، فأضف `-d` كمعامل.
- `docker compose down`: يوقف ويزيل جميع الحاويات والشبكات والأقراص المحددة في compose. سيتم إيقاف الخدمات التي تعمل وتنظيف جميع الموارد ذات الصلة.
- `docker compose pull`: يستخدم لجلب جميع الصور المحددة في compose أو لتحديث الصور.
- `docker compose start`: يشغل الحاويات الموجودة في compose ، ولن يتم إعادة إنشاء الحاويات أو إعادة بناء الصور.
- `docker compose stop`: يوقف الحاويات الموجودة في compose ، ولكن لا يزيلها.
- `docker compose restart`: يعيد تشغيل الحاويات الموجودة في compose.
- `docker compose pause`: يوقف الحاويات الموجودة في compose مؤقتًا.
- `docker compose unpause`: يستأنف تشغيل الحاويات الموجودة في compose بعد التوقف المؤقت.
- `docker compose ps`: يعرض حالة جميع الحاويات الموجودة في compose التي تعمل.
- `docker compose logs`: يعرض سجلات الحاويات الموجودة في compose.
- `docker compose exec`: يستخدم لتنفيذ الأوامر في الحاويات الموجودة في compose. على سبيل المثال: `docker exec -it [compose-name] /bin/bash`

هذه بعض الأوامر الشائعة ، يمكنك أيضًا تنفيذ `docker compose --help` لعرض المزيد من الأوامر المتاحة.

## المتغيرات البيئية

في Docker Compose ، على الرغم من أن المتغيرات البيئية ليست إلزامية ، إلا أنه من المستحسن استخدامها بشكل كبير لأنها تتمتع بالمزايا التالية:

1. **المرونة والقابلية للتكوين**: يمكنك بسهولة ضبط معلومات تكوين التطبيق دون الحاجة إلى تعديل صور Docker أو إعادة بناء الحاويات.
2. **الأمان والعزلة**: عن طريق تخزين المعلومات الحساسة في المتغيرات البيئية بدلاً من كتابتها مباشرة في الشفرة أو ملف التكوين ، يمكن زيادة أمان التطبيق عن طريق منح المتغيرات البيئية تراخيص منفصلة.
3. **التوافق عبر المنصات**: يمكن تمرير معلومات تكوين مختلفة عبر المنصات أو أنظمة التشغيل باستخدام المتغيرات البيئية دون الحاجة إلى تعديل ملفات التكوين أو شفرة الصورة.
4. **تبسيط النشر والإدارة**: من خلال استخدام المتغيرات البيئية لتكوين معلمات الحاويات المختلفة بشكل موحد ، يمكن تقليل المحتوى المكرر في ملفات التكوين وجعل العملية بأكملها أكثر وضوحًا وسهولة في الصيانة.
5. **التكامل والتلقائية**: يمكن تمرير معلمات تكوين التطبيق تلقائيًا إلى حاويات Docker باستخدام أدوات CI / CD والتكامل التلقائي.

المتغيرات البيئية هي ملف ينتهي بالامتداد `.env` ، وعادة ما يتم إنشاؤه مباشرة في نفس مستوى `compose.yaml` باسم `.env` ، وفيما يلي مثال:

```dotenv title=".env"
TAG=v1.5
```

يمكن الاستفادة من المتغيرات البيئية مباشرة في `compose.yaml`:

```yaml title="compose.yaml"
services:
  web:
    image: "webapp:${TAG}"
```

## نصائح

هناك موقع يحول واجهة سطر الأوامر CLI لـ Docker إلى Docker Compose YAML: [**composerize**](https://www.composerize.com/) ، ولكن نتائج التحويل قد لا تكون دقيقة وتحتاج إلى التحقق.

## المراجع والشكر

- [استخدام docker compose بدلاً من docker run](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [تثبيت Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [تفسير معلمات ملفات قالب Docker-Compose](https://blog.51cto.com/14154700/2466054)
- [في الأصل، يمكن استخدام Docker Compose على Synology NAS!](https://www.himiku.com/archives/docker-compose-for-synology-nas.html)
- [Docker - من البداية إلى العملية](https://docker-practice.github.io/zh-cn/)
- [سلسلة Docker - فهم ملف تكوين Docker Compose](https://blognas.hwb0307.com/linux/docker/3880)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.