# Notas de desarrollo de la biblioteca HAL - GPIO

## Principios básicos

GPIO significa **puerto de entrada/salida general** (General Purpose Input Output).

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200615205256.jpg)

Tomemos como ejemplo el chip F103C8T6 (en la imagen de arriba), todo lo que no sean los pines de color (pines de alimentación y algunos pines de función) se llaman GPIO. Se puede ver su grado de generalidad.

La función de GPIO es la entrada/salida de señales eléctricas. Echemos un vistazo a su estructura interna:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200615211744.jpg)

- El pin I/O más a la derecha es el pin del chip físico. Las dos diodos de protección arriba y abajo pueden prevenir en cierta medida que el voltaje anormal externo queme el chip a través del pin.
- El cuadro de línea roja es la función de entrada (el chip lee la señal externa). Las dos resistencias de pull-up/pull-down con interruptores son para implementar la función de entrada de pull-up/pull-down. Si ambos interruptores no están cerrados, lo llamamos entrada flotante (no hay nivel de referencia). Los tres modos de entrada leen una cantidad digital (nivel alto/bajo). Además, también hay una función de entrada analógica, que se entiende como la lectura directa de la señal analógica en el pin. (Hablaremos de la función de entrada de función múltiple más adelante).
- El cuadro de línea azul es la función de salida. Hay cuatro modos de salida: push-pull, open-drain, push-pull de función múltiple y open-drain de función múltiple.

### Modos de entrada/salida

Modos de entrada:

- **Entrada flotante**: ni pull-up ni pull-down, el modo predeterminado después del reinicio del STM32.
- **Entrada pull-up**: cierre el interruptor de la resistencia pull-up para mantener el nivel de referencia siempre en alto, y se activará cuando la señal de entrada sea de nivel bajo.
- **Entrada pull-down**: cierre el interruptor de la resistencia pull-down para mantener el nivel de referencia siempre en bajo, y se activará cuando la señal de entrada sea de nivel alto.
- **Entrada analógica**: en este modo, ni pull-up ni pull-down, ni pasa por el disparador TTL, el STM32 lee directamente la señal analógica en el pin.

Modos de salida:

- **Salida open-drain**: open-drain se refiere a la fuga de la fuente del N-MOSFET (el pin de arriba), este modo solo utiliza el N-MOSFET de abajo. Sabemos que el MOSFET es un componente controlado por voltaje. Entendámoslo como un grifo, cuando se ingresa una señal de nivel bajo al electrodo de la puerta del N-MOSFET (el pin izquierdo), el N-MOSFET se enciende.
- **Salida push-pull**: hay dos modos de push-pull, el primer modo es enviar una señal de nivel bajo a los electrodos de la puerta de los dos MOSFET al mismo tiempo, en este momento el P-MOSFET está encendido y el N-MOSFET está apagado, la corriente fluye desde VDD hacia el pin externo, y el pin es de nivel alto. El segundo modo es lo contrario, enviar una señal de nivel alto a los electrodos de la puerta de los dos MOSFET al mismo tiempo, en este momento el P-MOSFET está apagado y el N-MOSFET está encendido, la corriente fluye desde el pin externo hacia el GND interno, y el pin es de nivel bajo.
- **Salida open-drain de función múltiple**
- **Salida push-pull de función múltiple**

### Referencia de funciones GPIO comunes

Leer el estado GPIO, devolver nivel alto/bajo:

```c
GPIO_PinState HAL_GPIO_ReadPin(GPIOx, GPIO_Pin);
```

Escribir el estado GPIO, escribir nivel alto/bajo:

```c
HAL_GPIO_WritePin(GPIOx, GPIO_Pin, PinState);
```

Invertir el nivel GPIO:

```c
HAL_GPIO_TogglePin(GPIOx, GPIO_Pin);
```

## Encender el LED

Antes de continuar con el siguiente experimento, es necesario configurar varios parámetros como la descarga de la serie, el reloj, etc. en CubeMX. No se explicará aquí, por favor consulte el método en el artículo [**Notas de desarrollo de la biblioteca HAL - Configuración del entorno**](https://wiki-power.com/es/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE).

### Configuración GPIO en CubeMX

Configure el puerto GPIO correspondiente al LED como salida y establezca el nivel inicial.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210205150422.png)

En mi placa, necesito configurar los GPIO `PD4` y `PI3` como salida (`GPIO_Output`). Si quiero que se enciendan al encender, según el esquema del circuito, debo establecer el potencial inicial como bajo (`Low`).

### Configuración de GPIO en el código

Si la configuración es correcta, los dos LED de usuario se encenderán al encender. Si desea agregar un efecto intermitente, simplemente agregue algunas líneas de código en el área de código de usuario del bucle principal:

```c title="main.c"
/* USER CODE BEGIN 3 */

HAL_Delay(500);
HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_4);
HAL_GPIO_TogglePin(GPIOI, GPIO_PIN_3);

}
/* USER CODE END 3 */
```

Esto logrará el efecto intermitente.

## Control de luz con botón

Después de aprender sobre la salida GPIO, usaremos un botón para aprender sobre el modo de entrada GPIO.

### Configuración de GPIO en CubeMX

Después de configurar el puerto GPIO al que pertenece el LED según el método anterior, según el esquema del botón de la placa:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210205150422.png)

Configure el GPIO al que pertenece el botón (`PI8`) como entrada (`GPIO_Input`). Según el esquema, seleccione la resistencia pull-up interna (`Pull-up`). Genere el código.

### Configuración de GPIO en el código

Agregue el siguiente código al área de código de usuario del bucle principal:

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

Esto logrará el efecto de encender la luz al presionar el botón y apagarla al soltarlo.

Muchas personas no entienden qué significan `GPIO_PIN_SET` y `GPIO_PIN_RESET`. De hecho, la función de estas dos variables es simplemente establecer el nivel alto / bajo del pin GPIO. La luz específica está encendida o apagada, dependiendo del esquema del circuito.

Además, la función de `HAL_Delay(100)` es eliminar el rebote del botón. Sin embargo, la función `HAL_Delay()` utiliza una encuesta, lo que ocupará recursos y causará bloqueos. En el próximo artículo, usaremos interrupciones de hardware para resolver esta deficiencia.

## Referencias y agradecimientos

- [【STM32】STM32CubeMX Tutorial 2 - Uso básico (Crear un proyecto para encender un LED)](https://blog.csdn.net/as480133937/article/details/98947162)
- [STM32CubeMX Tutorial práctico (2) - Encender un LED con un botón](https://blog.csdn.net/weixin_43892323/article/details/104343933)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.