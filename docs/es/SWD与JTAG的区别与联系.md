# Diferencias y similitudes entre SWD y JTAG

Es bien sabido que SWD y JTAG son interfaces comunes para la descarga de programas y la depuración de microcontroladores. Sus similitudes son:

- **Rango de voltaje de alimentación**: 1.2 V - 5.5 V
- **Velocidad de reloj**: configurable hasta 10 MHz
- **Captura de seguimiento SWO**: velocidad de datos de hasta 50 Mbit/s (modo UART/NRZ)
- **Voltaje de aislamiento**: 1 kV
- **Conexión en caliente**: compatible

## JTAG

JTAG, cuyo nombre completo es Joint Test Action Group (Grupo de Acción Conjunta de Pruebas). El estándar más reciente hasta la fecha de este artículo es el IEEE Standard 1149.1-1990.

Su diagrama de topología (cadena de margaritas) es el siguiente:

![](https://img.wiki-power.com/d/wiki-media/img/20210209191921.png)

JTAG generalmente utiliza 5 pines:

- **TDI** (Test Data In): pin de entrada serial
- **TDO** (Test Data Out): pin de salida serial
- **TCK** (Test Clock): pin de reloj, generalmente con una resistencia de pull-down de 100k
- **TMS** (Test Mode Select): pin de selección de modo (señal de control)
- **TRST** (Test Reset): pin de reinicio

Las ventajas de JTAG son:

- No se limita a chips de la serie ARM
- Tiene más usos para programación, depuración y pruebas de producción

## SWD

El nombre completo es Serial Wire Debug (Depuración de Cable Serie), es un protocolo diseñado específicamente por ARM y solo es compatible con ARM (por lo que tiene un mejor rendimiento en microcontroladores de la serie ARM).

SWD generalmente utiliza 2 pines:

- **SWDIO** (Serial Wire Data Input Output): pin de entrada/salida de datos serial
- **SWCLK** (Serial Wire Clock): pin de reloj de cable serie

Las ventajas de SWD son:

- Utiliza menos pines, solo necesita 2 pines: SWDIO y SWCLK
- SWD tiene funciones especiales, como la impresión de información de depuración
- En comparación con JTAG, SWD tiene un mejor rendimiento general en velocidad

## Compatibilidad entre JTAG y SWD

Por lo general, las placas de microcontroladores tienen estos zócalos de grabación que son compatibles con JTAG y SWD al mismo tiempo:

![](https://img.wiki-power.com/d/wiki-media/img/20210210122923.jpg)

![](https://img.wiki-power.com/d/wiki-media/img/20210210123714.png)

- TCK es compatible con SWCLK
- TMS es compatible con SWDIO
- (TDO es compatible con SWO)

Razones para elegir SWD en lugar de JTAG:

- El diseño del esquemático del circuito debe ser lo suficientemente simple y se puede probar sin la función JTAG
- El PCB tiene limitaciones de tamaño y SWD puede ahorrar espacio
- El MCU ya no tiene pines adicionales para JTAG

## Referencias y agradecimientos

- [Diferencias entre la interfaz de descarga y depuración SWD y JTAG](https://mp.weixin.qq.com/s/MW57t266yvv6TOweeFEUVA)
- [Compartir el puerto de depuración Cortex JTAG, SWD](https://southlife.tistory.com/107)
- [Interfaz JTAG/SWD](https://www.keil.com/support/man/docs/ulinkplus/ulinkplus_jtagswd_interface.htm)
- [JTAG](https://en.wikipedia.org/wiki/JTAG)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
