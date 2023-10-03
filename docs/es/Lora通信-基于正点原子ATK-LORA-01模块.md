# Comunicación Lora - Módulo ATK-LORA-01 de Atom de Punto

El ATK-LORA-01 es un módulo de comunicación inalámbrica LORA de larga distancia de bajo consumo, bajo consumo de energía y alto rendimiento con un tamaño pequeño. El diseño del módulo utiliza el chip de expansión de espectro SX1278 de banda ISM eficiente, y la frecuencia de trabajo del módulo es de 410 MHz a 441 MHz, con un canal de paso de 1 MHz y un total de 32 canales. Se pueden modificar en línea varios parámetros, como la velocidad de transmisión de la interfaz serie, la potencia de transmisión, la velocidad aérea, el modo de trabajo, etc. mediante comandos AT, y también se admite la función de actualización de firmware.

## Parámetros básicos del módulo

- Frecuencia de trabajo: 410-441 MHz, 32 canales
- Banda industrial: banda libre de 433 MHz de fábrica
- Velocidad inalámbrica: 6 niveles ajustables (0,3, 1,2, 2,4, 4,8, 9,6, 19,2 Kbps)
- Modo de comunicación: TTL de serie, puerto serie UART, 8N1, 8E1, 8O1, desde 1200-115200, un total de 8 velocidades de transmisión (predeterminado 9600, 8N1)
- Potencia de transmisión: 100 mW (20 dB), 4 niveles ajustables (0-3), cada nivel aumenta o disminuye aproximadamente 3 dBm
- Voltaje de trabajo: 3,3-5V
- Corriente de trabajo: 2,3uA-118mA
  - Transmisión: 118 mA (20 dBm 100 mW voltaje 5V)
  - Recepción: 17 mA (modo 0, modo 1), mínimo de aproximadamente 2,3 uA (modo 2+2S de activación)
- Temperatura de trabajo: -40 ~ 85 ℃
- Sensibilidad de recepción de hasta -136 dBm, distancia de transmisión de 3000 metros
- Doble FIFO circular de 512

## Definición de interfaz

| Nombre | Modo IO        | Descripción                                                                 |
| ------ | -------------- | --------------------------------------------------------------------------- |
| MD0    | Entrada        | Configuración de parámetros de entrada; en el encendido, entra en el modo de actualización de firmware en combinación con el pin AUX |
| AUX    | ① Salida; ② Entrada | ① Se utiliza para indicar el estado de funcionamiento del módulo y despertar el MCU externo; ② En el encendido, entra en el modo de actualización de firmware en combinación con el pin MD0 |
| RXD    | Entrada        | Entrada de serie TTL, conectada al pin de salida TXD externo                  |
| TXD    | Salida         | Salida de serie TTL, conectada al pin de entrada RXD externo                  |
| GND    |                | Tierra                                                                      |
| VCC    |                | Entrada de alimentación DC3.3~5V                                             |

Notas:

1. El nivel de voltaje de los pines del módulo es de 3,3 V, y se requiere una adaptación de nivel de voltaje para comunicarse con un MCU de 5 V.
2. El módulo de comunicación inalámbrica es de nivel TTL, por lo que debe conectarse a un MCU de nivel TTL.

## Configuración del modo

Los pines MD0 y AUX tienen dos funciones, y se ingresa a diferentes estados según la combinación de ambos. Cuando el módulo se enciende por primera vez, el pin AUX está en modo de entrada. Si los pines MD0 y AUX se conectan simultáneamente a un nivel alto de 3,3 V TTL y se mantienen durante 1 segundo (sin cambios en el nivel de los pines), el módulo entrará en modo de actualización de firmware y esperará la actualización del firmware. De lo contrario, entra en el modo de comunicación inalámbrica (el pin AUX volverá al modo de salida para indicar el estado de funcionamiento del módulo).

Los pines MD0 y AUX tienen una resistencia interna de pull-down y están en nivel bajo si no se conectan. Si se conectan, están en nivel alto de 3,3 V TTL.

| Función       | Descripción              | Método de acceso                   |
| ------------- | ------------------------| ---------------------------------- |
| Configuración | Configuración de parámetros del módulo (comandos AT) | Después de encender, AUX en flotante, MD0 en alto |
| Comunicación  | Utilizado para comunicación inalámbrica | Después de encender, AUX en flotante, MD0 en flotante |
| Actualización de firmware | Utilizado para actualizar el firmware | Después de encender, AUX en alto, MD0 en alto, mantener por 1s |

En el modo de comunicación inalámbrica, el pin AUX es de salida y se utiliza para indicar el estado de trabajo del módulo.

