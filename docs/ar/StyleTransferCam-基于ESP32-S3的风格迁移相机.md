# StyleTransferCam - كاميرا نقل الأسلوب على أساس ESP32-S3

![](https://media.wiki-power.com/img/202308152238959.png)

عندما يتقاطع الفن والتكنولوجيا ، ينكشف عالم جديد أمامنا ، وهذا هو عرض رائع بصريًا ، وهو أيضًا استكشاف لا حدود له. تعد StyleTransferCam كاميرا نقل الأسلوب على أساس ESP32-S3. إنها تستخدم تقنية تعلم الآلة المعروفة باسم "نقل الأسلوب" ، حيث عند الضغط على زر اللوحة ، ستلتقط المشهد الحالي وتمزجه مع صورة نموذج أسلوب محددة مسبقًا (مثل "السماء النجمية" لفان جوخ) لتوليد عمل فني فريد.

تتكون StyleTransferCam تقريبًا من العمليات التالية:

1. الضغط على زر اللوحة - التقاط الصورة - تحميلها على الخادم الخلفي (يمكن أن يكون جهاز الكمبيوتر أو الهاتف القديم).
2. تشغيل برنامج Python لنقل الأسلوب تلقائيًا ، ومعالجة الصورة ، وإخراج الصورة المنمقة بأسلوب.
3. إذا كان لدى ESP32-S3 شاشة TFT مرفقة ، فيمكن أيضًا إرجاع الشاشة للعرض.

![](https://media.wiki-power.com/img/202308152244791.png)

## اختبار زر اللوحة والمصباح الأمامي

أولاً ، هناك برنامج Arduino بسيط يستخدم لاختبار ما إذا كان بإمكان استخدام زر اللوحة والمصباح الأمامي بشكل صحيح. يتم تعيين المقاطعة الأجهزة في البرنامج لالتقاط حدث الضغط على الزر ، وتشغيل المصباح الأمامي لمدة نصف ثانية ثم إيقافه تلقائيًا.

```cpp title="Onboard-Key-ctrl-LED_interrupt.ino"
#define ONBOARD_KEY 47  // زر اللوحة
#define ONBOARD_LED 21  // المصباح الأمامي

volatile bool buttonPressed = false;  // علامة توقف الانقطاع عند حدوث الضغط على الزر

void setup() {
  pinMode(ONBOARD_LED, OUTPUT);
  pinMode(ONBOARD_KEY, INPUT);
  Serial.begin(115200);
  attachInterrupt(digitalPinToInterrupt(ONBOARD_KEY), buttonInterrupt, FALLING);
}

void loop() {
  if (buttonPressed) {
    digitalWrite(ONBOARD_LED, HIGH);
    delay(500);
    digitalWrite(ONBOARD_LED, LOW);
    Serial.println("buttonPressed");
    buttonPressed = false;  // إعادة تعيين علامة الانقطاع
  }
}

void buttonInterrupt() {
  buttonPressed = true;  // تعيين علامة الانقطاع عند حدوث الانخفاض
}
```

## التقاط الصورة باستخدام الزر وتحميلها

بعد ذلك ، سنقوم بكتابة برنامج Arduino يستخدم زر اللوحة للتحكم في تصوير ESP32-S3 للتقاط صورة واحدة وتحميلها إلى موقع الشبكة المحدد. يتم تعيين موقع الشبكة هذا في الكود `serverName = "http://192.168.31.2:9000/upload"` ، ويجب تعديله ليتوافق مع عنوان خادم الخلفية الخاص بك. نحن نستخدم خدمة تحميل ملف Python في الخلفية (سيتم شرحها في الخطوات التالية) ، وهنا يجب تعديلها لتشغيل الخدمة على عنوان IP للجهاز الذي يقوم بتشغيل هذه الخدمة. (`9000` و `/upload` تم تعيينهما في برنامج `receive-photo.py` أدناه)

```cpp title="Capture-and-Upload.ino"
#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>

// عنوان الخادم المستخدم لتحميل الصور
const char *serverName = "http://192.168.31.2:9000/upload";
```

//
// تحذير!!! يتطلب وجود ذاكرة PSRAM IC للحصول على دقة UXGA وجودة JPEG عالية
// تأكد من تحديد وحدة ESP32 Wrover Module أو لوحة أخرى تحتوي على PSRAM
// سيتم نقل الصور الجزئية إذا تجاوزت الصورة حجم الذاكرة المؤقتة
//
// يجب عليك تحديد نظام التقسيم من قائمة اللوحة الذي يحتوي على مساحة تطبيق بحجم 3 ميجابايت على الأقل.
// تم تعطيل التعرف على الوجه لـ ESP32 و ESP32-S2 ، لأنه يستغرق من 15
// ثانية لمعالجة إطار واحد. تم تمكين كشف الوجه إذا تم تمكين PSRAM أيضًا

// ===================
// حدد نموذج الكاميرا
// ===================
#define PWDN_GPIO_NUM -1
#define RESET_GPIO_NUM -1
#define XCLK_GPIO_NUM 45
#define SIOD_GPIO_NUM 1
#define SIOC_GPIO_NUM 2

#define Y9_GPIO_NUM 48
#define Y8_GPIO_NUM 46
#define Y7_GPIO_NUM 8
#define Y6_GPIO_NUM 7
#define Y5_GPIO_NUM 4
#define Y4_GPIO_NUM 41
#define Y3_GPIO_NUM 40
#define Y2_GPIO_NUM 39
#define VSYNC_GPIO_NUM 6
#define HREF_GPIO_NUM 42
#define PCLK_GPIO_NUM 5

#define ONBOARD_KEY 47 // 板载按钮
#define ONBOARD_LED 21 // 板载 LED

volatile bool buttonPressed = false; // 按钮下降沿中断标志位

#include "DFRobot_AXP313A.h"

DFRobot_AXP313A axp;

// ===========================
// أدخل بيانات اعتماد WiFi الخاصة بك
// ===========================
const char *ssid = "اسم*شبكة*واي_فاي";
const char *password = "**\*\*\*\***";

void startCameraServer();

```cpp
void setup()
{
  pinMode(ONBOARD_KEY, INPUT);
  pinMode(ONBOARD_LED, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(ONBOARD_KEY), buttonInterrupt, FALLING);
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();
  while (axp.begin() != 0)
  {
    Serial.println("init error");
    delay(1000);
  }
  axp.enableCameraPower(axp.eOV2640); // Set camera power
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.frame_size = FRAMESIZE_UXGA;   // Photo resolution. Default is FRAMESIZE_UXGA
  config.pixel_format = PIXFORMAT_JPEG; // for streaming
  // config.pixel_format = PIXFORMAT_RGB565; // for face detection/recognition
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 0; // 63; // Photo quality. Default is 12
  config.fb_count = 1;

  /*
  FRAMESIZE_QVGA (320 x 240)
  FRAMESIZE_CIF (352 x 288)
  FRAMESIZE_VGA (640 x 480)
  FRAMESIZE_SVGA (800 x 600)
  FRAMESIZE_XGA (1024 x 768)
  FRAMESIZE_SXGA (1280 x 1024)
  FRAMESIZE_UXGA (1600 x 1200)
  */
}
```

// إذا تم العثور على رقاقة PSRAM ، قم بتهيئتها بدقة UXGA وجودة JPEG أعلى
// لحجم الذاكرة المؤقتة المخصصة للإطار الأكبر.
إذا (config.pixel_format == PIXFORMAT_JPEG)
{
إذا (psramFound())
{
config.jpeg_quality = 0; // 63; // جودة الصورة. القيمة الافتراضية هنا هي 10
config.fb_count = 2;
config.grab_mode = CAMERA_GRAB_LATEST;
}
آخر
{
// قم بتحديد حجم الإطار عندما لا يتوفر PSRAM
config.frame_size = FRAMESIZE_UXGA; // دقة الصورة. القيمة الافتراضية هنا هي FRAMESIZE_SVGA
config.fb_location = CAMERA_FB_IN_DRAM;
}
}
آخر
{
// أفضل خيار للكشف عن الوجه / التعرف عليه
config.frame_size = FRAMESIZE_UXGA; // FRAMESIZE_240X240;
#if CONFIG_IDF_TARGET_ESP32S3
config.fb_count = 2;
#endif
}

إذا تم تعريف (CAMERA_MODEL_ESP_EYE)
{
pinMode(13, INPUT_PULLUP);
pinMode(14, INPUT_PULLUP);
}

// تهيئة الكاميرا
esp_err_t err = esp_camera_init(&config);
إذا (err != ESP_OK)
{
Serial.printf("فشل تهيئة الكاميرا بسبب خطأ 0x%x", err);
عودة;
}

sensor_t \*s = esp_camera_sensor_get();
// الاستشعارات الأولية مقلوبة عمودياً والألوان مشبعة قليلاً
إذا (s->id.PID == OV3660_PID)
{
s->set_vflip(s, 1); // قم بعكسها
s->set_brightness(s, 1); // زيادة السطوع قليلاً
s->set_saturation(s, -2); // خفض التشبع
}
// قم بتقليل حجم الإطار لزيادة معدل الإطار الأولي
إذا (config.pixel_format == PIXFORMAT_JPEG)
{
s->set_framesize(s, FRAMESIZE_QVGA);
}

إذا تم تعريف (CAMERA_MODEL_M5STACK_WIDE) || تم تعريف (CAMERA_MODEL_M5STACK_ESP32CAM)
{
s->set_vflip(s, 1);
s->set_hmirror(s, 1);
}

إذا تم تعريف (CAMERA_MODEL_ESP32S3_EYE)
{
s->set_vflip(s, 1);
}

WiFi.begin(ssid, password);
WiFi.setSleep(false);

```cpp
while (WiFi.status() != WL_CONNECTED)
{
  delay(500);
  Serial.print(".");
}
Serial.println("");
Serial.println("WiFi connected");

startCameraServer();

Serial.print("Camera Ready! Use 'http://");
Serial.print(WiFi.localIP());
Serial.println("' to connect");
digitalWrite(ONBOARD_LED, LOW);
}

void loop()
{
  // Do nothing. Everything is done in another task by the web server
  // delay(10000);

  // Logic after button press
  if (buttonPressed)
  {
    digitalWrite(ONBOARD_LED, HIGH);
    delay(300);
    digitalWrite(ONBOARD_LED, LOW);

    // Take a photo
    camera_fb_t *fb = esp_camera_fb_get();
    if (!fb)
    {
      Serial.println("Failed to get camera frame buffer");
      return;
    }

    // Create an HTTP client
    HTTPClient http;

    // Upload the photo to the server
    http.begin(serverName);
    http.addHeader("Content-Type", "image/jpeg");
    int httpResponseCode = http.POST(fb->buf, fb->len);
    if (httpResponseCode > 0)
    {
      Serial.printf("Photo uploaded successfully, server response code: %d\n", httpResponseCode);

      // Blink again to indicate successful upload
      digitalWrite(ONBOARD_LED, HIGH);
      delay(300);
      digitalWrite(ONBOARD_LED, LOW);
    }
    else
    {
      Serial.printf("Failed to upload photo, error code: %s\n", http.errorToString(httpResponseCode).c_str());
    }
    http.end();

    // Release the frame buffer
    esp_camera_fb_return(fb);

    // delay(1000); // Wait for 1 second before taking another photo and uploading

    buttonPressed = false; // Reset interrupt flag
  }
}

void buttonInterrupt()
{
  buttonPressed = true; // Set falling edge interrupt flag
}
```

## Receiving Photo Uploads

Here we use the Python flask library to build an HTTP server that receives photo uploads.

```python title="receive-photo.py"
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        image = request.data
```

        # حفظ الصورة في المجلد المحدد
        with open('base.png', 'wb') as f:
            f.write(image)
        print("تم حفظ الصورة، جاري التقديم...")
        # تشغيل برنامج نقل الأنماط باستخدام البرنامج النصي بلغة Python
        subprocess.run(['python', './style_transfer.py'])

        return "تم رفع الصورة بنجاح", 200
    except Exception as e:
        print("فشل رفع الصورة:", str(e))
        return "فشل رفع الصورة", 500

if **name** == '**main**':
app.run(host='0.0.0.0', port=9000)

````

لا تقم بتشغيل البرنامج على الفور، `style_transfer.py` هو برنامج نقل الأنماط وسيتم عرضه في الخطوة التالية. منطق هذا البرنامج هو أنه إذا تم استلام الصورة بنجاح من ESP32-S3 ، فسيتم تشغيل البرنامج النصي لنقل الأنماط تلقائيًا باستخدام `subprocess`.

يرجى ملاحظة أنه إذا حدث خطأ في البرنامج وتظهر رسالة تشغيل المنفذ ، يمكنك محاولة تغيير القيمة `port=9000`.

## برنامج نقل الأنماط

في نفس المجلد `receive-photo.py` ، سنستخدم TensorFlow لكتابة برنامج Python لنقل الأنماط. أولاً ، قم بتثبيت التبعيات المطلوبة للبرنامج (بسبب بيئة الشبكة المحلية في الصين ، من الصعب تنزيل TensorFlow ، لذا يلزم الكثير من الصبر) ، ثم قم بتحضير صورة للنقل الأنماط في نفس المجلد واسمها `base.png` ؛ وصورة مرجعية للنمط ، واسمها `style_reference.png` ، يمكن أن تكون لوحة فنية مثل "السماء الليلية" لفان جوخ:

![](https://media.wiki-power.com/img/202308152239917.png)

ثم ، قم بكتابة برنامج نقل الأنماط:

```python title="style_transfer.py"
from IPython.display import Image, display
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import vgg19

base_image_path = "./base.png"  # مسار الصورة المراد نقل الأنماط عليها
style_reference_image_path = "./style_reference.png"  # مسار صورة النمط المرجعي

result_prefix = "img_generated"

# تعيين أوزان الخسارة لكل جزء
total_variation_weight = 1e-6
style_weight = 1e-6
content_weight = 2.5e-8

# حجم الصورة المولدة
width, height = keras.preprocessing.image.load_img(base_image_path).size
img_nrows = 400
img_ncols = int(width * img_nrows / height)

# استعراض الصورة الأساسية وصورة النمط المرجعي باستخدام الأمر التالي

display(Image(base_image_path))
display(Image(style_reference_image_path))

# معالجة الصورة
````

```python
def preprocess_image(image_path):
    # استخدام دالة مكتبة Keras لفتح الصورة وتعديل حجمها وتنسيقها كتنسيق تنسيق الأشكال المناسبة
    img = keras.preprocessing.image.load_img(
        image_path, target_size=(img_nrows, img_ncols)
    )
    img = keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = vgg19.preprocess_input(img)
    return tf.convert_to_tensor(img)


def deprocess_image(x):
    # استخدام الدالة مرة أخرى لتحويل التنسيق إلى صورة صالحة
    x = x.reshape((img_nrows, img_ncols, 3))
    # إزالة المركز الصفري عن طريق متوسط البكسل
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    # 'BGR'->'RGB'
    x = x[:, :, ::-1]
    x = np.clip(x, 0, 255).astype("uint8")
    return x


# مصفوفة جرام لتنسيق الصورة (ضرب مصفوفة الميزات وتحويلها إلى ترانسبوز)

def gram_matrix(x):
    x = tf.transpose(x, (2, 0, 1))
    features = tf.reshape(x, (tf.shape(x)[0], -1))
    gram = tf.matmul(features, tf.transpose(features))
    return gram

# "خسارة الأسلوب" تهدف إلى الحفاظ على أسلوب الصورة المرجعية في الصورة المولدة.
# يستند إلى مصفوفة جرام (استخراج الأسلوب) من صورة الأسلوب المرجعي
# وخرائط الميزات من الصورة المولدة منها


def style_loss(style, combination):
    S = gram_matrix(style)
    C = gram_matrix(combination)
    channels = 3
    size = img_nrows * img_ncols
    return tf.reduce_sum(tf.square(S - C)) / (4.0 * (channels ** 2) * (size ** 2))

# تصميم وظيفة الخسارة المساعدة للحفاظ على المحتوى الأساسي للصورة في الصورة المولدة


def content_loss(base, combination):
    return tf.reduce_sum(tf.square(combination - base))

# الدالة الثالثة للخسارة هي خسارة التباين الكلي
# تم تصميم هذه الوظيفة للحفاظ على التماسك المحلي للصورة المولدة.


def total_variation_loss(x):
    a = tf.square(
        x[:, : img_nrows - 1, : img_ncols - 1, :] - x[:, 1:, : img_ncols - 1, :]
    )
    b = tf.square(
        x[:, : img_nrows - 1, : img_ncols - 1, :] - x[:, : img_nrows - 1, 1:, :]
    )
    return tf.reduce_sum(tf.pow(a + b, 1.25))

# بعد ذلك ، دعنا ننشئ نموذج استخراج الميزات ، والذي يسترد الأنشطة المتوسطة لـ VGG19 (بناءً على الاسم).

# استبدل بمسار الوزن الذي تم تنزيله محليًا
weights_path = "./dependencies/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5"
```

# إنشاء نموذج VGG19 يحمل وزنًا مدربًا مسبقًا لـ ImageNet

model = vgg19.VGG19(weights=weights_path, include_top=False)

# الحصول على الإخراج الرمزي لكل طبقة "مهمة" (نحدد لها اسمًا فريدًا).

outputs_dict = dict([(layer.name, layer.output) for layer in model.layers])

# إنشاء نموذج يعيد قيم التنشيط لكل طبقة في VGG19 (كقاموس).

feature_extractor = keras.Model(inputs=model.inputs, outputs=outputs_dict)

# وأخيرًا، هذا هو الكود الذي يحسب خسارة نقل الأنماط.

# قائمة الطبقات المستخدمة لفقدان الأنماط.

style_layer_names = [
"block1_conv1",
"block2_conv1",
"block3_conv1",
"block4_conv1",
"block5_conv1",
]

# الطبقة المستخدمة لفقدان المحتوى.

content_layer_name = "block5_conv2"

def compute_loss(combination_image, base_image, style_reference_image):
input_tensor = tf.concat(
[base_image, style_reference_image, combination_image], axis=0
)
features = feature_extractor(input_tensor)

    # تهيئة الخسارة
    loss = tf.zeros(shape=())

    # إضافة فقدان المحتوى
    layer_features = features[content_layer_name]
    base_image_features = layer_features[0, :, :, :]
    combination_features = layer_features[2, :, :, :]
    loss = loss + content_weight * content_loss(
        base_image_features, combination_features
    )
    # إضافة فقدان الأنماط
    for layer_name in style_layer_names:
        layer_features = features[layer_name]
        style_reference_features = layer_features[1, :, :, :]
        combination_features = layer_features[2, :, :, :]
        sl = style_loss(style_reference_features, combination_features)
        loss += (style_weight / len(style_layer_names)) * sl

    # إضافة فقدان التغير الكلي
    loss += total_variation_weight * total_variation_loss(combination_image)
    return loss

# إضافة مزيد من الأداء إلى حساب الخسارة وحساب التدرج عن طريق إضافة الديكور tf.function، مما يجعله يعمل بشكل أسرع أثناء الترجمة

```python
@tf.function
def compute_loss_and_grads(combination_image, base_image, style_reference_image):
    with tf.GradientTape() as tape:
        loss = compute_loss(combination_image, base_image,
                            style_reference_image)
    grads = tape.gradient(loss, combination_image)
    return loss, grads

# تنفيذ خطوات الانحدار التدرجي بالدُفعات للحد الأقصى للخسارة وحفظ الصورة المُولَدة كل 100 تكرار.
# يتم خفض معدل التعلم بنسبة 0.96 كل 100 خطوة.

optimizer = keras.optimizers.SGD(
    keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate=100.0, decay_steps=100, decay_rate=0.96
    )
)

base_image = preprocess_image(base_image_path)
style_reference_image = preprocess_image(style_reference_image_path)
combination_image = tf.Variable(preprocess_image(base_image_path))

iterations = 4000
for i in range(1, iterations + 1):
    loss, grads = compute_loss_and_grads(
        combination_image, base_image, style_reference_image
    )
    optimizer.apply_gradients([(grads, combination_image)])
    if i % 100 == 0:
        print("تكرار %d: الخسارة=%.2f" % (i, loss))
        img = deprocess_image(combination_image.numpy())
        fname = result_prefix + "_at_iteration_%d.png" % i
        keras.preprocessing.image.save_img(fname, img)

# بعد 4000 تكرار، يتم إخراج النتيجة:
display(Image(result_prefix + "_at_iteration_4000.png"))
```

الآن يمكنك تشغيل هذا البرنامج بمفرده، إذا لم يكن هناك أي أخطاء في البرنامج، بعد فترة قصيرة (الوقت المحدد يعتمد على أداء جهاز الكمبيوتر الخاص بك)، يمكنك العثور على الصورة بعد تطبيق تحويل الأنماط في الدليل الحالي.

إذا كان البرنامج يعمل بشكل صحيح، يمكنك تشغيل `receive-photo.py` مباشرة لاستلام الصور من ESP32-S3 وتطبيق تحويل الأنماط تلقائيًا.

![](https://media.wiki-power.com/img/202308152246623.png)

## المراجع والشكر

- [تنفيذ تحويل الأنماط باستخدام TensorFlow](https://zhuanlan.zhihu.com/p/349072196)
- [تحويل الأنماط العصبية](https://www.tensorflow.org/tutorials/generative/style_transfer?hl=zh-cn)
- [استخدام الكاميرا](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12)

```

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
```
