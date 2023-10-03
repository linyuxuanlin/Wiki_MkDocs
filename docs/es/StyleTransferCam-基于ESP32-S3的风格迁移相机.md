# StyleTransferCam - Cámara de transferencia de estilo basada en ESP32-S3

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308152238959.png)

Cuando el arte y la tecnología se unen, un nuevo mundo se despliega ante nosotros, es un maravilloso banquete visual y una exploración de infinitas posibilidades. StyleTransferCam es una cámara de transferencia de estilo basada en ESP32-S3. Utiliza una técnica de aprendizaje automático llamada "transferencia de estilo". Cuando presionas el botón de la placa, toma una foto de la escena actual y la mezcla con una foto de plantilla de estilo preestablecida (como "Starry Night" de Van Gogh) para generar una obra única y creativa.

StyleTransferCam consta de los siguientes procesos:

1. Presionar el botón de la placa - tomar una foto - cargarla en un servidor backend (también puede ser una PC o un teléfono antiguo).
2. Iniciar automáticamente el programa Python de transferencia de estilo para procesar la foto y generar una foto estilizada.
3. Si el ESP32-S3 tiene una pantalla TFT adjunta, también puede devolver la foto para mostrarla en la pantalla.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308152244791.png)

## Probar el botón de la placa y el LED

Primero, escribimos un programa de Arduino simple para probar si el botón de la placa y el LED funcionan correctamente. El programa establece una interrupción de hardware para capturar el evento de presionar el botón y enciende el LED durante medio segundo antes de apagarse automáticamente.

```cpp title="Onboard-Key-ctrl-LED_interrupt.ino"
#define ONBOARD_KEY 47  // Botón de la placa
#define ONBOARD_LED 21  // LED de la placa

volatile bool buttonPressed = false;  // Bandera de interrupción de flanco descendente del botón

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
    buttonPressed = false;  // Restablecer la bandera de interrupción
  }
}

void buttonInterrupt() {
  buttonPressed = true;  // Establecer la bandera de interrupción de flanco descendente
}
```

## Tomar una foto y cargarla con el botón

A continuación, escribimos un programa de Arduino para usar el botón de la placa para controlar la toma de una foto con ESP32-S3 y cargarla en una ubicación de red específica. Esta ubicación de red se establece en el código como `serverName = "http://192.168.31.2:9000/upload"`, que debe modificarse para la dirección de su servidor backend. Utilizamos un servicio de carga de archivos Python backend (que se explicará en los siguientes pasos), y aquí debe modificarse a la dirección IP de la máquina que ejecuta este servicio. (`9000` y `/upload` se establecen en el programa `receive-photo.py` a continuación)

