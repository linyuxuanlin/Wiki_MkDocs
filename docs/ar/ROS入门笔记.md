# ملاحظات حول بدء التعامل مع ROS

هذا البرنامج التعليمي مستند إلى ROS2 Foxy و Ubuntu 20.04.

## تثبيت بيئة ROS

### تعيين الترميز UTF-8

```shell
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### تعيين مصادر البرامج

```shell
sudo apt update && sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

```shell
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
```

### تثبيت ROS2

```shell
sudo apt update
sudo apt install ros-foxy-desktop
```

### تعيين المتغيرات البيئية

```shell
source /opt/ros/foxy/setup.bash
```

### تثبيت أداة الاكمال التلقائي

```shell
sudo apt install python3-argcomplete
```

### اختبار التثبيت بنجاح

تشغيل الـ Talker:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_cpp talker
```

فتح نافذة سطر الأوامر الجديدة وتشغيل الـ Listener:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_py listener
```

### إلغاء تثبيت ROS إذا لزم الأمر

```shell
sudo apt remove ros-foxy-* && sudo apt autoremove
```

بعد ذلك، تحقق من وجود مجلدات ROS في ملفات `~/.bashrc` و `/opt/`.

## تكوين بيئة ROS2

```shell
source /opt/ros/foxy/setup.bash
```

تحقق من إعداداتك بعد الانتهاء:

```shell
printenv | grep -i ROS
```

## محاكاة سلحفاة صغيرة

### التثبيت

```shell
sudo apt update
sudo apt install ros-foxy-turtlesim
```

تحقق مما إذا كان التثبيت ناجحًا:

```shell
ros2 pkg executables turtlesim
```

### تشغيل محاكاة السلحفاة

```shell
ros2 run turtlesim turtlesim_node
```

لجعل السلحفاة الصغيرة تتحرك، يمكنك فتح نافذة سطر الأوامر جديدة وإدخال الأمر:

```shell
ros2 run turtlesim turtle_teleop_key
```

اتبع التعليمات على سطر الأوامر للتحكم.

### تثبيت أداة rqt

```shell
sudo apt update
sudo apt install ~nros-foxy-rqt*
```

### تشغيل أداة rqt

أولًا، تأكد من تشغيل السلحفاة الصغيرة في الخلفية. ثم، اكتب الأمر التالي في سطر الأوامر:

```shell
rqt
```

قم بتشغيل أداة rqt واذهب إلى `Plugins > Services > Service Caller`. انقر على زر التحديث لعرض جميع الخدمات.

اختر الخدمة `/spawn` واملأ اسم السلحفاة الصغيرة (على سبيل المثال، `'GuaiGuai'`) ومكانها لإنشاء سلحفاة إضافية. إذا كنت ترغب في تغيير لونها أو شكل مسارها، يمكنك تعديل محتوى الخدمة `/set_pen`.

تحكم في حركة السلحفاة المولدة حديثًا باستخدام الأمر التالي (يرجى ملاحظة اسم السلحفاة):

```shell
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=guaiguai/cmd_vel
```

## المراجع والشكر

- [دورة تعليم ROS2 للمبتدئين - الجزء 2: تثبيت ROS2 Foxy على Ubuntu 20.04](https://www.guyuehome.com/10226)
- [دورة تعليم ROS2 للمبتدئين - الجزء 3: تكوين بيئة ROS2](https://www.guyuehome.com/10243)
- [دورة تعليم ROS2 للمبتدئين - الجزء 4: الاستخدام الأساسي لمحاكاة السلحفاة الصغيرة](https://www.guyuehome.com/10386)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.