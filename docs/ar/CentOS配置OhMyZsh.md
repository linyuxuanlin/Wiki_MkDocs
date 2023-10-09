# تكوين Oh My Zsh على CentOS

## عرض الشل الحالي

```Shell
echo $SHELL
```

عادة ما يعود الرد `bin/bash`

## تثبيت zsh

```shell
yum install -y zsh
```

## تغيير الشل الافتراضي إلى zsh

يجب تشغيل هذا الأمر كمستخدم root:

```shell
chsh -s /bin/zsh
```

## تثبيت git

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

إذا لم يكن بإمكانك التثبيت بالطريقة السابقة (ربما بسبب الجدار الناري) ، فيمكنك التثبيت يدويًا عن طريق الطريقة التالية:

تنزيل الشفرة المصدرية:

```shell
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

نسخ التكوين:

```shell
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

## تغيير موضوع Oh My Zsh

عرض جميع الموضوعات:

```shell
ls ~/.oh-my-zsh/themes
```

تغيير الموضوع:

```shell
vim ~/.zshrc
```

قم بتغيير الموضوع الافتراضي `ZSH_THEME="robbyrussell"` إلى الموضوع الذي تفضله.

## إعادة التشغيل للتفعيل

```shell
reboot
```

## المراجع والشكر

- [centos7 安装 zsh 配置 oh-my-zsh](https://www.jianshu.com/p/4ce7d511bc13)
- [CentOs 安装 oh my zsh](https://www.jianshu.com/p/556ff130fc65)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.