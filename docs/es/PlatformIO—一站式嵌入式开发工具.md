# PlatformIO: Una Herramienta de Desarrollo Integrado Todo en Uno

— Creando un entorno de desarrollo integral para reemplazar Keil / Arduino IDE

![Imagen](https://media.wiki-power.com/img/20200531112801.png)

## Antecedentes

PlatformIO es una poderosa herramienta integral que presenta las siguientes características:

- Plataforma cruzada, solo requiere un entorno Python (lo que significa que se puede utilizar en Windows, MacOS y Linux).
- Puede instalarse como un complemento dentro de Visual Studio Code (finalmente, puedes decir adiós a Keil).
- Un ecosistema robusto que incluye:
  - [**Más de 800 placas de desarrollo comunes**](https://docs.platformio.org/en/latest/boards/index.html#boards): prácticamente todas las placas de desarrollo que puedas encontrar están disponibles aquí.
  - [**Más de 35 plataformas de desarrollo**](https://docs.platformio.org/en/latest/platforms/index.html#platforms): abarca Atmel AVR (Arduino), ESP, NXP, 8051, PIC32, FPGA, FreeRTOS, ARM (STM32) y mucho más.
  - [**Más de 20 marcos de trabajo**](https://docs.platformio.org/en/latest/frameworks/index.html#frameworks): incluye Arduino, CMSIS, STM32Cube y otros.
- Ofrece funciones de compilación, descarga, depuración y monitorización de puerto serie, y es compatible con una variedad de compiladores y depuradores.
- Proporciona una amplia variedad de bibliotecas de funciones.
- Ofrece autocompletado de código, verificación de sintaxis, gestión de múltiples proyectos y opciones de personalización de temas.
- Funcionalidad de desarrollo remoto (no probada).
- Pruebas unitarias (no probadas).
- Disponible en entorno de línea de comandos y entorno gráfico de usuario.

En resumen, es hora de dejar atrás diversas IDEs como Arduino IDE, Keil o IAR, y disfrutar de un enfoque integral.

## Descarga e Instalación

En primer lugar, asegúrate de tener instalado Visual Studio Code en tu computadora (puedes consultar [**este artículo**](https://wiki-power.com/VSCode生产力指南-环境配置) para obtener instrucciones de descarga e instalación).

Dentro de Visual Studio Code, ve a la sección de `Extensiones` (puedes hacerlo presionando `Ctrl + Shift + X`) y busca e instala las extensiones `Python` y `PlatformIO IDE`.

![Imagen](https://media.wiki-power.com/img/20200531113916.png)

Una vez que las extensiones se instalen con éxito, haz clic en `Recargar` para activarlas y luego toma una taza de café mientras se instalan automáticamente los componentes centrales de PlatformIO (esto puede llevar algo de tiempo la primera vez).

Una vez finalizada la instalación, puedes iniciar PlatformIO haciendo clic en los botones relacionados en la barra lateral.

## Referencias y Agradecimientos

- [PlatformIO](https://platformio.org/)
- [Documentación de PlatformIO](https://docs.platformio.org/en/latest/index.html)
- [ussserrr/stm32pio](https://github.com/ussserrr/stm32pio#requirements)
- [Usar Visual Studio Code como Plataforma de Desarrollo STM32 (PlatformIO)](https://www.jianshu.com/p/49cfa03d6164)
- [PlatformIO IDE (Visual Studio Code) - Proyecto con el marco de trabajo STM32Cube](https://www.smslit.top/2019/08/24/platformio-stm32-cubemx/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
