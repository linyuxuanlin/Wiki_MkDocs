# TinyMonitor - Monitor de estado del servidor compacto

![](https://f004.backblazeb2.com/file/wiki-media/img/202305261716469.jpg)

TinyMonitor es un monitor de estado del servidor extremadamente compacto y minimalista que consta solo de un controlador principal ESP32 y una pantalla OLED, que muestra los parámetros de estado en tiempo real del servidor para facilitar la observación y la depuración.

## Preparación previa

Los materiales de hardware utilizados en este proyecto son muy simples: un Beetle ESP32-C3 con Wi-Fi y Bluetooth incorporados, y una pantalla OLED de 128x64.

![](https://f004.backblazeb2.com/file/wiki-media/img/202305261541993.png)

La definición de pines de Beetle ESP32-C3 es la siguiente.

![](https://f004.backblazeb2.com/file/wiki-media/img/202305261545236.png)

Como se puede utilizar el modo I2C de software (es decir, pines I2C personalizados) para controlar la pantalla OLED, he definido los pines `0`/`1` de Beetle ESP32-C3 como funciones `SCL`/`SDA`. De esta manera, el cableado es muy sencillo, solo hay que soldar los 4 pines juntos.

![](https://f004.backblazeb2.com/file/wiki-media/img/202305261546367.png)

Nota: antes de cargar el programa en Beetle ESP32-C3, es necesario agregar el paquete ESP32 para reconocer correctamente el modelo de la placa. Consulte su [**página Wiki**](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3) para obtener más detalles.

### Encender la pantalla

Se puede utilizar este programa sencillo para comprobar si se puede mostrar información correctamente en la pantalla OLED:

```cpp title="OLED_SoftwareI2C_HelloWorld.ino"
#include <U8g2lib.h>

#define OLED_SDA 1
#define OLED_SCL 0

U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R2,  OLED_SCL, OLED_SDA, U8X8_PIN_NONE);

void setup(void) {
  u8g2.begin();
}

void loop(void) {
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_ncenB08_tr);
  u8g2.drawStr(0,10,"Hello World!");
  u8g2.sendBuffer();
  delay(1000);
}
```

## Servicio de agente MQTT

MQTT es un protocolo de transmisión de mensajes basado en cliente-servidor y publicación/suscripción. En este proyecto, MQTT es el puente de comunicación entre el servidor y ESP32. Para mayor comodidad, he desplegado el servicio MQTT en el servidor que se va a supervisar; si es necesario, también se puede desplegar en otras máquinas.

### Despliegue del servicio Mosquitto

Mosquitto es un software de agente de mensajes de código abierto que implementa el protocolo de envío de mensajes MQTT v3.1. En este caso, he utilizado la implementación de Docker [**eclipse-mosquitto**](https://hub.docker.com/_/eclipse-mosquitto) como servidor de agente MQTT. Si no está familiarizado con la implementación de Docker, puede consultar los artículos [**Guía sencilla de Docker**](https://wiki-power.com/es/Docker%E7%AE%80%E6%98%93%E6%8C%87%E5%8D%97/) y [**Docker Compose - Una forma más elegante de abrir**](https://wiki-power.com/es/DockerCompose-%E6%9B%B4%E4%BC%98%E9%9B%85%E7%9A%84%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F/).

Según las instrucciones oficiales, primero debe crear los siguientes directorios y archivos para que Mosquitto los use y otorgarles permisos suficientes: (por favor, cambie `${STACK_DIR}` a la ruta local donde se almacenan los datos, por ejemplo, `/DATA/AppData/mosquitto`, lo mismo a continuación)

```bash
mkdir -vp ${STACK_DIR}/{config,data,log} \
&& touch ${STACK_DIR}/config/mosquitto.conf \
&& chmod -R 755 ${STACK_DIR} \
&& chmod -R 777 ${STACK_DIR}/log \
```

Luego, escriba el siguiente contenido en el archivo `mosquitto.conf`:

```conf title="mosquitto.conf"
persistence true
persistence_location /mosquitto/data
log_dest file /mosquitto/log/mosquitto.log

# Desactivar el modo anónimo
allow_anonymous false
# Especificar el archivo de contraseña
password_file /mosquitto/config/pwfile.conf
```

Implemente el contenedor utilizando `docker-compose`:

```yaml title="compose.yaml"
version: "3"
services:
  mosquitto:
    container_name: mosquitto_app
    image: eclipse-mosquitto:1.6.14 # La versión 2.x puede tener problemas de compatibilidad
    ports:
      - "1883:1883"
      - "9001:9001"
    volumes:
      - ${STACK_DIR}/config/mosquitto.conf:/mosquitto/config/mosquitto.conf
      - ${STACK_DIR}/data:/mosquitto/data
      - ${STACK_DIR}/log:/mosquitto/log
    #privileged: true
    restart: always
```

Ingrese al contenedor y cambie la contraseña:

```bash
cd ruta donde se encuentra compose.yaml
docker compose up

docker compose ps # Encuentre el ID del contenedor en ejecución
docker exec -it ID_del_contenedor sh # Ingrese al shell del contenedor

touch /mosquitto/config/pwfile.conf
chmod -R 755 /mosquitto/config/pwfile.conf

# Cree un usuario y una contraseña, nombre de usuario: test, contraseña: 123
mosquitto_passwd -b /mosquitto/config/pwfile.conf test 123

exit # Salga del shell del contenedor
docker restart ID_del_contenedor # Reinicie el contenedor para que surtan efecto los cambios
```

### Prueba de la disponibilidad del servidor MQTT

Después de iniciar normalmente el servicio `mosquitto`, podemos usar [**MQTTBox**](https://apps.microsoft.com/store/detail/mqttbox/9NBLGGH55JZG) para probar la disponibilidad del servidor proxy MQTT.

Después de instalar el software, haga clic en `Create MQTT Client` para crear una nueva conexión y complete los parámetros relevantes según la siguiente imagen:

![](https://f004.backblazeb2.com/file/wiki-media/img/202305261456592.png)

Donde `HOST` es la dirección del servidor donde se encuentra el servicio MQTT (por ejemplo, la dirección de mi servidor en la red local es `192.168.1.2`); el nombre de usuario y la contraseña deben coincidir con los valores configurados al configurar Mosquitto anteriormente.

Después de hacer clic en `Save`, si ve `Connected` en la barra de estado superior en verde, significa que ya se ha conectado al servidor.

## Script de monitoreo del servidor

Podemos capturar información en tiempo real del dispositivo y enviarla al tema correspondiente en el servidor MQTT mediante el siguiente programa Python que se ejecuta en el servidor. Primero, debe instalar los siguientes paquetes de dependencia:

```bash
pip install paho-mqtt psutil
```

Cree y ejecute el programa Python:

```python title="status-collector.py"
import paho.mqtt.client as mqtt
import psutil
import time

# Conéctese al servidor proxy MQTT
client = mqtt.Client()
client.username_pw_set("MQTT用户名", "MQTT密码")
client.connect("MQTT服务器地址", 端口号)
# Ejemplo: client.connect("192.168.1.2", 1883)

# Recopile el estado del servidor y envíelo al tema MQTT
while True:
    client.publish("USAGE_CPU", psutil.cpu_percent())
    client.publish("USAGE_MEM", psutil.virtual_memory().percent)
    client.publish("USAGE_DISK", psutil.disk_usage('/').percent)
    time.sleep(1) # Publicar cada segundo
```

Después de ejecutar con éxito, podemos hacer clic en `Add subscriber` en la barra de estado superior de MQTTBox para suscribirse a estos tres temas, por ejemplo:

![](https://f004.backblazeb2.com/file/wiki-media/img/202305261513642.png)

Si todo va bien, debería poder ver la información de estado del servidor que se devuelve constantemente en MQTTBox.

## Pantalla Arduino ESP32

Cree el siguiente código de Arduino, modifique los parámetros y grabe en ESP32. Si todo va bien, debería poder ver la información de estado actualizada constantemente.

```cpp title="Received-from-MQTT-and-Display.ino"
#include <Wire.h>
#include <U8g2lib.h>
#include <WiFi.h>
#include <PubSubClient.h>

// Conexión OLED mediante I2C de software, redefinir los pines
#define OLED_SDA 1
#define OLED_SCL 0

```

// Definición de MQTT
#define WIFI_SSID "Nombre de Wi-Fi"
#define WIFI_PASSWORD "Contraseña de Wi-Fi"
#define MQTT_BROKER "Dirección del servidor MQTT" // por ejemplo 192.168.31.2
#define MQTT_PORT Puerto MQTT // por ejemplo 1883
#define MQTT_USERNAME "Nombre de usuario MQTT" //test, debe coincidir con la configuración anterior
#define MQTT_PASSWORD "Contraseña MQTT" //123, debe coincidir con la configuración anterior
#define MQTT_TOPIC_CPU "USO_CPU" // tema suscrito
#define MQTT_TOPIC_MEM "USO_MEM"
#define MQTT_TOPIC_DISK "USO_DISK"

char msg_cpu_usage[10];
char msg_mem_usage[10];
char msg_disk_usage[10];

// Definición del objeto de pantalla OLED
U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R2, OLED_SCL, OLED_SDA, U8X8_PIN_NONE);

// Objeto cliente WIFI
WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

// Función de devolución de llamada MQTT
void mqttCallback(char* topic, byte* payload, unsigned int length) {
  if (strcmp(topic, MQTT_TOPIC_CPU) == 0) {
    // Registrar el uso de CPU
    for (int i = 0; i < length; i++)
      msg_cpu_usage[i] = (char)payload[i];
  } else if (strcmp(topic, MQTT_TOPIC_MEM) == 0) {
    // Registrar el uso de memoria
    for (int i = 0; i < length; i++)
      msg_mem_usage[i] = (char)payload[i];
  } else if (strcmp(topic, MQTT_TOPIC_DISK) == 0) {
    // Registrar el uso de disco
    for (int i = 0; i < length; i++)
      msg_disk_usage[i] = (char)payload[i];
  }
}

void setup() {
  u8g2.begin();  // Inicializar la pantalla OLED
  Wire.begin();  // Iniciar la transmisión I2C

  // Conectar a WIFI
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }

  // Conectar al servidor proxy MQTT
  mqttClient.setServer(MQTT_BROKER, MQTT_PORT);
  mqttClient.setCallback(mqttCallback);
  if (mqttClient.connect("ESP32", MQTT_USERNAME, MQTT_PASSWORD)) {
    mqttClient.subscribe(MQTT_TOPIC_CPU);
    mqttClient.subscribe(MQTT_TOPIC_MEM);
    mqttClient.subscribe(MQTT_TOPIC_DISK);
  }
}

void loop() {
  mqttClient.loop();  // Procesar mensajes MQTT
  u8g2.firstPage();
  do {
    u8g2.setFont(u8g2_font_9x15_tf);

// Mostrar el uso de la CPU
u8g2.setCursor(0, 12);
u8g2.print("CPU: ");
for (int i = 0; i < 9; i++)
  u8g2.print(msg_cpu_usage[i]);
u8g2.print(" %");

// Mostrar el uso de la memoria
u8g2.setCursor(0, 35);
u8g2.print("Mem: ");
for (int i = 0; i < 9; i++)
  u8g2.print(msg_mem_usage[i]);
u8g2.print(" %");

// Mostrar el uso del disco
u8g2.setCursor(0, 58);
u8g2.print("Disk: ");
for (int i = 0; i < 9; i++)
  u8g2.print(msg_disk_usage[i]);
u8g2.print(" %");

} while (u8g2.nextPage());
}
```

## Más ideas de expansión

Las siguientes ideas están pendientes de implementación:

- Agregar batería y una carcasa de impresión 3D para crear un adorno de escritorio más refinado.
- Agregar un túnel de red interna para crear un adorno de pared que permita observar el estado del servidor incluso cuando no esté en casa.
- Empaquetar el programa de monitoreo de Python para su implementación en Docker.
- Optimizar el diseño de la interfaz de usuario para monitorear más parámetros.
- Agregar la capacidad de monitorear el estado de múltiples servidores.
- Agregar la capacidad de alertar cuando ciertos parámetros superen los umbrales.

Adjunto: Una foto de Beetle ESP32-C3 y Seeed XIAO ESP32C3 juntos.

![](https://f004.backblazeb2.com/file/wiki-media/img/202305261719170.jpg)

## Referencias y agradecimientos

- [DFRobot Wiki · Beetle ESP32 C3](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3)
- [Creación de un sistema de monitoreo de rendimiento de Raspberry Pi con Arduino y MQTT](https://www.zhihu.com/tardis/zm/art/463880669?source_id=1003)
- [eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto)
- [Docker - Tutorial de instalación y implementación del servicio Mosquitto a través de contenedores (servidor MQTT)](https://www.hangge.com/blog/cache/detail_2896.html)
- [Serie de tutoriales MQTT 3 (Instalación y uso de la herramienta de cliente MQTTBox)](https://www.hangge.com/blog/cache/detail_2350.html)
- [linyuxuanlin/TinyMonitor](https://github.com/linyuxuanlin/TinyMonitor)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.