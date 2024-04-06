# Comunicación Lora - Módulo basado en ATK-LORA-01 de Atomic Pi

El ATK-LORA-01 es un módulo inalámbrico Lora de largo alcance, de pequeño tamaño, bajo consumo de energía y alto rendimiento. Este módulo utiliza el eficiente chip de espectro ensanchado SX1278 en la banda de frecuencia ISM. La frecuencia de operación del módulo se encuentra en el rango de 410 MHz a 441 MHz, con pasos de 1 MHz entre canales, lo que da un total de 32 canales. Es posible modificar la velocidad de la interfaz, la potencia de transmisión, la velocidad aérea y varios parámetros más utilizando comandos AT, y además, admite actualizaciones de firmware.

## Parámetros Básicos del Módulo

- Frecuencia de operación: 410-441 MHz, 32 canales
- Banda industrial: Predeterminado de fábrica en 433 MHz, sin necesidad de licencia
- Velocidad inalámbrica: Ajustable en 6 niveles (0.3, 1.2, 2.4, 4.8, 9.6, 19.2 Kbps)
- Modo de comunicación: Interfaz serie TTL, UART serie, configuración 8N1, 8E1, 8O1, con velocidades desde 1200 hasta 115200 (predeterminado: 9600, 8N1)
- Potencia de transmisión: 100 mW (20 dB), ajustable en 4 niveles (0-3), con una variación de aproximadamente 3 dBm por nivel.
- Voltaje de operación: 3.3-5V
- Corriente de operación: 2.3 uA-118 mA
  - Transmisión: 118 mA (20 dBm, 100 mW, voltaje de 5V)
  - Recepción: 17 mA (Modo 0, Modo 1), mínimo de aproximadamente 2.3 uA (Modo 2+2S de despertar)
- Temperatura de operación: -40 a 85°C
- Sensibilidad de recepción de hasta -136 dBm, con un alcance de transmisión de 3000 metros
- Doble FIFO circular de 512 bytes

## Definición de Interfaz

| Nombre | Modo I/O            | Descripción                                                                                                                                                   |
| ------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MD0    | Entrada             | Configuración de parámetros de entrada; junto con el pin AUX entra en modo de actualización de firmware al encenderse                                         |
| AUX    | ① Salida; ② Entrada | ① Indica el estado de funcionamiento del módulo y despierta a un MCU externo; ② Junto con el pin MD0 entra en modo de actualización de firmware al encenderse |
| RXD    | Entrada             | Entrada serie TTL, conectada al pin TXD externo                                                                                                               |
| TXD    | Salida              | Salida serie TTL, conectada al pin RXD externo                                                                                                                |
| GND    |                     | Conexión a tierra                                                                                                                                             |
| VCC    |                     | Entrada de energía de CC 3.3~5V                                                                                                                               |

Notas Importantes:

1. El nivel de voltaje de los pines del módulo es de 3.3V; se requiere una adaptación de nivel para la comunicación con microcontroladores de 5V.
2. El módulo inalámbrico opera a nivel TTL; debe conectarse a un MCU compatible con nivel TTL.

## Configuración de Modos

Los pines MD0 y AUX tienen dos funciones, dependiendo de su combinación, permiten acceder a diferentes estados. Al encenderse por primera vez, el pin AUX se encuentra en modo de entrada. Si tanto el pin MD0 como el pin AUX se conectan a un nivel alto de 3.3V TTL simultáneamente y se mantienen en ese estado durante 1 segundo (sin cambios de nivel), el módulo entrará en el modo de actualización de firmware, listo para recibir una actualización. De lo contrario, entrará en el modo de comunicación inalámbrica (el pin AUX volverá a ser un pin de salida para indicar el estado de funcionamiento del módulo).

Los pines MD0 y AUX tienen una resistencia pull-down interna y están en estado bajo cuando no se conectan. Se vuelven de alto nivel a 3.3V TTL cuando se elevan.

