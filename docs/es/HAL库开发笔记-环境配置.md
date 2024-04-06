# Notas de desarrollo de la biblioteca HAL - Configuración del entorno

Nota: Este tutorial se basa en la placa STM32F429IGT6 de REKA.

## Instalación de software

### Keil MDK

Ver el artículo [**Guía de configuración de Keil MDK**](https://wiki-power.com/KeilMDK%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97)

### Entorno de ejecución de Java

Esto es necesario para STM32CubeMX. Puede descargarlo e instalarlo desde el [**enlace oficial**](https://www.java.com/en/download/).

### STM32CubeMX

Descargue e instale STM32CubeMX desde el [**enlace oficial**](https://my.st.com/content/my_st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.license=1611899126599.product=STM32CubeMX.version=6.1.1.html).

## Configuración del proyecto

### Inicialización

Cree un nuevo proyecto y, después de seleccionar el microcontrolador, guárdelo.

### Configuración de SYS

`Pinout & Configurations` - `System Core` - `SYS`

Cambie la opción `Debug` a `Serial Wire` (consulte el artículo [**Consejos para CubeMX y CubeIDE**](https://wiki-power.com/CubeMX与CubeIDE避坑) para obtener más detalles).

### Configuración de RCC

`Pinout & Configurations` - `System Core` - `RCC`

Configure según las especificaciones de la placa.

Por ejemplo, siga el esquema de la placa:

![](https://media.wiki-power.com/img/20210205205030.png)

Simplemente configure las opciones de `HSE` y `LSE` para utilizar osciladores de cristal externos:

![](https://media.wiki-power.com/img/20210205205140.png)

### Configuración del árbol de reloj

Realice la configuración en la interfaz de `Clock Configuration`.

![](https://media.wiki-power.com/img/20210205205550.png)

Siga estos pasos de acuerdo con la imagen anterior:

1. Ingrese los valores de las dos frecuencias de la oscilación externa de acuerdo con los parámetros del oscilador externo en la placa.
2. Seleccione `HSE` ya que la frecuencia y precisión del oscilador externo son superiores a los internos.
3. Marque la casilla `PLLCLK` para usar la multiplicación de frecuencia mediante el PLL.
4. Ingrese el valor de `HCKL`, generalmente según la frecuencia máxima recomendada que se muestra debajo. Después de ingresar el valor, presione Enter y se calculará automáticamente el divisor y el multiplicador.

### Configuración de opciones de gestión de proyectos

![](https://media.wiki-power.com/img/20210130095224.png)

![](https://media.wiki-power.com/img/20210130095239.png)

## Diferencias entre la biblioteca HAL y la biblioteca estándar

Para mejorar la portabilidad, la biblioteca HAL incluye tres características adicionales en comparación con la biblioteca estándar: **manejadores (handles), funciones MSP (Manejo del Estado de Memoria) y funciones de devolución de llamada (callbacks)**. Puede encontrar más detalles en los enlaces citados al final del documento.

## Referencias y agradecimientos

- [**Desglose detallado del sistema de reloj RCC en STM32**](https://blog.csdn.net/as480133937/article/details/98845509)
- [**Inicialización de la placa: configuración completa del árbol de reloj RCC y su proceso detallado**](https://www.notion.so/2-RCC-770c0c454f954408a3956257aa0fb523)
- [**Resumen exhaustivo del conocimiento de STM32 HAL**](https://mp.weixin.qq.com/s/ffcjKtl7JdRibLRNGquGXA)
- [**Una visión más clara del resumen exhaustivo del conocimiento de STM32 HAL**](https://mp.weixin.qq.com/s/qkj0fQS5NrCXmbppKEhaAg)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
