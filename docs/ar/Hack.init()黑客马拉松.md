# هاك.اينيت( ) هاكاثون

- Wight: نظام إضاءة لاسلكي قائم على منصة سحابية.

![](https://img.wiki-power.com/d/wiki-media/img/wight.jpg)

Repository المستودع : [**linyuxuanlin / Wight**](https://github.com/linyuxuanlin/Wight)

## الخلفية

تم إنشاء هذا المشروع في ماراثون Hack.init () لعام 2017. بعد أكثر من 20 ساعة من البرمجة والنمذجة وتصحيح الأخطاء المتنوعة والانتظار للطباعة والعرض والتقديم ، بدأ المشروع يظهر بشكل ما.

يستخدم هذا المشروع بشكل رئيسي في نظام إضاءة الشوارع في المناطق النائية في الريف. النموذج قليلاً مجرد تمثيل لعمود إضاءة الشوارع.

## نقاط الابتكار في المشروع

- **تزويد الطاقة بالطاقة الشمسية.** الاكتفاء الذاتي (بعد الاطلاع على المعلومات المفصلة ، يكفي طاقة الشمس لإضاءة LED)
- **التخلص من الأسلاك.** توفير الراحة للمناطق الجبلية النائية التي لا يمكن تمديد الأسلاك فيها
- **خوارزمية ذكية.** عند الكشف عن الليل ، يتم تشغيل الإضاءة تلقائيًا ؛ عند الكشف عن مرور الأشخاص أو المركبات ، يتم زيادة سطوع LED
- **التحكم الموحد في المنصة السحابية.** يتم استخدام المراقب الرئيسي GSM ، ويمكن التصحيح عن بعد بالجملة
- **قابلية التوسع.** توفير مجموعة متنوعة من الوظائف المخصصة للمستخدمين الذين لديهم متطلبات إضاءة مخصصة

## المبدأ والتنفيذ

**الشفرة:**

```cpp
#define BUTTONS_address   "channel/widget4_0/cmd/control" //أمر التشغيل / الإيقاف
#define LIGHT_STATUS_address  "channel/widget4_0/data/light"//حالة التشغيل / الإيقاف
#define ITENSITY_DATA_address "channel/widget4_0/data/lightsensor"
#define LEDPIN1    D1    //تعريف دبوس تحكم المصباح
#define LEDPIN2    D2
#define LEDPIN3    D3
#define LEDPIN4    D5
#define CHECKIN1   A0
#define CHECKIN2   D4
```

int autostate = 2;
int light_state = 2;
void buttons_function(uint8_t *payload, uint32_t len)//الأزرار الأوتوماتيكية والري
{
uint8_t SwitchKey;
uint8_t SwitchKey2;
aJsonClass aJson;
aJsonObject *root = aJson.parse((char _)payload);
if(root == NULL)
{
aJson.deleteItem(root);
return;
}
aJsonObject _\_switch = aJson.getObjectItem(root, "mode");
if(\_switch != NULL)
{
SwitchKey = atoi(\_switch->valuestring);
if(SwitchKey)
{
SerialUSB.println("auto on");
autostate=1;
IntoRobot.publish(LIGHT_STATUS_address,"1");
}
else
{
SerialUSB.println("auto off");
autostate=0;
IntoRobot.publish(LIGHT_STATUS_address,"0");
}
}
aJsonObject \*\_switch2 = aJson.getObjectItem(root, "manual");
if(\_switch2 != NULL)
{
SwitchKey2 = atoi(\_switch2->valuestring);
if(SwitchKey2)
{
SerialUSB.println("manual on");
light_state=1;
IntoRobot.publish(LIGHT_STATUS_address,"1");
}
else
{
SerialUSB.println("manual off");
light_state=0;
IntoRobot.publish(LIGHT_STATUS_address,"0");
}
}
else
{
}
aJson.deleteItem(root);
}
void lightup()
{
digitalWrite(LEDPIN1, HIGH); // تشغيل المصباح
digitalWrite(LEDPIN2, HIGH); // تشغيل المصباح
digitalWrite(LEDPIN3, HIGH); // تشغيل المصباح
digitalWrite(LEDPIN4, HIGH); // تشغيل المصباح

}
void light_half_up()
{
analogWrite(LEDPIN1, 80); // تشغيل المصباح
analogWrite(LEDPIN2, 80); // تشغيل المصباح
analogWrite(LEDPIN3, 80); // تشغيل المصباح
analogWrite(LEDPIN4, 80); // تشغيل المصباح

}
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
if(getlight()>=400)
{
IntoRobot.publish(LIGHT_STATUS_address,"1");
if (get_IR_data()==0)
lightup();
else
light_half_up();
}
else
{
IntoRobot.publish(LIGHT_STATUS_address,"0");
lightdown();
}
}

void HUMIDITY_print_function(uint8_t \*payload, uint32_t len)
{

}

// IntoRobot.publish(LIGHT_STATUS_address,"1");
// IntoRobot.publish(LIGHT_STATUS_address,"0");
void setup()
{
pinMode(D4,INPUT);
SerialUSB.begin(115200);
SerialUSB.println("hello world");
pinMode(LEDPIN1, OUTPUT); //initialize
pinMode(LEDPIN2, OUTPUT); //initialize
pinMode(LEDPIN3, OUTPUT); //initialize
pinMode(LEDPIN4, OUTPUT); //initialize
//Device receives light switch command from cloud platform
IntoRobot.subscribe(BUTTONS_address,NULL,buttons_function);
IntoRobot.subscribe(ITENSITY_DATA_address,NULL,HUMIDITY_print_function);
}
void loop()
{
int a =map(getlight() ,0,1024,100,0);
IntoRobot.publish(LIGHT,a);
SerialUSB.println(getlight());
if(autostate==0)
{
if(light_state ==1)
lightup();
else
lightdown();
}
else if (autostate==1)
{
SerialUSB.println("state=1");
automode();
}
delay(100);
}

```

بسبب وقت المسابقة المحدود، لم نتمكن من رسم نموذج مفصل، ولكن تم طباعته وتجميعه.

## الأسئلة الشائعة

س: هل سيتم متابعة المشروع في المستقبل؟
ج: ليس لدينا خطط حاليًا للمتابعة. النقطة المبتكرة جيدة، ولكن ما إذا كان لها قيمة تجارية، فهذا يحتاج إلى التحقق.

## الخلاصة

لم نفز في المسابقة هذه المرة. ومع ذلك، تدربنا على البرمجة والتقديم، وأتاحت لنا الفرصة لتجربة العمل الإضافي والإطلاع على الكثير من الناس والحصول على العديد من الهدايا التذكارية.

## المراجع والشكر



- فريق العمل: لين بي جي، هوانغ يوي فنغ، تشانغ زي يي
- [منصة إنتو روبوت السحابية](https://www.intorobot.com/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
```
