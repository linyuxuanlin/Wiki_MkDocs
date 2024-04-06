# Homelab - منصة إدارة تطبيقات الحاويات Portainer

![](https://media.wiki-power.com/img/202304111545899.png)

**Portainer** هو أداة إدارة رسومية لتطبيقات الحاويات (بما في ذلك Docker / Docker Compose / Swarm / Kubernetes)، والتي يمكن استخدامها لإدارة بيئة Docker من خلال واجهة ويب. يوفر أيضًا العديد من الميزات مثل عرض السجلات، بدء وإيقاف الحاويات، إدارة الصور، وإدارة الشبكات والأقراص وغيرها.

## النشر (Docker Compose)

أولاً، يجب إنشاء ملف `compose.yaml` ولصق المحتوى التالي:

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

(اختياري) يُوصى بإنشاء ملف `.env` في نفس دليل `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة في `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `portainer`).

```dotenv title=".env"
STACK_NAME=portainer
STACK_DIR=xxx # تخصيص مسار تخزين المشروع الخاص بك، مثل ./portainer

# portainer
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك، اختر منفذًا غير مستخدم
```

أخيرًا، يمكنك تشغيل حاويات التكوين بنجاح بتنفيذ الأمر `docker compose up -d` في نفس دليل `compose.yaml`.

## توضيحات عن التكوين

يرجى ملاحظة أن الصورة المجتمعية للنسخة الخالية من المشكلات هي `portainer/portainer-ce`، وتختلف عن الإصدار التجاري (portainer-be).

## المراجع والشكر

- [الموقع الرسمي](https://www.portainer.io/)
- [الوثائق](https://docs.portainer.io/)
- [مستودع GitHub](https://github.com/portainer/portainer)
- [مستودع Docker Hub](https://hub.docker.com/r/portainer/portainer-ce)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
