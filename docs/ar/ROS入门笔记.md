# ملاحظات مقدمة حول ROS

يستند هذا البرنامج التعليمي إلى ROS2 Foxy و Ubuntu20.04.

## تثبيت بيئة ROS

### تعيين ترميز UTF-8

```shell
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### تعيين مصدر البرنامج

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

### تعيين متغيرات البيئة

```shell
source /opt/ros/foxy/setup.bash
```

### تثبيت أداة الإكمال التلقائي

```shell
sudo apt install python3-argcomplete
```

### اختبار التثبيت الناجح

تشغيل Talker:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_cpp talker
```

فتح نافذة سطر الأوامر الجديدة وتشغيل Listener:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_py listener
```

### إذا كنت ترغب في إلغاء تثبيت ROS

```shell
sudo apt remove ros-foxy-* && sudo apt autoremove
```

ثم تحقق من وجود مجلد ROS في ~/.bashrc أو /opt/ directory.

## تكوين بيئة ROS2

```shell
source /opt/ros/foxy/setup.bash
```

التحقق من الإعدادات بعد الانتهاء:

```shell
printenv | grep -i ROS
```

## محاكي السلحفاة الصغيرة

### تثبيت

```shell
sudo apt update
sudo apt install ros-foxy-turtlesim
```

التحقق من نجاح التثبيت:

```shell
ros2 pkg executables turtlesim
```

### تشغيل محاكي السلحفاة

```shell
ros2 run turtlesim turtlesim_node
```

لجعل السلحفاة الصغيرة تتحرك ، يمكن فتح نافذة سطر الأوامر جديدة وإدخال الأمر:

```shell
ros2 run turtlesim turtle_teleop_key
```

اتبع التعليمات الموجودة في سطر الأوامر.

### تثبيت أداة rqt

```shell
sudo apt update
sudo apt install ~nros-foxy-rqt*
```

### تشغيل أداة rqt

أولاً ، تأكد من تشغيل السلحفاة الصغيرة في الخلفية. أدخل في سطر الأوامر:

```shell
rqt
```

استدعاء أداة rqt ، افتح Plugins> Services> Service Caller بالترتيب ، وانقر فوق زر التحديث ، وستظهر جميع الخدمات.

حدد الخدمة / spawn ، واملأ اسم السلحفاة الصغيرة (مثل `'GuaiGuai'`) والموقع ، ويمكنك إنشاء سلحفاة صغيرة إضافية. إذا كنت ترغب في تغيير لون وشكل مسارها ، فيمكنك تعديل محتوى الخدمة / set_pen.

يمكن التحكم في حركة السلاحف البحرية الجديدة التي تم إنشاؤها باستخدام الأمر التالي (يرجى ملاحظة اسم السلحفاة):

```shell
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=guaiguai/cmd_vel
```

## المراجع والشكر

- [دليل مقدمة في ROS2 - 2. تثبيت ROS2 Foxy على Ubuntu20.04](https://www.guyuehome.com/10226)
- [دليل مقدمة في ROS2 - 3. تكوين بيئة ROS2](https://www.guyuehome.com/10243)
- [دليل مقدمة في ROS2 - 4. استخدام أساسيات محاكي السلاحف البحرية الصغيرة](https://www.guyuehome.com/10386)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.