## Configuración de funciones

En "Configuración de funciones", el puerto serie debe configurarse como ASDASD: velocidad de transmisión "115200", bits de parada "1", bits de datos "8", paridad "ninguna", y se deben configurar los parámetros de trabajo del módulo mediante comandos AT. Consulte la siguiente tabla de comandos AT como referencia al configurar el software:

| Comando      | Función                       |
| ------------ | -----------------------------|
| AT           | Prueba de respuesta del módulo |
| AT+MODEL?    | Consulta del modelo del dispositivo |
| AT+CGMR?     | Obtención del número de versión del software |
| AT+UPDATE    | Consulta si el dispositivo está en modo de actualización de firmware |
| ATE1         | Eco de comandos                |
| ATE0         | Sin eco de comandos            |
| AT+RESET     | Reinicio del módulo            |
| AT+DEFAULT   | Restablecimiento de la configuración de fábrica |
| AT+FLASH=    | Guardar parámetros              |
| AT+ADDR=?    | Consulta del rango de direcciones de configuración del dispositivo |
| AT+ADDR?     | Consulta de la dirección del dispositivo |
| AT+ADDR=     | Configuración de la dirección del dispositivo |
| AT+TPOWER=?  | Consulta del rango de configuración de la potencia de transmisión |
| AT+TPOWER?   | Consulta de la potencia de transmisión |
| AT+TPOWER=   | Configuración de la potencia de transmisión |
| AT+CWMODE=?  | Consulta del rango de configuración del modo de trabajo |
| AT+CWMODE?   | Consulta del modo de trabajo |
| AT+CWMODE=   | Configuración del modo de trabajo |
| AT+TMODE=?   | Consulta del rango de configuración del estado de envío |
| AT+TMODE?    | Consulta del estado de envío |
| AT+TMODE=    | Configuración del estado de envío |
| AT+WLRATE=?  | Consulta del rango de configuración de la velocidad inalámbrica y el canal |
| AT+WLRATE?   | Consulta de la velocidad inalámbrica y el canal |
| AT+WLRATE=   | Configuración de la velocidad inalámbrica y el canal |
| AT+WLTIME=?  | Consulta del rango de configuración del tiempo de inactividad |
| AT+WLTIME?   | Consulta del tiempo de inactividad |
| AT+WLTIME=   | Configuración del tiempo de inactividad |
| AT+UART=?    | Consulta del rango de configuración del puerto serie |
| AT+UART?     | Consulta de la configuración del puerto serie |
| AT+UART=     | Configuración del puerto serie |

Cuando se sale de la función de configuración (MD0=0), el módulo volverá a configurar los parámetros. Durante el proceso de configuración, AUX se mantendrá en alto y después de completar la configuración, se establecerá en bajo, lo que indica que el módulo ha vuelto al estado inactivo.

## Tiempo de suspensión

El tiempo de suspensión es el intervalo de escucha para el receptor y el tiempo de transmisión continua del código de activación para el emisor. Cuando el modo de trabajo del módulo está en "modo de activación", se agregará automáticamente un código de activación de tiempo de suspensión antes de los datos del usuario. Cuando el modo de trabajo del módulo está en "modo de ahorro de energía", el tiempo de suspensión configurado se convierte en el intervalo de escucha.

## Modo de dispositivo

### Modo general (modo 0)

- Emisión: El módulo recibe los datos del usuario desde el puerto serie y emite un paquete de datos inalámbrico de 58 bytes. Cuando los datos de entrada del usuario alcanzan los 58 bytes, el módulo iniciará la transmisión inalámbrica. Si el usuario necesita transmitir menos de 58 bytes, el módulo esperará un byte. Si no hay más datos de entrada del usuario, se considera que los datos han terminado y el módulo enviará todos los datos a través de la radio. Cuando el módulo comienza a enviar el primer paquete de datos del usuario, el pin AUX emitirá una señal de alto. Después de que el módulo haya transmitido todos los datos a través del chip RF y haya iniciado la transmisión, AUX emitirá una señal de bajo. Esto indica que se ha enviado el último paquete de datos inalámbricos y que el usuario puede seguir ingresando datos de hasta 512 bytes. Los paquetes de datos enviados por el modo general solo pueden ser recibidos por los módulos de recepción en modo general y de activación.
- Recepción: El módulo siempre está activado para recibir datos inalámbricos y puede recibir paquetes de datos enviados por el modo general y el modo de activación. Después de recibir el paquete de datos, AUX emitirá una señal de alto. Después de un retraso de 2-3 ms, el módulo comenzará a enviar los datos inalámbricos a través del pin TXD del puerto serie. Después de que se hayan enviado todos los datos inalámbricos a través del puerto serie, AUX emitirá una señal de bajo.

