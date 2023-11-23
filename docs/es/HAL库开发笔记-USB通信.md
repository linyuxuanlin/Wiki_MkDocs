# Notas de desarrollo de la biblioteca HAL para USB - Comunicación 🚧

Este artículo se basa en el kit de desarrollo RobotCtrl de desarrollo propio, con un núcleo de microcontrolador STM32F407ZET6 y pines USB_Slave en `PA11` y `PA12`. Para el esquema y una descripción detallada, consulte [**RobotCtrl - Kit de desarrollo STM32 universal**[por_sustituir[3]]RobotCtrl-STM32-Universal-Development-Kit).

## Pasos sencillos para realizar una prueba de bucle de retroalimentación

### Configuración interna de CubeMX

1. Configure el reloj como reloj externo de alta velocidad (HSE).
2. Configure el árbol de reloj para asegurarse de que la velocidad del reloj en el extremo del árbol de reloj sea de 48 MHz.
3. En la página `USB_OTG_FS`, configure el `Modo` como `Solo dispositivo`, con los pines predeterminados `PA11` y `PA12`.
4. En la página `USB_DEVICE`, configure la `Clase para FS IP` como `Clase de dispositivo de comunicación (Puerto virtual COM)`.

### Configuración en el código

Para implementar la funcionalidad de bucle de retroalimentación de datos, solo es necesario agregar una línea en la función `CDC_Receive_FS` del archivo `usbd_cdc_if.c`:

```c title="usbd_cdc_if.c"
CDC_Transmit_FS(Buf, *Len); // Devolver los mismos datos
```

### Pruebas

Abra el Administrador de dispositivos y verifique si el dispositivo se muestra. Si no se encuentra el dispositivo o hay un signo de exclamación amarillo, descargue el controlador desde el sitio web de ST: [**Controlador de puerto COM virtual STM32**](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html).

Si ha instalado el controlador y aún no se reconoce correctamente, intente ajustar el `Tamaño mínimo de montón` a `0x600` o más alto en CubeMX - `Project Manager` - `Project` - `Linker Settings`.

Abra una herramienta de terminal serie (con cualquier velocidad de baudios) y verá que al enviar cualquier carácter, recibirá el mismo carácter de vuelta.

## Referencias y agradecimientos

- [Generación rápida de proyectos de puerto serie virtual USBVCP con la biblioteca HAL de STM32 utilizando CubeMX](https://blog.csdn.net/yxy244/article/details/102620249)

[por_sustituir[1]]  
[por_sustituir[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.