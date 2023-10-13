# أساسيات Docker

![](https://img.wiki-power.com/d/wiki-media/img/20210116153041.png)

من المعروف أن تكوين البيئة هو واحد من أكثر الأشياء المزعجة في تطوير البرمجيات. يمكن أن تؤدي اختلافات بيئة التشغيل إلى نتائج غير متوقعة ، ويمكن تجنب هذه المشكلة باستخدام Docker.

## Docker وتقنية الحاويات

يقوم Docker بتعبئة البرنامج نفسه والبيئة التي يحتاجها في حزمة واحدة ، لذلك لا يحتاج المستخدم إلى تكوين البيئة مرة أخرى (لأن البيئة موجودة في الحزمة) ، وبالتالي يمكن ضمان أن بيئتك مطابقة لبيئة المطور وتجنب مشكلات الاختلاف في بيئة التشغيل.

يستخدم Docker تقنية **الحاويات**. عندما نتحدث عن تقنية الحاويات ، يمكننا مقارنتها بـ **حاوية الشحن**. إنها حاوية كبيرة **موحدة** يمكن تحميلها وتفريغها بسهولة بين مختلف وسائل النقل (مثل السفن والقطارات والشاحنات) ، دون الحاجة إلى النظر في تكوين محتوياتها الداخلية. بطريقة مماثلة ، تقوم تقنية الحاويات بتعبئة التطبيق وجميع الاعتماديات الخاصة به في بيئة مستقلة وقابلة للتنقل ، وتسمى الحاوية.

الهدف الرئيسي لتقنية الحاويات هو تحقيق نشر التطبيقات بسرعة وقابلية التوسع والعزلة البيئية. من خلال تعبئة التطبيق والاعتماديات ذات الصلة في حاوية واحدة ، يمكننا التأكد من تشغيل التطبيق بنفس الطريقة على أجهزة الكمبيوتر أو الخوادم المختلفة ، دون الحاجة إلى القلق بشأن اختلافات البيئة أو تعارض الاعتماديات. هذا يتيح للمطورين تسليم التطبيقات بشكل أسرع ، ويبسط أيضًا عملية نشر وإدارة التطبيقات.

أحد مزايا تقنية الحاويات الرئيسية هو أنها توفر حلًا للتجاوز الخفيف للتقنية الافتراضية. بالمقارنة مع الآلة الافتراضية التقليدية ، تقنية الحاويات أخف وزنًا وتستهلك موارد أقل. يتم تشغيل كل حاوية على نفس النواة في نظام التشغيل المضيف ، ويتم مشاركة موارد نظام التشغيل ، لذلك يتم تشغيل الحاوية بشكل أسرع وتستهلك ذاكرة أقل ، ويمكن تشغيل عدة حاويات في نفس الجهاز.

يعد Docker حاليًا حلًا شائعًا لتقنية الحاويات. يتكون بشكل أساسي من ثلاثة عناصر ، وهي Image (صورة) و Container (حاوية) و Repository (مستودع).

- **Image (صورة)**: الصورة هي ملف قابل للتنفيذ ، يحتوي على جميع نظام الملفات الخاص بالتطبيق واعتمادياته (الشفرة والوقت التشغيلي وأدوات النظام وملفات المكتبات) والتكوين. يمكننا النظر إلى الصورة على أنها قالب الحاوية ، ويمكن استخدامها لإنشاء عدة حاويات مختلفة.
- **Container (حاوية)**: الحاوية هي نسخة تعمل من الصورة. كل حاوية معزولة وتعمل بشكل مستقل ، ويمكن تشغيل التطبيقات فيها.
- **Repository (مستودع)**: المستودع هو مكان لتخزين ومشاركة الصور. يمكننا دفع الصور التي أنشأناها إلى المستودع ، ويمكننا أيضًا سحب الصور التي أنشأها الآخرون من المستودع.

علاقة الحاوية بالصورة تشبه علاقة الكائن بالفئة في برمجة الكائنات.

## تثبيت وتكوين Docker

قبل تثبيت Docker ، يمكن استخدام الأمر التالي لإلغاء تثبيت حزم الإصدارات القديمة وتجنب التعارض:

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

يمكن تنزيل وتثبيت Docker Engine باستخدام البرنامج النصي الرسمي للموقع الرسمي لـ Docker: (يتطلب صلاحيات root)

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

نظرًا لأن Docker يعمل ويعتمد على بيئة Linux ، فإنه لا يتسبب في أي فقد في الكفاءة. ومع ذلك ، إذا كنت ترغب في نشر Docker على أنظمة أخرى ، فيجب عليك تثبيت بيئة Linux افتراضية أولاً.

![](https://img.wiki-power.com/d/wiki-media/img/20230708005714.png)

للحصول على طريقة تثبيت Docker على Windows ، يرجى الرجوع إلى الوثائق الرسمية [**Install Docker Desktop on Windows**](https://docs.docker.com/desktop/install/windows-install/).

للحصول على طريقة تثبيت Docker على MacOS ، يرجى الرجوع إلى الوثائق الرسمية [**Install Docker Desktop on Mac**](https://docs.docker.com/desktop/install/mac-install/).

بعد الانتهاء من التثبيت ، يمكننا استخدام الأمر التالي للتحقق مما إذا كان Docker قد تم تثبيته بنجاح:

```shell
docker version
```

بعد تثبيت Docker Engine على Linux ، إذا كنت ترغب في استخدامه كمستخدم غير root ، فيمكنك استخدام الأمر التالي لتكوين الأذونات:

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
```

بعد الانتهاء من التكوين ، قد يكون من الضروري تسجيل الخروج وتسجيل الدخول مرة أخرى لتحديث الأذونات.

إذا واجهت مشكلة أثناء التثبيت ، يرجى الرجوع إلى الوثائق الرسمية [**Troubleshoot Docker Engine installation**](https://docs.docker.com/engine/install/troubleshoot/) .

## مثال: Hello World

سنستخدم مثال hello-world الرسمي لـ Docker لشرح كيفية استخدامه. قم بفتح الطرفية أو موجه الأوامر وأدخل الأمر التالي لتشغيل حاوية hello-world:

```shell
docker run hello-world
```

سيتم تنزيل صورة hello-world من مستودع صور Docker وإنشاء وتشغيل الحاوية. عندما ترى إخراج hello world ، فهذا يعني أن التشغيل نجح.

## بعض أوامر CLI الشائعة لـ Docker

يوفر Docker مجموعة قوية وغنية من الأوامر لإدارة وتشغيل الموارد مثل الحاويات والصور والشبكات. فيما يلي بعض الأوامر الشائعة لـ Docker CLI:

- `docker run`: يستخدم لإنشاء وتشغيل حاوية جديدة بناءً على الصورة المحددة. على سبيل المثال ، `docker run -d -p 8080:80 nginx` سيشغل حاوية NGINX في الخلفية ويعيد توجيه منفذ 8080 من المضيف إلى منفذ 80 في الحاوية.
- `docker ps`: يعرض الحاويات التي تعمل حاليًا. عندما يتم تشغيل هذا الأمر ، يتم عرض معلومات مثل معرف الحاوية والصورة والأمر. باستخدام الأمر `docker ps -a` يمكن عرض جميع الحاويات ، بما في ذلك تلك التي تم إيقافها.
- `docker stop`: يتوقف عن تشغيل حاوية واحدة أو أكثر. يمكن تحديد معرف الحاوية أو الاسم. على سبيل المثال ، `docker stop mycontainer` سيتوقف عن تشغيل الحاوية التي تحمل الاسم `mycontainer`.
- `docker start`: يبدأ حاوية واحدة أو أكثر التي تم إيقاف تشغيلها. يمكن تحديد معرف الحاوية أو الاسم.
- `docker stop`: يتوقف عن تشغيل حاوية واحدة أو أكثر.
- `docker restart`: يعيد تشغيل حاوية واحدة أو أكثر.
- `docker rm`: يحذف حاوية واحدة أو أكثر. يمكن استخدام الأمر `docker rm -f` لحذف الحاويات التي تعمل حاليًا.
- `docker images`: يعرض الصور المحلية. يتم عرض قائمة بالصور التي تم تنزيلها وإنشاؤها على الكمبيوتر المحلي ، بما في ذلك معرف الصورة والحجم ووقت الإنشاء.
- `docker rmi`: يحذف صورة واحدة أو أكثر. يمكن تحديد معرف الصورة أو العلامة. على سبيل المثال ، `docker rmi myimage:1.0` سيحذف الصورة التي تحمل الاسم `myimage` والعلامة `1.0`.
- `docker build`: يستخدم لبناء صورة مخصصة بناءً على Dockerfile. على سبيل المثال ، `docker build -t myimage:1.0 .` سيقوم ببناء صورة تحمل الاسم `myimage` والعلامة `1.0` بناءً على Dockerfile الموجود في الدليل الحالي.
- `docker exec`: يستخدم لتنفيذ أمر داخل حاوية تعمل. يمكن تحديد معرف الحاوية أو الاسم والأمر الذي يجب تنفيذه. على سبيل المثال ، `docker exec -it mycontainer bash` سيبدأ محطة عمل تفاعلية جديدة داخل الحاوية التي تحمل الاسم `mycontainer`.

هذه بعض الأوامر الشائعة لـ Docker لإدارة وتشغيل الحاويات والصور. هناك المزيد من الأوامر التي يمكن استكشافها ، يمكن العثور على قائمة كاملة للأوامر والخيارات الأخرى المتاحة من خلال الأمر `docker --help` ، كما يمكن الرجوع إلى الوثائق الرسمية [**Use the Docker command line**](https://docs.docker.com/engine/reference/commandline/cli/) .

لمزيد من المعلومات حول Docker ، يرجى الرجوع إلى المقالات التالية:

- [**Docker Compose - أداة ترتيب الصور**](](https://wiki-power.com/ar/DockerCompose-%E9%95%9C%E5%83%8F%E7%BC%96%E6%8E%92%E5%B7%A5%E5%85%B7/)
- [**تغليف التطبيق كحاوية Docker**](](https://wiki-power.com/ar/%E5%B0%86%E5%BA%94%E7%94%A8%E5%B0%81%E8%A3%85%E4%B8%BADocker%E5%AE%B9%E5%99%A8/)

إذا كنت ترغب في البدء في التطبيق العملي مباشرةً ، فيمكنك الاطلاع على سلسلة المقالات التالية:

- [بناء HomeLab الخاص بك](https://wiki-power.com/ar/بناء HomeLab الخاص بك)
- [Homelab - لوحة إدارة خادم خفيفة CasaOS](https://wiki-power.com/ar/Homelab - لوحة إدارة خادم خفيفة CasaOS)
- [Homelab - لوحة إدارة شهادة الوكيل Nginx Proxy Manager](https://wiki-power.com/ar/Homelab - لوحة إدارة شهادة الوكيل Nginx Proxy Manager)
- [Homelab - أداة اختراق الشبكة الداخلية frp](https://wiki-power.com/ar/Homelab - أداة اختراق الشبكة الداخلية frp)
- [Homelab - بديل مجاني لأداة اختراق الشبكة الداخلية Cloudflared](https://wiki-power.com/ar/Homelab - بديل مجاني لأداة اختراق الشبكة الداخلية Cloudflared)
- [Homelab - محرر كود عبر الإنترنت code-server](https://wiki-power.com/ar/Homelab - محرر كود عبر الإنترنت code-server)
- [Homelab - أداة مراقبة حالة الموقع على الإنترنت Uptime Kuma](https://wiki-power.com/ar/Homelab - أداة مراقبة حالة الموقع على الإنترنت Uptime Kuma)
- [Homelab - أداة ضغط صور عالية الجودة TinyPNG-docker](https://wiki-power.com/ar/Homelab - أداة ضغط صور عالية الجودة TinyPNG-docker)
- [Homelab - موقع توجيه الإشارات المرجعية الشخصي البسيط Flare](https://wiki-power.com/ar/Homelab - موقع توجيه الإشارات المرجعية الشخصي البسيط Flare)
- [Homelab - منصة إدارة تطبيقات الحاويات Portainer](https://wiki-power.com/ar/Homelab - منصة إدارة تطبيقات الحاويات Portainer)
- [Homelab - أداة مزامنة عبر الأجهزة Syncthing](https://wiki-power.com/ar/Homelab - أداة مزامنة عبر الأجهزة Syncthing)
- [Homelab - أداة ملاحظات متناثرة memos](https://wiki-power.com/ar/Homelab - أداة ملاحظات متناثرة memos)
- [Homelab - نظام ويكي قوي Wiki.js](https://wiki-power.com/ar/Homelab - نظام ويكي قوي Wikijs)
- [Homelab - أداة إدارة كلمات المرور الذاتية الاستضافة Vaultwarden](https://wiki-power.com/ar/Homelab - أداة إدارة كلمات المرور الذاتية الاستضافة Vaultwarden)
- [Homelab - نظام تخزين الصور العام يدعم Cloudreve](https://wiki-power.com/ar/Homelab - نظام تخزين الصور العام يدعم Cloudreve)
- [Homelab - مجمع RSS الذاتي الاستضافة FreshRSS](https://wiki-power.com/ar/Homelab - مجمع RSS الذاتي الاستضافة FreshRSS)
- [Homelab - جهاز حماية متعدد البروتوكولات Next Terminal](https://wiki-power.com/ar/Homelab - جهاز حماية متعدد البروتوكولات Next Terminal)
- [Homelab - صندوق أدوات PDF متعدد الوظائف Stirling-PDF](https://wiki-power.com/ar/Homelab - صندوق أدوات PDF متعدد الوظائف Stirling-PDF)
- [Homelab - أداة جلب رمز الموقع favicon iconserver](https://wiki-power.com/ar/Homelab - أداة جلب رمز الموقع favicon iconserver)
- [Homelab - أداة تحديث الحاويات Docker تلقائيًا Watchtower](https://wiki-power.com/ar/Homelab - أداة تحديث الحاويات Docker تلقائيًا Watchtower)
- [Homelab - برنامج قائمة الملفات الذي يدعم العديد من التخزين Alist](https://wiki-power.com/ar/Homelab - برنامج قائمة الملفات الذي يدعم العديد من التخزين Alist)
- [Homelab - برنامج لوحة الإعلانات الغني بالميزات WeKan](https://wiki-power.com/ar/Homelab - برنامج لوحة الإعلانات الغني بالميزات WeKan)
- [Homelab - خادم البودكاست والكتب الصوتية Audiobookshelf](https://wiki-power.com/ar/Homelab - خادم البودكاست والكتب الصوتية Audiobookshelf)
- [Homelab - خادم الموسيقى السحابي Navidrome](https://wiki-power.com/ar/Homelab - خادم الموسيقى السحابي Navidrome)
- [Homelab - خادم الوسائط المرئية والسمعية Jellyfin](https://wiki-power.com/ar/Homelab - خادم الوسائط المرئية والسمعية Jellyfin)
- [Homelab - خادم إدارة الكتب الإلكترونية calibre-web](https://wiki-power.com/ar/Homelab - خادم إدارة الكتب الإلكترونية calibre-web)
- [Homelab - خادم المنزل الذكي Home Assistant](https://wiki-power.com/ar/Homelab - خادم المنزل الذكي Home Assistant)
- [Homelab - برنامج مساعدة الذاكرة بالبطاقات Anki](https://wiki-power.com/ar/Homelab - برنامج مساعدة الذاكرة بالبطاقات Anki)

## المراجع والشكر

- [Docker - من البداية إلى العملية](https://yeasy.gitbook.io/docker_practice/)
- [دليل Docker](https://www.runoob.com/docker/docker-tutorial.html)
- [دليل بدء استخدام Docker](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [تثبيت Docker على CentOS](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
