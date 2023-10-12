# StyleTransferCam - كاميرا نقل الأسلوب على أساس ESP32-S3

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308152238959.png)

عندما يتقاطع الفن والتكنولوجيا ، ينتشر عالم جديد أمامنا ، وهذا هو عرض رائع للغاية بصريًا ، وهو أيضًا استكشاف لا حدود له. StyleTransferCam هو كاميرا نقل الأسلوب على أساس ESP32-S3. إنه يستخدم تقنية تعلم الآلة المسماة "نقل الأسلوب" ، وعند الضغط على زر اللوحة ، يلتقط المشهد الحالي ويخلطه مع صورة نموذجية محددة مسبقًا (يمكن أن يكون "السماء" لفان جوخ) لإنشاء عمل فني فريد.

يتكون StyleTransferCam تقريبًا من العمليات التالية:

1. الضغط على زر اللوحة - التقاط صورة - تحميلها على الخادم الخلفي (يمكن أن يكون PC أو هاتف قديم).
2. تشغيل برنامج Python لنقل الأسلوب تلقائيًا ، ومعالجة الصورة وإخراجها بأسلوب الأسلوب.
3. إذا كان ESP32-S3 يحتوي على شاشة TFT مرفقة ، فيمكن إعادة الشاشة للعرض.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308152244791.png)

## اختبار زر اللوحة و LED

أولاً ، برنامج Arduino بسيط لاختبار إذا كان بإمكان زر اللوحة و LED استخدامهما بشكل صحيح. يتم تعيين المقاطعة الأجهزة في البرنامج لالتقاط حدث الضغط على الزر وإضاءة LED لمدة نصف ثانية قبل الإطفاء تلقائيًا.

```cpp title="Onboard-Key-ctrl-LED_interrupt.ino"
#define ONBOARD_KEY 47  // زر اللوحة
#define ONBOARD_LED 21  // LED اللوحة

volatile bool buttonPressed = false;  // علامة تبويب انخفاض المقاطعة

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
    buttonPressed = false;  // إعادة تعيين علامة المقاطعة
  }
}

void buttonInterrupt() {
  buttonPressed = true;  // تعيين علامة انخفاض المقاطعة
}
```

## التقاط الصورة باستخدام الزر وتحميلها

ثم ، نكتب برنامج Arduino لاستخدام زر اللوحة للتحكم في ESP32-S3 لالتقاط صورة واحدة وتحميلها إلى موقع الشبكة المحدد. يتم تعيين هذا الموقع في الكود `serverName = "http://192.168.31.2:9000/upload"` ، ويجب تعديله على عنوان خادم الخلفية الخاص بك. كنا نستخدم خدمة تحميل ملف Python الخلفية (وسوف نشرح هذا في الخطوات التالية) ، ويجب تعديلها على عنوان IP لجهاز تشغيل هذه الخدمة. (`9000` و `/upload` تم تعيينهما في برنامج `receive-photo.py` في الخطوات التالية)