| Función                                    | Descripción                                          | Método de acceso                                                                  |
| ------------------------------------------ | ---------------------------------------------------- | --------------------------------------------------------------------------------- |
| Funcionalidad de configuración             | Configuración de parámetros del módulo (comandos AT) | Después de encender, dejar el pin AUX sin conexión y elevar MD0                   |
| Funcionalidad de comunicación              | Utilizado para comunicación inalámbrica              | Después de encender, dejar el pin AUX sin conexión y MD0 sin conexión             |
| Funcionalidad de actualización de firmware | Utilizado para actualizar el firmware                | Después de encender, elevar el pin AUX, elevar MD0 y mantenerlo durante 1 segundo |

En el modo de comunicación inalámbrica, el pin AUX es una salida que indica el estado de funcionamiento del módulo.

## Configuración de Funciones

En "Funcionalidad de configuración", el puerto serial debe configurarse con los siguientes parámetros: Baud Rate "115200", Bit de Parada "1", Bits de Datos "8", Paridad "Ninguna". Esto se logra mediante comandos AT para configurar los parámetros de funcionamiento del módulo. Consulte la siguiente tabla de comandos AT como referencia:

| Comando     | Función                                                                |
| ----------- | ---------------------------------------------------------------------- |
| AT          | Comprobar la respuesta del módulo                                      |
| AT+MODEL?   | Consultar el modelo del dispositivo                                    |
| AT+CGMR?    | Obtener la versión del software                                        |
| AT+UPDATE   | Consultar si el dispositivo está en modo de actualización de firmware  |
| ATE1        | Activar la respuesta de comandos                                       |
| ATE0        | Desactivar la respuesta de comandos                                    |
| AT+RESET    | Reiniciar el módulo                                                    |
| AT+DEFAULT  | Restaurar la configuración de fábrica                                  |
| AT+FLASH=   | Guardar parámetros                                                     |
| AT+ADDR=?   | Consultar el rango de direcciones de configuración del dispositivo     |
| AT+ADDR?    | Consultar la dirección del dispositivo                                 |
| AT+ADDR=    | Configurar la dirección del dispositivo                                |
| AT+TPOWER=? | Consultar el rango de configuración de potencia de transmisión         |
| AT+TPOWER?  | Consultar la potencia de transmisión                                   |
| AT+TPOWER=  | Configurar la potencia de transmisión                                  |
| AT+CWMODE=? | Consultar el rango de modos de trabajo configurados                    |
| AT+CWMODE?  | Consultar el modo de trabajo                                           |
| AT+CWMODE=  | Configurar el modo de trabajo                                          |
| AT+TMODE=?  | Consultar el rango de estados de transmisión configurados              |
| AT+TMODE?   | Consultar el estado de transmisión                                     |
| AT+TMODE=   | Configurar el estado de transmisión                                    |
| AT+WLRATE=? | Consultar el rango de configuración de velocidad inalámbrica y canales |
| AT+WLRATE?  | Consultar la velocidad inalámbrica y los canales                       |
| AT+WLRATE=  | Configurar la velocidad inalámbrica y los canales                      |
| AT+WLTIME=? | Consultar el rango de tiempo de suspensión configurado                 |
| AT+WLTIME?  | Consultar el tiempo de suspensión                                      |
| AT+WLTIME=  | Configurar el tiempo de suspensión                                     |
| AT+UART=?   | Consultar el rango de configuración de puertos serie                   |
| AT+UART?    | Consultar la configuración de puertos serie                            |
| AT+UART=    | Configurar puertos serie                                               |

Cuando se sale de la función de configuración (MD0=0), el módulo volverá a configurar los parámetros. Durante el proceso de configuración, AUX se mantendrá en un nivel alto y, al completarse, pasará a un nivel bajo, indicando que el módulo ha vuelto al estado de reposo.

## Tiempo de Reposo