### Modo de activación (modo 1)

- Emisión: Las condiciones para iniciar la transmisión de paquetes de datos son las mismas que en el modo general, con la única diferencia de que el módulo agregará automáticamente un código de activación de tiempo de suspensión antes de cada paquete de datos (el código de activación de tiempo de suspensión tiene una longitud que depende del tiempo de suspensión configurado por el usuario). El propósito del código de activación de tiempo de suspensión es activar el modo de ahorro de energía del módulo receptor. Por lo tanto, los datos enviados en el modo de activación pueden ser recibidos por el modo general y los modos 1 y 2 de recepción.
- Recepción: Es igual que en el modo general.

### Modo de ahorro de energía (modo 2)

- Emisión: El módulo está en estado de suspensión y el puerto serie está cerrado, por lo que no puede recibir datos del MCU externo. Por lo tanto, este modo no tiene función de transmisión inalámbrica.
- Recepción: En el modo de ahorro de energía, el emisor debe estar en modo de activación. El módulo inalámbrico escuchará el código de activación de forma periódica. Una vez que se recibe un código de activación válido, el módulo permanecerá en modo de recepción hasta que se complete la recepción de todo el paquete de datos válido. Luego, AUX emitirá una señal de alto y, después de un retraso de 2-3 ms, el módulo abrirá el puerto serie y enviará los datos inalámbricos recibidos a través del pin TXD. Después de que se hayan enviado todos los datos inalámbricos a través del puerto serie, AUX emitirá una señal de bajo. El módulo inalámbrico continuará trabajando en el modo "suspensión-escucha". Al configurar diferentes tiempos de activación, el módulo tendrá diferentes tiempos de respuesta y consumo de energía. Los usuarios deben encontrar un equilibrio entre el tiempo de retraso de comunicación y el consumo de energía promedio.

### Modo de intensidad de señal (modo 3)

El modo de intensidad de señal se utiliza para ver la intensidad de la señal de ambas partes de la comunicación y evaluar la calidad de la comunicación.

- Emisión: Es igual que en el modo general.
- Recepción: Se muestra la información de la intensidad de la señal.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220118110058.png)

SNR: relación señal-ruido (cuanto mayor sea, más estable), RSSI: indicador de intensidad de señal recibida (cuanto mayor sea, más estable).

## Modo de comunicación

- Transmisión transparente: Por ejemplo, el dispositivo A envía datos de 5 bytes AA BB CC DD EE al dispositivo B, y el dispositivo B recibirá los datos AA BB CC DD EE. (Transmisión transparente, para la comunicación entre dispositivos con la misma dirección y canal de comunicación, los datos del usuario pueden ser caracteres o datos en formato hexadecimal).
  - Punto a punto
  - Punto a múltiples
  - Escucha de difusión
- Transmisión dirigida: Por ejemplo, el dispositivo A (dirección: 0x1400, canal: 0x17 (canal 23, 433 MHz)) necesita enviar datos AA BB CC al dispositivo B (dirección: 0x1234, canal: 0x10 (canal 16, 426 MHz)). El formato de comunicación es: 12 34 10 AA BB CC, donde 1234 es la dirección del módulo B y 10 es el canal. El módulo B recibirá AA BB CC. De manera similar, si el dispositivo B necesita enviar datos AA BB CC al dispositivo A, el formato de comunicación es: 14 00 17 AA BB CC, y el dispositivo A recibirá AA BB CC. (Transmisión dirigida, para la comunicación entre dispositivos con direcciones y canales de comunicación diferentes, el formato de datos es hexadecimal, el formato de envío es: dirección de bits altos + dirección de bits bajos + canal + datos de usuario).
  - Punto a múltiples
  - Escucha de difusión

Radio y monitoreo de datos: al establecer la dirección del módulo como 0xFFFF, se puede monitorear la transmisión de datos de todos los módulos en el mismo canal; los datos enviados pueden ser recibidos por cualquier módulo en la misma canal, lo que cumple la función de radiodifusión y monitoreo.

## Modo de transmisión transparente

### Punto a punto

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220118110614.png)

- Dos módulos con la misma dirección, canal y velocidad inalámbrica (no la velocidad de baudios del puerto serie) pueden enviar y recibir datos entre sí (uno envía, el otro recibe).
- Cada módulo puede enviar / recibir.
- Los datos son completamente transparentes, lo que se envía es lo que se recibe.

