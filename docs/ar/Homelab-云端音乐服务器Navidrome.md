# Homelab - خادم الموسيقى السحابي Navidrome

![](https://media.wiki-power.com/img/20230531212854.png)

**Navidrome** هو خادم موسيقى ووسائط متعددة مفتوح المصدر وقائم على الويب. يمكنك تخزين موسيقاك الخاصة والاستماع إليها على عدة عملاء.

## النشر (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  navidrome:
    container_name: ${STACK_NAME}_app
    image: deluan/navidrome:${APP_VERSION}
    user: 1000:1000 # إذا كانت هناك مشكلة في الأذونات ، يمكنك محاولة النشر باستخدام root (0:0)
    ports:
      - "${APP_PORT}:4533"
    environment:
      # اختياري: ضع تخصيصات خيارات التكوين الخاصة بك هنا. أمثلة:
      ND_SCANSCHEDULE: 24h
      ND_LOGLEVEL: info
      ND_SESSIONTIMEOUT: 24h
      ND_BASEURL: ""
    volumes:
      - ${STACK_DIR}:/data
      - ${DATA_DIR}:/music:ro
    restart: unless-stopped
```

(اختياري) يُوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، يمكنك تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `navidrome`).

```dotenv title=".env"
STACK_NAME=navidrome
STACK_DIR=xxx # تخصيص مسار تخزين المشروع ، على سبيل المثال ./navidrome
DATA_DIR=xxx # تخصيص مسار تخزين الموسيقى ، على سبيل المثال ./music

# navidrome
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول ، اختر منفذًا غير مستخدم
```

إذا كان لديك NAS ، يمكنك أيضًا توصيل مساحة التخزين على NAS باستخدام بروتوكول NFS لتخزين الموسيقى على NAS وتوفير مساحة الخادم. لمزيد من التفاصيل ، يرجى الاطلاع على [**توسيع مساحة القرص الصلب لـ NAS Synology تحت Linux (NFS)**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مجلد `compose.yaml` لتشغيل الحاوية المنظمة.

## تعليمات التكوين

هناك العديد من التطبيقات المتاحة للهواتف المحمولة ، وأفضل تجربة لدي على Android هي substreamer. يمكنك الاطلاع على المزيد من التطبيقات في القائمة الرسمية [**Apps**](https://www.navidrome.org/docs/overview/#apps).

## المراجع والشكر

- [الموقع الرسمي](https://www.navidrome.org/)
- [الوثائق](https://www.navidrome.org/docs/installation/docker/)
- [مستودع GitHub](https://github.com/navidrome/navidrome/)
- [Docker Hub](https://hub.docker.com/r/deluan/navidrome)
- [موقع العرض التوضيحي](https://demo.navidrome.org/app/) (اسم المستخدم وكلمة المرور هما demo)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
