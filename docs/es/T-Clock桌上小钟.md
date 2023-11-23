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
2. Agregue un nuevo producto en la consola (puede elegir la versión gratuita)
3. Copie la clave de la API

### Bibliotecas necesarias

- [**Adafruit_SSD1306.h**](https://github.com/adafruit/Adafruit_SSD1306)

### Ejemplo final

- [**T-Clock/Software/Codes/Weather_Clock_OLED_I2C**](https://github.com/linyuxuanlin/T-Clock/tree/master/Software/Codes/Weather_Clock_OLED_I2C)

Nota: Asegúrese de cambiar el nombre y la contraseña de WiFi, la ciudad y la clave de la API por los suyos propios.  
Si encuentra un error de compilación que se encuentra en `#error("Height incorrect, please fix Adafruit_SSD1306.h!");`, abra el archivo de la biblioteca `Adafruit_SSD1306.h` y cambie `#define SSD1306_128_32` a `#define SSD1306_128_64`.

Nota: ¡El proyecto de hardware personalizado está en camino!

## Referencias y agradecimientos

- [T-Clock Reloj de escritorio (antiguo)](https://wiki-power.com/unlist/T-Clock桌上小钟（旧）)
- [Seniverse](https://www.seniverse.com/)
- [ESP8266 accede a la API de Seniverse【Programa + Explicación detallada】](https://www.bilibili.com/video/av89935868/?spm_id_from=333.788.b_636f6d6d656e74.4)
- [ESP8266 + OLED = Reloj de red y pronóstico del tiempo de los próximos 3 días](https://www.bilibili.com/video/av88920975/)
- [My_ESP8266/Seniverse](https://gitee.com/young_people_only_love_her/My_ESP8266/tree/master/%E5%BF%83%E7%9F%A5%E5%A4%A9%E6%B0%94)
- [Interfaz de pantalla gráfica OLED con NodeMCU](https://www.electronicwings.com/nodemcu/oled-graphic-display-interfacing-with-nodemcu)
- [adafruit/Adafruit_SSD1306](https://github.com/adafruit/Adafruit_SSD1306)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.