# Comunicación Lora - Módulo ATK-LORA-01 basado en Atom de Elecrow

El ATK-LORA-01 es un módulo inalámbrico LORA de larga distancia de tamaño pequeño, baja potencia y bajo consumo de energía. El diseño del módulo utiliza el chip de espectro ensanchado SX1278 de frecuencia ISM eficiente. La frecuencia de trabajo del módulo está en el rango de 410 MHz a 441 MHz, con un paso de canal de 1 MHz y un total de 32 canales. Se pueden modificar varios parámetros como la velocidad de transmisión, la potencia de transmisión, la velocidad aérea y el modo de trabajo a través de comandos AT, y también se admite la función de actualización de firmware.

## Parámetros básicos del módulo

- Frecuencia de trabajo: 410-441 MHz, 32 canales
- Banda industrial: Banda predeterminada de fábrica de 433 MHz sin necesidad de solicitud
- Velocidad inalámbrica: 6 niveles ajustables (0.3, 1.2, 2.4, 4.8, 9.6, 19.2 Kbps)
- Modo de comunicación: Puerto serie TTL, puerto serie UART, 8N1, 8E1, 8O1, 8 tipos de velocidad de baudios de 1200 a 115200 (predeterminado 9600, 8N1)
- Potencia de transmisión: 100 mW (20 dB), 4 niveles ajustables (0-3), cada nivel aumenta o disminuye aproximadamente 3 dBm
- Voltaje de trabajo: 3.3-5V
- Corriente de trabajo: 2.3uA-118mA
  - Transmisión: 118 mA (20 dBm, 100 mW, voltaje de 5V)
  - Recepción: 17 mA (modo 0, modo 1), mínimo de aproximadamente 2.3uA (modo 2+2S de activación)
- Temperatura de trabajo: -40~85℃
- Sensibilidad de recepción de hasta -136dBm, distancia de transmisión de 3000 metros
- Doble FIFO anular de 512 bytes

## Definición de interfaces

| Nombre | Modo de IO      | Descripción                                                                 |
| ------ | -------------- | --------------------------------------------------------------------------- |
| MD0    | Entrada        | Configuración para ingresar parámetros; al encenderse, se combina con el pin AUX para ingresar al modo de actualización de firmware |
| AUX    | ① Salida; ② Entrada | ① Se utiliza para indicar el estado de funcionamiento del módulo y despertar al MCU externo; ② Al encenderse, se combina con el pin MD0 para ingresar al modo de actualización de firmware |
| RXD    | Entrada        | Entrada de puerto serie TTL, conectada al pin de salida TXD externo             |
| TXD    | Salida         | Salida de puerto serie TTL, conectada al pin de entrada RXD externo             |
| GND    |                | Conexión a tierra                                                            |
| VCC    |                | Entrada de alimentación de 3.3~5V DC                                           |

Notas:

1. El nivel de voltaje de los pines del módulo es de 3.3V, se requiere una adaptación de nivel de voltaje para comunicarse con un microcontrolador de 5V.
2. El módulo de puerto serie inalámbrico es de nivel TTL, por favor, conéctelo a un MCU de nivel TTL.

## Configuración de modos

Los pines MD0 y AUX tienen dos funciones, según su combinación se ingresa a diferentes estados. Cuando se enciende el módulo por primera vez, el pin AUX está en modo de entrada. Si los pines MD0 y AUX están conectados simultáneamente a un nivel alto de 3.3V TTL y se mantienen durante 1 segundo (sin cambios en el nivel del pin), el módulo ingresará al modo de actualización de firmware y esperará la actualización del firmware. De lo contrario, ingresará al modo de comunicación inalámbrica (el pin AUX volverá a estar en modo de salida para indicar el estado de funcionamiento del módulo).

Los pines MD0 y AUX tienen una resistencia interna de pull-down y están en nivel bajo cuando no están conectados. Se vuelven a nivel alto a 3.3V TTL cuando se conectan.