|          | Módulo emisor | Módulo receptor |
| -------- | ------------- | --------------- |
| Cantidad | 1             | 1               |
| Contenido de transmisión | Datos | Datos |

Por ejemplo:

Los dispositivos A y B tienen la dirección 0x1234, el canal es 0x12 y la velocidad es la misma.  
El dispositivo A envía: AA BB CC DD  
El dispositivo B recibe: AA BB CC DD

La transmisión transparente es simple, solo se usa el módulo Lora como un puerto serie, el dispositivo A envía datos a través del puerto serie y el dispositivo B puede recibirlos a través del puerto serie, y viceversa.

### Punto a varios

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220118110709.png)

- Los módulos con la misma dirección, canal y velocidad inalámbrica (no la velocidad de baudios del puerto serie) pueden enviar y recibir datos entre sí (uno envía, varios reciben).
- Cada módulo puede enviar / recibir.
- Los datos son completamente transparentes, lo que se envía es lo que se recibe.

|          | Módulo emisor | Módulo receptor |
| -------- | ------------- | --------------- |
| Cantidad | 1             | N               |
| Contenido de transmisión | Datos | Datos |

La diferencia con el punto a punto es que varios módulos pueden recibir.

Por ejemplo:
Los dispositivos A a F tienen la dirección 0x1234 y el canal es 0x12, y la velocidad es la misma.  
El dispositivo A envía: AA BB CC DD  
Los dispositivos B a F reciben: AA BB CC DD

### Radiodifusión y monitoreo

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220118110853.png)

- Si la dirección del módulo es 0xFFFF, el módulo está en modo de radiodifusión y monitoreo, los datos enviados pueden ser recibidos por todos los demás módulos en el mismo canal y velocidad (radiodifusión); al mismo tiempo, se puede monitorear la transmisión de datos de todos los módulos en el mismo canal y velocidad (monitoreo).
- La radiodifusión y el monitoreo no requieren la misma dirección.

|          | Módulo emisor | Módulo receptor |
| -------- | ------------- | --------------- |
| Cantidad | 1             | N               |
| Contenido de transmisión | Datos | Datos |

La diferencia con el punto a varios es que las direcciones pueden ser diferentes.

Por ejemplo:
El dispositivo A tiene la dirección 0xFFFF, las direcciones de los dispositivos B a F no son todas iguales, las direcciones de los dispositivos B y C son 0x1234, y las direcciones de los dispositivos D, E y F son 0x5678. Todos los dispositivos A a F tienen la misma velocidad.  
Radiodifusión:  
El dispositivo A transmite: AA BB CC DD  
Los dispositivos B a F reciben: AA BB CC DD  
Monitoreo:  
El dispositivo B envía a C: AA BB CC DD  
El dispositivo A monitorea: AA BB CC DD  
El dispositivo D envía a E y F: 11 22 33 44  
El dispositivo A monitorea: 11 22 33 44

## Modo de transmisión direccionado

### Punto a punto

- Al enviar el módulo, se puede modificar la dirección y el canal, y el usuario puede especificar que los datos se envíen a cualquier dirección y canal.
- Se pueden realizar funciones de red y de relé.

|          | Módulo emisor | Módulo receptor |
| -------- | ------------- | --------------- |
| Cantidad | 1             | 1               |
| Contenido de transmisión | Dirección + canal + datos | Datos |



La diferencia con la transmisión punto a punto es que la dirección del módulo y el canal son variables, pero la velocidad sigue siendo la misma.

Por ejemplo:
Dispositivo A con dirección 0X1234 y canal 0X17;
Dispositivo B con dirección 0xABCD y canal 0X01;
Dispositivo C con dirección 0X1256 y canal 0x13.

Dispositivo A envía: AB CD 01 AA BB CC DD
Dispositivo B recibe: AA BB CC DD
Dispositivo C recibe: nada

Dispositivo A envía: 12 56 13 AA BB CC DD
Dispositivo B recibe: nada
Dispositivo C recibe: AA BB CC DD

#### Prueba sin código

Prepara 2 USB a TTL, 2 módulos LoRa. Conéctalos a los USB a TTL (alimentación, tierra común, TX/RX conectados), conecta los dos MD0 a VCC, enchufa los USB a la computadora, abre el software de configuración y configura los siguientes parámetros:

Dispositivo A:

- Modo normal
- Transmisión direccionada
- **Velocidad de transmisión: 115200 (debe ser 115200)**
- Bit de paridad: ninguno
- Velocidad en el aire: 19.2k
- Tiempo de espera: 1s
- **Dirección del módulo: 0**
- **Canal de comunicación: 0**
- Potencia de transmisión: 20dBm

