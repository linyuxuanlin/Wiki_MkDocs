# DIY CMSIS-DAP 🚧

CMSIS DAP es un simulador de código abierto lanzado por ARM que es compatible con todos los dispositivos Cortex-ARM y admite interfaces JTAG/SWD. En la última versión del firmware, también admite la interfaz SWO de un solo cable, lo que permite que los datos correspondientes se envíen directamente desde el programa a la ventana de depuración a través de la interfaz SWO, lo que cumple una función similar a la depuración por puerto serie. Las principales características de DAP son las siguientes:

1. Es completamente de código abierto y no tiene restricciones de licencia, por lo que el precio correspondiente es muy económico.
2. No requiere controladores, se puede usar de forma plug-and-play.
3. En las versiones más recientes de DAP se ha integrado un puerto serie, por lo que además de la depuración y descarga, también puede funcionar como un módulo USB a serie, lo que le da una doble utilidad.
4. En cuanto al rendimiento, ya puede satisfacer las necesidades de los usuarios en general.

(En proceso)

Repositorio en GitHub: [**linyuxuanlin/DashDAP**](https://github.com/linyuxuanlin/DashDAP)

## Referencias y agradecimientos

- [x893/CMSIS-DAP](https://github.com/x893/CMSIS-DAP)
- [Introducción a DAP en el sitio web oficial de ARM](http://www.keil.com/pack/doc/cmsis/DAP/html/index.html)
- [El encanto de un friki electrónico: el simulador CMSIS-DAP](http://www.stmcu.org.cn/module/forum/thread-610968-1-2.html)
- [Simulador CMSIS-DAP](https://item.taobao.com/item.htm?spm=a1z10.1-c.w5003-21405148310.36.78726a3dta5ieC&id=550828063764&scene=taobao_shop)
- [konosubakonoakua/Various_MCU_Debugger_DIY](https://github.com/konosubakonoakua/Various_MCU_Debugger_DIY)

---

Edición de la versión 2.0

![](https://media.wiki-power.com/img/20200613154907.jpg)

Vista previa del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/DashDAP/raw/master/Hardware/DashDAP.zip"
  ></div>
</div>

## Contexto

CMSIS-DAP / DAP-Link tiene las siguientes ventajas en comparación con J-Link / ST-Link:

- Es completamente de código abierto, por lo que no hay riesgo legal.
- Admite puertos serie virtuales.
- No requiere controladores.
- DAPLink es CMSIS-DAP y admite la grabación mediante arrastrar y soltar en una unidad USB / actualización de firmware.

## Parte de hardware

### MCU

#### Oscilador

Se utiliza un oscilador pasivo Murata de 8 MHz, modelo CSTCE8M00G53-R0, encapsulado en 3213, con una capacidad de 15 pF. ¿Por qué se eligió este oscilador? Porque tiene un tamaño relativamente pequeño y los dos condensadores de oscilación están integrados en él, lo que simplifica mucho el diseño de hardware. En cuanto a la forma de nombrar los modelos de osciladores de Murata, se puede consultar la siguiente tabla:

![](https://media.wiki-power.com/img/20200612143451.jpg)

### Fuente de alimentación

### Módulos de funciones

## Parte de software

### Controladores

No es necesario instalar manualmente los controladores en Win10 / MacOS / Linux; en Windows 8 y versiones anteriores, es necesario instalar los controladores manualmente.

### Descarga mediante arrastrar y soltar (MSC)

Simplemente arrastre el archivo `.hex` o `.bin` generado por la compilación al disco virtual de DAPLink para realizar la grabación. Si se produce un error, la información del error se guardará en `FAIL.txt`.

### Puerto serie virtual (CDC)

La función del puerto serie virtual (CDC) tiene las mismas características que un puerto serie normal, permite la comunicación bidireccional y permite enviar comandos de interrupción para restablecer la placa objetivo.

## Referencias y agradecimientos

- [Diferencias en el uso de JLink, STLink, DAPLink y CMSIS DAP](https://blog.csdn.net/zhouml_msn/article/details/105298776)
- [Jixin · Simulador DAPLink](https://www.jixin.pro/bbs/topic/4187)
- [wuxx / nanoDAP](https://github.com/wuxx/nanoDAP)
- [LGG001 / Folleto DAPLink](https://github.com/LGG001/DAPLink-Brochure)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
