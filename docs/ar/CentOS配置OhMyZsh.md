```markdown
# تكوين Oh My Zsh على CentOS

## عرض الشيل الحالي

```Shell
echo $SHELL
```

عادة ما سيعيد `bin/bash` تحت معظم الظروف.

## تثبيت Zsh

```shell
yum install -y zsh
```

## تغيير الشيل الافتراضي إلى Zsh

يتعين تشغيل هذا الأمر تحت المستخدم الجذر:

```shell
chsh -s /bin/zsh
```

## تثبيت Git

```shell
yum install -y git
```

## تثبيت Oh My Zsh

### تلقائيًا

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
أو
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

### يدويًا

إذا كان غير ممكن تثبيته بالطرق السابقة (ربما بسبب جدار ناري)، يمكنك تثبيته يدويًا على النحو التالي:

قم بتنزيل الشيفرة المصدرية:

```shell
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

انسخ الإعدادات:

```shell
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

## تغيير مظهر Oh My Zsh

قائمة بجميع المظاهر المتاحة:

```shell
ls ~/.oh-my-zsh/themes
```

قم بتعديل المظهر:

```shell
vim ~/.zshrc
```

قم بتغيير المظهر الافتراضي `ZSH_THEME="robbyrussell"` إلى المظهر الذي تفضله.

## إعادة التشغيل للتفعيل

```shell
reboot
```

## المراجع والشكر

- [centos7 تثبيت Zsh وتكوين oh-my-zsh](https://www.jianshu.com/p/4ce7d511bc13)
- [تثبيت oh my zsh على CentOS](https://www.jianshu.com/p/556ff130fc65)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```

يرجى ملاحظة أنَّ الروابط "> عنوان النص: <https://wiki-power.com/>" و "> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر." لم تتم ترجمتها، وهي تحتاج إلى ترجمة يدوية إذا كانت تشير إلى موارد معينة.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.