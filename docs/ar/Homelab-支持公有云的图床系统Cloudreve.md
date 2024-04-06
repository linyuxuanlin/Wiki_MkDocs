# الورشة المنزلية - نظام Cloudreve لدعم السحابة العامة

![](https://media.wiki-power.com/img/20230304195423.png)

**Cloudreve** هو نظام ملفات سحابي عام يدعم عدة محركات تخزين سحابي ويدعم الاستخدام المحلي والفرعي ومخزن الشبكة الداخلية ومخزن البيانات الشخصي من شركات مثل QiNiu وAlibaba Cloud OSS وTencent Cloud COS وUpYun وOneDrive وبروتوكول S3 المتوافق. كما يتيح النظام التفاعل مع Aria2 للتنزيل دون اتصال ويدعم العديد من المستخدمين وتحميل وإدارة الملفات بالسحب والإفلات ومعاينة وتحرير الوثائق عبر الإنترنت ودعم WebDAV. السيناريو النموذجي للاستخدام هو مشاركة الصور الشخصية أو إدارة ملفات الخدمة السحابية الشخصية.

## النشر (Docker Compose)

أولاً، نحتاج إلى إنشاء بنية الدليل. قم بالتنقل إلى الدليل الذي تحتفظ فيه بـ Cloudreve (على سبيل المثال، `/DATA/AppData/cloudreve`) وقم بتنفيذ الأمر التالي:

```shell
mkdir -vp cloudreve/{uploads,avatar,data} \
&& touch cloudreve/conf.ini \
&& touch cloudreve/cloudreve.db \
&& mkdir -p aria2/config \
&& mkdir -p cloudreve/data/aria2 \
&& chmod -R 777 cloudreve/data/aria2 \
&& mkdir data
```

أولاً، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي فيه:

```yaml title="compose.yaml"
version: "3.8"
services:
  cloudreve:
    container_name: ${STACK_NAME}_app
    image: cloudreve/cloudreve:${APP_VERSION}
    ports:
      - "${APP_PORT}:5212"
    volumes:
      - temp_data:/data
      - ${STACK_DIR}/cloudreve/uploads:/cloudreve/uploads
      - ${STACK_DIR}/cloudreve/conf.ini:/cloudreve/conf.ini
      - ${STACK_DIR}/cloudreve/cloudreve.db:/cloudreve/cloudreve.db
      - ${STACK_DIR}/cloudreve/avatar:/cloudreve/avatar
    restart: unless-stopped
    depends_on:
      - aria2
  aria2:
    container_name: ${STACK_NAME}_aria2
    image: p3terx/aria2-pro:${ARIA2_VERSION}
    volumes:
      - ${STACK_DIR}/aria2/config:/config
      - ${STACK_DIR}/data:/var/lib/docker/volumes/cloudreve_temp_data/_data
    environment:
      - RPC_SECRET=${ARIA2_RPC_SECRET}
      - RPC_PORT=${ARIA2_RPC_PORT}
    restart: unless-stopped
volumes:
  temp_data:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/temp_data
      o: bind
```

(اختياري) نوصي بإنشاء ملف `.env` في نفس الدليل الذي يحتوي على `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا لم ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة داخل `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `cloudreve`).

````markdown
```dotenv title=".env"
STACK_NAME=cloudreve
STACK_DIR=xxx # Custom project storage path, e.g., ./cloudreve

# cloudreve
APP_VERSION=latest
APP_PORT=xxxx # Custom access port, choose one that is not in use

# aria2
ARIA2_VERSION=latest
ARIA2_RPC_SECRET=xxx # ARIA2 password
ARIA2_RPC_PORT=6800
```
````

Finally, in the same directory as `compose.yaml`, execute the `docker compose up -d` command to start the orchestrated containers.

## Configuration Explanation

During the initial startup, an initial administrator account will be automatically created, which can be found in the log. If you miss it, please delete the `cloudreve.db` file in the directory and restart the main program to initialize a new administrator account.

I use the image naming convention: `{year}{month}{day}{hour}{minute}{second}{ext}`.

## References and Acknowledgments

- [Official Website](https://docs.cloudreve.org/)
- [Documentation](https://docs.cloudreve.org/getting-started/install#docker-compose)
- [Forum](https://forum.cloudreve.org/)
- [GitHub Repository](https://github.com/cloudreve/Cloudreve)
- [Docker Hub](https://hub.docker.com/r/cloudreve/cloudreve)
- [Demo Site](https://demo.cloudreve.org/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

```


> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
```
