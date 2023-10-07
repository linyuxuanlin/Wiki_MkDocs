# T-Clock Reloj de escritorio

## Materiales necesarios

1. **NodeMCU**: basado en ESP8266
2. **OLED**: resolución de 128x64, interfaz I2C (para SPI, consulte el enlace de referencia)

## Conexiones

| OLED | NodeMCU |
| :--: | :-----: |
| GND  |   GND   |
| VCC  |  3.3V   |
| SCL  |   D1    |
| SDA  |   D2    |

## Ejemplo de código

### Configuración de la API

1. Regístrese en [**Seniverse**](https://www.seniverse.com/)
2. Agregue un nuevo producto en la consola (la versión gratuita es suficiente)
3. Copie la clave API privada

### Bibliotecas necesarias

- [**Adafruit_SSD1306.h**](https://github.com/adafruit/Adafruit_SSD1306)

### Ejemplo de código final

- [**T-Clock/Software/Codes/Weather_Clock_OLED_I2C**](https://github.com/linyuxuanlin/T-Clock/tree/master/Software/Codes/Weather_Clock_OLED_I2C)

Nota: debe cambiar el nombre y la contraseña de WiFi, la ciudad y la clave privada por los suyos.  
Si hay un error de compilación y el mensaje de error se encuentra en `#error("Height incorrect, please fix Adafruit_SSD1306.h!");`, debe abrir el archivo de biblioteca `Adafruit_SSD1306.h` y cambiar `#define SSD1306_128_32` por `#define SSD1306_128_64`.

Nota: ¡El proyecto de hardware personalizado está en camino!

## Referencias y agradecimientos

- [T-Clock Reloj de escritorio (antiguo)](https://wiki-power.com/es/unlist/T-Clock桌上小钟（旧）)
- [Seniverse](https://www.seniverse.com/)
- [Conexión de ESP8266 a la API de Seniverse (programa + explicación detallada)](https://www.bilibili.com/video/av89935868/?spm_id_from=333.788.b_636f6d6d656e74.4)
- [ESP8266 + OLED = Reloj de red y pronóstico del tiempo para los próximos 3 días](https://www.bilibili.com/video/av88920975/)
- [My_ESP8266/Seniverse](https://gitee.com/young_people_only_love_her/My_ESP8266/tree/master/%E5%BF%83%E7%9F%A5%E5%A4%A9%E6%B0%94)
- [Interfaz de pantalla gráfica OLED con NodeMCU](https://www.electronicwings.com/nodemcu/oled-graphic-display-interfacing-with-nodemcu)
- [adafruit/Adafruit_SSD1306](https://github.com/adafruit/Adafruit_SSD1306)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.