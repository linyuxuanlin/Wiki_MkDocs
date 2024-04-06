````markdown
# هاك.انيت( ) هاكثون القرصنة

—— وايت · نظام إضاءة بدون أسلاك مبني على منصة السحابة.

![](https://media.wiki-power.com/img/wight.jpg)

مستودع المشروع: [**linyuxuanlin / Wight**](https://github.com/linyuxuanlin/Wight)

## الخلفية

تم إنشاء هذا المشروع في هاك.انيت( ) هاكثون القرصنة عام 2017. قضينا أكثر من 20 ساعة برمجة ونمذجة وإصلاح مجموعة متنوعة من الأخطاء والتحضير للطباعة والعرض والمحاضرة، وأخيرًا تم الحصول على منتج جاهز بعض الشيء.

يستخدم هذا المشروع بشكل رئيسي في نظام إضاءة أعمدة الإنارة على الطرق في المناطق النائية والريفية. النموذج قد يبدو مجرداً قليلاً، ولكن في الواقع يقوم بدور أحد أعمدة الإنارة.

## نقاط الابتكار في المشروع

- **الطاقة الشمسية.** نظام مستدام (وفقًا للبيانات المفصلة، الطاقة الشمسية كافية لإضاءة اللمبات اللدنية)
- **بدون أسلاك.** يوفر الراحة في مناطق الجبال البعيدة حيث يكون من الصعب tendireك الأسلاك
- **خوارزميات ذكية.** يتم اكتشاف الليل تلقائيًا، وتشغيل الأضواء تلقائيًا؛ وفي حالة اكتشاف وجود أشخاص أو مركبات، يتم زيادة سطوع اللدنة
- **التحكم الموحد عبر منصة السحابة.** يتم التحكم الرئيسي باستخدام GSM ويمكن تنفيذ عمليات التصحيح عن بعد بكميات كبيرة
- **مرونة التوسع.** يتم توفير مجموعة متنوعة من الوظائف المخصصة للمستخدمين الذين لديهم متطلبات خاصة للإضاءة

## المبدأ والتنفيذ

**الشيفرة:**

```cpp
#define BUTTONS_address   "channel/widget4_0/cmd/control" //أوامر التشغيل والإيقاف
#define LIGHT_STATUS_address  "channel/widget4_0/data/light"//حالة التشغيل
#define ITENSITY_DATA_address "channel/widget4_0/data/lightsensor"
#define LEDPIN1    D1    //تحديد مدخل التحكم باللمبة
#define LEDPIN2    D2
#define LEDPIN3    D3
#define LEDPIN4    D5
#define CHECKIN1   A0
#define CHECKIN2   D4
```
````

```arduino
int autostate = 2;
int light_state = 2;

void buttons_function(uint8_t *payload, uint32_t len) // دالة الأزرار - التشغيل الآلي والري
{
    uint8_t SwitchKey;
    uint8_t SwitchKey2;
    aJsonClass aJson;
    aJsonObject *root = aJson.parse((char *)payload);

    if (root == NULL)
    {
        aJson.deleteItem(root);
        return;
    }

    aJsonObject *_switch = aJson.getObjectItem(root, "mode");

    if (_switch != NULL)
    {
        SwitchKey = atoi(_switch->valuestring);

        if (SwitchKey)
        {
            SerialUSB.println("التشغيل الآلي قيد التشغيل");
            autostate = 1;
            IntoRobot.publish(LIGHT_STATUS_address, "1");
        }
        else
        {
            SerialUSB.println("التشغيل الآلي متوقف");
            autostate = 0;
            IntoRobot.publish(LIGHT_STATUS_address, "0");
        }
    }

    aJsonObject *_switch2 = aJson.getObjectItem(root, "manual");

    if (_switch2 != NULL)
    {
        SwitchKey2 = atoi(_switch2->valuestring);

        if (SwitchKey2)
        {
            SerialUSB.println("التشغيل اليدوي قيد التشغيل");
            light_state = 1;
            IntoRobot.publish(LIGHT_STATUS_address, "1");
        }
        else
        {
            SerialUSB.println("التشغيل اليدوي متوقف");
            light_state = 0;
            IntoRobot.publish(LIGHT_STATUS_address, "0");
        }
    }
    else
    {
    }
    aJson.deleteItem(root);
}

void lightup()
{
    digitalWrite(LEDPIN1, HIGH); // تشغيل المصابيح
    digitalWrite(LEDPIN2, HIGH); // تشغيل المصابيح
    digitalWrite(LEDPIN3, HIGH); // تشغيل المصابيح
    digitalWrite(LEDPIN4, HIGH); // تشغيل المصابيح
}

void light_half_up()
{
    analogWrite(LEDPIN1, 80); // تشغيل المصابيح بشكل جزئي
    analogWrite(LEDPIN2, 80); // تشغيل المصابيح بشكل جزئي
    analogWrite(LEDPIN3, 80); // تشغيل المصابيح بشكل جزئي
    analogWrite(LEDPIN4, 80); // تشغيل المصابيح بشكل جزئي
}
```

Note: I've translated the code while preserving the original markdown format. Please let me know if you need any further assistance.

````markdown
# ترجمة

```cpp
void lightdown()
{
    digitalWrite(LEDPIN1, LOW);
    digitalWrite(LEDPIN2, LOW);
    digitalWrite(LEDPIN3, LOW);
    digitalWrite(LEDPIN4, LOW);
}

int getlight()
{
    int k = analogRead(CHECKIN1);
    SerialUSB.println(k);
    return k;
}

int get_IR_data()
{
    int b = digitalRead(CHECKIN2);
    SerialUSB.println(b);
    return b;
}

void automode()
{
    if (getlight() >= 400)
    {
        IntoRobot.publish(LIGHT_STATUS_address, "1");
        if (get_IR_data() == 0)
            lightup();
        else
            light_half_up();
    }
    else
    {
        IntoRobot.publish(LIGHT_STATUS_address, "0");
        lightdown();
    }
}

void HUMIDITY_print_function(uint8_t *payload, uint32_t len)
{
}

// IntoRobot.publish(LIGHT_STATUS_address,"1");
// IntoRobot.publish(LIGHT_STATUS_address,"0");
void setup()
{
    pinMode(D4, INPUT);
    SerialUSB.begin(115200);
    SerialUSB.println("hello world");
    pinMode(LEDPIN1, OUTPUT);    // تهيئة
    pinMode(LEDPIN2, OUTPUT);    // تهيئة
    pinMode(LEDPIN3, OUTPUT);    // تهيئة
    pinMode(LEDPIN4, OUTPUT);    // تهيئة
    // الجهاز يستقبل أوامر تشغيل/إيقاف الإضاءة من منصة السحاب
    IntoRobot.subscribe(BUTTONS_address, NULL, buttons_function);
    IntoRobot.subscribe(ITENSITY_DATA_address, NULL, HUMIDITY_print_function);
}

void loop()
{
    int a = map(getlight(), 0, 1024, 100, 0);
    IntoRobot.publish(LIGHT, a);
    SerialUSB.println(getlight());
    if (autostate == 0)
    {
        if (light_state == 1)
            lightup();
        else
            lightdown();
    }
    else if (autostate == 1)
    {
        SerialUSB.println("state=1");
        automode();
    }
    delay(100);
}
```
````

بسبب قلة الوقت المتاح للمسابقة، يتعذر علينا تقديم نموذج مفصل، ونقوم بالطباعة الخشنة والتجميع.

## الأسئلة الشائعة

السؤال: هل هناك خطة لمتابعة المشروع في المستقبل؟
الجواب: ليس لدينا حاليًا خطة لمتابعة المشروع. الفكرة جيدة، لكنها تحتاج إلى التحقق من قيمتها التجارية.

## الختام

لم نفز في هذه المسابقة، ولكن المشاركة فيها ساعدتنا على تطوير مهارات البرمجة والتقديم. كما أتاحت لنا فرصة مبكرة لتجربة العمل الإضافي والنشر. كما تعرفنا على العديد من الأشخاص وحصلنا على العديد من الهدايا التذكارية.

## المراجع والشكر

```

- فريق العمل: لين بي جيه، هوانغ يويه فنغ، زهانغ زي يي
- [منصة إنتو روبوت السحابية](https://www.intorobot.com/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
```