```cpp title="Capture-and-Upload.ino"
#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>

// عنوان الخادم المستخدم لتحميل الصورة
const char *serverName = "http://192.168.31.2:9000/upload";

//
// تحذير!!! يتطلب IC PSRAM لدقة UXGA وجودة JPEG عالية
// تأكد من تحديد وحدة ESP32 Wrover Module أو لوحة أخرى تحتوي على PSRAM
// سيتم نقل الصور الجزئية إذا تجاوز حجم الصورة حجم الذاكرة المؤقتة
//
// يجب عليك تحديد نظام التقسيم من قائمة اللوحة الذي يحتوي على مساحة تطبيقية بحجم 3 ميجابايت على الأقل.
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

#define ONBOARD_KEY 47 // زر المجلس
#define ONBOARD_LED 21 // LED المجلس

volatile bool buttonPressed = false; // علامة انقطاع الزر الانخفاضي

#include "DFRobot_AXP313A.h"

DFRobot_AXP313A axp;

// ===========================
// أدخل بيانات اعتماد WiFi الخاصة بك
// ===========================
const char *ssid = "WiFi_SSID";
const char *password = "********";

void startCameraServer();

لا يوجد ترجمة لهذه المقالة حيث أنها تحتوي على رموز برمجية ولغة برمجة.

إذا كانت وحدة PSRAM موجودة، فقم بتهيئتها بدقة UXGA وجودة JPEG أعلى للحصول على حجم إطار مخصص أكبر.

إذا كان تنسيق البكسل هو PIXFORMAT_JPEG، فإنه إذا كان هناك وحدة PSRAM، فإن جودة JPEG تكون 0، وعدد إطارات الفيديو المخصصة هو 2، وطريقة الالتقاط هي CAMERA_GRAB_LATEST. وإذا لم يكن هناك وحدة PSRAM، فإن حجم الإطار يكون محدودًا عند FRAMESIZE_UXGA، وموقع إطار الفيديو المخصص هو CAMERA_FB_IN_DRAM.

وإذا كان تنسيق البكسل ليس PIXFORMAT_JPEG، فإن أفضل خيار للكشف عن الوجه / التعرف عليه هو FRAMESIZE_UXGA.

إذا كان نموذج الكاميرا هو ESP_EYE، فقم بتعيين دبوس 13 و 14 على INPUT_PULLUP.

تهيئة الكاميرا.

إذا فشلت عملية تهيئة الكاميرا، فإنه يتم عرض رسالة خطأ.

يتم الحصول على مستشعر الكاميرا ويتم عكسه رأسيًا وتشبع الألوان قليلاً.

إذا كان تنسيق البكسل هو PIXFORMAT_JPEG، فإن حجم الإطار ينخفض للحصول على معدل إطار أعلى.

إذا كان نموذج الكاميرا هو M5STACK_WIDE أو M5STACK_ESP32CAM، فإن المستشعر يتم عكسه رأسيًا وأفقيًا.

إذا كان نموذج الكاميرا هو ESP32S3_EYE، فإن المستشعر يتم عكسه رأسيًا.

يتم بدء تشغيل WiFi وإدخال اسم المستخدم وكلمة المرور، ويتم تعطيل وضع النوم.

```arduino
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

  // الخطوط السابقة تحتوي على الشرح باللغة الإنجليزية

  if (buttonPressed)
  {
    digitalWrite(ONBOARD_LED, HIGH);
    delay(300);
    digitalWrite(ONBOARD_LED, LOW);

    camera_fb_t *fb = esp_camera_fb_get();
    if (!fb)
    {
      Serial.println("فشل في الحصول على مخبأ الإطار من الكاميرا");
      return;
    }

    HTTPClient http;

    http.begin(serverName);
    http.addHeader("Content-Type", "image/jpeg");
    int httpResponseCode = http.POST(fb->buf, fb->len);
    if (httpResponseCode > 0)
    {
      Serial.printf("تم تحميل الصورة بنجاح، رمز الاستجابة من الخادم: %d\n", httpResponseCode);

      digitalWrite(ONBOARD_LED, HIGH);
      delay(300);
      digitalWrite(ONBOARD_LED, LOW);
    }
    else
    {
      Serial.printf("فشل تحميل الصورة، رمز الخطأ: %s\n", http.errorToString(httpResponseCode).c_str());
    }
    http.end();

    esp_camera_fb_return(fb);

    buttonPressed = false;
  }
}

void buttonInterrupt()
{
  buttonPressed = true;
}
```

## استقبال الصور المرفوعة

هنا، سنستخدم مكتبة flask في Python لإنشاء خادم HTTP يستقبل الصور المرفوعة.

```python title="receive-photo.py"
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        image = request.data

# حفظ الصور في المجلد المحدد
with open('base.png', 'wb') as f:
    f.write(image)
print("تم حفظ الصورة، جاري التقنين ...")
# تشغيل برنامج نقل الأسلوب باستخدام لغة برمجة بايثون
subprocess.run(['python', './style_transfer.py'])

return "تم تحميل الصورة بنجاح", 200
except Exception as e:
    print("فشل تحميل الصورة:", str(e))
    return "فشل تحميل الصورة", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

لا تقم بتشغيل البرنامج بعد، `style_transfer.py` هو برنامج نقل الأسلوب وسيتم عرضه في الخطوة التالية. منطق هذا البرنامج هو إذا تم استلام الصورة التي تم إرسالها من ESP32-S3 بنجاح، فسيتم استخدام `subprocess` لتشغيل برنامج نقل الأسلوب تلقائيًا.