Dispositivo B:

- Modo normal
- Transmisión direccionada
- **Velocidad de transmisión: 115200 (debe ser 115200)**
- Bit de paridad: ninguno
- Velocidad en el aire: 19.2k
- Tiempo de espera: 1s
- **Dirección del módulo: 65534**
- **Canal de comunicación: 10**
- Potencia de transmisión: 20dBm

Después de configurar, haz clic en "Guardar configuración" y **desconecta MD0 y luego desconecta la alimentación**.

Vuelve a encender los dos módulos, abre el software de configuración y marca "HEX" (hexadecimal) tanto en enviar como en recibir.

En el área de envío de A, ingresa "FF FE 0A 11 12 13 14", haz clic en enviar y podrás recibir "11 12 13 14" en el área de recepción de B; o en el área de envío de B, ingresa "00 00 00 11 12 13" y podrás recibir "11 12 13" en el área de recepción de A.

Entre ellos, "FF FE" es el número hexadecimal de la dirección 65534 de B, el canal es 10 (el número hexadecimal es "0A"), y los datos enviados son "11 12 13 14". De manera similar, los datos enviados por B incluyen la dirección de A "00 00", el canal "00" y los datos "11 12 13". El formato de envío de datos es **dirección de alta orden + dirección de baja orden + canal + datos de usuario**.

#### Prueba con código

La transmisión punto a punto solo tiene un byte de dirección más que la transmisión punto a punto transparente. Puedes definirlo de esta manera:

```c title="main.c"
/* USER CODE BEGIN PV */
uint8_t B_Addr[2] = { 0xFF, 0xFE };
uint8_t B_Chan[1] = { 0x0A };
/* USER CODE END PV */
```

Después de configurar el código (entorno de biblioteca HAL), envía el byte de dirección antes de enviar los datos cada vez:

```c title="main.c"
HAL_UART_Transmit(&huart1, B_Addr, 2, 0xFFFF);
HAL_UART_Transmit(&huart1, B_Chan, 1, 0xFFFF);
```

De esta manera, el dispositivo receptor (dispositivo B) puede recibir un marco de datos enviado por A (sin byte de dirección).

### Escucha de difusión

- Si la dirección del módulo es 0xFFFF, el módulo está en modo de escucha de difusión, los datos enviados pueden ser recibidos por todos los demás módulos con la misma velocidad y canal (difusión); al mismo tiempo, se pueden escuchar todas las transmisiones de datos en el mismo canal y velocidad de todos los demás módulos (escucha);
- La escucha de difusión no requiere que las direcciones sean iguales.
- La dirección del canal se puede configurar. Cuando la dirección es 0xFFFF, es el modo de difusión; de lo contrario, es el modo de transmisión direccionada.

|          | Módulo de envío  | Módulo de recepción |
| -------- | ---------------- | -------------------- |
| Cantidad | 1                | N                    |
| Contenido de transmisión | 0xFFFF + canal + datos | Datos                |

Por ejemplo:

Dispositivo A con dirección 0xFFFF y canal 0x12;
Dispositivos B y C con dirección 0x1234 y canal 0x13;
Dispositivo D con dirección 0xAB00 y canal 0x01;
Dispositivo E con dirección 0xAB01 y canal 0x12;
Dispositivo F con dirección 0xAB02 y canal 0x12;

Dispositivo A transmite: FF FF 13 AA BB CC DD
Dispositivos B y C reciben: AA BB CC DD

Dispositivo A envía: AB 00 01 11 22 33 44
Solo el dispositivo D recibe: 11 22 33 44

Dispositivo E envía: AB 02 12 66 77 88 99
Dispositivo F recibe: 66 77 88 99
Dispositivo A escucha: 66 77 88 99

## Referencias y agradecimientos

- [Módulo LORA ATK-LORA-01](http://www.openedv.com/docs/modules/iot/atk-lora-01.html)
- [Tutorial de uso del módulo LORA ATK-LORA de la marca Zhengdianyuan](https://www.bilibili.com/video/BV1D44y1t7bn)
- [Descarga de materiales y enlaces de discusión técnica del módulo LORA ATK-LORA-01 de la marca Zhengdianyuan](http://www.openedv.com/thread-309019-1-1.html)
- [Método de prueba de transmisión de datos en modo general con dos módulos LORA (prueba con una computadora)](http://www.openedv.com/forum.php?mod=viewthread&tid=288951)
- [Módulo inalámbrico de puerto serie ATK-LORA-01 solo recibe 00](http://www.openedv.com/forum.php?mod=viewthread&tid=328190&highlight=ATK-LORA-01)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.