# Notas de desarrollo de la biblioteca HAL - Configuración del entorno

Nota: Este tutorial se basa en la placa STM32F429IGT6 de Refkit.

## Instalación de software

### Keil MDK

Consulte el artículo [**Guía de configuración de Keil MDK**](enlace_a_reemplazar) para obtener instrucciones detalladas.

### Entorno de ejecución de Java

Esto es necesario para STM32CubeMX. Puede descargar e instalar el entorno de ejecución de Java desde el [**enlace oficial**](https://www.java.com/en/download/).

### STM32CubeMX

Descargue e instale STM32CubeMX desde el [**enlace oficial**](https://my.st.com/content/my_st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.license=1611899126599.product=STM32CubeMX.version=6.1.1.html).

## Configuración del proyecto

### Inicialización

Cree un nuevo proyecto y seleccione el microcontrolador antes de guardar.

### Configuración de SYS

`Pinout & Configurations` - `System Core` - `SYS`

Cambie la opción de `Debug` a `Serial Wire` (consulte el artículo [**Evitando problemas con CubeMX y CubeIDE**](enlace_a_reemplazar) para conocer los detalles).

### Configuración de RCC

`Pinout & Configurations` - `System Core` - `RCC`

Ajuste la configuración según las especificaciones de la placa.

Por ejemplo, consulte el esquema de la placa:

![Esquema de la placa](https://img.wiki-power.com/d/wiki-media/img/20210205205030.png)

Configure las opciones `HSE` y `LSE` para utilizar osciladores de cristal externos, como se muestra a continuación:

![Configuración de HSE y LSE](https://img.wiki-power.com/d/wiki-media/img/20210205205140.png)

### Configuración del árbol de reloj

Realice la configuración en la interfaz de `Clock Configuration`.

Siga estos pasos según la imagen anterior:

1. Ingrese los valores de las dos frecuencias en el lado izquierdo, de acuerdo con los parámetros del oscilador de cristal externo de la placa.
2. Seleccione `HSE` ya que la frecuencia y precisión del oscilador de cristal externo son mejores que las internas.
3. Marque `PLLCLK` para usar la multiplicación de PLL para obtener una frecuencia alta.
4. Ingrese el valor de `HCKL`, generalmente se basa en la frecuencia máxima indicada a continuación. Después de ingresar el valor, presione Enter y se calculará automáticamente el divisor y la multiplicación.

### Configuración de opciones de administración del proyecto

![Opciones de administración del proyecto](https://img.wiki-power.com/d/wiki-media/img/20210130095224.png)

![Opciones de administración del proyecto](https://img.wiki-power.com/d/wiki-media/img/20210130095239.png)

## Diferencias entre la biblioteca HAL y la biblioteca estándar

Para mejorar la portabilidad, la biblioteca HAL agrega tres características adicionales en comparación con la biblioteca estándar: **manejadores, funciones MSP y funciones de devolución de llamada**. Para obtener más detalles, consulte los enlaces citados al final del documento.

## Referencias y agradecimientos

- [【STM32】Explanation of RCC System Clock](https://blog.csdn.net/as480133937/article/details/98845509)
- [Initialization of the Board, Complete Configuration of the RCC Clock Tree](https://www.notion.so/2-RCC-770c0c454f954408a3956257aa0fb523)
- [Comprehensive Summary of STM32 HAL Knowledge](https://mp.weixin.qq.com/s/ffcjKtl7JdRibLRNGquGXA)
- [Clear and Comprehensive Summary of STM32 HAL Knowledge](https://mp.weixin.qq.com/s/qkj0fQS5NrCXmbppKEhaAg)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.