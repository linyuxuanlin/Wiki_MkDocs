# TinyMonitor - Un Monitor de Estado de Servidor Compacto

![](https://media.wiki-power.com/img/202305261716469.jpg)

TinyMonitor es una terminal de monitoreo de estado de servidor extremadamente compacta y sencilla. Consiste únicamente en un controlador principal ESP32 y una pantalla OLED, con la capacidad de mostrar los parámetros de estado en tiempo real del servidor para facilitar la observación y la depuración.

## Preparativos Iniciales

Los materiales de hardware necesarios para este proyecto son muy simples: un Beetle ESP32-C3 con Wi-Fi y Bluetooth incorporados, y una pantalla OLED de 128x64 píxeles.

![](https://media.wiki-power.com/img/202305261541993.png)

A continuación, se detallan las definiciones de los pines para el Beetle ESP32-C3.

![](https://media.wiki-power.com/img/202305261545236.png)

Dado que es posible utilizar una interfaz I2C de software (es decir, personalizar los pines I2C), he definido los pines `0`/`1` del Beetle ESP32-C3 para que cumplan la función de `SCL`/`SDA`. Esto simplifica la conexión, ya que solo es necesario soldar cuatro pines uno junto al otro.

![](https://media.wiki-power.com/img/202305261546367.png)

Nota: Antes de cargar el programa en el Beetle ESP32-C3, es necesario agregar el paquete de ESP32 para que el modelo de la placa se reconozca correctamente. Consulta su [**página de Wiki**](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3) para obtener más detalles.

### Encender la Pantalla

Puedes usar este sencillo programa para comprobar si la información se muestra correctamente en la pantalla OLED:

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
  u8g2.drawStr(0,10,"¡Hola Mundo!");
  u8g2.sendBuffer();
  delay(1000);
}
```

## Servicio de Agente MQTT

MQTT es un protocolo de transporte de mensajes basado en el modelo cliente-servidor y publicación/suscripción. En este proyecto, MQTT actúa como puente de comunicación entre el servidor y el ESP32. Para mayor comodidad, he desplegado el servicio MQTT en el servidor que se va a monitorear, aunque también es posible desplegarlo en otras máquinas si es necesario.

### Despliegue del Servicio Mosquitto

Mosquitto es un software de agente de mensajes de código abierto que implementa el protocolo MQTT v3.1. En este caso, he desplegado [**eclipse-mosquitto**](https://hub.docker.com/_/eclipse-mosquitto) como servidor de agente MQTT utilizando Docker. Si no estás familiarizado con el despliegue mediante Docker, puedes consultar los artículos [**Guía Básica de Docker**](https://wiki-power.com/Docker%E7%AE%80%E6%98%93%E6%8C%87%E5%8D%97/) y [**Docker Compose: Una Forma más Elegante de Comenzar**](https://wiki-power.com/DockerCompose-%E6%9B%B4%E4%BC%98%E9%9B%85%E7%9A%84%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F/) para obtener más información.

De acuerdo con las instrucciones oficiales, primero debes crear los siguientes directorios y archivos para que Mosquitto los utilice, y otorgarles los permisos adecuados: (asegúrate de reemplazar `${STACK_DIR}` con la ruta local donde deseas almacenar los datos, por ejemplo, `/DATA/AppData/mosquitto`, como se muestra a continuación)

```bash
mkdir -vp ${STACK_DIR}/{config,data,log} \
&& touch ${STACK_DIR}/config/mosquitto.conf \
&& chmod -R 755 ${STACK_DIR} \
&& chmod -R 777 ${STACK_DIR}/log \
```

A continuación, en el archivo `mosquitto.conf`, debes agregar el siguiente contenido:

```conf title="mosquitto.conf"
persistence true
persistence_location /mosquitto/data
log_dest file /mosquitto/log/mosquitto.log

# Desactivar el modo anónimo
allow_anonymous false
# Especificar el archivo de contraseñas
password_file /mosquitto/config/pwfile.conf
```

Luego, implementa el contenedor utilizando `docker-compose`:

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

Ingresa al contenedor y modifica la contraseña:

```bash
cd ruta donde se encuentra compose.yaml
docker compose up

docker compose ps # Encuentra la ID del contenedor en ejecución
docker exec -it ID_del_contenedor sh # Ingresa al shell del contenedor

touch /mosquitto/config/pwfile.conf
chmod -R 755 /mosquitto/config/pwfile.conf

# Crea un usuario y contraseña, usuario: test, contraseña: 123
mosquitto_passwd -b /mosquitto/config/pwfile.conf test 123

exit # Sal del shell del contenedor
docker restart ID_del_contenedor # Reinicia el contenedor para que los cambios surtan efecto
```

### Prueba de disponibilidad del servidor MQTT

Una vez que hayas iniciado el servicio `mosquitto` correctamente, puedes utilizar [**MQTTBox**](https://apps.microsoft.com/store/detail/mqttbox/9NBLGGH55JZG) para probar la disponibilidad del servidor MQTT.

Después de instalar el software, crea una nueva conexión haciendo clic en "Create MQTT Client" y completa los parámetros según se muestra a continuación:

![imagen](https://media.wiki-power.com/img/202305261456592.png)

En este caso, `HOST` corresponde a la dirección del servidor MQTT (por ejemplo, si tu servidor se encuentra en una dirección de la red local, podría ser `192.168.1.2`); el nombre de usuario y la contraseña deben coincidir con los valores que configuraste anteriormente en Mosquitto.

Haz clic en "Save" para guardar la configuración. Si ves "Connected" en verde en la barra de estado, significa que te has conectado al servidor con éxito.

## Script de Monitoreo del Servidor

````markdown
Podemos capturar información en tiempo real de un dispositivo y enviarla a los temas correspondientes en un servidor MQTT ejecutando el siguiente programa en Python en el servidor. Primero, debe instalar las dependencias necesarias:

```bash
pip install paho-mqtt psutil
```
````

Luego, cree y ejecute el programa en Python:

```python title="status-collector.py"
import paho.mqtt.client as mqtt
import psutil
import time

# Conéctese al servidor MQTT
cliente = mqtt.Client()
cliente.username_pw_set("Nombre_de_usuario_MQTT", "Contraseña_MQTT")
cliente.connect("Dirección_del_servidor_MQTT", Puerto)
# Ejemplo: cliente.connect("192.168.1.2", 1883)

# Recopile el estado del servidor y envíelo a los temas MQTT
while True:
    cliente.publish("USO_CPU", psutil.cpu_percent())
    cliente.publish("USO_MEM", psutil.virtual_memory().percent)
    cliente.publish("USO_DISCO", psutil.disk_usage('/').percent)
    time.sleep(1) # Publique cada segundo
```

Después de ejecutar con éxito este programa, puede agregar suscripciones a estos tres temas en MQTTBox desde la barra de estado en la parte superior, como se muestra a continuación:

![Ejemplo](https://media.wiki-power.com/img/202305261513642.png)

Si todo está configurado correctamente, debería ver información continua sobre el estado del servidor en MQTTBox.

## Pantalla Arduino ESP32

Cree el siguiente código en Arduino, ajuste los parámetros según sea necesario y cárguelo en su ESP32. Si todo está configurado correctamente, debería ver información actualizada constantemente.

```cpp title="Recibir desde MQTT y Mostrar en OLED.ino"
#include <Wire.h>
#include <U8g2lib.h>
#include <WiFi.h>
#include <PubSubClient.h>

// Conexión del OLED mediante I2C, defina los pines nuevamente si es necesario
#define OLED_SDA 1
#define OLED_SCL 0

// Definiciones MQTT
#define WIFI_SSID "Nombre_de_la_red_Wi-Fi"
#define WIFI_PASSWORD "Contraseña_de_Wi-Fi"
#define MQTT_BROKER "Dirección_del_servidor_MQTT" // Por ejemplo, 192.168.31.2
#define MQTT_PORT Puerto_de_MQTT // Por ejemplo, 1883
#define MQTT_USERNAME "Nombre_de_usuario_MQTT" // Debe coincidir con la configuración anterior
#define MQTT_PASSWORD "Contraseña_de_MQTT" // Debe coincidir con la configuración anterior
#define MQTT_TOPIC_CPU "USO_CPU" // Tema al que está suscrito
#define MQTT_TOPIC_MEM "USO_MEM"
#define MQTT_TOPIC_DISK "USO_DISCO"

char msg_cpu_usage[10];
char msg_mem_usage[10];
char msg_disk_usage[10];

// Objeto de pantalla OLED
U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R2, OLED_SCL, OLED_SDA, U8X8_PIN_NONE);

// Objeto cliente Wi-Fi
WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);
```

```cpp
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
  Wire.begin();  // Iniciar la comunicación I2C

  // Conectar a la red WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }

  // Conectar al servidor MQTT
  mqttClient.setServer(MQTT_BROKER, MQTT_PORT);
  mqttClient.setCallback(mqttCallback);
  if (mqttClient.connect("ESP32", MQTT_USERNAME, MQTT_PASSWORD)) {
    mqttClient.subscribe(MQTT_TOPIC_CPU);
    mqttClient.subscribe(MQTT_TOPIC_MEM);
    mqttClient.subscribe(MQTT_TOPIC_DISK);
  }
}