يجب ملاحظة أنه إذا حدث خطأ في البرنامج وتم الإشارة إلى أن المنفذ مشغول، يمكنك محاولة تغيير `port=9000` إلى قيمة أخرى.

## برنامج نقل الأسلوب

في نفس المجلد `receive-photo.py`، سنستخدم TensorFlow لكتابة برنامج Python لنقل الأسلوب. أولاً، قم بتثبيت الاعتماديات اللازمة للبرنامج (بسبب بيئة الشبكة في الصين، من الصعب على TensorFlow تنزيل البرامج، لذا يجب أن تكون صبورًا)، ثم قم بإعداد صورة للتحويل إلى نمط واحد، وقم بتسميتها `base.png`؛ وصورة مرجعية للنمط، واسمها `style_reference.png`، يمكن أن تكون لوحة فنية مثل "السماء الليلية" لفان جوخ:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308152239917.png)

ثم، قم بكتابة برنامج نقل الأسلوب:

```python title="style_transfer.py"
from IPython.display import Image, display
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import vgg19

base_image_path = "./base.png"  # عنوان الصورة التي سيتم تحويلها إلى نمط واحد
style_reference_image_path = "./style_reference.png"  # عنوان صورة النمط المرجعي

result_prefix = "img_generated"

# تعيين أوزان الخسارة لكل جزء
total_variation_weight = 1e-6
style_weight = 1e-6
content_weight = 2.5e-8

# حجم الصورة المولدة
width, height = keras.preprocessing.image.load_img(base_image_path).size
img_nrows = 400
img_ncols = int(width * img_nrows / height)

# استخدام الأمر التالي لعرض الصورة الأساسية وصورة النمط المرجعي التي سيتم تحويلها

display(Image(base_image_path))
display(Image(style_reference_image_path))

# معالجة الصور

```

تعديل الصورة

```python
def preprocess_image(image_path):
    # استخدام دالة مكتبة Keras لفتح الصورة وتعديل حجمها وتنسيقها كتنسيق تنسيق الأنابيب المناسب
    img = keras.preprocessing.image.load_img(
        image_path, target_size=(img_nrows, img_ncols)
    )
    img = keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = vgg19.preprocess_input(img)
    return tf.convert_to_tensor(img)


def deprocess_image(x):
    # استخدام دالة أخرى لتحويل التنسيق إلى صورة صالحة
    x = x.reshape((img_nrows, img_ncols, 3))
    # إزالة المركز الصفري عن طريق متوسط البكسل
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    # 'BGR'->'RGB'
    x = x[:, :, ::-1]
    x = np.clip(x, 0, 255).astype("uint8")
    return x


# مصفوفة gram لتنسيق الصورة (ضرب مصفوفة الميزات وتحويلها إلى ترتيب مصفوفة الميزات)

def gram_matrix(x):
    x = tf.transpose(x, (2, 0, 1))
    features = tf.reshape(x, (tf.shape(x)[0], -1))
    gram = tf.matmul(features, tf.transpose(features))
    return gram

# "خسارة الأسلوب" تهدف إلى الحفاظ على أسلوب الصورة المرجعية في الصورة المولدة.
# يعتمد على مصفوفة gram (استخراج الأسلوب) من صورة الأسلوب المرجعية
# وخرائط الميزات التي تم إنشاؤها منها في الصورة المولدة


def style_loss(style, combination):
    S = gram_matrix(style)
    C = gram_matrix(combination)
    channels = 3
    size = img_nrows * img_ncols
    return tf.reduce_sum(tf.square(S - C)) / (4.0 * (channels ** 2) * (size ** 2))

# تصميم دالة الخسارة المساعدة للحفاظ على محتوى الصورة الأساسي في الصورة المولدة


def content_loss(base, combination):
    return tf.reduce_sum(tf.square(combination - base))

# الدالة الخسارة الثالثة هي خسارة التباين الإجمالي
# تم تصميم هذه الوظيفة للحفاظ على التماسك المحلي للصورة المولدة.


def total_variation_loss(x):
    a = tf.square(
        x[:, : img_nrows - 1, : img_ncols - 1, :] - x[:, 1:, : img_ncols - 1, :]
    )
    b = tf.square(
        x[:, : img_nrows - 1, : img_ncols - 1, :] - x[:, : img_nrows - 1, 1:, :]
    )
    return tf.reduce_sum(tf.pow(a + b, 1.25))

# بعد ذلك ، دعونا ننشئ نموذج استخراج الميزات الذي يسترد النشاط الوسطي لـ VGG19 (حسب الاسم المعطى).


# استبدال مسار الوزن الذي تم تنزيله محليًا
weights_path = "./dependencies/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5"
```

