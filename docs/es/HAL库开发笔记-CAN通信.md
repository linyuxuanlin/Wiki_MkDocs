# Notas de desarrollo de la biblioteca HAL - Comunicación CAN 🚧

En este artículo, basado en el kit de desarrollo RobotCtrl de desarrollo propio, con núcleo de microcontrolador STM32F407ZET6 y uso de chips TJA1050 para la comunicación CAN. Para ver el esquema y obtener una introducción detallada, consulta [**RobotCtrl - Kit de desarrollo STM32 universal**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Pasos sencillos para la prueba de bucle de retroalimentación

### Configuración interna de CubeMX

1. Según el hardware CAN utilizado, en la barra lateral izquierda, abre la página `CAN1` o `CAN2`, marca la casilla `Activated`, y en la página de parámetros, configura los siguientes parámetros:
   1. Establece `Prescaler (for Time Quantum)` en `6`, y configura `Time Quanta in Bit Segment 1` y `Time Quanta in Bit Segment 2` en `3 Times`. Esta combinación ajusta la velocidad de bits a 1 Mbps (máxima velocidad).
   2. Configura `ReSynchronization Jump Width` en `1 Time`, que es el máximo paso ajustable durante la resincronización.
   3. Configura el `Operating Mode` en `Loopback` para la prueba de bucle de retroalimentación.
2. En la pestaña `NVIC Settings`, habilita `CANx RX0 interrupts`.

### Configuración en el código

En el proyecto, crea un archivo `can.c` y configura el filtro. Aquí se configura en modo de lista y se filtra el ID extendido `0x2233` y el ID estándar `0`:

```c title="can.c"/*
 * Nombre de la función: CAN_Filter_Config
 * Descripción: Configuración del filtro CAN
 * Entrada: Ninguna
 * Salida: Ninguna
 * Llamado: Llamado interno
 */
static void CAN_Filter_Config(void) {
	CAN_FilterTypeDef CAN_FilterTypeDef;

	/* Inicialización del filtro CAN */
	CAN_FilterTypeDef.FilterBank = 0;						// Grupo de filtro 0
	CAN_FilterTypeDef.FilterMode = CAN_FILTERMODE_IDLIST;	// Funcionamiento en modo de lista
	CAN_FilterTypeDef.FilterScale = CAN_FILTERSCALE_32BIT;	// Ancho de filtro de 32 bits individual.
	/* Habilitar el filtro y comparar según el contenido de la bandera, desechar si no coincide con el ID extendido a continuación; si coincide, se almacenará en FIFO0. */

	CAN_FilterTypeDef.FilterIdHigh = ((((uint32_t) 0x2233 << 3) | CAN_ID_EXT
			| CAN_RTR_DATA) & 0xFFFF0000) >> 16;		// Alto ID a filtrar
	CAN_FilterTypeDef.FilterIdLow = (((uint32_t) 0x2233 << 3) | CAN_ID_EXT
			| CAN_RTR_DATA) & 0xFFFF; // Bajo ID a filtrar
	CAN_FilterTypeDef.FilterMaskIdHigh = 0;		// Alto ID del segundo filtro
	CAN_FilterTypeDef.FilterMaskIdLow = 0;			// Bajo ID del segundo filtro
	CAN_FilterTypeDef.FilterFIFOAssignment = CAN_FILTER_FIFO0;	// Asignación del filtro al FIFO0
	CAN_FilterTypeDef.FilterActivation = ENABLE;			// Habilitar el filtro
	HAL_CAN_ConfigFilter(&hcan1, &CAN_FilterTypeDef);
}
```

### Prueba

Abre el Administrador de Dispositivos para verificar si el dispositivo se muestra. Si no encuentras el dispositivo o ves un signo de exclamación amarillo, visita el sitio web oficial de ST y descarga el controlador [**STM32 Virtual COM Port Driver**](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html).

Si instalaste el controlador pero aún no se reconoce correctamente, intenta ajustar el "Tamaño Mínimo de Montón" a `0x600` o un valor superior en CubeMX, en la sección de "Project Manager" - "Project" - "Linker Settings".

Abre una herramienta de comunicación serie (la velocidad de baudios puede ser cualquiera) y envía cualquier carácter. Deberías recibir el mismo carácter como respuesta.

## Referencias y Agradecimientos

- [STM32CubeMX y Aprendizaje de la Biblioteca HAL - Prueba de Bucle CAN Simple](https://blog.csdn.net/weixin_45209978/article/details/119850600)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.