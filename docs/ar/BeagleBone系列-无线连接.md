# سلسلة BeagleBone - الاتصال اللاسلكي

## الاختلافات بين مختلف إصدارات BeagleBone

| BeagleBone® Black | Seeed Studio BeagleBone® Green | Seeed Studio BeagleBone® Green Wireless       | Seeed Studio BeagleBone® Green Gateway                                 |
| ----------------- | ------------------------------ | --------------------------------------------- | ---------------------------------------------------------------------- |
| 60.00 دولار أمريكي | 44.00 دولار أمريكي | 52.90 دولار أمريكي | 78.90 دولار أمريكي |
| 1 x منفذ USB      | 1 x منفذ USB                   | 4 x منافذ USB2.0                              | 2 x منافذ USB2.0                                                        |
| إيثرنت          | إيثرنت 10/100 ميجابت في الثانية  | واي فاي 802.11b/g/n بتردد 2.4 جيجاهرتز وبلوتوث 4.1 منخفض الطاقة | إيثرنت 10/100 ميجابت في الثانية وواي فاي 802.11b/g/n بتردد 2.4 جيجاهرتز وبلوتوث 4.1 منخفض الطاقة |
| منفذ HDMI         | 2 x منفذ Grove Connectors           | 2 x منفذ Grove Connectors                          | 2 x منفذ Grove Connectors                                                   |

## BeagleBone Green Gateway

### الاتصال بالواي فاي

```shell
debian@beaglebone:~$ connmanctl
connmanctl> scan wifi
اكتمل البحث عن شبكات الواي فاي
connmanctl> services
    se.101               wifi_1862e41aec0d_73652e313031_managed_psk
    STU-EE               wifi_1862e41aec0d_5354552d4545_managed_psk
connmanctl> agent on
الوكيل مسجل
connmanctl> connect wifi_1862e41aec0d_5354552d4545_managed_psk
طلب الوكيل الإدخال wifi_1862e41aec0d_5354552d4545_managed_psk
  كلمة المرور = [النوع=psk، المتطلب=إلزامي، بدائل=[WPS]]
  WPS = [النوع=wpspin، المتطلب=بديل]
كلمة المرور؟ أدخل كلمة المرور
تم الاتصال بنجاح بشبكة wifi_1862e41aec0d_5354552d4545_managed_psk
connmanctl> quit
```

### الاتصال بالبلوتوث

```markdown
```shell
sudo apt install bluez
```

إذا كان هناك خطأ، قم بتحديث النظام أولاً:

```shell
sudo apt update
```

الاتصال بأجهزة البلوتوث المجاورة:

```shell
bb-wl18xx-bluetooth
bluetoothctl
scan on
```

قم بإقامة اتصال مقترن مع الجهاز (السلسلة التي تأتي بعد ذلك هي عنوان MAC للجهاز الذي ترغب في إقامة اتصال مقترن معه):

```shell
pair A4:xx:xx:xx:xx:30
trust A4:xx:xx:xx:xx:30
connect A4:xx:xx:xx:xx:30
```

يمكنك استخدام الأمر `quit` للخروج من واجهة سطر الأوامر للبلوتوث.

## المراجعة والشكر

- [Seeed Studio BeagleBone® Green Gateway](https://wiki.seeedstudio.com/BeagleBone-Green-Gateway/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```


> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.