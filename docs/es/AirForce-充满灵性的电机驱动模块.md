# AirForce - Módulo de control de motor con gran capacidad espiritual

El proyecto AirForce es un kit de combinación de control de motor que incluye una placa base AirPort con función de regulación de voltaje integrada y una placa secundaria de control de motor de doble canal llamada AirCraft. Puede expandir libremente el control de hasta 16 motores según sus necesidades. Debido a su tamaño compacto, ligereza, alto rendimiento y gran capacidad de expansión, se le ha dado el nombre de Proyecto AirForce.

Características:

- Tamaño pequeño y fácil de conectar.
- Interfaz no completamente sellada en una caja negra, lo que mejora la capacidad de conexión.
- No utiliza demasiados pines de temporizador del microcontrolador (STM32).

Repositorio del proyecto: [**linyuxuanlin/AirForceDVR**](https://github.com/linyuxuanlin/AirForceDVR)

## AirPort - Placa base con función de regulación de voltaje integrada

🚧

## AirCraft - Placa secundaria de control de motor de doble canal

![](https://f004.backblazeb2.com/file/wiki-media/img/20201101231734.jpg)

La placa secundaria de control de motor de doble canal AirCraft está diseñada con el chip integrado de control TB6612FNG y un método de control lógico que solo requiere 4 pines (2 canales normales + 2 canales PWM) para controlar dos motores (dirección / velocidad). En comparación con las soluciones generales del mercado, se reducen dos pines de entrada/salida, lo que reduce el uso de los valiosos pines de entrada/salida del microcontrolador principal. En cuanto a los parámetros del chip de control, la corriente máxima de conducción continua de un solo canal puede alcanzar los 1,2 A, con un pico de 2 A/3,2 A (pulso continuo / pulso único), lo que es más que suficiente para controlar los motores de un robot común.

### Parámetros del producto

- Voltaje de entrada de la parte lógica VCC: 3,3 ~ 5 V (predeterminado **5 V**)
- Voltaje de entrada del controlador VM: 2,5 ~ 12 V (predeterminado **12 V**)
- Número de canales de control de motor: 2 canales
- Corriente máxima de conducción continua de **un solo canal**: **1,2 A**
- Pico de arranque: **2 A/3,2 A** (pulso continuo / pulso único)
- Método de conexión: clavija de fila de 2,54 mm, conector hembra XH2.54
- Tamaño del módulo: 23,7 × 15,8 (mm)

### Descripción de los pines

![](https://f004.backblazeb2.com/file/wiki-media/img/20201022104033.png)

| Grupo de interfaz | Nombre | Descripción de la función |
| :--------------: | :----: | :----------------------: |
| Interfaz de control | PWM1 | Pin de control de velocidad del motor M1 |
| Interfaz de control | DIR1 | Pin de control de dirección del motor M1 |
| Interfaz de control | DIR2 | Pin de control de dirección del motor M2 |
| Interfaz de control | PWM2 | Pin de control de velocidad del motor M2 |
| Interfaz de alimentación | 5V | Fuente de alimentación para la parte de control lógico |
| Interfaz de alimentación | G | Tierra |
| Interfaz de alimentación | 12V | Fuente de alimentación para el motor |
| Interfaz del motor | M1+ | Salida 1 del motor M1 |
| Interfaz del motor | M1- | Salida 2 del motor M1 |
| Interfaz del motor | M2+ | Salida 1 del motor M2 |
| Interfaz del motor | M1- | Salida 2 del motor M2 |

### Tutorial de control

- Interfaz de control
  - **DIR1/DIR2**: Entrada de señal de control de avance y retroceso.
    - Por ejemplo, si se asigna un valor de 1 (nivel alto) a DIR1, el motor M1 girará en sentido horario; si se asigna un valor de 0 (nivel bajo), el motor M1 girará en sentido antihorario.
  - **PWM1/PWM2**: Son los dos pines de habilitación del control de los dos motores (se pueden utilizar para controlar la velocidad mediante PWM).
- Interfaz de alimentación: Conectar a cualquier interfaz de alimentación de la placa base AirPort (o conectar una fuente de alimentación externa de 12V y 5V).
- Interfaz del motor: Conectar a la entrada del motor.

### Diagrama de tamaño

🚧

## Referencias y agradecimientos

- [Módulo de controlador de motor dual TB6612 para motores pequeños](https://wiki.dfrobot.com.cn/_SKU_DRI0044_Dual_Motor_Driver__TB6612__%E5%BE%AE%E5%9E%8B%E7%94%B5%E6%9C%BA%E9%A9%B1%E5%8A%A8%E6%A8%A1%E5%9D%97)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.