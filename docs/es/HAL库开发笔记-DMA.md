# Notas de desarrollo de la biblioteca HAL - DMA

DMA (Acceso Directo a la Memoria, por sus siglas en inglés) permite la comunicación directa entre dispositivos de hardware a diferentes velocidades, sin necesidad de depender en gran medida de la carga de interrupciones de la CPU.

## Principios básicos

### ¿Qué es DMA?

DMA proporciona transferencia de datos de alta velocidad entre periféricos/memoria o memoria/memoria sin utilizar los recursos de la CPU.

![DMA](https://media.wiki-power.com/img/20210404153423.png)

Como se muestra en la imagen, la serie STM32F4 tiene dos controladores DMA con un total de 12 canales (DMA1 tiene 7 y DMA2 tiene 5). Los controladores DMA comparten el bus de datos del sistema con el núcleo Cortex-M3.

En términos simples, cuando la CPU no desea mover una gran cantidad de datos a otro lugar, o cuando tiene tareas más importantes que atender, puede delegar esta tarea al DMA, y el DMA se encargará de ella o informará a la CPU si surge algún problema.

### Escenarios de uso de DMA

- **Comunicación serie**: es el caso más común, cuando se leen o escriben grandes cantidades de datos desde/hacia un puerto serie, se puede utilizar el DMA. De esta manera, se libera la CPU para tareas más importantes.
- **ADC** (Conversor Analógico-Digital): generalmente se utiliza el DMA en el modo de exploración de canales cuando se necesita el ADC.
- **Lectura/escritura en tarjetas SD**: se utiliza el DMA cuando se necesita leer o escribir grandes cantidades de datos en una tarjeta SD.

### Direcciones de transferencia DMA

- **P2P** (De periférico a periférico).
- **P2M** (De periférico a memoria): se utiliza generalmente para enviar datos de sensores a la microcontroladora a través del puerto serie.
- **M2P** (De memoria a periférico): se utiliza generalmente para enviar datos desde la microcontroladora a actuadores a través del puerto serie.
- **M2M** (De memoria a memoria): transferencia interna de datos en el MCU, comúnmente utilizada para transferir datos entre búferes o para leer/escribir datos desde/hacia un búfer. Solo el DMA2 es capaz de realizar operaciones M2M.

### Modos de transferencia DMA

- **DMA_Mode_Normal** (Modo normal): se detiene el DMA después de completar la tarea. Si se necesita realizar otra transferencia, debe iniciarse manualmente.
- **DMA_Mode_Circular** (Modo circular): modo de transferencia cíclica. Cuando se completa la transferencia, el hardware recargará automáticamente el registro de cantidad de datos de transferencia y realizará la siguiente ronda de transferencia de datos.

### Referencia de funciones DMA comunes

#### Envío de datos por DMA en el puerto serie

```c
HAL_UART_Transmit_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
```

Función: Envia datos de la UART especificada mediante DMA.
Parámetros:

- **UART_HandleTypeDef \*huart**: Nombre de la UART (por ejemplo: UART_HandleTypeDef huart1 -> huart1).
- **\*pData**: Datos a enviar.
- **Size**: Número de bytes a enviar.

Ejemplo:

```c
HAL_UART_Transmit_DMA(&huart1, (uint8_t *)Senbuff, sizeof(Senbuff));  // Enviar el array Senbuff a través del puerto serie.
```

#### Recepción de datos por DMA en el puerto serie

```c
HAL_UART_Receive_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
```

Función: Recibe datos en la UART especificada mediante DMA.
Parámetros:

- **UART_HandleTypeDef \*huart**: Nombre de la UART (por ejemplo: UART_HandleTypeDef huart1 -> huart1).
- **\*pData**: Arreglo para almacenar los datos recibidos.
- **Size**: Número de bytes a recibir.

Ejemplo:

```c
HAL_UART_Receive_DMA(&huart1, (uint8_t *)Recbuff, sizeof(Recbuff));  // Recibir datos del puerto serie y almacenarlos en el arreglo Recbuff.
```

#### Función de reinicio de DMA en el puerto serie

```c
HAL_UART_DMAResume(&huart1)
```

Function: Resumes DMA transmission
Return Value: 0 (resuming) or 1 (resumed successfully)

## DMA Serial Transmission Experiment

### Configuring DMA in CubeMX

For the configuration of the UART section, please refer to the article [**HAL Library Development Notes - Serial Communication**](https://wiki-power.com/es/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1).

After configuring the USART pins and NVIC interrupts, switch to the `DMA Settings` tab and configure as shown below:

![](https://media.wiki-power.com/img/20210404165541.png)

- Click `Add` to add channels (USART1_RX and USART1_TX).
- Set the priority of both to `Medium`.
- DMA transfer mode is set to `Normal`.
- DMA memory address increments by one byte each time.

Next, in the `System Core` tab, find `DMA` and add a `MEMTOMEM` section as shown below:

![](https://media.wiki-power.com/img/20210404170002.png)

### Configuring DMA in the Code

```c title="main.c"
/* USER CODE BEGIN Init */

uint8_t Senbuff[] = "Serial Output Message by DMA \r\n";  // Custom string to be sent

/* USER CODE END Init */

......

/* USER CODE BEGIN 3 */

HAL_UART_Transmit_DMA(&huart1, (uint8_t *)Senbuff, sizeof(Senbuff));
HAL_Delay(1000);

}
/* USER CODE END 3 */
```

Flash the program, open a serial assistant, and you will see the custom array being sent in a loop.

## References and Acknowledgments

- [Advanced Part IV [DMA]](https://alchemicronin.github.io/posts/90d72de/#4-0-%E7%BB%83%E4%B9%A0%E9%A1%B9%E7%9B%AE)
- [【STM32】HAL Library STM32CubeMX Tutorial Eleven - DMA (UART DMA Transmission and Reception)](https://blog.csdn.net/as480133937/article/details/104827639)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

```


> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
```
