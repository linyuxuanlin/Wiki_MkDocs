# Hack.init() Hackathon

—— Wight · Sistema de iluminación sin cables basado en plataforma en la nube.

![](https://f004.backblazeb2.com/file/wiki-media/img/wight.jpg)

Repositorio del proyecto: [**linyuxuanlin / Wight**](https://github.com/linyuxuanlin/Wight)

## Antecedentes

El proyecto se realizó en el hack.init() Hackathon de 2017. Después de más de 20 horas de codificación, modelado, depuración de todo tipo de errores, esperando la impresión, presentación y discurso, finalmente se logró algo parecido a un producto.

Este proyecto se utiliza principalmente para el sistema de iluminación de farolas en áreas remotas y rurales. El modelo es un poco abstracto, en realidad representa una farola.

## Puntos innovadores del proyecto

- **Alimentación solar.** Autosuficiente (según la información detallada, la energía solar es suficiente para encender LED)
- **Sin cables.** Proporciona comodidad para áreas remotas de montaña donde no es conveniente instalar cables.
- **Algoritmo inteligente.** Detecta la noche y enciende automáticamente las luces; detecta la presencia de personas o vehículos y aumenta el brillo de los LED.
- **Control unificado en la plataforma en la nube.** Utiliza un controlador principal GSM, que permite la depuración remota en lotes.
- **Escalabilidad.** Proporciona diversas funciones personalizadas para usuarios especiales con necesidades de iluminación personalizadas.

## Principios y realización

**Código:**

```cpp
#define BUTTONS_address   "channel/widget4_0/cmd/control" //comando de encendido / apagado
#define LIGHT_STATUS_address  "channel/widget4_0/data/light"//estado de encendido / apagado
#define ITENSITY_DATA_address "channel/widget4_0/data/lightsensor"
#define LEDPIN1    D1    //definir el pin de control de la bombilla
#define LEDPIN2    D2
#define LEDPIN3    D3
#define LEDPIN4    D5
#define CHECKIN1   A0
#define CHECKIN2   D4
```

int autostate = 2;
int light_state = 2;
void buttons_function(uint8_t *payload, uint32_t len)//Botones de automático y riego
{
    uint8_t SwitchKey;
    uint8_t SwitchKey2;
    aJsonClass aJson;
    aJsonObject *root = aJson.parse((char *)payload);
    if(root == NULL)
    {
        aJson.deleteItem(root);
        return;
    }
    aJsonObject *_switch = aJson.getObjectItem(root, "modo");
    if(_switch != NULL)
    {
        SwitchKey = atoi(_switch->valuestring);
        if(SwitchKey)
        {
            SerialUSB.println("automático encendido");
            autostate=1;
             IntoRobot.publish(LIGHT_STATUS_address,"1");
        }
        else
        {
            SerialUSB.println("automático apagado");
            autostate=0;
             IntoRobot.publish(LIGHT_STATUS_address,"0");
        }
    }
    aJsonObject *_switch2 = aJson.getObjectItem(root, "manual");
    if(_switch2 != NULL)
    {
        SwitchKey2 = atoi(_switch2->valuestring);
        if(SwitchKey2)
        {
            SerialUSB.println("manual encendido");
            light_state=1;
             IntoRobot.publish(LIGHT_STATUS_address,"1");
        }
        else
        {
            SerialUSB.println("manual apagado");
            light_state=0;
             IntoRobot.publish(LIGHT_STATUS_address,"0");
        }
    }
    else
    {
    }
    aJson.deleteItem(root);
}
void lightup()
{
    digitalWrite(LEDPIN1, HIGH);    // Encender la bombilla
    digitalWrite(LEDPIN2, HIGH);    // Encender la bombilla
    digitalWrite(LEDPIN3, HIGH);    // Encender la bombilla
    digitalWrite(LEDPIN4, HIGH);    // Encender la bombilla

}
void light_half_up()
{
    analogWrite(LEDPIN1, 80);    // Encender la bombilla
    analogWrite(LEDPIN2, 80);    // Encender la bombilla
    analogWrite(LEDPIN3, 80);    // Encender la bombilla
    analogWrite(LEDPIN4, 80);    // Encender la bombilla

void lightdown()
{
    digitalWrite(LEDPIN1, LOW);
    digitalWrite(LEDPIN2, LOW);
    digitalWrite(LEDPIN3, LOW);
    digitalWrite(LEDPIN4, LOW);

}
int getlight()
{
    int k  = analogRead(CHECKIN1);

    SerialUSB.println(k);
    return k;
}
int get_IR_data()
{
    int b = digitalRead(CHECKIN2);
    SerialUSB.println(b);
    return b;
}
void automode()
{
    if(getlight()>=400)
    {
        IntoRobot.publish(LIGHT_STATUS_address,"1");
        if (get_IR_data()==0)
        lightup();
        else
        light_half_up();
    }
    else
    {
    IntoRobot.publish(LIGHT_STATUS_address,"0");
    lightdown();
    }
}

void HUMIDITY_print_function(uint8_t *payload, uint32_t len)
{

}

// IntoRobot.publish(LIGHT_STATUS_address,"1");
// IntoRobot.publish(LIGHT_STATUS_address,"0");
void setup()
{
    pinMode(D4,INPUT);
    SerialUSB.begin(115200);
    SerialUSB.println("hola mundo");
    pinMode(LEDPIN1, OUTPUT);    //inicialización
    pinMode(LEDPIN2, OUTPUT);    //inicialización
    pinMode(LEDPIN3, OUTPUT);    //inicialización
    pinMode(LEDPIN4, OUTPUT);    //inicialización
    //el dispositivo recibe comandos de encendido y apagado de la luz de la plataforma en la nube
    IntoRobot.subscribe(BUTTONS_address,NULL,buttons_function);
    IntoRobot.subscribe(ITENSITY_DATA_address,NULL,HUMIDITY_print_function);
}
void loop()
{
   int a =map(getlight() ,0,1024,100,0);
   IntoRobot.publish(LIGHT,a);
    SerialUSB.println(getlight());
    if(autostate==0)
    {
        if(light_state ==1)
        lightup();
        else
        lightdown();
    }
    else if (autostate==1)
    {
        SerialUSB.println("estado=1");
        automode();
    }
    delay(100);
}
```

Debido al tiempo limitado del concurso, solo pudimos dibujar un modelo aproximado y ensamblarlo después de imprimirlo.

## Preguntas frecuentes

P: ¿Habrá seguimiento del proyecto en el futuro?
R: Actualmente no tenemos planes de seguimiento. La idea es interesante, pero aún queda por ver si tiene valor comercial.

## Conclusión

No ganamos el concurso, pero nos permitió mejorar nuestras habilidades de programación y presentación, y experimentar la sensación de trabajar horas extras para lanzar un proyecto. También conocimos a muchas personas y recibimos muchos recuerdos.

## Referencias y agradecimientos

- Miembros del equipo: Lin Peijie, Huang Yuefeng, Zhang Ziyi
- [Plataforma en la nube de IntoRobot](https://www.intorobot.com/)

por_reemplazar[1]
por_reemplazar[2]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.