# إنشاء نموذج VGG19 يحمل وزن ImageNet المدرب مسبقًا
model = vgg19.VGG19(weights=weights_path, include_top=False)

# الحصول على الإخراج الرمزي لكل طبقة "حاسمة" (نحدد لها اسمًا فريدًا).
outputs_dict = dict([(layer.name, layer.output) for layer in model.layers])

# إنشاء نموذج يعيد قيم التنشيط لكل طبقة في VGG19 (على شكل قاموس).
feature_extractor = keras.Model(inputs=model.inputs, outputs=outputs_dict)

# وأخيرًا، هذا هو الكود الذي يحسب خسارة نقل الأسلوب.

# قائمة الطبقات المستخدمة لفقدان الأسلوب.
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

    # تهيئة الخسارة.
    loss = tf.zeros(shape=())

    # إضافة فقدان المحتوى.
    layer_features = features[content_layer_name]
    base_image_features = layer_features[0, :, :, :]
    combination_features = layer_features[2, :, :, :]
    loss = loss + content_weight * content_loss(
        base_image_features, combination_features
    )
    # إضافة فقدان الأسلوب.
    for layer_name in style_layer_names:
        layer_features = features[layer_name]
        style_reference_features = layer_features[1, :, :, :]
        combination_features = layer_features[2, :, :, :]
        sl = style_loss(style_reference_features, combination_features)
        loss += (style_weight / len(style_layer_names)) * sl

    # إضافة فقدان التغير الكلي.
    loss += total_variation_weight * total_variation_loss(combination_image)
    return loss


# إضافة مزود الخدمة tf.function إلى حساب الخسارة وحساب التدرج لتشغيلها بشكل أسرع أثناء الترجمة.

@tf.function
def compute_loss_and_grads(combination_image, base_image, style_reference_image):
    with tf.GradientTape() as tape:
        loss = compute_loss(combination_image, base_image,
                            style_reference_image)
    grads = tape.gradient(loss, combination_image)
    return loss, grads

# تنفيذ خطوات الانحدار التدريجي الجماعي بشكل متكرر لتقليل الخسارة قدر الإمكان وحفظ الصور المولدة كل 100 تكرار.
# تخفيض معدل التعلم بنسبة 0.96 كل 100 خطوة.

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
        print("Iteration %d: loss=%.2f" % (i, loss))
        img = deprocess_image(combination_image.numpy())
        fname = result_prefix + "_at_iteration_%d.png" % i
        keras.preprocessing.image.save_img(fname, img)

# بعد 4000 تكرارًا ، يتم إخراج النتيجة:
display(Image(result_prefix + "_at_iteration_4000.png"))
```

الآن ، يمكنك تشغيل هذا البرنامج بمفرده ، وإذا لم يتم الإبلاغ عن أي أخطاء في البرنامج ، فسوف تجد الصورة التي تم تحويلها بنجاح بعد فترة قصيرة (الوقت يعتمد على أداء جهاز الكمبيوتر الخاص بك) في الدليل الحالي.

إذا تم تشغيل البرنامج بنجاح ، فيمكنك تشغيل `receive-photo.py` مباشرةً لاستلام الصور التي تم التقاطها بواسطة ESP32-S3 وتحويلها مباشرةً إلى صور بأسلوب معين.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308152246623.png)

## المراجع والشكر

- [تنفيذ TensorFlow لنقل الأسلوب](https://zhuanlan.zhihu.com/p/349072196)
- [نقل الأسلوب العصبي](https://www.tensorflow.org/tutorials/generative/style_transfer?hl=zh-cn)
- [استخدام الكاميرا](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.