| Función            | Descripción                | Método de acceso                    |
| ------------------ | ------------------------- | ----------------------------------- |
| Función de ajuste  | Configuración de parámetros del módulo (comandos AT) | Después de encender, AUX en flotante, MD0 en alto |
| Función de comunicación | Utilizada para la comunicación inalámbrica | Después de encender, AUX en flotante, MD0 en flotante |
| Función de actualización de firmware | Utilizada para la actualización del firmware | Después de encender, AUX en alto, MD0 en alto, mantener durante 1s |

En el modo de comunicación inalámbrica, el pin AUX es de salida y se utiliza para indicar el estado de funcionamiento del módulo.

## Configuración de funciones

En la sección "Función de ajuste", el puerto serie debe configurarse con los siguientes parámetros: velocidad de transmisión "115200", bits de parada "1", bits de datos "8", paridad "ninguna", y se deben configurar los parámetros de funcionamiento del módulo mediante comandos AT. Consulte la siguiente tabla de comandos AT como referencia a través del software de configuración:

| Comando       | Función                       |
| ------------- | ----------------------------- |
| AT            | Prueba de respuesta del módulo |
| AT+MODEL?     | Consulta del modelo del dispositivo |
| AT+CGMR?      | Obtención del número de versión del software |
| AT+UPDATE     | Consulta si el dispositivo está en modo de actualización de firmware |
| ATE1          | Eco de comandos                |
| ATE0          | Sin eco de comandos            |
| AT+RESET      | Reinicio del módulo            |
| AT+DEFAULT    | Restauración de la configuración de fábrica |
| AT+FLASH=     | Guardar parámetros              |
| AT+ADDR=?     | Consulta del rango de direcciones de configuración del dispositivo |
| AT+ADDR?      | Consulta de la dirección del dispositivo |
| AT+ADDR=      | Configuración de la dirección del dispositivo |
| AT+TPOWER=?   | Consulta del rango de configuración de potencia de transmisión |
| AT+TPOWER?    | Consulta de la potencia de transmisión |
| AT+TPOWER=    | Configuración de la potencia de transmisión |
| AT+CWMODE=?   | Consulta del rango de modos de trabajo configurables |
| AT+CWMODE?    | Consulta del modo de trabajo |
| AT+CWMODE=    | Configuración del modo de trabajo |
| AT+TMODE=?    | Consulta del rango de estados de transmisión configurables |
| AT+TMODE?     | Consulta del estado de transmisión |
| AT+TMODE=     | Configuración del estado de transmisión |
| AT+WLRATE=?   | Consulta del rango de velocidad inalámbrica y configuración de canal |
| AT+WLRATE?    | Consulta de la velocidad inalámbrica y el canal |
| AT+WLRATE=    | Configuración de la velocidad inalámbrica y el canal |
| AT+WLTIME=?   | Consulta del rango de tiempo de suspensión configurado |
| AT+WLTIME?    | Consulta del tiempo de suspensión |
| AT+WLTIME=    | Configuración del tiempo de suspensión |
| AT+UART=?     | Consulta del rango de configuración del puerto serie |
| AT+UART?      | Consulta de la configuración del puerto serie |
| AT+UART=      | Configuración del puerto serie |

Cuando se sale de la función de configuración (MD0=0), el módulo volverá a configurar los parámetros. Durante el proceso de configuración, AUX se mantiene en nivel alto y después de completar la configuración, se establece en nivel bajo, indicando que el módulo ha vuelto al estado de inactividad.

## Tiempo de suspensión

El tiempo de suspensión es el intervalo de escucha para el receptor y el tiempo de transmisión continua del código de activación para el transmisor. Cuando el modo de funcionamiento del módulo está en "modo de activación", se agregará automáticamente el código de activación de tiempo de suspensión antes de los datos del usuario. Cuando el modo de funcionamiento del módulo está en "modo de ahorro de energía", el tiempo de suspensión configurado se convierte en el intervalo de escucha.

