# Notas de desarrollo de la biblioteca HAL - DMA

DMA (Acceso directo a memoria) permite que dispositivos de hardware de diferentes velocidades se comuniquen directamente sin depender de una gran carga de interrupción de la CPU.

## Principios básicos

### ¿Qué es DMA?

DMA proporciona transferencia de datos de alta velocidad entre periféricos/memoria o memoria/memoria sin ocupar recursos de la CPU.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210404153423.png)

Como se muestra en la figura anterior, la serie STM32F4 tiene dos controladores DMA con un total de 12 canales (DMA1 tiene 7 y DMA2 tiene 5). El controlador DMA comparte el bus de datos del sistema con el núcleo Cortex-M3.

En resumen, cuando la CPU no quiere transferir una gran cantidad de datos a otro lugar o cuando tiene cosas más importantes que hacer, puede dejar esta tarea a DMA para que la haga y DMA informará a la CPU cuando termine o si hay algún problema.

### Escenarios de uso de DMA

- **Comunicación serie**: el caso de uso más común, cuando hay una gran cantidad de datos que se leen o escriben desde el puerto serie, se utiliza DMA para procesarlos. Esto puede liberar la CPU para que maneje cosas más importantes.
- **ADC**: generalmente se puede utilizar DMA en el modo de escaneo de canal cuando se necesita ADC.
- **Lectura/escritura de tarjeta SD**: generalmente se utiliza DMA para manejar grandes cantidades de datos que se leen o escriben en la tarjeta SD.

### Dirección de transferencia de DMA

- **P2P** (de periférico a periférico).
- **P2M** (de periférico a memoria): generalmente se utiliza cuando un sensor envía datos a la MCU a través del puerto serie.
- **M2P** (de memoria a periférico): generalmente se utiliza cuando la MCU envía datos a un actuador a través del puerto serie.
- **M2M** (de memoria a memoria): transferencia de datos interna de MCU, comúnmente utilizada para transferir datos entre búferes o para leer/escribir datos desde/hacia un búfer. Solo DMA2 puede realizar operaciones M2M.

### Modo de transferencia de DMA

- **DMA_Mode_Normal**: modo normal. El DMA se detiene después de completar la tarea y debe iniciarse manualmente si se necesita de nuevo.
- **DMA_Mode_Circular**: modo de transferencia circular. Cuando se completa la transferencia, el hardware recarga automáticamente el registro de cantidad de datos transferidos para realizar la siguiente transferencia de datos.

### Referencia de funciones DMA comunes

#### Enviar datos por DMA a través del puerto serie

```c
HAL_UART_Transmit_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
```

Función: envía datos de longitud especificada a través del puerto serie mediante DMA.  
Parámetros:

- **UART_HandleTypeDef \*huart**: alias de UART (por ejemplo: UART_HandleTypeDef huart1 -> huart1)
- **\*pData**: datos que se enviarán
- **Size**: número de bytes que se enviarán

Ejemplo:

```c
HAL_UART_Transmit_DMA(&huart1, (uint8_t *)Senbuff, sizeof(Senbuff));  //envía el array Senbuff a través del puerto serie
```

#### Recibir datos por DMA a través del puerto serie

```c
HAL_UART_Receive_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
```

Función: recibe datos de longitud especificada a través del puerto serie mediante DMA.  
Parámetros:

- **UART_HandleTypeDef \*huart**: alias de UART (por ejemplo: UART_HandleTypeDef huart1 -> huart1)
- **\*pData**: array donde se almacenarán los datos recibidos
- **Size**: número de bytes que se recibirán

Ejemplo:

```c
HAL_UART_Receive_DMA(&huart1, (uint8_t *)Recbuff, sizeof(Recbuff));  //recibe datos a través del puerto serie y los almacena en el array Recbuff
```

#### Función de recuperación de DMA de puerto serie

```c
HAL_UART_DMAResume(&huart1)
```

Función: reanuda la transferencia DMA  
Valor de retorno: 0 (reanudando); 1 (recuperación completada)

## Experimento de transferencia de DMA de puerto serie

### Configuración de DMA en CubeMX

Para la configuración de la parte de puerto serie, consulte el artículo [**HAL 库开发笔记 - 串口通信**](https://wiki-power.com/es/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1) (en chino).

Después de configurar los pines USART y las interrupciones NVIC, cambie a la pestaña `DMA Settings` y configure según la siguiente imagen:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210404165541.png)

- Haga clic en `Add` para agregar canales (USART1_RX y USART1_TX)
- Establezca la prioridad de ambos como `Medium`
- El modo de transferencia DMA es `Normal`
- La dirección de memoria DMA se incrementa automáticamente, aumentando un byte cada vez.

Luego, en la pestaña `System Core`, agregue una sección `MEMTOMEM`, como se muestra en la siguiente imagen:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210404170002.png)

### Configuración de DMA en el código

```c title="main.c"
/* USER CODE BEGIN Init */

uint8_t Senbuff[] = "Serial Output Message by DMA \r\n";  // Cadena personalizada para enviar

/* USER CODE END Init */

......

/* USER CODE BEGIN 3 */

HAL_UART_Transmit_DMA(&huart1, (uint8_t *)Senbuff, sizeof(Senbuff));
HAL_Delay(1000);

}
/* USER CODE END 3 */
```

Grabe el programa, abra el asistente de puerto serie y verá la matriz personalizada que se envía en bucle.

## Referencias y agradecimientos

- [进阶篇 IV [DMA]](https://alchemicronin.github.io/posts/90d72de/#4-0-%E7%BB%83%E4%B9%A0%E9%A1%B9%E7%9B%AE) (en chino)
- [【STM32】HAL 库 STM32CubeMX 教程十一 ---DMA (串口 DMA 发送接收)](https://blog.csdn.net/as480133937/article/details/104827639) (en chino)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.