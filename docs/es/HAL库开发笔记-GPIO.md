# Notas de desarrollo de la biblioteca HAL - GPIO

## Principios básicos

GPIO significa **Entrada/Salida de Propósito General** (General Purpose Input Output).

![](https://media.wiki-power.com/img/20200615205256.jpg)

Tomemos como ejemplo el chip F103C8T6 (imagen superior), aparte de los pines de colores (alimentación y algunos pines de función específica), todos los demás se llaman GPIO. Esto demuestra su versatilidad.

La función de GPIO es la de entrada/salida de señales eléctricas. Veamos su estructura interna:

![](https://media.wiki-power.com/img/20200615211744.jpg)

- El pin I/O más a la derecha es el pin físico del chip. Las `diodos de protección` superior e inferior evitan que el chip se dañe por voltajes anormales externos.
- El recuadro de línea roja representa la función de entrada (lectura de señales externas). Los dos interruptores con resistencias pull-up/pull-down se utilizan para implementar la función de entrada con resistencia pull-up/pull-down. Si ambos interruptores están abiertos, se considera una entrada flotante (sin nivel de referencia). Estos tres modos de entrada se leen como valores digitales (alto/bajo). Además, también existe la función de entrada analógica, que consiste en leer directamente el valor analógico del pin. (La función de entrada de multiplexación se mencionará más adelante).
- El recuadro de línea azul representa la función de salida. Hay 4 modos de salida: push-pull, drenaje abierto, multiplexación push-pull y multiplexación drenaje abierto.

### Modos de entrada/salida

Modos de entrada:

- **Entrada flotante**: ni pull-up ni pull-down, es el modo predeterminado después del reinicio del STM32.
- **Entrada con pull-up**: cerrar el interruptor de resistencia pull-up para mantener el nivel de referencia en alto, se activa cuando la señal de entrada es baja.
- **Entrada con pull-down**: cerrar el interruptor de resistencia pull-down para mantener el nivel de referencia en bajo, se activa cuando la señal de entrada es alta.
- **Entrada analógica**: en este modo, no hay pull-up ni pull-down, ni tampoco hay un disparador TTL. El STM32 lee directamente la señal analógica del pin.

Modos de salida:

- **Salida drenaje abierto**: el drenaje abierto se refiere a la fuente de drenaje del transistor N-MOS (el pin superior). Este modo solo utiliza el transistor N-MOS inferior. Sabemos que el transistor MOS es un dispositivo controlado por voltaje. Podemos entenderlo como una llave de paso de agua. Cuando se aplica una señal de bajo nivel al gate del N-MOS (el pin izquierdo), el N-MOS se activa.
- **Salida push-pull**: hay dos modos de push-pull. En el primer modo, se aplica una señal de bajo nivel a los gates de los dos transistores MOS al mismo tiempo, lo que hace que el P-MOS se active y el N-MOS se corte. La corriente fluye desde VDD hacia el pin externo, lo que hace que el pin esté en alto. En el segundo modo, se aplica una señal de alto nivel a los gates de los dos transistores MOS al mismo tiempo, lo que hace que el P-MOS se corte y el N-MOS se active. La corriente fluye desde el pin externo hacia el GND interno, lo que hace que el pin esté en bajo.
- **Multiplexación drenaje abierto**
- **Multiplexación push-pull**

### Referencia de funciones GPIO comunes

Leer el estado de GPIO, devuelve alto/bajo:

```c
GPIO_PinState HAL_GPIO_ReadPin(GPIOx, GPIO_Pin);
```

Escribir el estado de GPIO, establecer alto/bajo:

```c
HAL_GPIO_WritePin(GPIOx, GPIO_Pin, PinState);
```

Invertir el nivel de GPIO:

```c
HAL_GPIO_TogglePin(GPIOx, GPIO_Pin);
```

## Encender un LED

Antes de continuar con el siguiente experimento, es necesario configurar varios parámetros en CubeMX, como la descarga a través del puerto serie y la configuración del reloj.
No se explicará aquí, por favor consulte el artículo [**Notas de desarrollo de la biblioteca HAL - Configuración del entorno**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) para obtener instrucciones sobre cómo configurarlos.

### Configuración de GPIO en CubeMX

Configure los pines GPIO correspondientes al LED como salida y establezca el nivel inicial.

![](https://media.wiki-power.com/img/20210205150422.png)

En mi placa, los pines `PD4` y `PI3` deben configurarse como salida (`GPIO_Output`).
Si desea que el LED se encienda al encender la placa, según el esquema del circuito, establezca el nivel inicial en bajo (`Low`).

### Configuración de GPIO en el código

Si la configuración es correcta, las dos luces LED de usuario se encenderán al encender el dispositivo.  
Si se desea agregar un efecto de parpadeo, solo es necesario agregar algunas líneas de código dentro del área de código de usuario del bucle principal:

```c title="main.c"
/* USER CODE BEGIN 3 */

HAL_Delay(500);
HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_4);
HAL_GPIO_TogglePin(GPIOI, GPIO_PIN_3);

}
/* USER CODE END 3 */
```

![](https://media.wiki-power.com/img/20210205151322.png)

Esto logrará el efecto de parpadeo de las luces.

## Control de luces mediante pulsadores

Después de aprender sobre la salida de GPIO, vamos a aprender sobre el modo de entrada de GPIO utilizando pulsadores.

### Configuración de GPIO en CubeMX

Después de configurar el puerto GPIO al que pertenecen las luces LED siguiendo los pasos anteriores, según el esquema del pulsador en la placa:

![](https://media.wiki-power.com/img/20210205150422.png)

Configurar el GPIO correspondiente al pulsador (`PI8`) como entrada (`GPIO_Input`). Según el esquema, seleccionar la resistencia de pull-up interna (`Pull-up`). Generar el código.

### Configuración de GPIO en el código

Agregar el siguiente código dentro del área de código de usuario del bucle principal:

```c title="main.c"
/* USER CODE BEGIN 3 */

if(HAL_GPIO_ReadPin(KEY1_GPIO_Port,KEY1_Pin)==0)
{
	HAL_Delay(100);
	if(HAL_GPIO_ReadPin(KEY1_GPIO_Port,KEY1_Pin)==0)
	{
		HAL_GPIO_WritePin(LED1_GPIO_Port,LED1_Pin,GPIO_PIN_RESET);
	}
}else{
	HAL_GPIO_WritePin(LED1_GPIO_Port,LED1_Pin,GPIO_PIN_SET);
}

}
/* USER CODE END 3 */
```

Esto logrará el efecto de encender la luz al presionar el pulsador y apagarla al soltarlo.

Muchas personas no entienden qué significa `GPIO_PIN_SET` y `GPIO_PIN_RESET`. En realidad, estas dos variables solo se utilizan para establecer el nivel alto/bajo del pin GPIO. Si la luz está encendida o apagada específicamente, se debe consultar el esquema del circuito.

Además, la función de `HAL_Delay(100)` es eliminar el rebote del pulsador. Sin embargo, la función `HAL_Delay()` utiliza un bucle de espera, lo que consume recursos y puede causar bloqueos. En el próximo artículo, resolveremos esta deficiencia utilizando interrupciones de hardware.

## Referencias y agradecimientos

- [【STM32】STM32CubeMX Tutorial 2 - Uso básico (Crear proyecto para encender luces LED)](https://blog.csdn.net/as480133937/article/details/98947162)
- [STM32CubeMX Practical Tutorial 2 - Encender luces con pulsadores](https://blog.csdn.net/weixin_43892323/article/details/104343933)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