void loop() {
  mqttClient.loop();  // Procesar los mensajes MQTT
  u8g2.firstPage();
  do {
    u8g2.setFont(u8g2_font_9x15_tf);

    // Mostrar el uso de CPU
    u8g2.setCursor(0, 12);
    u8g2.print("CPU: ");
    for (int i = 0; i < 9; i++)
      u8g2.print(msg_cpu_usage[i]);
    u8g2.print(" %");

    // Mostrar el uso de memoria
    u8g2.setCursor(0, 35);
    u8g2.print("Mem: ");
    for (int i = 0; i < 9; i++)
      u8g2.print(msg_mem_usage[i]);
    u8g2.print(" %");

    // Mostrar el uso de disco
    u8g2.setCursor(0, 58);
    u8g2.print("Disco: ");
    for (int i = 0; i < 9; i++)
      u8g2.print(msg_disk_usage[i]);
    u8g2.print(" %");

  } while (u8g2.nextPage());
}
```

## Ideas para expansiones adicionales

Las siguientes ideas están pendientes de implementación:

```cpp
// Agregar una función de registro de datos para almacenar las métricas en una base de datos.
// Implementar la capacidad de enviar notificaciones por correo electrónico o mensajes SMS cuando se superen ciertos umbrales de uso.
// Crear una interfaz de usuario web para monitorear y controlar el dispositivo de forma remota.
// Agregar una función de gráficos para mostrar tendencias de uso a lo largo del tiempo.
// Implementar un mecanismo de seguridad para proteger la información sensible transmitida a través de MQTT.
```

Estas sugerencias pueden enriquecer aún más la funcionalidad de tu proyecto.

- Añadir una carcasa mejorada con batería y tecnología de impresión 3D para crear adornos de escritorio más refinados.
- Implementar la funcionalidad de penetración en la red interna y convertirlo en un colgante, permitiendo la observación del estado del servidor incluso cuando no esté en casa.
- Empaquetar el programa de monitoreo en Python en un contenedor Docker para su implementación.
- Mejorar el diseño de la interfaz de usuario para permitir un mayor monitoreo de parámetros.
- Incorporar la capacidad de monitorear el estado de múltiples servidores.
- Agregar una función de alerta para parámetros que excedan los umbrales especificados.

Adjunto: Fotografía conjunta de Beetle ESP32-C3 y Seeed XIAO ESP32C3.

![Imagen](https://media.wiki-power.com/img/202305261719170.jpg)

## Referencias y Agradecimientos

- [DFRobot Wiki · Beetle ESP32 C3](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3)
- [Creación de un sistema de monitoreo de rendimiento de Raspberry Pi con Arduino y MQTT](https://www.zhihu.com/tardis/zm/art/463880669?source_id=1003)
- [eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto)
- [Docker - Tutorial de instalación y despliegue del servicio Mosquitto a través de contenedores (Servidor MQTT)](https://www.hangge.com/blog/cache/detail_2896.html)
- [Serie de tutoriales sobre MQTT 3 (Instalación y uso de la herramienta cliente MQTTBox)](https://www.hangge.com/blog/cache/detail_2350.html)
- [linyuxuanlin/TinyMonitor](https://github.com/linyuxuanlin/TinyMonitor)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