```cpp title="Capture-and-Upload.ino"
#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>

// Dirección del servidor para cargar fotos
const char *serverName = "http://192.168.31.2:9000/upload";

//
// ¡¡¡ADVERTENCIA!!! Se requiere un IC PSRAM para la resolución UXGA y alta calidad JPEG
//            Asegúrese de seleccionar el módulo ESP32 Wrover o cualquier otra placa con PSRAM
//            Se transmitirán imágenes parciales si la imagen excede el tamaño del búfer
//
//            Debe seleccionar el esquema de partición del menú de la placa que tenga al menos 3 MB de espacio APP.
//            El reconocimiento facial está DESACTIVADO para ESP32 y ESP32-S2, porque tarda alrededor de 15
//            segundos en procesar un solo fotograma. La detección facial está ACTIVADA si PSRAM también está habilitado.

// ===================
// Seleccionar modelo de cámara
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

#define ONBOARD_KEY 47 // Botón de la placa
#define ONBOARD_LED 21 // LED de la placa

volatile bool buttonPressed = false; // Bandera de interrupción de flanco descendente del botón

#include "DFRobot_AXP313A.h"

DFRobot_AXP313A axp;

// ===========================
// Ingrese sus credenciales de WiFi
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
    Serial.println("error de inicialización");
    delay(1000);
  }
  axp.enableCameraPower(axp.eOV2640); // Configurar alimentación de la cámara
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
  config.frame_size = FRAMESIZE_UXGA;   // Resolución de la foto. Aquí se establece en FRAMESIZE_UXGA por defecto
  config.pixel_format = PIXFORMAT_JPEG; // para streaming
  // config.pixel_format = PIXFORMAT_RGB565; // para detección/reconocimiento facial
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 0; // 63; // Calidad de la foto. Aquí se establece en 12 por defecto
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

// si el IC PSRAM está presente, inicializar con resolución UXGA y calidad JPEG más alta
// para un búfer de fotograma preasignado más grande.
if (config.pixel_format == PIXFORMAT_JPEG)
{
  if (psramFound())
  {
    config.jpeg_quality = 0; // 63; // Calidad de la foto. Por defecto es 10.
    config.fb_count = 2;
    config.grab_mode = CAMERA_GRAB_LATEST;
  }
  else
  {
    // Limitar el tamaño del fotograma cuando PSRAM no está disponible
    config.frame_size = FRAMESIZE_UXGA; // Resolución de la foto. Por defecto es FRAMESIZE_SVGA.
    config.fb_location = CAMERA_FB_IN_DRAM;
  }
}
else
{
  // Mejor opción para la detección/reconocimiento facial
  config.frame_size = FRAMESIZE_UXGA; // FRAMESIZE_240X240;
#if CONFIG_IDF_TARGET_ESP32S3
  config.fb_count = 2;
#endif
}

#if defined(CAMERA_MODEL_ESP_EYE)
  pinMode(13, INPUT_PULLUP);
  pinMode(14, INPUT_PULLUP);
#endif

  // inicialización de la cámara
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK)
  {
    Serial.printf("La inicialización de la cámara falló con el error 0x%x", err);
    return;
  }

  sensor_t *s = esp_camera_sensor_get();
  // los sensores iniciales están volteados verticalmente y los colores están un poco saturados
  if (s->id.PID == OV3660_PID)
  {
    s->set_vflip(s, 1);       // voltear de vuelta
    s->set_brightness(s, 1);  // aumentar el brillo un poco
    s->set_saturation(s, -2); // reducir la saturación
  }
  // reducir el tamaño del fotograma para una velocidad de fotograma inicial más alta
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

while (WiFi.status() != WL_CONNECTED)
{
  delay(500);
  Serial.print(".");
}
Serial.println("");
Serial.println("WiFi conectado");

startCameraServer();

Serial.print("¡Cámara lista! Use 'http://");
Serial.print(WiFi.localIP());
Serial.println("' para conectarse");
digitalWrite(ONBOARD_LED, LOW);
}

void loop()
{
  // No hacer nada. Todo se hace en otra tarea por el servidor web
  // delay(10000);

  // Lógica después de presionar el botón
  if (buttonPressed)
  {
    digitalWrite(ONBOARD_LED, HIGH);
    delay(300);
    digitalWrite(ONBOARD_LED, LOW);

    // Tomar una foto
    camera_fb_t *fb = esp_camera_fb_get();
    if (!fb)
    {
      Serial.println("Error al obtener el búfer de fotogramas de la cámara");
      return;
    }

    // Establecer cliente HTTP
    HTTPClient http;

    // Subir la foto al servidor
    http.begin(serverName);
    http.addHeader("Content-Type", "image/jpeg");
    int httpResponseCode = http.POST(fb->buf, fb->len);
    if (httpResponseCode > 0)
    {
      Serial.printf("Foto subida con éxito, código de respuesta del servidor: %d\n", httpResponseCode);

      // Parpadear para indicar que se ha subido correctamente
      digitalWrite(ONBOARD_LED, HIGH);
      delay(300);
      digitalWrite(ONBOARD_LED, LOW);
    }
    else
    {
      Serial.printf("Error al subir la foto, código de error: %s\n", http.errorToString(httpResponseCode).c_str());
    }
    http.end();

    // Liberar el búfer de fotogramas
    esp_camera_fb_return(fb);

    // delay(1000); // Esperar 1 segundo antes de tomar y subir otra foto

    buttonPressed = false; // Restablecer la bandera de interrupción
  }
}

void buttonInterrupt()
{
  buttonPressed = true; // Establecer la bandera de interrupción de flanco descendente
}
```

## Servicio de recepción de fotos subidas

Aquí usamos la biblioteca flask de Python para construir un servidor HTTP que reciba fotos subidas.