El tiempo de reposo se refiere al intervalo de escucha para el receptor y al tiempo de transmisión continua del código de activación para el transmisor. Cuando el módulo está en modo "Modo de Activación", se añadirá automáticamente un código de activación de tiempo de reposo antes de los datos del usuario. Cuando el módulo está en modo "Modo de Ahorro de Energía", el tiempo de reposo configurado se convierte en el intervalo de escucha.

## Modo del Dispositivo

### Modo Normal (Modo 0)

- Transmisión: El módulo recibe datos del usuario a través del puerto serie y transmite paquetes de datos inalámbricos de 58 bytes de longitud. Cuando los datos del usuario alcanzan los 58 bytes, el módulo iniciará la transmisión inalámbrica. En este punto, el usuario puede seguir introduciendo datos para transmitir. Si el usuario necesita transmitir menos de 58 bytes, el módulo esperará un byte y, si no se introducen más datos, se considerará que la transmisión de datos ha terminado. En este momento, el pin AUX emitirá un nivel alto. Cuando el módulo envía todos los datos a través del chip RF y comienza la transmisión, el pin AUX emitirá un nivel bajo, indicando que se ha completado la transmisión del último paquete de datos inalámbricos. En el modo normal, los paquetes de datos transmitidos solo pueden ser recibidos por módulos receptores en modo normal o de activación.
- Recepción: El módulo mantendrá continuamente activada la función de recepción inalámbrica y podrá recibir paquetes de datos enviados por módulos en modo normal o de activación. Después de recibir un paquete de datos, el pin AUX del módulo emitirá un nivel alto, y después de un retraso de 2-3 ms, comenzará a enviar los datos inalámbricos a través del pin TXD del puerto serie. Una vez que se hayan enviado todos los datos inalámbricos a través del puerto serie, el pin AUX volverá a emitir un nivel bajo.

### Modo de Activación (Modo 1)

- Transmisión: Las condiciones para iniciar la transmisión de paquetes de datos son las mismas que en el modo normal, excepto que, en el modo de activación, se añadirá automáticamente un código de activación (tiempo de reposo) antes de cada paquete de datos. La longitud del código de activación dependerá del tiempo de reposo configurado en los parámetros del usuario. El propósito del código de activación es despertar a los módulos receptores en modo de ahorro de energía. Por lo tanto, los datos transmitidos en modo de activación pueden ser recibidos por módulos en modo normal, 1 y 2.
- Recepción: Similar al modo normal.

### Modo de Ahorro de Energía (Modo 2)

- Transmisión: El módulo está en estado de reposo, el puerto serie está desactivado y no puede recibir datos del MCU externo. Por lo tanto, este modo no permite la transmisión inalámbrica.
- Recepción: En el modo de ahorro de energía, el transmisor debe estar en modo de activación. El módulo inalámbrico escuchará periódicamente el código de activación y, una vez que reciba un código de activación válido, entrará en modo de recepción. Esperará a que se complete la recepción de un paquete de datos válido antes de enviar los datos inalámbricos a través del pin TXD con un retraso de 2-3 ms. Después de la transmisión, el pin AUX emitirá un nivel bajo. El módulo inalámbrico seguirá en el estado de "reposo-escucha", y configurando diferentes tiempos de activación se puede ajustar el equilibrio entre el retraso de respuesta de recepción y el consumo de energía promedio.

### Modo de Intensidad de Señal (Modo 3)

El modo de intensidad de señal permite visualizar la intensidad de señal de ambas partes en la comunicación y evaluar la calidad de la comunicación.

- Transmisión: Similar al modo normal.
- Recepción: Proporciona información sobre la intensidad de señal.

