# StyleTransferCam - Style Transfer Camera based on ESP32-S3

![](https://f004.backblazeb2.com/file/wiki-media/img/202308152238959.png)

When art meets technology, a new world unfolds before us. It is a wonderful visual feast and an exploration of infinite possibilities. StyleTransferCam is a style transfer camera based on ESP32-S3. It uses a machine learning technique called "style transfer". When you press the onboard button, it takes a picture of the current scene, blends it with a preset style template photo (such as Van Gogh's "Starry Night"), and generates a unique and creative work.

StyleTransferCam consists of the following processes:

1. Press the onboard button - take a photo - upload it to a backend server (which can be a PC or an old phone).
2. Automatically start the Python program for style transfer, process the photo, and output the stylized photo.
3. If ESP32-S3 comes with a TFT screen, it can also be sent back to the screen for display.

![](https://f004.backblazeb2.com/file/wiki-media/img/202308152244791.png)

## Test Onboard Button and LED

First, a simple Arduino program is used to test whether the onboard button and LED can be used normally. The program sets up a hardware interrupt to capture the button press event, and the LED is turned on for half a second before automatically turning off.

```cpp title="Onboard-Key-ctrl-LED_interrupt.ino"
#define ONBOARD_KEY 47  // Onboard button
#define ONBOARD_LED 21  // Onboard LED

volatile bool buttonPressed = false;  // Button falling edge interrupt flag

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
    buttonPressed = false;  // Reset interrupt flag
  }
}

void buttonInterrupt() {
  buttonPressed = true;  // Set falling edge interrupt flag
}
```

## Take and Upload Photo with Button

Next, we write an Arduino program to use the onboard button to control ESP32-S3 to take a photo and upload it to a specified network location. This network location is set in the code as `serverName = "http://192.168.31.2:9000/upload"`, which needs to be modified to the address of your backend server. We use a backend Python file upload service (which will be explained in the following steps), and here it needs to be modified to the IP address of the machine running this service. (`9000` and `/upload` are set in the `receive-photo.py` program below)

```cpp title="Capture-and-Upload.ino"
#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>

// Server address for uploading photos
const char *serverName = "http://192.168.31.2:9000/upload";

//
// WARNING!!! PSRAM IC required for UXGA resolution and high JPEG quality
//            Ensure ESP32 Wrover Module or other board with PSRAM is selected
//            Partial images will be transmitted if image exceeds buffer size
//
//            You must select partition scheme from the board menu that has at least 3MB APP space.
//            Face Recognition is DISABLED for ESP32 and ESP32-S2, because it takes up from 15
//            seconds to process single frame. Face Detection is ENABLED if PSRAM is enabled as well

// ===================
// Select camera model
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

#define ONBOARD_KEY 47 // Onboard button
#define ONBOARD_LED 21 // Onboard LED

volatile bool buttonPressed = false; // Button interrupt flag

#include "DFRobot_AXP313A.h"

DFRobot_AXP313A axp;

// ===========================
// Enter your WiFi credentials
// ===========================
const char *ssid = "WiFi_SSID";
const char *password = "********";

void startCameraServer();

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

// if PSRAM IC present, init with UXGA resolution and higher JPEG quality
// for larger pre-allocated frame buffer.
if (config.pixel_format == PIXFORMAT_JPEG)
{
  if (psramFound())
  {
    config.jpeg_quality = 0; // 63; // Photo quality. Default is 10
    config.fb_count = 2;
    config.grab_mode = CAMERA_GRAB_LATEST;
  }
  else
  {
    // Limit the frame size when PSRAM is not available
    config.frame_size = FRAMESIZE_UXGA; // Photo resolution. Default is FRAMESIZE_SVGA
    config.fb_location = CAMERA_FB_IN_DRAM;
  }
}
else
{
  // Best option for face detection/recognition
  config.frame_size = FRAMESIZE_UXGA; // FRAMESIZE_240X240;
#if CONFIG_IDF_TARGET_ESP32S3
  config.fb_count = 2;
#endif
}

#if defined(CAMERA_MODEL_ESP_EYE)
  pinMode(13, INPUT_PULLUP);
  pinMode(14, INPUT_PULLUP);
#endif

// Camera initialization
esp_err_t err = esp_camera_init(&config);
if (err != ESP_OK)
{
  Serial.printf("Camera init failed with error 0x%x", err);
  return;
}

sensor_t *s = esp_camera_sensor_get();
// Initial sensors are flipped vertically and colors are a bit saturated
if (s->id.PID == OV3660_PID)
{
  s->set_vflip(s, 1);       // Flip it back
  s->set_brightness(s, 1);  // Increase brightness just a bit
  s->set_saturation(s, -2); // Lower saturation
}
// Drop down frame size for higher initial frame rate
if (config.pixel_format == PIXFORMAT_JPEG)
{
  s->set_framesize(s, FRAMESIZE_QVGA);
}

#if defined(CAMERA_MODEL_M5STACK_WIDE) || defined(CAMERA_MODEL_M5STACK_ESP32CAM)
  s->set_vflip(s, 1);
  s->set_hmirror(s, 1);
#endif

#if defined(CAMERA_MODEL_ESP32S3_EYE)
  s->set_vflip(s, 1);
#endif

WiFi.begin(ssid, password);
WiFi.setSleep(false);

The following code is in Arduino format:

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

    // Take photo
    camera_fb_t *fb = esp_camera_fb_get();
    if (!fb)
    {
      Serial.println("Failed to get camera frame buffer");
      return;
    }

    // Create HTTP client
    HTTPClient http;

    // Upload photo to server
    http.begin(serverName);
    http.addHeader("Content-Type", "image/jpeg");
    int httpResponseCode = http.POST(fb->buf, fb->len);
    if (httpResponseCode > 0)
    {
      Serial.printf("Photo uploaded successfully, server response code: %d\n", httpResponseCode);

      // Blink LED again to indicate successful upload
      digitalWrite(ONBOARD_LED, HIGH);
      delay(300);
      digitalWrite(ONBOARD_LED, LOW);
    }
    else
    {
      Serial.printf("Photo upload failed, error code: %s\n", http.errorToString(httpResponseCode).c_str());
    }
    http.end();

    // Release frame buffer
    esp_camera_fb_return(fb);

    // delay(1000); // Wait for 1 second before taking and uploading another photo

    buttonPressed = false; // Reset interrupt flag
  }
}

void buttonInterrupt()
{
  buttonPressed = true; // Set falling edge interrupt flag
}
```

## Receiving photo uploads with a server

Here we use the Python flask library to build an HTTP server that receives photo uploads.

```python title="receive-photo.py"
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        image = request.data

# Save photos to specified directory
with open('base.png', 'wb') as f:
    f.write(image)
print("Photo saved, rendering...")
# Launch the style transfer Python script
subprocess.run(['python', './style_transfer.py'])

return "Photo uploaded successfully", 200
except Exception as e:
    print("Failed to upload photo:", str(e))
    return "Failed to upload photo", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

Don't run the program yet. `style_transfer.py` is the style transfer program, which will be shown in the next step. The logic of this program is that if the photo sent back by ESP32-S3 is successfully received, the script for style transfer will be automatically called using `subprocess`.

Note that if the program encounters an exception and reports that the port is occupied, you can try changing `port=9000` to a different value.

## Style Transfer Program

In the same directory as `receive-photo.py`, we use TensorFlow to write a Python program for style transfer. First, install the dependencies required by the program (due to the network environment in China, it is difficult to download TensorFlow, so you need to be patient), and then prepare a photo to be stylized in the same directory, named `base.png`; and a style reference image named `style_reference.png`. This image can be an artwork, such as Van Gogh's "Starry Night":

![](https://f004.backblazeb2.com/file/wiki-media/img/202308152239917.png)

Next, write the style transfer program:

```python title="style_transfer.py"
from IPython.display import Image, display
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import vgg19

base_image_path = "./base.png"  # Path to the image to be stylized
style_reference_image_path = "./style_reference.png"  # Path to the style reference image

result_prefix = "img_generated"

# Set weights for each loss component
total_variation_weight = 1e-6
style_weight = 1e-6
content_weight = 2.5e-8

# Size of the generated image
width, height = keras.preprocessing.image.load_img(base_image_path).size
img_nrows = 400
img_ncols = int(width * img_nrows / height)

# View the base image and style reference image to be used for style transfer
display(Image(base_image_path))
display(Image(style_reference_image_path))

# Image preprocessing

# Image Preprocessing

The `preprocess_image` function uses Keras library functions to open an image, resize it to the appropriate tensor size, and format it as a tensor. The image is then preprocessed using VGG19.

The `deprocess_image` function converts the tensor back into a valid image. The function removes the zero center by averaging the pixels, converts the image from 'BGR' to 'RGB', and clips the values to be between 0 and 255.

The `gram_matrix` function calculates the gram matrix of an image tensor. The gram matrix is the product of the feature matrix and its transpose.

# Style Loss

The `style_loss` function is designed to maintain the style of the reference image in the generated image. It is based on the gram matrix (style extraction) from the style reference image and the feature map from the generated image.

# Content Loss

The `content_loss` function is designed to maintain the content of the base image in the generated image.

# Total Variation Loss

The `total_variation_loss` function is designed to maintain local coherence in the generated image.

# Feature Extraction Model

The feature extraction model retrieves the intermediate activations of VGG19 based on their names. The weights for the model are stored locally in the `weights_path` variable.

# Building a VGG19 model with pre-trained ImageNet weights
model = vgg19.VGG19(weights=weights_path, include_top=False)

# Get symbolic outputs of each "key" layer (we gave them unique names)
outputs_dict = dict([(layer.name, layer.output) for layer in model.layers])

# Build a model that returns the activation values for every layer in VGG19 (as a dictionary)
feature_extractor = keras.Model(inputs=model.inputs, outputs=outputs_dict)

# Finally, here is the code to compute the style transfer loss.

# List of layers to use for style loss
style_layer_names = [
    "block1_conv1",
    "block2_conv1",
    "block3_conv1",
    "block4_conv1",
    "block5_conv1",
]
# Layer to use for content loss
content_layer_name = "block5_conv2"


def compute_loss(combination_image, base_image, style_reference_image):
    input_tensor = tf.concat(
        [base_image, style_reference_image, combination_image], axis=0
    )
    features = feature_extractor(input_tensor)

    # Initialize loss
    loss = tf.zeros(shape=())

    # Add content loss
    layer_features = features[content_layer_name]
    base_image_features = layer_features[0, :, :, :]
    combination_features = layer_features[2, :, :, :]
    loss = loss + content_weight * content_loss(
        base_image_features, combination_features
    )
    # Add style loss
    for layer_name in style_layer_names:
        layer_features = features[layer_name]
        style_reference_features = layer_features[1, :, :, :]
        combination_features = layer_features[2, :, :, :]
        sl = style_loss(style_reference_features, combination_features)
        loss += (style_weight / len(style_layer_names)) * sl

    # Add total variation loss
    loss += total_variation_weight * total_variation_loss(combination_image)
    return loss


# Add the tf.function decorator to the loss and gradient computation to make it run faster during compilation.

@tf.function
def compute_loss_and_grads(combination_image, base_image, style_reference_image):
    with tf.GradientTape() as tape:
        loss = compute_loss(combination_image, base_image,
                            style_reference_image)
    grads = tape.gradient(loss, combination_image)
    return loss, grads

# Repeat the batch gradient descent steps to minimize the loss as much as possible, and save the generated images every 100 iterations.
# Reduce the learning rate by 0.96 every 100 steps.

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

# After 4000 iterations, output the result:
display(Image(result_prefix + "_at_iteration_4000.png"))
```

Now, you can try running this Python program separately. If the program does not report an error, wait for a while (the specific time depends on the performance of your computer), and you can find the stylized photos after the iterative style transfer in the current directory.

If this program can run normally, you can directly run `receive-photo.py` to receive photos taken by ESP32-S3 and generate stylized photos automatically.

![](https://f004.backblazeb2.com/file/wiki-media/img/202308152246623.png)

## References and Acknowledgments

- [Style Transfer TensorFlow Implementation](https://zhuanlan.zhihu.com/p/349072196)
- [Neural Style Transfer](https://www.tensorflow.org/tutorials/generative/style_transfer?hl=zh-cn)
- [Camera Usage](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12)

Sorry, there is no Chinese article provided to be translated. Please provide the article for translation.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.