# Homelab - منصة إدارة تطبيقات الحاويات Portainer

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304111545899.png)

**Portainer** هي أداة إدارة رسومية لتطبيقات الحاويات (بما في ذلك Docker / Docker compose / Swarm / Kubernetes) ، والتي يمكن استخدامها لإدارة بيئة Docker من خلال واجهة الويب. كما توفر العديد من الميزات مثل عرض السجلات وبدء وإيقاف تشغيل الحاويات وإدارة الصور والشبكات والأقراص الافتراضية وغيرها.

## التنصيب (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` ولصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3.3"
services:
  portainer:
    container_name: ${STACK_NAME}_app
    image: portainer/portainer-ce:${APP_VERSION}
    ports:
      - ${APP_PORT_HTTP}:9000 # HTTP
    # - ${APP_PORT_HTTPS}:9443 # HTTPS (اختياري)
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ${STACK_DIR}/portainer_data:/data
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، فيمكنك تخصيص المعلمات الخاصة بك مباشرة في `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `portainer`).

```dotenv title=".env"
STACK_NAME=portainer
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./portainer

# portainer
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك ، واختيار غير مستخدم يكون مناسبًا
```

أخيرًا ، يمكنك تشغيل حاويات الترتيب المسبق بتنفيذ الأمر `docker compose up -d` في نفس مستوى `compose.yaml`.

## شرح التكوين

يجب ملاحظة أن صورة الإصدار المجتمعي هي `portainer/portainer-ce` ، وتختلف عن الإصدار التجاري (portainer-be).

## المراجع والشكر

- [الموقع الرسمي](https://www.portainer.io/)
- [الوثائق](https://docs.portainer.io/)
- [مستودع GitHub](https://github.com/portainer/portainer)
- [Docker Hub](https://hub.docker.com/r/portainer/portainer-ce)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