```python title="receive-photo.py"
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        image = request.data

# Guardar foto en un directorio específico
con open('base.png', 'wb') como f:
    f.write(imagen)
print("Foto guardada, renderizando...")
# Ejecutar el script de transferencia de estilo en Python
subprocess.run(['python', './style_transfer.py'])

return "Foto cargada exitosamente", 200
except Exception as e:
    print("Error al cargar la foto:", str(e))
    return "Error al cargar la foto", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

No ejecute el programa todavía, `style_transfer.py` es el programa de transferencia de estilo que se mostrará en el siguiente paso. La lógica de este programa es que si la foto enviada por ESP32-S3 se recibe correctamente, se iniciará automáticamente el script de transferencia de estilo utilizando `subprocess`.

Tenga en cuenta que si hay una excepción en el programa y se muestra un mensaje de puerto ocupado, puede intentar cambiar `port=9000` por otro valor.

## Programa de transferencia de estilo

En el mismo directorio que `receive-photo.py`, utilizaremos TensorFlow para escribir un programa de transferencia de estilo en Python. Primero, instale las dependencias necesarias para el programa (debido a la red en China, es difícil descargar TensorFlow, así que tenga paciencia) y luego prepare una foto para ser estilizada en el mismo directorio, nómbrela como `base.png`. También necesitará una imagen de referencia de estilo, nómbrela como `style_reference.png`. Esta imagen puede ser una pintura artística, como "La noche estrellada" de Van Gogh:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308152239917.png)

A continuación, escriba el programa de transferencia de estilo:

```python title="style_transfer.py"
from IPython.display import Image, display
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import vgg19

base_image_path = "./base.png"  # Dirección de la imagen a estilizar
style_reference_image_path = "./style_reference.png"  # Dirección de la imagen de referencia de estilo

result_prefix = "img_generated"

# Peso de cada parte de la pérdida
total_variation_weight = 1e-6
style_weight = 1e-6
content_weight = 2.5e-8

# Tamaño de la imagen generada
width, height = keras.preprocessing.image.load_img(base_image_path).size
img_nrows = 400
img_ncols = int(width * img_nrows / height)

# Ver la imagen base y la imagen de referencia de estilo que se utilizarán para la transferencia de estilo
display(Image(base_image_path))
display(Image(style_reference_image_path))

# Preprocesamiento de la imagen

def preprocess_image(image_path):
    # Utilizamos la función de la biblioteca Keras para abrir la imagen, ajustar su tamaño y formatearla como un tensor adecuado
    img = keras.preprocessing.image.load_img(
        image_path, target_size=(img_nrows, img_ncols)
    )
    img = keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = vgg19.preprocess_input(img)
    return tf.convert_to_tensor(img)


def deprocess_image(x):
    # Utilizamos otra función para convertir el tensor en una imagen válida
    x = x.reshape((img_nrows, img_ncols, 3))
    # Eliminamos el centro cero mediante el promedio de píxeles
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    # 'BGR'->'RGB'
    x = x[:, :, ::-1]
    x = np.clip(x, 0, 255).astype("uint8")
    return x


# La matriz Gram de un tensor de imagen (el producto de la matriz de características y su transposición)

def gram_matrix(x):
    x = tf.transpose(x, (2, 0, 1))
    features = tf.reshape(x, (tf.shape(x)[0], -1))
    gram = tf.matmul(features, tf.transpose(features))
    return gram

# La "pérdida de estilo" tiene como objetivo mantener el estilo de la imagen de referencia en la imagen generada.
# Se basa en la matriz Gram (extracción de estilo) de la imagen de referencia de estilo
# y los mapas de características de la imagen generada a partir de ella.


def style_loss(style, combination):
    S = gram_matrix(style)
    C = gram_matrix(combination)
    channels = 3
    size = img_nrows * img_ncols
    return tf.reduce_sum(tf.square(S - C)) / (4.0 * (channels ** 2) * (size ** 2))

# La función de pérdida de contenido se utiliza para mantener el contenido básico de la imagen en la imagen generada.


def content_loss(base, combination):
    return tf.reduce_sum(tf.square(combination - base))

# La tercera función de pérdida es la pérdida total de variación,
# diseñada para mantener la coherencia local en la imagen generada.