## Modo del dispositivo

### Modo general (Modo 0)

- Transmisión: El módulo recibe los datos del usuario desde el puerto serie y transmite paquetes de datos inalámbricos de 58 bytes. Cuando los datos de entrada del usuario alcanzan los 58 bytes, el módulo iniciará la transmisión inalámbrica. En este momento, el usuario puede seguir ingresando los datos que desea transmitir. Si el número de bytes que el usuario desea transmitir es menor a 58, el módulo esperará 1 byte de tiempo. Si no se ingresan más datos del usuario, se considera que los datos han terminado y el módulo transmitirá todos los datos a través de la radiofrecuencia. Cuando el módulo comienza a enviar el primer paquete de datos del usuario, el pin AUX se establecerá en nivel alto. Después de que el módulo haya transmitido todos los datos a través del chip RF y haya iniciado la transmisión, el pin AUX se establecerá en nivel bajo. Esto indica que se ha completado la transmisión del último paquete de datos inalámbricos y el usuario puede seguir ingresando datos de hasta 512 bytes. Los paquetes de datos enviados en el modo general solo pueden ser recibidos por módulos receptores en el modo general o en el modo de activación.
- Recepción: El módulo mantiene la función de recepción inalámbrica abierta y puede recibir paquetes de datos enviados desde el modo general o el modo de activación. Después de recibir un paquete de datos, el pin AUX del módulo se establecerá en nivel alto. Después de un retraso de 2-3 ms, el módulo comenzará a enviar los datos inalámbricos a través del pin TXD del puerto serie. Después de que se hayan enviado todos los datos inalámbricos a través del puerto serie, el pin AUX del módulo se establecerá en nivel bajo.

### Modo de activación (Modo 1)

- Transmisión: Las condiciones para iniciar la transmisión de paquetes de datos son las mismas que en el modo general, con la única diferencia de que el módulo agregará automáticamente un código de activación (tiempo de suspensión) antes de cada paquete de datos. La longitud del código de activación depende del tiempo de suspensión configurado en los parámetros del usuario. El propósito del código de activación es despertar a los módulos receptores que están en modo de ahorro de energía. Por lo tanto, los datos transmitidos en el modo de activación pueden ser recibidos por módulos en el modo general, modo 1 y modo 2.
- Recepción: Es igual al modo general.

### Modo de ahorro de energía (Modo 2)

- Transmisión: El módulo está en estado de suspensión y el puerto serie está cerrado, por lo que este modo no tiene la función de transmisión inalámbrica.
- Recepción: En el modo de ahorro de energía, se requiere que el transmisor funcione en modo de activación. El módulo inalámbrico escucha continuamente el código de activación. Una vez que recibe un código de activación válido, el módulo se mantendrá en estado de recepción y esperará a que se complete la recepción del paquete de datos completo. Luego, el pin AUX se establecerá en nivel alto y después de un retraso de 2-3 ms, se abrirá el puerto serie y se enviarán los datos inalámbricos recibidos a través del pin TXD. Después de completar la transmisión, el pin AUX se establecerá en nivel bajo. El módulo inalámbrico continuará en el estado de "suspensión-escucha" y, al configurar diferentes tiempos de activación, el módulo tendrá diferentes tiempos de respuesta de recepción y consumo de energía. Los usuarios deben encontrar un equilibrio entre el tiempo de retraso de comunicación y el consumo promedio de energía.

### Modo de intensidad de señal (Modo 3)

El modo de intensidad de señal permite ver la intensidad de la señal de ambas partes de la comunicación y proporciona una referencia para evaluar la calidad de la comunicación.

- Transmisión: Igual al modo general.
- Recepción: Muestra información sobre la intensidad de la señal.

