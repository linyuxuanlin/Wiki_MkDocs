# Notas de desarrollo de la biblioteca HAL - Configuración del entorno

Nota: Este tutorial se basa en la placa STM32F429IGT6 de Reverse Costumer.

## Instalación de software

### Keil MDK

Consulte el artículo [**Guía de configuración de Keil MDK**](https://wiki-power.com/es/KeilMDK%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97) para obtener más información.

### Java Runtime Environment

Este es el entorno Java necesario para STM32CubeMX. Descárguelo e instálelo desde el [**enlace oficial**](https://www.java.com/en/download/).

### STM32CubeMX

Descargue e instale STM32CubeMX desde el [**enlace oficial**](https://my.st.com/content/my_st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.license=1611899126599.product=STM32CubeMX.version=6.1.1.html).

## Configuración del proyecto

### Inicialización

Cree un nuevo proyecto y guarde después de seleccionar el chip.

### Configuración SYS

`Pinout & Configurations` - `System Core` - `SYS`

Cambie la opción `Debug` a `Serial Wire` (consulte el artículo [**Evite problemas con CubeMX y CubeIDE**](https://wiki-power.com/es/CubeMX与CubeIDE避坑) para obtener más información).

### Configuración RCC

`Pinout & Configurations` - `System Core` - `RCC`

Configure según la placa.

Por ejemplo, consulte el esquemático de la placa:

![](https://img.wiki-power.com/d/wiki-media/img/20210205205030.png)

Configure las opciones `HSE` y `LSE` como cristales externos:

![](https://img.wiki-power.com/d/wiki-media/img/20210205205140.png)

### Configuración del árbol de reloj

Configure en la interfaz `Clock Configuration`.

![](https://img.wiki-power.com/d/wiki-media/img/20210205205550.png)

Siga los pasos de la imagen anterior:

1. Ingrese los valores de las dos frecuencias más a la izquierda según los parámetros del cristal externo de la placa.
2. Seleccione `HSE`, ya que la frecuencia y precisión del cristal externo son mayores que las del interno.
3. Seleccione `PLLCLK` para obtener una frecuencia alta mediante multiplicación de fase de bucle cerrado (PLL).
4. Ingrese el valor de `HCKL`, generalmente según la frecuencia máxima indicada en la parte inferior, y presione Enter para calcular automáticamente la frecuencia de división y multiplicación.

### Configuración de opciones de gestión de proyectos

![](https://img.wiki-power.com/d/wiki-media/img/20210130095224.png)

![](https://img.wiki-power.com/d/wiki-media/img/20210130095239.png)

## Diferencias entre la biblioteca HAL y la biblioteca estándar

Para aumentar la portabilidad, la biblioteca HAL tiene tres funciones adicionales en comparación con la biblioteca estándar: **manejador, funciones MSP y funciones de devolución de llamada**. Consulte el contenido en los enlaces de referencia al final del artículo para obtener más información.

## Referencias y agradecimientos

- [【STM32】Explicación detallada del RCC del reloj del sistema](https://blog.csdn.net/as480133937/article/details/98845509)
- [Inicialización de la placa, configuración completa y detallada del árbol de reloj RCC](https://www.notion.so/2-RCC-770c0c454f954408a3956257aa0fb523)
- [Resumen completo del conocimiento de STM32 HAL](https://mp.weixin.qq.com/s/ffcjKtl7JdRibLRNGquGXA)
- [Resumen claro del conocimiento completo de STM32 HAL](https://mp.weixin.qq.com/s/qkj0fQS5NrCXmbppKEhaAg)

a_reemplazar[1]  
a_reemplazar[2]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
