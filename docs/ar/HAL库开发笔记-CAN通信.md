# Notas de desarrollo de la biblioteca HAL - Comunicación CAN 🚧

Este artículo se basa en el kit de desarrollo RobotCtrl, con núcleo de microcontrolador STM32F407ZET6 y uso del chip TJA1050 para la comunicación CAN. Para obtener el esquema y una introducción detallada, consulte [**RobotCtrl - Kit de desarrollo STM32 universal**](https://wiki-power.com/es/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Pasos simples para la prueba de bucle de retorno

### Configuración interna de CubeMX

1. Según el hardware CAN utilizado, abra la página `CAN1` o `CAN2` en la barra lateral izquierda, marque `Activated` y configure estos parámetros en la página de parámetros:
   1. Configure `Prescaler (for Time Quantum)` en `6`, `Time Quanta in Bit Segment 1` y `Time Quanta in Bit Segment 2` en `3 Times`. Esta combinación establece la velocidad de bits en 1 Mbps (máxima).
   2. Configure `ReSynchronization Jump Width` en `1 Time`, que es el máximo paso ajustable durante la resincronización.
   3. Configure `Operating Mode` en `Loopback` para la prueba de bucle de retorno.
2. En la pestaña `NVIC Settings`, active `CANx RX0 interrupts`.

### Configuración interna del código

Cree `can.c` en el proyecto, configure el filtro y configure el modo de lista, filtrando la ID extendida `0x2233` y la ID estándar `0`:

```c title="can.c"/*
 * Función: CAN_Filter_Config
 * Descripción: Configuración del filtro CAN
 * Entrada: Ninguna
 * Salida: Ninguna
 * Llamada: Llamada interna
 */
static void CAN_Filter_Config(void) {
	CAN_FilterTypeDef CAN_FilterTypeDef;

	/*Inicialización del filtro CAN*/
	CAN_FilterTypeDef.FilterBank = 0;						//Grupo de filtro 0
	CAN_FilterTypeDef.FilterMode = CAN_FILTERMODE_IDLIST;	//Modo de lista de trabajo
	CAN_FilterTypeDef.FilterScale = CAN_FILTERSCALE_32BIT;	//Ancho de bits del filtro es un solo 32 bits.
	/* Habilitar el filtro, comparar y filtrar según el contenido de la bandera. Si la ID extendida no es la siguiente, se descarta. Si lo es, se almacenará en FIFO0. */

	CAN_FilterTypeDef.FilterIdHigh = ((((uint32_t) 0x2233 << 3) | CAN_ID_EXT
			| CAN_RTR_DATA) & 0xFFFF0000) >> 16;		//ID alto a filtrar
	CAN_FilterTypeDef.FilterIdLow = (((uint32_t) 0x2233 << 3) | CAN_ID_EXT
			| CAN_RTR_DATA) & 0xFFFF; //ID bajo a filtrar
	CAN_FilterTypeDef.FilterMaskIdHigh = 0;		//ID alto del segundo filtro
	CAN_FilterTypeDef.FilterMaskIdLow = 0;			//ID bajo del segundo filtro
	CAN_FilterTypeDef.FilterFIFOAssignment = CAN_FILTER_FIFO0;	//El filtro está asociado con FIFO0
	CAN_FilterTypeDef.FilterActivation = ENABLE;			//Habilitar el filtro
	HAL_CAN_ConfigFilter(&hcan1, &CAN_FilterTypeDef);
}
```

### Prueba

Abra el Administrador de dispositivos para verificar si el dispositivo se muestra. Si no se encuentra el dispositivo o hay un signo de exclamación amarillo, descargue el controlador [STM32 Virtual COM Port Driver](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html) desde el sitio web de ST.

Si después de instalar el controlador aún no se reconoce correctamente, intente ajustar el "Tamaño mínimo de la pila" a "0x600" o superior en CubeMX - "Administrador de proyectos" - "Proyecto" - "Configuración del enlazador".

Abra la herramienta de comunicación en serie (con cualquier velocidad de transmisión) y envíe cualquier carácter para recibir el mismo carácter de vuelta.

Referencias y agradecimientos:

- [STM32CubeMX y aprendizaje de la biblioteca HAL - prueba de bucle de retorno CAN simple](https://blog.csdn.net/weixin_45209978/article/details/119850600)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.