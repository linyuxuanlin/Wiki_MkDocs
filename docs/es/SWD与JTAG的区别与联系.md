# Diferencias y Conexiones entre SWD y JTAG

Como es ampliamente conocido, SWD (Serial Wire Debug) y JTAG (Joint Test Action Group) son interfaces comunes utilizadas para la descarga de programas y la depuración en microcontroladores. Sus similitudes incluyen:

- **Rango de voltaje de alimentación**: 1.2 V - 5.5 V
- **Velocidad del reloj**: Configurable hasta 10 MHz
- **Seguimiento y captura de SWO**: Velocidad de datos de hasta 50 Mbit/s (modo UART/NRZ)
- **Aislamiento de voltaje**: 1 kV
- **Conexión en caliente**: Compatible

## JTAG

JTAG, cuyo nombre completo es Joint Test Action Group (Grupo de Acción de Prueba Conjunta), se basa en el estándar IEEE 1149.1-1990, el más reciente en el momento de redacción de este artículo.

Su topología, conocida como "cadena en serie", se presenta a continuación:

![JTAG Topología](https://media.wiki-power.com/img/20210209191921.png)

JTAG generalmente utiliza 5 pines:

- **TDI** (Test Data In): Pin de entrada en serie.
- **TDO** (Test Data Out): Pin de salida en serie.
- **TCK** (Test Clock): Pin de reloj, normalmente con una resistencia pull-down de 100k.
- **TMS** (Test Mode Select): Pin de selección de modo (señal de control).
- **TRST** (Test Reset): Pin de reinicio.

Ventajas de JTAG:

- No se limita a los chips de la serie ARM.
- Tiene una variedad de aplicaciones en programación, depuración y pruebas de producción.

## SWD

Serial Wire Debug (Depuración por Cable Serie), desarrollado específicamente por ARM, es compatible solo con microcontroladores ARM (por lo que tiene un rendimiento superior en dispositivos ARM).

SWD generalmente utiliza 2 pines:

- **SWDIO** (Serial Wire Data Input Output): Pin de entrada/salida de datos en serie.
- **SWCLK** (Serial Wire Clock): Pin de reloj en serie.

Ventajas de SWD:

- Utiliza menos pines, solo SWDIO y SWCLK.
- SWD tiene funciones especiales, como la impresión de información de depuración.
- En comparación con JTAG, SWD ofrece un rendimiento general superior en términos de velocidad.

## Compatibilidad entre JTAG y SWD

Por lo general, en una placa de microcontroladores, se encuentran ranuras de programación que son compatibles tanto con JTAG como con SWD:

![Compatibilidad JTAG y SWD](https://media.wiki-power.com/img/20210210122923.jpg)

![Compatibilidad JTAG y SWD](https://media.wiki-power.com/img/20210210123714.png)

- TCK es compatible con SWCLK.
- TMS es compatible con SWDIO.
- (TDO es compatible con SWO).

Razones para elegir SWD en lugar de JTAG:

- El diseño del esquema eléctrico debe ser lo suficientemente sencillo y permitir pruebas sin la funcionalidad JTAG.
- Las limitaciones de espacio en la PCB se pueden abordar de manera más eficiente con SWD.
- El microcontrolador ya no dispone de pines adicionales para JTAG.

## Referencias y Agradecimientos

- [Diferencias entre las interfaces de descarga y depuración SWD y JTAG](https://mp.weixin.qq.com/s/MW57t266yvv6TOweeFEUVA)
- [Compartir el Puerto de Depuración Cortex JTAG y SWD](https://southlife.tistory.com/107)
- [Interfaz JTAG/SWD](https://www.keil.com/support/man/docs/ulinkplus/ulinkplus_jtagswd_interface.htm)
- [JTAG](https://en.wikipedia.org/wiki/JTAG)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
