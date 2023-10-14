# Cómo hacer tu propio CMSIS-DAP 🚧

CMSIS DAP es un simulador de ARM de código abierto lanzado por ARM, que soporta todos los dispositivos Cortex-ARM y las interfaces JTAG / SWD. En la última versión del firmware, también soporta la interfaz SWO de una sola línea, que puede enviar los datos correspondientes directamente a la ventana de depuración a través de la interfaz SWO en el programa, lo que cumple con el propósito de la depuración de la serie de puertos. Las principales características de DAP son las siguientes:

1. Completamente de código abierto, sin restricciones de licencia, por lo que el precio correspondiente será muy barato.
2. Plug and play, no se requiere controlador.
3. La última versión de DAP integra un puerto serie, que puede utilizarse como un módulo de conversión USB a serie además de la descarga y la depuración, lo que permite su uso dual.
4. En cuanto al rendimiento, ya puede satisfacer las necesidades de los usuarios generales.

(No terminado)

Repositorio de GitHub: [**linyuxuanlin/DashDAP**](https://github.com/linyuxuanlin/DashDAP)

## Referencias y agradecimientos

- [x893/CMSIS-DAP](https://github.com/x893/CMSIS-DAP)
- [Introducción de DAP en el sitio web oficial de ARM](http://www.keil.com/pack/doc/cmsis/DAP/html/index.html)
- [El entusiasmo de los nerds electrónicos: simulador CMSIS DAP](http://www.stmcu.org.cn/module/forum/thread-610968-1-2.html)
- [Simulador CMSIS DAP](https://item.taobao.com/item.htm?spm=a1z10.1-c.w5003-21405148310.36.78726a3dta5ieC&id=550828063764&scene=taobao_shop)
- [konosubakonoakua/Various_MCU_Debugger_DIY](https://github.com/konosubakonoakua/Various_MCU_Debugger_DIY)

---

`Versión 2.0 en edición`

![](https://img.wiki-power.com/d/wiki-media/img/20200613154907.jpg)

Vista previa del proyecto en línea:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/DashDAP/raw/master/Hardware/DashDAP.zip"
  ></div>
</div>

## Contexto

CMSIS-DAP / DAP-Link tiene las siguientes ventajas en comparación con J-Link / ST-Link:

- Completamente de código abierto, sin riesgo legal.
- Soporta puerto serie virtual.
- Sin necesidad de controlador.
- DAPLink es CMSIS-DAP, que soporta la grabación de arrastrar y soltar / actualización de firmware.

## Parte de hardware

### MCU

#### Cristal

Se selecciona un cristal pasivo de Murata de 8 MHz, modelo CSTCE8M00G53-R0, encapsulado en 3213, con una capacidad de 15 pF. ¿Por qué se selecciona este? Es porque su tamaño es relativamente pequeño y integra dos capacitores de oscilación, lo que ahorra mucho trabajo en el diseño de hardware. En cuanto al método de nomenclatura del modelo de cristal de Murata, se puede consultar la siguiente tabla:

![](https://img.wiki-power.com/d/wiki-media/img/20200612143451.jpg)

### Fuente de alimentación

### Módulo de función

## Parte de software

### Controlador

No es necesario instalar el controlador en Win10 / MacOS / Linux; se necesita instalar el controlador manualmente en Win8 y sistemas más antiguos.

### Grabación de arrastrar y soltar (MSC)

Simplemente arrastre y suelte el archivo `.hex` o `.bin` compilado en la unidad flash virtual de DAPLink para grabar. Si se produce un error, la información del error se almacenará en `FAIL.txt`.

### Puerto serie virtual (CDC)

La función del puerto serie virtual CDC tiene funciones generales de puerto serie, permite la comunicación bidireccional y permite enviar comandos de interrupción para restablecer la placa objetivo.

## Referencias y agradecimientos

- [Diferencias en el uso de JLink, STLink, DAPLink y CMSIS DAP](https://blog.csdn.net/zhouml_msn/article/details/105298776)
- [Tecnología nueva · Simulador DAPLink](https://www.jixin.pro/bbs/topic/4187)
- [wuxx / nanoDAP](https://github.com/wuxx/nanoDAP)
- [LGG001 / Folleto DAPLink](https://github.com/LGG001/DAPLink-Brochure)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
