````markdown
# Hack.init( ) 黑客马拉松

—— Wight · Un sistema de iluminación descentralizado basado en la plataforma en la nube.

![](https://media.wiki-power.com/img/wight.jpg)

Repositorio del proyecto: [**linyuxuanlin / Wight**](https://github.com/linyuxuanlin/Wight)

## Contexto

Este proyecto se creó durante el hack.init() Hackathon de 2017. Se pasaron más de 20 horas programando, modelando, depurando una variedad de problemas, esperando impresiones, y finalmente, presentando y dando discursos para obtener algo que se asemejara a un producto terminado.

El proyecto se centra principalmente en un sistema de iluminación para farolas en áreas rurales y remotas. Aunque el concepto suena abstracto, en realidad, funciona como una farola convencional.

## Puntos de Innovación del Proyecto

- **Alimentación Solar.** Capaz de autoabastecerse (según la información detallada, la energía solar es suficiente para encender los LED).
- **Descentralización.** Proporciona una solución conveniente para áreas remotas donde no es práctico tender cables.
- **Algoritmos Inteligentes.** Detecta la oscuridad y enciende automáticamente las luces; aumenta la intensidad de los LED al detectar la presencia de personas o vehículos.
- **Control Unificado en la Nube.** Utiliza un controlador principal GSM, lo que permite el ajuste remoto a gran escala.
- **Escalabilidad.** Ofrece diversas funciones personalizadas para usuarios con necesidades específicas de iluminación.

## Principios e Implementación

**Código:**

```cpp
#define BUTTONS_address   "channel/widget4_0/cmd/control" // Comandos de encendido y apagado
#define LIGHT_STATUS_address  "channel/widget4_0/data/light" // Estado de encendido y apagado
#define ITENSITY_DATA_address "channel/widget4_0/data/lightsensor"
#define LEDPIN1    D1    // Definición de los pines de control de las bombillas
#define LEDPIN2    D2
#define LEDPIN3    D3
#define LEDPIN4    D5
#define CHECKIN1   A0
#define CHECKIN2   D4
```
````

````

```cpp
int autostate = 2;
int light_state = 2;

void buttons_function(uint8_t *payload, uint32_t len) // Función de botones (Auto y Riego)
{
    uint8_t SwitchKey;
    uint8_t SwitchKey2;
    aJsonClass aJson;
    aJsonObject *root = aJson.parse((char *)payload);

    if (root == NULL)
    {
        aJson.deleteItem(root);
        return;
    }

    aJsonObject *_switch = aJson.getObjectItem(root, "mode");

    if (_switch != NULL)
    {
        SwitchKey = atoi(_switch->valuestring);

        if (SwitchKey)
        {
            SerialUSB.println("Encendido automático");
            autostate = 1;
            IntoRobot.publish(LIGHT_STATUS_address, "1");
        }
        else
        {
            SerialUSB.println("Apagado automático");
            autostate = 0;
            IntoRobot.publish(LIGHT_STATUS_address, "0");
        }
    }

    aJsonObject *_switch2 = aJson.getObjectItem(root, "manual");

    if (_switch2 != NULL)
    {
        SwitchKey2 = atoi(_switch2->valuestring);

        if (SwitchKey2)
        {
            SerialUSB.println("Encendido manual");
            light_state = 1;
            IntoRobot.publish(LIGHT_STATUS_address, "1");
        }
        else
        {
            SerialUSB.println("Apagado manual");
            light_state = 0;
            IntoRobot.publish(LIGHT_STATUS_address, "0");
        }
    }
    else
    {
    }

    aJson.deleteItem(root);
}

void lightup()
{
    digitalWrite(LEDPIN1, HIGH);    // Encender bombilla
    digitalWrite(LEDPIN2, HIGH);    // Encender bombilla
    digitalWrite(LEDPIN3, HIGH);    // Encender bombilla
    digitalWrite(LEDPIN4, HIGH);    // Encender bombilla
}

void light_half_up()
{
    analogWrite(LEDPIN1, 80);    // Encender bombilla (mitad de intensidad)
    analogWrite(LEDPIN2, 80);    // Encender bombilla (mitad de intensidad)
    analogWrite(LEDPIN3, 80);    // Encender bombilla (mitad de intensidad)
    analogWrite(LEDPIN4, 80);    // Encender bombilla (mitad de intensidad)
}
````

````markdown
# Código Traducido

```cpp
}
void apagarLuces()
{
    digitalWrite(LEDPIN1, LOW);
    digitalWrite(LEDPIN2, LOW);
    digitalWrite(LEDPIN3, LOW);
    digitalWrite(LEDPIN4, LOW);
}

int obtenerNivelLuz()
{
    int lecturaLuz = analogRead(CHECKIN1);

    SerialUSB.println(lecturaLuz);
    return lecturaLuz;
}

int obtenerDatosIR()
{
    int estadoIR = digitalRead(CHECKIN2);
    SerialUSB.println(estadoIR);
    return estadoIR;
}

void modoAutomatico()
{
    if (obtenerNivelLuz() >= 400)
    {
        IntoRobot.publish(LIGHT_STATUS_address, "1");
        if (obtenerDatosIR() == 0)
            encenderLuces();
        else
            encenderMitadLuces();
    }
    else
    {
        IntoRobot.publish(LIGHT_STATUS_address, "0");
        apagarLuces();
    }
}

void funcionImpresionHUMEDAD(uint8_t *datos, uint32_t longitud)
{

}

void configuracion()
{
    pinMode(D4, INPUT);
    SerialUSB.begin(115200);
    SerialUSB.println("Hola, mundo");
    pinMode(LEDPIN1, OUTPUT);
    pinMode(LEDPIN2, OUTPUT);
    pinMode(LEDPIN3, OUTPUT);
    pinMode(LEDPIN4, OUTPUT);
    IntoRobot.subscribe(BUTTONS_address, NULL, funcionBotones);
    IntoRobot.subscribe(ITENSITY_DATA_address, NULL, funcionImpresionHUMEDAD);
}

void bucle()
{
    int mapeoLuz = map(obtenerNivelLuz(), 0, 1024, 100, 0);
    IntoRobot.publish(LIGHT, mapeoLuz);
    SerialUSB.println(obtenerNivelLuz());
    if (autostate == 0)
    {
        if (estadoLuz == 1)
            encenderLuces();
        else
            apagarLuces();
    }
    else if (autostate == 1)
    {
        SerialUSB.println("Estado = 1");
        modoAutomatico();
    }
    delay(100);
}
```
````

**FAQ**

**P:** ¿Habrá un seguimiento del proyecto en el futuro?
**R:** Actualmente no tenemos planes de seguimiento. Aunque el proyecto tiene un buen potencial innovador, todavía debe validar su valor de aplicación comercial.

**Resumen**

No ganamos el concurso esta vez. Sin embargo, el concurso nos ayudó a mejorar nuestras habilidades para programar y presentar, además de experimentar el trabajo extra y la presión de cumplir con los plazos. También conocimos a muchas personas y recibimos muchos obsequios como recuerdo.

**Referencias y Agradecimientos**

```

- **Miembros del equipo:** Lin Peijie, Huang Yuefeng, Zhang Ziyi
- [Plataforma en la nube de IntoRobot](https://www.intorobot.com/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
```
