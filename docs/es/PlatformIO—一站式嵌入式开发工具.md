# PlatformIO - Herramienta de desarrollo integrado para sistemas embebidos

- Construye un entorno de desarrollo integrado para reemplazar Keil / Arduino IDE

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200531112801.png)

## Contexto

PlatformIO es una herramienta poderosa de desarrollo integrado que cuenta con las siguientes características:

- Multiplataforma, solo requiere un entorno Python (lo que significa que se puede utilizar en Windows/MacOS/Linux)
- Se puede instalar como un complemento dentro de VSCode (finalmente se puede abandonar Keil)
- Ecosistema poderoso:
  - [**800+ placas de desarrollo comunes**](https://docs.platformio.org/en/latest/boards/index.html#boards): casi todas las placas de desarrollo comunes que se pueden comprar están disponibles aquí
  - [**35+ plataformas de desarrollo**](https://docs.platformio.org/en/latest/platforms/index.html#platforms): cubre Atmel AVR (Arduino) / ESP / NXP / 8051 / PIC32 / FPGA / FreeRTOS / ARM (STM32) y muchas más
  - [**20+ frameworks**](https://docs.platformio.org/en/latest/frameworks/index.html#frameworks): Arduino / CMSIS / STM32Cube y muchos más
- Funciones de compilación / descarga / depuración / monitor de puerto serie, y soporte para varios compiladores / depuradores
- Proporciona una variedad de bibliotecas de funciones
- Autocompletado de código, verificación de sintaxis, gestión de múltiples proyectos, adaptación de temas
- Función de desarrollo remoto (no probada)
- Pruebas unitarias (no probadas)
- Disponible en línea de comandos y en entorno gráfico

En resumen, es hora de abandonar los diferentes IDE (como Arduino IDE / Keil / IAR) y disfrutar de un servicio integral.

## Descarga e instalación

Primero, asegúrate de tener VSCode instalado en tu computadora (la descarga e instalación de VSCode se puede encontrar en [**este artículo**](https://wiki-power.com/VSCode生产力指南-环境配置))

Busca e instala `Python` y `PlatformIO IDE` en la sección de `Extensiones` (`Ctrl + Shift + X`).

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200531113916.png)

Una vez que se haya instalado el complemento, haz clic en `Recargar` para iniciar el complemento, luego haz una taza de café mientras se instala automáticamente el componente principal `platformIO-core` (la instalación inicial puede tardar un poco).

Una vez que se complete la instalación, haz clic en el botón correspondiente en la barra lateral para iniciar PlatformIO.

## Referencias y agradecimientos

- [PlatformIO](https://platformio.org/)
- [PlatformIO Docs](https://docs.platformio.org/en/latest/index.html)
- [ussserrr/stm32pio](https://github.com/ussserrr/stm32pio#requirements)
- [Usar VS Code como plataforma de desarrollo STM32 (platformIO)](https://www.jianshu.com/p/49cfa03d6164)
- [PlatformIO IDE (VSCode) - Proyecto con marco STM32Cube](https://www.smslit.top/2019/08/24/platformio-stm32-cubemx/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.