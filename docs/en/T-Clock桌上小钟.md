# T-Clock Desktop Clock

## Preparation

1. **NodeMCU**: Based on ESP8266
2. **OLED**: 128x64 resolution, I2C interface (for SPI, please refer to the reference link)

## Wiring

| OLED | NodeMCU |
| :--: | :-----: |
| GND  |   GND   |
| VCC  |  3.3V   |
| SCL  |   D1    |
| SDA  |   D2    |

## Example

### API Configuration

1. Register an account on [**Seniverse**](https://www.seniverse.com/)
2. Add a new product in the console (choose the free version)
3. Copy the API key

### Library Files

- [**Adafruit_SSD1306.h**](https://github.com/adafruit/Adafruit_SSD1306)

### Final Example

- [**T-Clock/Software/Codes/Weather_Clock_OLED_I2C**](https://github.com/linyuxuanlin/T-Clock/tree/master/Software/Codes/Weather_Clock_OLED_I2C)

Note: You need to change the WiFi name and password, city, and API key to your own.  
If you encounter an error during compilation and the error message points to `#error("Height incorrect, please fix Adafruit_SSD1306.h!");`, you need to open the library file `Adafruit_SSD1306.h` and change `#define SSD1306_128_32` to `#define SSD1306_128_64`.

Note: Custom hardware projects are on the way~

## References and Acknowledgements

- [T-Clock Desktop Clock (Old)](https://wiki-power.com/unlist/T-Clock桌上小钟（旧）)
- [Seniverse](https://www.seniverse.com/)
- [ESP8266 Access to Seniverse API [Program + Detailed Explanation]](https://www.bilibili.com/video/av89935868/?spm_id_from=333.788.b_636f6d6d656e74.4)
- [ESP8266 + OLED = Network Clock and 3-day Weather Forecast](https://www.bilibili.com/video/av88920975/)
- [My_ESP8266/Seniverse](https://gitee.com/young_people_only_love_her/My_ESP8266/tree/master/%E5%BF%83%E7%9F%A5%E5%A4%A9%E6%B0%94)
- [OLED Graphic Display Interfacing with NodeMCU](https://www.electronicwings.com/nodemcu/oled-graphic-display-interfacing-with-nodemcu)
- [adafruit/Adafruit_SSD1306](https://github.com/adafruit/Adafruit_SSD1306)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.