# Notas de desarrollo de la biblioteca HAL - Comunicación USB 🚧

Este artículo se basa en el kit de desarrollo RobotCtrl, desarrollado internamente, con un núcleo de microcontrolador STM32F407ZET6, y los pines USB_Slave son `PA11` y `PA12`. Para obtener el esquema y una descripción detallada, consulte [**RobotCtrl - Kit de desarrollo STM32 universal**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Pasos simples para la prueba de bucle de retroalimentación

### Configuración interna de CubeMX

1. Configure el reloj externo de alta velocidad (HSE).
2. Configure el árbol de reloj para asegurarse de que el extremo del árbol de reloj "48MHz Clocks (MHz)" sea 48MHz.
3. En la página `USB_OTG_FS`, configure el `Mode` como `Device_Only`, y los pines predeterminados son `PA11` y `PA12`.
4. En la página `USB_DEVICE`, configure `Class For FS IP` como `Commmunication Device Class (Virtual Port Com)`.

### Configuración interna del código

Para implementar la función de retroalimentación de datos, solo necesita agregar una línea en la función `CDC_Receive_FS` del archivo `usbd_cdc_if.c`:

```c title="usbd_cdc_if.c"
CDC_Transmit_FS(Buf,*Len); // Devuelve los mismos datos
```

### Prueba

Abra el Administrador de dispositivos para ver si el dispositivo se ha mostrado. Si no se encuentra el dispositivo o hay un signo de exclamación amarillo, descargue el controlador de la página web de ST [**STM32 Virtual COM Port Driver**](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html).

Si ha instalado el controlador pero aún no se puede reconocer correctamente, intente ajustar el `Minimum Heap Size` a `0x600` o superior en CubeMX - `Project Manager` - `Project` - `Linker Settings`.

Abra la herramienta de puerto serie (cualquier velocidad de transmisión) y envíe cualquier carácter. Devolverá el mismo carácter.

## Referencias y agradecimientos

- [STM32 utiliza CubeMX HAL para generar rápidamente el proyecto USBVCP Virtual Serial Port](https://blog.csdn.net/yxy244/article/details/102620249)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.