# Notas de desarrollo de la biblioteca HAL - Comunicación CAN 🚧

En este artículo, basado en el kit de desarrollo RobotCtrl de desarrollo propio, el núcleo del microcontrolador es el STM32F407ZET6, y se utiliza el chip TJA1050 para la comunicación CAN. Para obtener el esquema y una descripción detallada, consulte [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/es/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Pasos sencillos para la prueba de bucle de retroalimentación

### Configuración interna de CubeMX

1. En función del hardware CAN utilizado, en la barra lateral izquierda, abra la página `CAN1` o `CAN2`, marque la casilla `Activated` y configure los siguientes parámetros en la página de parámetros:
   1. Establezca `Prescaler (for Time Quantum)` en `6`, y configure `Time Quanta in Bit Segment 1` y `Time Quanta in Bit Segment 2` en `3 Times`. Esta combinación establecerá la velocidad de bits en 1 Mbps (máxima).
   2. Configure `ReSynchronization Jump Width` en `1 Time`, que es el salto máximo ajustable durante la resincronización.
   3. Configure `Operating Mode` en `Loopback` para la prueba de bucle de retroalimentación.
2. En la pestaña `NVIC Settings`, habilite `CANx RX0 interrupts`.

### Configuración en el código

En el proyecto, cree un archivo llamado `can.c` y configure los filtros. En este caso, se ha configurado el modo de lista para filtrar el ID extendido `0x2233` y el ID estándar `0`:

```c title="can.c"/*
 * Nombre de la función: CAN_Filter_Config
 * Descripción: Configuración de filtros CAN
 * Entrada: Ninguna
 * Salida: Ninguna
 * Llamada: Llamada interna
 */
static void CAN_Filter_Config(void) {
	CAN_FilterTypeDef CAN_FilterTypeDef;

	/* Inicialización del filtro CAN */
	CAN_FilterTypeDef.FilterBank = 0;						// Grupo de filtro 0
	CAN_FilterTypeDef.FilterMode = CAN_FILTERMODE_IDLIST;	// Funcionamiento en modo de lista
	CAN_FilterTypeDef.FilterScale = CAN_FILTERSCALE_32BIT;	// Ancho de bits del filtro de 32 bits individual.
	/* Habilitar el filtro, comparar según el contenido de la bandera, deseche si el ID extendido no coincide, de lo contrario, almacene en FIFO0. */

	CAN_FilterTypeDef.FilterIdHigh = ((((uint32_t) 0x2233 << 3) | CAN_ID_EXT
			| CAN_RTR_DATA) & 0xFFFF0000) >> 16;		// Alto ID a filtrar
	CAN_FilterTypeDef.FilterIdLow = (((uint32_t) 0x2233 << 3) | CAN_ID_EXT
			| CAN_RTR_DATA) & 0xFFFF; // Bajo ID a filtrar
	CAN_FilterTypeDef.FilterMaskIdHigh = 0;		// Alto ID del segundo
	CAN_FilterTypeDef.FilterMaskIdLow = 0;			// Bajo ID del segundo
	CAN_FilterTypeDef.FilterFIFOAssignment = CAN_FILTER_FIFO0;	// El filtro se asocia con FIFO0
	CAN_FilterTypeDef.FilterActivation = ENABLE;			// Habilitar el filtro
	HAL_CAN_ConfigFilter(&hcan1, &CAN_FilterTypeDef);
}
```

### Prueba

Abre el Administrador de dispositivos para comprobar si el dispositivo se muestra. Si no encuentras el dispositivo o si ves un signo de exclamación amarillo, por favor, visita la página oficial de ST y descarga el controlador [**STM32 Virtual COM Port Driver**](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html).

Si a pesar de instalar el controlador no logras que el reconocimiento sea exitoso, puedes intentar ajustar el "Tamaño mínimo de montón" a `0x600` o un valor superior en CubeMX en la sección de "Configuración de Enlace" (Linker Settings) bajo "Project Manager" y "Proyecto" (Project).

Abre una herramienta de comunicación serial (puedes elegir cualquier velocidad de transmisión) y observarás que al enviar cualquier carácter, obtendrás el mismo carácter de vuelta.

## Referencias y Agradecimientos

- [STM32CubeMX y Aprendizaje de la Biblioteca HAL - Prueba sencilla de bucle de retorno CAN](https://blog.csdn.net/weixin_45209978/article/details/119850600)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.