![Imagen](https://media.wiki-power.com/img/20220118110058.png)

SNR: Relación señal/ruido (mayor es más estable), RSSI: Indicador de intensidad de señal recibida (mayor es más estable).

## Modo de Comunicación

- Transmisión Transparente: Por ejemplo, el dispositivo A envía 5 bytes de datos AA BB CC DD EE al dispositivo B, y el dispositivo B recibe los datos AA BB CC DD EE. Esta forma de comunicación se aplica a dispositivos con la misma dirección y en el mismo canal de comunicación. Los datos de usuario pueden estar en formato de caracteres o datos en hexadecimal.
  - Punto a punto
  - Punto a varios
  - Difusión y escucha
- Transmisión Dirigida: Por ejemplo, el dispositivo A (con dirección 0x1400 y canal 0x17) necesita enviar datos AA BB CC al dispositivo B (con dirección 0x1234 y canal 0x10). El formato de comunicación es 1234 10 AA BB CC, donde 1234 es la dirección del módulo B y 10 es el canal. De manera similar, si el dispositivo B necesita enviar datos AA BB CC al dispositivo A, el formato de comunicación es 14 00 17 AA BB CC, y el dispositivo A puede recibir los datos. Esta forma de comunicación permite que dispositivos con direcciones y canales diferentes se comuniquen entre sí, y el formato de datos es en hexadecimal (alta dirección + baja dirección + canal + datos del usuario).
  - Punto a varios
  - Difusión y escucha

# Radiodifusión y Monitoreo de Datos: Configurando la dirección del módulo como 0xFFFF, puedes escuchar la transmisión de datos de todos los módulos en el mismo canal. Los datos enviados pueden ser recibidos por cualquier módulo con la misma dirección en el mismo canal, lo que permite funciones de radiodifusión y escucha.

## Modo de Transmisión Transparente

### Punto a Punto

![](https://media.wiki-power.com/img/20220118110614.png)

- Dos módulos con direcciones idénticas, mismos canales y velocidades inalámbricas (no velocidades de baudios seriales) pueden comunicarse uno con otro, uno envía y el otro recibe (debe ser un envío y una recepción).
- Cada módulo puede enviar y recibir datos.
- Los datos son completamente transparentes, lo que se envía es lo que se recibe.

|                          | Módulo de Envío | Módulo de Recepción |
| ------------------------ | --------------- | ------------------- |
| Cantidad                 | 1               | 1                   |
| Contenido de Transmisión | Datos           | Datos               |

Ejemplo:

Los dispositivos A y B tienen la dirección 0x1234, el mismo canal y la misma velocidad.  
Dispositivo A envía: AA BB CC DD  
Dispositivo B recibe: AA BB CC DD

La transmisión transparente es simple, simplemente utiliza el módulo LoRa como un puerto serie; el dispositivo A envía datos a través del puerto serie, y el dispositivo B puede recibirlos a través del puerto serie, y viceversa.

### Punto a Varios

![](https://media.wiki-power.com/img/20220118110709.png)

- Módulos con direcciones idénticas, mismos canales y velocidades inalámbricas (no velocidades de baudios seriales) pueden enviar datos, y otros módulos pueden recibirlos.
- Cada módulo puede enviar y recibir datos.
- Los datos son completamente transparentes, lo que se envía es lo que se recibe.

|                          | Módulo de Envío | Módulo de Recepción |
| ------------------------ | --------------- | ------------------- |
| Cantidad                 | 1               | N                   |
| Contenido de Transmisión | Datos           | Datos               |

La diferencia con el punto a punto es que puede haber varios módulos de recepción.

Ejemplo:

Dispositivos A~F tienen la dirección 0x1234, el canal es 0x12 y la velocidad es la misma.  
Dispositivo A envía: AA BB CC DD  
Dispositivos B~F reciben: AA BB CC DD

### Radiodifusión y Escucha

![](https://media.wiki-power.com/img/20220118110853.png)

- Si la dirección del módulo es 0xFFFF, el módulo está en modo de radiodifusión y escucha. Los datos enviados pueden ser recibidos por todos los demás módulos en el mismo canal y velocidad (radiodifusión). Al mismo tiempo, puede escuchar la transmisión de datos de todos los módulos en el mismo canal y velocidad (escucha).
- La radiodifusión y escucha no requieren direcciones idénticas.

|                          | Módulo de Envío | Módulo de Recepción |
| ------------------------ | --------------- | ------------------- |
| Cantidad                 | 1               | N                   |
| Contenido de Transmisión | Datos           | Datos               |

La diferencia con el punto a varios es que las direcciones pueden ser diferentes.

Ejemplo:

Dispositivo A tiene la dirección 0xFFFF, los dispositivos B~F tienen direcciones diferentes, los dispositivos B y C tienen la dirección 0x1234, y los dispositivos D~F tienen la dirección 0x5678. Todos los dispositivos A~F tienen la misma velocidad.  
Radiodifusión:  
Dispositivo A radiodifunde: AA BB CC DD  
Dispositivos B~F reciben: AA BB CC DD  
Escucha:  
Dispositivo B envía a C: AA BB CC DD  
Dispositivo A escucha: AA BB CC DD  
Dispositivo D envía a E y F: 11 22 33 44  
Dispositivo A escucha: 11 22 33 44

## Modo de Transmisión Direccional

### Punto a Punto

- Al enviar un módulo, puedes cambiar la dirección y el canal. Los usuarios pueden especificar el envío de datos a cualquier dirección y canal.
- Puede implementar la función de red y de repetidor.

|                          | Módulo de Envío       | Módulo de Recepción |
| ------------------------ | --------------------- | ------------------- |
| Cantidad                 | 1                     | 1                   |
| Contenido de Transmisión | Dirección+Canal+Datos | Datos               |

La diferencia con el punto a punto transparente es que la dirección y el canal del módulo pueden cambiar, pero la velocidad sigue siendo la misma.

![](https://media.wiki-power.com/img/20220118111903.png)

Por ejemplo:

Dispositivo A: Dirección 0X1234, Canal 0X17;
Dispositivo B: Dirección 0xABCD, Canal 0X01;
Dispositivo C: Dirección 0X1256, Canal 0x13.

Dispositivo A envía: AB CD 01 AA BB CC DD
Dispositivo B recibe: AA BB CC DD
Dispositivo C recibe: Nada

Dispositivo A envía: 12 56 13 AA BB CC DD
Dispositivo B recibe: Nada
Dispositivo C recibe: AA BB CC DD

#### Prueba sin código

Prepara 2 adaptadores USB a TTL y 2 módulos LoRa. Conéctalos por separado a los adaptadores USB a TTL (alimentación, tierra común, emisor/receptor TX/RX). Luego, conecta los pines MD0 de los dos módulos LoRa a VCC. Conecta estos dispositivos a un puerto USB de la computadora y abre el software de configuración. Ajusta los siguientes parámetros:

Dispositivo A:

- Modo general
- Transmisión dirigida
- **Velocidad de baudios: 115200 (debe ser 115200)**
- Paridad: Ninguna
- Tasa aérea: 19.2k
- Tiempo de inactividad: 1 segundo
- **Dirección del módulo: 0**
- **Canal de comunicación: 0**
- Potencia de transmisión: 20 dBm

Dispositivo B:

- Modo general
- Transmisión dirigida
- **Velocidad de baudios: 115200 (debe ser 115200)**
- Paridad: Ninguna
- Tasa aérea: 19.2k
- Tiempo de inactividad: 1 segundo
- **Dirección del módulo: 65534**
- **Canal de comunicación: 10**
- Potencia de transmisión: 20 dBm

Después de configurar los parámetros, haz clic en "Guardar configuración" y luego desconecta MD0 antes de cortar la alimentación.

Vuelve a encender ambos módulos, abre el software de configuración y selecciona la opción "HEX" (hexadecimal) tanto para transmitir como para recibir.

En la zona de envío de A, ingresa `FF FE 0A 11 12 13 14` y haz clic en "Enviar". Ahora podrás recibir `11 12 13 14` en la zona de recepción de B. O bien, en la zona de envío de B, ingresa `00 00 00 11 12 13` y podrás recibir `11 12 13` en la zona de recepción de A.

En este caso, `FF FE` representa la dirección de B, que es 65534 en hexadecimal, y el canal es 10 (en hexadecimal, es `0A`). El contenido de los datos enviados es `11 12 13 14`. De manera similar, los datos enviados por B incluyen la dirección de A (`00 00`), el canal (`00`) y el contenido (`11 12 13`). El formato de los datos enviados es **dirección de alta orden + dirección de baja orden + canal + datos del usuario**.

#### Prueba con código

La transmisión punto a punto solo agrega bytes de dirección en comparación con la transmisión punto a punto transparente. Puedes definirlo de la siguiente manera:

```c title="main.c"
/* USER CODE BEGIN PV */
uint8_t B_Addr[2] = { 0xFF, 0xFE };
uint8_t B_Chan[1] = { 0x0A };
/* USER CODE END PV */
```

Después de configurar el código con la biblioteca HAL para la comunicación serial, envía los bytes de dirección antes de enviar datos:

```c title="main.c"
HAL_UART_Transmit(&huart1, B_Addr, 2, 0xFFFF);
HAL_UART_Transmit(&huart1, B_Chan, 1, 0xFFFF);
```

De esta manera, el dispositivo receptor (dispositivo B) podrá recibir un marco de datos enviado por el dispositivo A (sin los bytes de dirección).

### Recepción y transmisión de difusión

![](https://media.wiki-power.com/img/20220118112544.png)

- Si la dirección del módulo es 0xFFFF, el módulo se encuentra en modo de escucha de difusión. Los datos enviados pueden ser recibidos por todos los demás módulos que estén en el mismo canal y velocidad de transmisión (difusión). Al mismo tiempo, puede escuchar la transmisión de datos de todos los demás módulos en el mismo canal y velocidad de transmisión (escucha).
- La escucha de difusión no requiere que las direcciones sean iguales.
- La dirección del canal se puede configurar. Cuando la dirección es 0xFFFF, está en modo de difusión; en otro caso, está en modo de transmisión dirigida.

|                          | Módulo de envío        | Módulo de recepción |
| ------------------------ | ---------------------- | ------------------- |
| Cantidad                 | 1                      | N                   |
| Contenido de transmisión | 0xFFFF + canal + datos | Datos               |

Por ejemplo:

```markdown
设备 A con dirección 0xFFFF en el canal 0x12;
Los dispositivos B y C tienen direcciones 0x1234 y operan en el canal 0x13;
El dispositivo D posee la dirección 0xAB00 y utiliza el canal 0x01;
El dispositivo E tiene la dirección 0xAB01 y se comunica en el canal 0x12;
El dispositivo F está configurado con la dirección 0xAB02 y el canal 0x12.

Cuando el dispositivo A realiza una transmisión de difusión, los datos enviados son: FF FF 13 AA BB CC DD.
Los dispositivos B y C reciben los siguientes datos: AA BB CC DD.

Cuando el dispositivo A envía datos, que son: AB 00 01 11 22 33 44, solo el dispositivo D los recibe: 11 22 33 44.

Cuando el dispositivo E envía datos: AB 02 12 66 77 88 99, el dispositivo F los recibe: 66 77 88 99. Además, el dispositivo A está en modo escucha y detecta estos datos: 66 77 88 99.

## Referencias y Agradecimientos

- [Módulo LORA ATK-LORA-01](http://www.openedv.com/docs/modules/iot/atk-lora-01.html)
- [Tutorial de uso del módulo LORA ATK-LORA de Elecrow](https://www.bilibili.com/video/BV1D44y1t7bn)
- [Recursos y discusiones sobre el módulo LORA ATK-LORA-01 de Elecrow](http://www.openedv.com/thread-309019-1-1.html)
- [Método de prueba de datos de transmisión direccional en modo normal para dos módulos LORA (pruebas con una computadora host)](http://www.openedv.com/forum.php?mod=viewthread&tid=288951)
- [Problemas de recepción de datos en el módulo inalámbrico ATK-LORA-01](http://www.openedv.com/forum.php?mod=viewthread&tid=328190&highlight=ATK-LORA-01)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
