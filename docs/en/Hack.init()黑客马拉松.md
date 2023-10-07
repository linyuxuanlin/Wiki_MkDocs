# Hack.init() Hackathon

- Wight: A Cloud-based Wireless Lighting System

![](https://f004.backblazeb2.com/file/wiki-media/img/wight.jpg)

Project Repository: [**linyuxuanlin / Wight**](https://github.com/linyuxuanlin/Wight)

## Background

This project was created during the 2017 hack.init() hackathon. After more than 20 hours of coding, modeling, debugging various bugs, waiting for printing, and presenting & speaking, it finally took on a somewhat finished appearance.

This project is mainly used for lighting systems for street lamps in remote rural areas. The model is a bit abstract, but it actually plays the role of a street lamp.

## Project Innovations

- **Solar power supply.** Self-sufficient (after consulting detailed information, the amount of solar power generated is sufficient to light the LED)
- **Wireless connectivity.** Provides convenience for remote mountainous areas where it is difficult to lay cables
- **Intelligent algorithm.** Automatically turns on the lights at night; increases the brightness of the LED when people or vehicles pass by
- **Cloud-based unified control.** Uses GSM control, which can be remotely debugged in batches
- **Expandability.** Provides various customized functions for individual users with special lighting requirements

## Principles and Implementation

**Code:**

```cpp
#define BUTTONS_address   "channel/widget4_0/cmd/control" //switch command
#define LIGHT_STATUS_address  "channel/widget4_0/data/light"//switch status
#define ITENSITY_DATA_address "channel/widget4_0/data/lightsensor"
#define LEDPIN1    D1    //define bulb control pin
#define LEDPIN2    D2
#define LEDPIN3    D3
#define LEDPIN4    D5
#define CHECKIN1   A0
#define CHECKIN2   D4
```

int autostate = 2;
int light_state = 2;

void buttons_function(uint8_t *payload, uint32_t len)//Auto & Watering Buttons
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
    aJsonObject *_switch = aJson.getObjectItem(root, "mode");
    if(_switch != NULL)
    {
        SwitchKey = atoi(_switch->valuestring);
        if(SwitchKey)
        {
            SerialUSB.println("auto on");
            autostate=1;
            IntoRobot.publish(LIGHT_STATUS_address,"1");
        }
        else
        {
            SerialUSB.println("auto off");
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
            SerialUSB.println("manual on");
            light_state=1;
            IntoRobot.publish(LIGHT_STATUS_address,"1");
        }
        else
        {
            SerialUSB.println("manual off");
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
    digitalWrite(LEDPIN1, HIGH);    // Turn on LED 1
    digitalWrite(LEDPIN2, HIGH);    // Turn on LED 2
    digitalWrite(LEDPIN3, HIGH);    // Turn on LED 3
    digitalWrite(LEDPIN4, HIGH);    // Turn on LED 4
}

```
void light_half_up()
{
    analogWrite(LEDPIN1, 80);    // Turn on the light bulb
    analogWrite(LEDPIN2, 80);    // Turn on the light bulb
    analogWrite(LEDPIN3, 80);    // Turn on the light bulb
    analogWrite(LEDPIN4, 80);    // Turn on the light bulb
}

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
```

// IntoRobot.publish(LIGHT_STATUS_address,"1");
// IntoRobot.publish(LIGHT_STATUS_address,"0");
void setup()
{
    pinMode(D4,INPUT);
    SerialUSB.begin(115200);
    SerialUSB.println("hello world");
    pinMode(LEDPIN1, OUTPUT);    //initialize
    pinMode(LEDPIN2, OUTPUT);    //initialize
    pinMode(LEDPIN3, OUTPUT);    //initialize
    pinMode(LEDPIN4, OUTPUT);    //initialize
    //device receives light switch command from cloud platform
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
        SerialUSB.println("state=1");
        automode();
    }
    delay(100);
}
```

Due to time constraints of the competition, we can only roughly draw the model and assemble it by printing it out.

## FAQ

Q: Will there be follow-up to the project in the future?  
A: There are currently no plans for follow-up. The innovation is quite good, but whether it has commercial value remains to be verified.

## Conclusion

We did not win any awards in this competition. However, the competition improved our ability to code quickly and present on stage, and also gave me a taste of the feeling of working overtime to go live. I also met many people and received many souvenirs.

## References and Acknowledgments

- Team members: Lin Peijie, Huang Yuefeng, Zhang Ziyi
- [IntoRobot Cloud Platform](https://www.intorobot.com/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.