def total_variation_loss(x):
    a = tf.square(
        x[:, : img_nrows - 1, : img_ncols - 1, :] - x[:, 1:, : img_ncols - 1, :]
    )
    b = tf.square(
        x[:, : img_nrows - 1, : img_ncols - 1, :] - x[:, : img_nrows - 1, 1:, :]
    )
    return tf.reduce_sum(tf.pow(a + b, 1.25))

# A continuación, creamos un modelo de extracción de características que recupera las activaciones intermedias de VGG19 (creando un diccionario según el nombre).


# Reemplaza con la ruta de archivo de peso descargado localmente
weights_path = "./dependencies/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5"

# Crear un modelo VGG19 con pesos pre-entrenados de ImageNet
model = vgg19.VGG19(weights=weights_path, include_top=False)

# Obtener la salida simbólica de cada capa "clave" (a las que hemos asignado un nombre único).
outputs_dict = dict([(layer.name, layer.output) for layer in model.layers])

# Crear un modelo que devuelva los valores de activación de cada capa en VGG19 (en forma de diccionario).
feature_extractor = keras.Model(inputs=model.inputs, outputs=outputs_dict)

# Finalmente, aquí está el código para calcular la pérdida de transferencia de estilo.

# Lista de capas para la pérdida de estilo.
style_layer_names = [
    "block1_conv1",
    "block2_conv1",
    "block3_conv1",
    "block4_conv1",
    "block5_conv1",
]
# Capa para la pérdida de contenido.
content_layer_name = "block5_conv2"


def compute_loss(combination_image, base_image, style_reference_image):
    input_tensor = tf.concat(
        [base_image, style_reference_image, combination_image], axis=0
    )
    features = feature_extractor(input_tensor)

    # Inicializar la pérdida.
    loss = tf.zeros(shape=())

    # Agregar la pérdida de contenido.
    layer_features = features[content_layer_name]
    base_image_features = layer_features[0, :, :, :]
    combination_features = layer_features[2, :, :, :]
    loss = loss + content_weight * content_loss(
        base_image_features, combination_features
    )
    # Agregar la pérdida de estilo.
    for layer_name in style_layer_names:
        layer_features = features[layer_name]
        style_reference_features = layer_features[1, :, :, :]
        combination_features = layer_features[2, :, :, :]
        sl = style_loss(style_reference_features, combination_features)
        loss += (style_weight / len(style_layer_names)) * sl

    # Agregar la pérdida total de variación.
    loss += total_variation_weight * total_variation_loss(combination_image)
    return loss


# Agregar el decorador tf.function a los cálculos de pérdida y gradiente para que se ejecuten más rápido durante la compilación.

@tf.function
def compute_loss_and_grads(combination_image, base_image, style_reference_image):
    with tf.GradientTape() as tape:
        loss = compute_loss(combination_image, base_image,
                            style_reference_image)
    grads = tape.gradient(loss, combination_image)
    return loss, grads

# Repetir el proceso de descenso de gradiente en lotes para minimizar la pérdida al máximo y guardar la imagen generada cada 100 iteraciones.
# Reduzca la tasa de aprendizaje en un 0,96 cada 100 pasos.

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
        print("Iteración %d: pérdida=%.2f" % (i, loss))
        img = deprocess_image(combination_image.numpy())
        fname = result_prefix + "_en_iteracion_%d.png" % i
        keras.preprocessing.image.save_img(fname, img)

# Después de 4000 iteraciones, se produce la siguiente salida:
display(Image(result_prefix + "_en_iteracion_4000.png"))
```

Ahora puedes probar a ejecutar este programa de Python por separado. Si no hay errores, espera un momento (el tiempo exacto depende del rendimiento de tu ordenador) y encontrarás la foto con estilo transferido en el directorio actual.

Si este programa funciona correctamente, puedes ejecutar `receive-photo.py` directamente para recibir automáticamente las fotos tomadas por ESP32-S3 y generar fotos con estilo transferido.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308152246623.png)

## Referencias y agradecimientos

- [Implementación de estilo de transferencia en TensorFlow](https://zhuanlan.zhihu.com/p/349072196)
- [Transferencia de estilo neuronal](https://www.tensorflow.org/tutorials/generative/style_transfer?hl=zh-cn)
- [Uso de la cámara](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.