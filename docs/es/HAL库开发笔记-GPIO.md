# Notas de desarrollo de la biblioteca HAL - GPIO

## Principios Básicos

GPIO es el acrónimo de **General Purpose Input Output** (Entrada/Salida de Propósito General).

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20200615205256.jpg)

Tomemos como ejemplo el chip F103C8T6 (ver imagen de arriba). Aparte de los pines de color (que son para alimentación y algunas funciones específicas), todos los demás se llaman GPIO. Esto demuestra su versatilidad.

La función de GPIO es la de entrada/salida de señales eléctricas. Echemos un vistazo a su estructura interna:

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20200615211744.jpg)

- Los pines I/O más a la derecha son los pines físicos del chip. Las dos "diodos de protección" superior e inferior evitan que las tensiones anormales desde el exterior dañen el chip.
- Dentro del recuadro rojo punteado se encuentra la función de entrada (lectura de señales externas). Los dos interruptores con resistencias pull-up/pull-down permiten la activación de entradas con polaridad definida. Si ambos interruptores están abiertos, se denomina entrada en flotación (sin referencia de nivel lógico). Los tres modos de entrada mencionados proporcionan valores lógicos (alto/bajo). Además, existe la función de entrada analógica que lee directamente la señal analógica en el pin (mencionaremos la función multiplexada más adelante).
- Dentro del recuadro azul punteado se encuentra la función de salida. Hay cuatro modos de salida: push-pull, drenaje abierto, push-pull multiplexado y drenaje abierto multiplexado.

### Modos de Entrada y Salida

Modos de entrada:

- **Entrada en flotación**: Ni pull-up ni pull-down activados, modo predeterminado después del reinicio del STM32.
- **Entrada pull-up**: Activación de la resistencia pull-up, manteniendo el nivel lógico alto como referencia, lo que activa la entrada cuando la señal es baja.
- **Entrada pull-down**: Activación de la resistencia pull-down, manteniendo el nivel lógico bajo como referencia, lo que activa la entrada cuando la señal es alta.
- **Entrada analógica**: En este modo, ni pull-up ni pull-down están activados y la señal se lee directamente sin pasar por un disparador TTL.

Modos de salida:

- **Salida drenaje abierto**: El "drenaje abierto" se refiere a la apertura del drenaje del transistor N-MOS (el pin superior en la imagen). Este modo utiliza únicamente el transistor N-MOS inferior. Recordemos que los transistores MOS son componentes controlados por voltaje. Imaginemos un grifo de agua: cuando se aplica un nivel bajo al terminal de puerta (el pin izquierdo), el N-MOS conduce.
- **Salida push-pull**: El push-pull tiene dos modos. En el primer modo, se aplica un nivel bajo a los terminales de puerta de ambos transistores MOS, lo que permite que el P-MOS conduzca y el N-MOS esté en corte. En este caso, la corriente fluye desde VDD hacia el pin de salida, lo que genera un nivel alto en el pin. En el segundo modo, se aplica un nivel alto a los terminales de puerta de ambos transistores, lo que permite que el N-MOS conduzca y el P-MOS esté en corte. En este caso, la corriente fluye desde el pin de salida hacia el GND interno, lo que genera un nivel bajo en el pin.
- **Salida drenaje abierto multiplexado**
- **Salida push-pull multiplexado**

### Funciones GPIO comunes de uso

Para leer el estado de GPIO y obtener un nivel alto o bajo:

```c
GPIO_PinState HAL_GPIO_ReadPin(GPIOx, GPIO_Pin);
```

Para escribir el estado de GPIO y establecer un nivel alto o bajo:

```c
HAL_GPIO_WritePin(GPIOx, GPIO_Pin, PinState);
```

Para cambiar el estado de GPIO:

```c
HAL_GPIO_TogglePin(GPIOx, GPIO_Pin);
```

## Encender un LED

Antes de continuar con el siguiente experimento, es necesario configurar diversos parámetros en CubeMX, como la descarga de serie y la configuración de reloj.
No abordaremos estos detalles aquí, por favor refiérase al artículo [**Notas de desarrollo de la biblioteca HAL - Configuración del entorno**](enlace_a_la_configuración).

### Configuración de GPIO en CubeMX

Configure los pines GPIO correspondientes a los LEDs como salidas y establezca el nivel inicial.

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20210205150422.png)

En mi placa, los pines `PD4` y `PI3` deben configurarse como salidas (`GPIO_Output`). Si desea que el LED se encienda al encender la alimentación, según el diagrama eléctrico, establezca el nivel inicial en "Bajo" (`Low`).

### Configuración de GPIO en el código


Si la configuración es correcta, al encender el dispositivo, se iluminarán dos LEDs de usuario. Si deseas agregar un efecto intermitente, solo necesitas agregar algunas líneas de código en la zona de código de usuario del bucle principal:

```c title="main.c"
/* USER CODE BEGIN 3 */

HAL_Delay(500);
HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_4);
HAL_GPIO_TogglePin(GPIOI, GPIO_PIN_3);

}
/* USER CODE END 3 */
```

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20210205151322.png)

Esto permitirá lograr el efecto intermitente.

## Control de LEDs mediante pulsadores

Después de aprender sobre la salida GPIO, ahora vamos a aprender sobre el modo de entrada GPIO utilizando pulsadores.

### Configuración de GPIO en CubeMX

Después de configurar el puerto GPIO al que pertenecen los LEDs de acuerdo con el método mencionado anteriormente, siguiendo el esquemático de los pulsadores en la placa:

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20210205150422.png)

Configura el GPIO del pulsador (`PI8`) como entrada (`GPIO_Input`) y selecciona la resistencia de pull-up interna (`Pull-up`) según el esquemático. Luego, genera el código.

### Configuración de GPIO en el código

Agrega el siguiente código en la zona de código de usuario del bucle principal:

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

Esto permitirá que al presionar el pulsador, se encienda el LED, y al soltar el pulsador, se apague el LED.

Muchas personas pueden confundirse acerca de lo que significa `GPIO_PIN_SET` y `GPIO_PIN_RESET`. Estas dos variables simplemente establecen el nivel alto o bajo del pin GPIO. Si el LED está encendido o apagado depende del esquemático del circuito.

Además, la función `HAL_Delay(100)` se utiliza para eliminar el rebote del pulsador en el código. Sin embargo, la función `HAL_Delay()` utiliza un enfoque de espera activa, lo que puede consumir recursos y hacer que el sistema se bloquee. En el próximo artículo, abordaremos esta limitación utilizando interrupciones de hardware.

## Referencias y Agradecimientos

- [Tutorial STM32CubeMX - Fundamentos para encender un LED](https://blog.csdn.net/as480133937/article/details/98947162)
- [STM32CubeMX Practical Tutorial Part 2 - LED Control with Buttons](https://blog.csdn.net/weixin_43892323/article/details/104343933)

[Reemplazar[1]]
[Reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.