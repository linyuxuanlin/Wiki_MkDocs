# StyleTransferCam - Style Transfer Camera Based on ESP32-S3

![Image](https://img.wiki-power.com/d/wiki-media/img/202308152238959.png)

When art and technology intersect, a new world unfolds before us. It is a visual feast and an exploration of infinite possibilities. StyleTransferCam is a style transfer camera based on ESP32-S3. It utilizes a machine learning technique called "style transfer." When you press the onboard button, it captures the current scene and blends it with a predefined style template photo, which can be something like Van Gogh's "Starry Night," creating a uniquely crafted artwork.

StyleTransferCam consists of the following main processes:

1. Press the onboard button - Capture a photo - Upload it to the backend server (which can also be a PC or an old phone).
2. Automatically launch a Python program for style transfer, process the photo, and generate a stylized image.
3. If the ESP32-S3 is equipped with a TFT screen, it can also display the image on the screen.

![Image](https://img.wiki-power.com/d/wiki-media/img/202308152244791.png)

## Testing the Onboard Button and LED

First, there's a simple Arduino program to test whether the onboard button and LED are functioning properly. The program sets up a hardware interrupt to detect button presses, illuminates the LED for half a second after the button press, and then automatically turns it off.

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

## Capturing and Uploading Photos Using the Button

Next, we create an Arduino program to capture a photo with the ESP32-S3 using the onboard button and upload it to a specified network location. The server address for photo upload is set in the code as `serverName = "http://192.168.31.2:9000/upload"` and should be modified to match your backend server's address. We are using a backend Python file upload service (explained in the following steps), and here you should change it to the IP address of the machine running this service (`9000` and `/upload` are set in the `receive-photo.py` program in the subsequent steps).

```cpp title="Capture-and-Upload.ino"
#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>

// Server address for photo upload
const char *serverName = "http://192.168.31.2:9000/upload";


```markdown
//
// WARNING!!! PSRAM IC required for UXGA resolution and high JPEG quality
//            Ensure ESP32 Wrover Module or other board with PSRAM is selected
//            Partial images will be transmitted if the image exceeds the buffer size
//
//            You must select a partition scheme from the board menu that has at least 3MB of APP space.
//            Face Recognition is DISABLED for ESP32 and ESP32-S2 because it takes up to 15
//            seconds to process a single frame. Face Detection is ENABLED if PSRAM is also enabled.

// ===================
// Select the camera model
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

volatile bool buttonPressed = false; // Button falling edge interrupt flag

#include "DFRobot_AXP313A.h"

DFRobot_AXP313A axp;

// ===========================
// Enter your WiFi credentials
// ===========================
const char *ssid = "WiFi_SSID";
const char *password = "********";

void startCameraServer();
```

```cpp
void setup() {
  // Configure pins and initialize serial communication
  pinMode(ONBOARD_KEY, INPUT);
  pinMode(ONBOARD_LED, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(ONBOARD_KEY), buttonInterrupt, FALLING);
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();

  // Initialize AXP Power Management
  while (axp.begin() != 0) {
    Serial.println("Initialization error");
    delay(1000);
  }

  // Enable camera power supply for OV2640
  axp.enableCameraPower(axp.eOV2640);

  // Configure camera settings
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
  config.frame_size = FRAMESIZE_UXGA; // Photo resolution (default is FRAMESIZE_UXGA)
  config.pixel_format = PIXFORMAT_JPEG; // Use PIXFORMAT_JPEG for streaming

  // For face detection/recognition, use PIXFORMAT_RGB565
  // config.pixel_format = PIXFORMAT_RGB565;

  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 0; // Photo quality (default is 12)
  config.fb_count = 1;

  /*
  Available photo resolutions:
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

```c
// If a PSRAM IC is present, initialize with UXGA resolution and higher JPEG quality
// for a larger pre-allocated frame buffer.
if (config.pixel_format == PIXFORMAT_JPEG)
{
    if (psramFound())
    {
        config.jpeg_quality = 0; // 63; // Photo quality. Default here is 10
        config.fb_count = 2;
        config.grab_mode = CAMERA_GRAB_LATEST;
    }
    else
    {
        // Limit the frame size when PSRAM is not available
        config.frame_size = FRAMESIZE_UXGA; // Photo resolution. Default here is FRAMESIZE_SVGA
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
    Serial.printf("Camera initialization failed with error 0x%x", err);
    return;
}

sensor_t *s = esp_camera_sensor_get();
// Initial sensors are flipped vertically, and colors are a bit saturated
if (s->id.PID == OV3660_PID)
{
    s->set_vflip(s, 1);       // Flip it back
    s->set_brightness(s, 1);  // Increase the brightness slightly
    s->set_saturation(s, -2); // Reduce the saturation
}
// Reduce frame size for a higher initial frame rate if the pixel format is JPEG
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
```

```cpp
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

    // Capture a photo
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

      // Flash the LED to indicate successful upload
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

    // delay(1000); // Wait for 1 second before capturing and uploading again

    buttonPressed = false; // Reset the interrupt flag
  }
}

void buttonInterrupt()
{
  buttonPressed = true; // Set the falling edge interrupt flag
}
```

## Service for Receiving Photo Uploads

Here, we use Python's Flask library to set up an HTTP server for receiving photo uploads.

```python title="receive-photo.py"
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        image = request.data
```

```python
# Save the photo to the specified directory
with open('base.png', 'wb') as f:
    f.write(image)
print("Photo saved, rendering in progress...")

# Launch the style transfer Python script
subprocess.run(['python', './style_transfer.py'])

return "Photo uploaded successfully", 200
except Exception as e:
    print("Photo upload failed:", str(e))
    return "Photo upload failed", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

Before running the program, note that `style_transfer.py` is the style transfer program, which will be shown in the next step. The logic of this program is that if it successfully receives a photo from ESP32-S3, it will automatically launch the style transfer script using `subprocess`.

Please be aware that if the program encounters an exception and reports that the port is already in use, you can try changing the `port=9000` value to a different one.

## Style Transfer Program

In the same directory as `receive-photo.py`, we have a Python program for style transfer written using TensorFlow. First, install the dependencies required for the program (due to the network environment in China, TensorFlow may be challenging to download, so please be patient). Then, in the same directory, prepare an image to be stylized named `base.png`, and another image for style reference named `style_reference.png`. The style reference image can be an artwork, such as Van Gogh's "Starry Night":

![](https://img.wiki-power.com/d/wiki-media/img/202308152239917.png)

Next, write the style transfer program:

```python title="style_transfer.py"
from IPython.display import Image, display
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import vgg19

base_image_path = "./base.png"  # Path to the image for style transfer
style_reference_image_path = "./style_reference.png"  # Path to the style reference image

result_prefix = "img_generated"

# Weight settings for different loss components
total_variation_weight = 1e-6
style_weight = 1e-6
content_weight = 2.5e-8

# Image dimensions for generating the output
width, height = keras.preprocessing.image.load_img(base_image_path).size
img_nrows = 400
img_ncols = int(width * img_nrows / height)

# Use the following commands to view the base image and style reference image for style transfer

display(Image(base_image_path))
display(Image(style_reference_image_path))

# Image preprocessing
```

```python
# Define a function to preprocess an image
def preprocess_image(image_path):
    # Use Keras library functions to open the image, resize it, and format it as an appropriate tensor
    img = keras.preprocessing.image.load_img(
        image_path, target_size=(img_nrows, img_ncols)
    )
    img = keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = vgg19.preprocess_input(img)
    return tf.convert_to_tensor(img)

# Define a function to deprocess an image
def deprocess_image(x):
    # Reshape the tensor to create a valid image
    x = x.reshape((img_nrows, img_ncols, 3))
    # Remove zero center by adding mean pixel values
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    # Convert from 'BGR' to 'RGB'
    x = x[:, :, ::-1]
    x = np.clip(x, 0, 255).astype("uint8")
    return x

# Calculate the gram matrix of an image tensor (the product of feature matrix and its transpose)
def gram_matrix(x):
    x = tf.transpose(x, (2, 0, 1))
    features = tf.reshape(x, (tf.shape(x)[0], -1))
    gram = tf.matmul(features, tf.transpose(features))
    return gram

# Style loss function aims to preserve the style of the reference image in the generated image
# It is based on the gram matrix (style extraction) from the style reference image
# and the feature maps from the generated image
def style_loss(style, combination):
    S = gram_matrix(style)
    C = gram_matrix(combination)
    channels = 3
    size = img_nrows * img_ncols
    return tf.reduce_sum(tf.square(S - C)) / (4.0 * (channels ** 2) * (size ** 2))

# Content loss function is designed to maintain the content of the base image in the generated image
def content_loss(base, combination):
    return tf.reduce_sum(tf.square(combination - base)

# The third loss function is the total variation loss, designed to make the generated image locally coherent
def total_variation_loss(x):
    a = tf.square(
        x[:, :img_nrows - 1, :img_ncols - 1, :] - x[:, 1:, :img_ncols - 1, :]
    )
    b = tf.square(
        x[:, :img_nrows - 1, :img_ncols - 1, :] - x[:, :img_nrows - 1, 1:, :]
    )
    return tf.reduce_sum(tf.pow(a + b, 1.25))

# Next, let's create a feature extraction model that retrieves intermediate activations of VGG19 (based on layer names).

# Replace with the path to your locally downloaded weight file
weights_path = "./dependencies/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5"
```

```python
# Create a VGG19 model with pre-trained ImageNet weights
model = vgg19.VGG19(weights=weights_path, include_top=False)

# Obtain symbolic outputs for each "key" layer (we assign them unique names).
outputs_dict = dict([(layer.name, layer.output) for layer in model.layers])

# Build a model that returns activations for each layer in VGG19 as a dictionary.
feature_extractor = keras.Model(inputs=model.inputs, outputs=outputs_dict)

# Finally, here's the code for computing style transfer loss.

# List of layers for style loss
style_layer_names = [
    "block1_conv1",
    "block2_conv1",
    "block3_conv1",
    "block4_conv1",
    "block5_conv1",
]

# Layer for content loss
content_layer_name = "block5_conv2"


def compute_loss(combination_image, base_image, style_reference_image):
    input_tensor = tf.concat(
        [base_image, style_reference_image, combination_image], axis=0
    )
    features = feature_extractor(input_tensor)

    # Initialize the loss
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

# Add the tf.function decorator to the loss computation and gradient computation for faster compilation
```

```python
@tf.function
def compute_loss_and_grads(combination_image, base_image, style_reference_image):
    with tf.GradientTape() as tape:
        loss = compute_loss(combination_image, base_image,
                            style_reference_image)
    grads = tape.gradient(loss, combination_image)
    return loss, grads

# Perform batch gradient descent steps repeatedly to minimize the loss as much as possible and save the generated images every 100 iterations.
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

# After 4000 iterations, the output is as follows:
display(Image(result_prefix + "_at_iteration_4000.png"))
```

Now, you can try running this Python program on its own. If the program runs without errors, wait for a little while (the exact time depends on your computer's performance), and you will find the stylized photos in the current directory after the iterative style transfer.

If this program runs successfully, you can run `receive-photo.py` to automatically receive photos captured by ESP32-S3 and generate stylized photos.

![Stylized Image](https://img.wiki-power.com/d/wiki-media/img/202308152246623.png)

## References and Acknowledgments

- [Style Transfer TensorFlow Implementation](https://zhuanlan.zhihu.com/p/349072196)
- [Neural Style Transfer](https://www.tensorflow.org/tutorials/generative/style_transfer?hl=zh-cn)
- [Camera Usage](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12)
```

Certainly, here is the translation:

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.