![](https://img.wiki-power.com/d/wiki-media/img/20220118110058.png)

SNR: Relación señal-ruido (cuanto mayor, más estable), RSSI: Indicador de intensidad de señal recibida (cuanto mayor, más estable)

## Modo de comunicación

- Transmisión transparente: Por ejemplo, el dispositivo A envía datos de 5 bytes AA BB CC DD EE al dispositivo B, y el dispositivo B recibe los datos AA BB CC DD EE (transmisión transparente, para la comunicación entre dispositivos con la misma dirección y el mismo canal de comunicación, los datos del usuario pueden ser caracteres o en forma de datos hexadecimales).
  - Punto a punto
  - Punto a múltiple
  - Escucha de difusión
- Transmisión dirigida: Por ejemplo, el dispositivo A (dirección: 0x1400, canal: 0x17 (canal 23, 433 MHz)) necesita enviar datos AA BB CC al dispositivo B (dirección: 0x1234, canal: 0x10 (canal 16, 426 MHz)). El formato de comunicación es: 12 34 10 AA BB CC, donde 1234 es la dirección del módulo B y 10 es el canal. Por lo tanto, el módulo B puede recibir AA BB CC. De manera similar, si el dispositivo B necesita enviar datos AA BB CC al dispositivo A, el formato de comunicación sería: 14 00 17 AA BB CC, y el dispositivo A puede recibir AA BB CC (transmisión dirigida, permite la comunicación entre dispositivos con direcciones y canales diferentes, el formato de datos es hexadecimal, formato de envío: dirección de bits altos + dirección de bits bajos + canal + datos del usuario).
  - Punto a múltiple
  - Escucha de difusión

## Transmisión transparente

### Punto a punto

![](https://img.wiki-power.com/d/wiki-media/img/20220118110614.png)

- Dos módulos con la misma dirección, el mismo canal y la misma velocidad inalámbrica (no la velocidad de la interfaz serie). Un módulo envía y el otro recibe (debe haber un emisor y un receptor).
- Cada módulo puede enviar y recibir.
- Los datos son completamente transparentes, lo que se envía es lo que se recibe.

|          | Módulo emisor | Módulo receptor |
| -------- | ------------- | --------------- |
| Cantidad | 1             | 1               |
| Contenido | Datos        | Datos           |

Por ejemplo:

Los dispositivos A y B tienen la dirección 0x1234, el canal es 0x12 y la velocidad es la misma.  
Dispositivo A envía: AA BB CC DD  
Dispositivo B recibe: AA BB CC DD

La transmisión transparente es simple, solo se utiliza el módulo Lora como una interfaz serie. El dispositivo A envía datos a través de la interfaz serie y el dispositivo B los recibe de la misma manera.

### Punto a muchos

![](https://img.wiki-power.com/d/wiki-media/img/20220118110709.png)

- Módulos con la misma dirección, el mismo canal y la misma velocidad inalámbrica (no la velocidad de la interfaz serie), cualquier módulo puede enviar y los demás pueden recibir.
- Cada módulo puede enviar y recibir.
- Los datos son completamente transparentes, lo que se envía es lo que se recibe.

|          | Módulo emisor | Módulo receptor |
| -------- | ------------- | --------------- |
| Cantidad | 1             | N               |
| Contenido | Datos        | Datos           |

La diferencia con el punto a punto es que puede haber varios módulos receptores.

Por ejemplo:
Los dispositivos A~F tienen la dirección 0x1234, el canal es 0x12 y la velocidad es la misma.  
Dispositivo A envía: AA BB CC DD  
Dispositivos B~F reciben: AA BB CC DD

### Transmisión y escucha en modo de difusión

![](https://img.wiki-power.com/d/wiki-media/img/20220118110853.png)

- Si la dirección del módulo es 0xFFFF, el módulo está en modo de transmisión y escucha en modo de difusión. Los datos enviados pueden ser recibidos por todos los demás módulos en el mismo canal y velocidad (difusión); al mismo tiempo, puede escuchar la transmisión de datos de todos los demás módulos en el mismo canal y velocidad (escucha).
- No es necesario que las direcciones sean iguales en la transmisión y escucha en modo de difusión.

|          | Módulo emisor | Módulo receptor |
| -------- | ------------- | --------------- |
| Cantidad | 1             | N               |
| Contenido | Datos        | Datos           |

La diferencia con el punto a muchos es que las direcciones pueden ser diferentes.

Por ejemplo:
El dispositivo A tiene la dirección 0xFFFF, los dispositivos B~F tienen direcciones diferentes. Los dispositivos B y C tienen la dirección 0x1234, los dispositivos D, E y F tienen la dirección 0x5678. Todos los dispositivos A~F tienen la misma velocidad.  
Difusión:  
Dispositivo A difunde: AA BB CC DD  
Dispositivos B~F reciben: AA BB CC DD  
Escucha:  
Dispositivo B envía a C: AA BB CC DD  
Dispositivo A escucha: AA BB CC DD  
Dispositivo D envía a E y F: 11 22 33 44  
Dispositivo A escucha: 11 22 33 44

## Transmisión direccionada

### Punto a punto

- Al enviar, el módulo puede cambiar la dirección y el canal, el usuario puede especificar que los datos se envíen a cualquier dirección y canal.
- Puede lograr la formación de redes y la función de repetidor.

|          | Módulo emisor       | Módulo receptor |
| -------- | ------------------ | --------------- |
| Cantidad | 1                  | 1               |
| Contenido | Dirección+Canal+Datos | Datos           |

La diferencia con el punto a punto transparente es que la dirección y el canal del módulo pueden cambiar, pero la velocidad sigue siendo la misma.

![](https://img.wiki-power.com/d/wiki-media/img/20220118111903.png)

Por ejemplo:
  
Dispositivo A: Dirección 0X1234, Canal 0X17;
Dispositivo B: Dirección 0xABCD, Canal 0X01;
Dispositivo C: Dirección 0X1256, Canal 0x13.

Dispositivo A envía: AB CD 01 AA BB CC DD
Dispositivo B recibe: AA BB CC DD
Dispositivo C recibe: Ninguno

Dispositivo A envía: 12 56 13 AA BB CC DD
Dispositivo B recibe: Ninguno
Dispositivo C recibe: AA BB CC DD

#### Prueba sin código

Prepara 2 adaptadores USB a TTL y 2 módulos LoRa. Conéctalos a los adaptadores USB a TTL (alimentación, tierra común, conexión TX/RX). Después de conectar los dos módulos LoRa a VCC a través de MD0, conéctalos al puerto USB de la computadora. Abre el software de configuración y configura los siguientes parámetros:

Dispositivo A:

- Modo general
- Transmisión direccionada
- **Velocidad de baudios: 115200 (debe ser 115200)**
- Bit de paridad: Ninguno
- Velocidad aérea: 19.2k
- Tiempo de suspensión: 1s
- **Dirección del módulo: 0**
- **Canal de comunicación: 0**
- Potencia de transmisión: 20dBm

Dispositivo B:

- Modo general
- Transmisión direccionada
- **Velocidad de baudios: 115200 (debe ser 115200)**
- Bit de paridad: Ninguno
- Velocidad aérea: 19.2k
- Tiempo de suspensión: 1s
- **Dirección del módulo: 65534**
- **Canal de comunicación: 10**
- Potencia de transmisión: 20dBm

Después de configurar, haz clic en `Guardar configuración` y **desconecta MD0 y luego apaga la alimentación**.

Vuelve a encender los dos módulos, abre el software de configuración y selecciona la opción `HEX` (hexadecimal) tanto para enviar como para recibir.

En el área de envío de A, ingresa `FF FE 0A 11 12 13 14`, haz clic en enviar y podrás recibir `11 12 13 14` en el área de recepción de B; o en el área de envío de B, ingresa `00 00 00 11 12 13` y podrás recibir `11 12 13` en el área de recepción de A.

En este caso, `FF FE` es el número hexadecimal de la dirección B, que es 65534, y el canal es 10 (en hexadecimal es `0A`). Los datos enviados son `11 12 13 14`. De manera similar, los datos enviados por B incluyen la dirección de A `00 00`, el canal `00` y los datos `11 12 13`. El formato de los datos enviados es **dirección de alta orden + dirección de baja orden + canal + datos de usuario**.

#### Prueba con código

La transmisión direccionada punto a punto solo agrega un byte de dirección en comparación con la transmisión punto a punto. Puedes definirlo de la siguiente manera:

```c title="main.c"
/* USER CODE BEGIN PV */
uint8_t B_Addr[2] = { 0xFF, 0xFE };
uint8_t B_Chan[1] = { 0x0A };
/* USER CODE END PV */
```

Después de configurar el código con la biblioteca HAL, antes de enviar los datos, envía el byte de dirección:

```c title="main.c"
HAL_UART_Transmit(&huart1, B_Addr, 2, 0xFFFF);
HAL_UART_Transmit(&huart1, B_Chan, 1, 0xFFFF);
```

De esta manera, el dispositivo receptor (dispositivo B) puede recibir un marco de datos enviado por el dispositivo A (sin incluir el byte de dirección).

### Monitoreo de difusión

![](https://img.wiki-power.com/d/wiki-media/img/20220118112544.png)

- Si la dirección del módulo es 0xFFFF, el módulo está en modo de monitoreo de difusión, lo que significa que los datos enviados pueden ser recibidos por todos los demás módulos que tengan la misma velocidad y canal (difusión); al mismo tiempo, puede monitorear la transmisión de datos de todos los módulos en la misma velocidad y canal (monitoreo);
- No es necesario que las direcciones sean iguales para el monitoreo de difusión.
- La dirección del canal se puede configurar. Cuando la dirección es 0xFFFF, está en modo de difusión; de lo contrario, está en modo de transmisión direccionada.

|          | Módulo de envío  | Módulo de recepción |
| -------- | ---------------- | ------------------ |
| Cantidad | 1                | N                  |
| Contenido de transmisión | 0xFFFF+canal+datos | Datos |

Por ejemplo:

```markdown
Dispositivo A dirección 0xFFFF canal 0x12;
Dispositivos B y C dirección 0x1234, canal 0x13;
Dispositivo D dirección 0xAB00, canal 0x01;
Dispositivo E dirección 0xAB01, canal 0x12;
Dispositivo F dirección 0xAB02, canal 0x12;

Dispositivo A emite en broadcast: FF FF 13 AA BB CC DD
Dispositivos B y C reciben: AA BB CC DD

Dispositivo A envía: AB 00 01 11 22 33 44
Solo el dispositivo D recibe: 11 22 33 44

Dispositivo E envía: AB 02 12 66 77 88 99
Dispositivo F recibe: 66 77 88 99
Dispositivo A escucha: 66 77 88 99

## Referencias y Agradecimientos

- [Módulo LORA ATK-LORA-01](http://www.openedv.com/docs/modules/iot/atk-lora-01.html)
- [Tutorial de uso del módulo LORA ATK-LORA de DFRobot](https://www.bilibili.com/video/BV1D44y1t7bn)
- [Descarga de datos y enlaces de discusión técnica del módulo LORA ATK-LORA-01 de DFRobot](http://www.openedv.com/thread-309019-1-1.html)
- [Método de prueba para la transmisión de datos en modo direccionado general con dos módulos LORA (prueba con una computadora)](http://www.openedv.com/forum.php?mod=viewthread&tid=288951)
- [Módulo inalámbrico ATK-LORA-01 solo recibe 00](http://www.openedv.com/forum.php?mod=viewthread&tid=328190&highlight=ATK-LORA-01)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```


> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.