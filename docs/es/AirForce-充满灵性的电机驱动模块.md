# AirForce - Módulo de motorización con esencia

El proyecto AirForce es un conjunto de motorización que incluye la placa base AirPort con funcionalidad de regulación integrada y la subplaca de motorización de doble canal AirCraft. Puede expandir la capacidad de motorización para hasta 16 motores según sus necesidades. Debido a su diseño compacto y ligero, un rendimiento sólido y una alta capacidad de expansión, se le dio el nombre de Proyecto AirForce.

Características:

- Compacto y de fácil acceso para la conexión de interfaces.
- Interfaces no están completamente encapsuladas como cajas negras, lo que mejora la capacidad de conexión.
- No utiliza demasiados pines de temporizador de la unidad central de microcontroladores (STM32).

Repositorio del proyecto: [**linyuxuanlin/AirForceDVR**](https://github.com/linyuxuanlin/AirForceDVR)

## AirPort - Placa base con funcionalidad de regulación integrada

🚧

## AirCraft - Subplaca de motorización de doble canal

![Imagen](https://media.wiki-power.com/img/20201101231734.jpg)

La subplaca de motorización de doble canal AirCraft se basa en el diseño de un chip de motorización integrado TB6612FNG, con un método de control lógico adicional. Solo requiere 4 pines (2 canales normales y 2 canales PWM) para controlar dos motores (dirección/velocidad). En comparación con las soluciones convencionales en el mercado, se reducen dos canales de E/S, lo que ahorra valiosos recursos de pines en el controlador principal. En cuanto a las especificaciones del chip de motorización, la corriente máxima continua de un solo canal puede alcanzar 1.2A, con un pico de 2A/3.2A (pulsos continuos/pulsos únicos), lo que es más que suficiente para controlar los motores típicos de robots.

Parámetros del producto:

- Voltaje de entrada de la parte lógica VCC: 3.3~5V (predeterminado **5V**)
- Voltaje de entrada de la parte de motorización VM: 2.5~12V (predeterminado **12V**)
- Canales de motorización: 2 canales
- Corriente máxima continua de un solo canal: **1.2A**
- Corriente de arranque máxima: **2A/3.2A** (pulsos continuos/pulsos únicos)
- Interfaz: Pasadores espaciados a 2.54mm, conector XH2.54
- Tamaño del módulo: 23.7 × 15.8 mm

Descripción de los pines:

![Imagen](https://media.wiki-power.com/img/20201022104033.png)

|    Grupo de interfaces     | Nombre |        Descripción de la función         |
| :------------------------: | :----: | :--------------------------------------: |
|   Interfaces de control    |  PWM1  | Pin de control de velocidad del motor M1 |
|   Interfaces de control    |  DIR1  | Pin de control de dirección del motor M1 |
|   Interfaces de control    |  DIR2  | Pin de control de dirección del motor M2 |
|   Interfaces de control    |  PWM2  | Pin de control de velocidad del motor M2 |
| Interfaces de alimentación |   5V   |     Alimentación de la parte lógica      |
| Interfaces de alimentación |   G    |               Tierra (GND)               |
| Interfaces de alimentación |  12V   |       Alimentación de los motores        |
|    Interfaces del motor    |  M1+   |          Salida 1 del motor M1           |
|    Interfaces del motor    |  M1-   |          Salida 2 del motor M1           |
|    Interfaces del motor    |  M2+   |          Salida 1 del motor M2           |
|    Interfaces del motor    |  M1-   |          Salida 2 del motor M2           |

Tutorial de control:

- Interfaces de control
  - **DIR1/DIR2**: Entradas de señal de control de avance y retroceso
    - Ejemplo: Si DIR1 se establece en 1 (nivel alto), el motor M1 gira en sentido horario; si DIR1 se establece en 0 (nivel bajo), el motor M1 gira en sentido antihorario.
  - **PWM1/PWM2**: Habilitación de control de los dos motores respectivos (se pueden utilizar para control de velocidad mediante PWM).
- Interfaces de alimentación: Conectar a cualquier interfaz de alimentación en la placa base AirPort (o conectar 12V y 5V externos).
- Interfaces del motor: Conectar a las entradas del motor.

Imagen de dimensiones:

🚧

## Referencias y agradecimientos

- [Módulo de motorización de doble motor TB6612](https://wiki.dfrobot.com.cn/_SKU_DRI0044_Dual_Motor_Driver__TB6612__%E5%BE%AE%E5%9E%8B%E7%94%B5%E6%9C%BA%E9%A9%B1%E5%8A%A8%E6%A8%A1%E5%9D%97)

Certainly, here is the text translated into Spanish:

```markdown
> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

Por supuesto, aquí está el texto traducido al español:

```markdown
> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
