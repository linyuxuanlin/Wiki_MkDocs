# Hack.init() Hackathon

—— Wight · Cloud-Based Wireless Lighting System.

![](https://media.wiki-power.com/img/wight.jpg)

Project Repository: [**linyuxuanlin/Wight**](https://github.com/linyuxuanlin/Wight)

## Background

This project was created during the 2017 hack.init() hackathon. Over 20 hours of coding, modeling, debugging various messy bugs, waiting for prints, presentations, and speeches, we finally have something that resembles a finished product.

This project is primarily designed for lighting systems in rural and remote areas. The model may seem a bit abstract, but in reality, it serves as a streetlight.

## Key Innovations

- **Solar-Powered.** Self-sustaining (after detailed research, solar power output is sufficient to illuminate LEDs).
- **Wireless Connectivity.** Convenient for areas where laying cables is impractical.
- **Smart Algorithms.** Automatically turns on the lights at night, increases LED brightness when people or vehicles pass by.
- **Cloud-Based Unified Control.** Utilizes a GSM central controller for remote batch debugging.
- **Expandability.** Offers various custom features for individual users with unique lighting requirements.

## Principles and Implementation

**Code:**

```cpp
#define BUTTONS_address   "channel/widget4_0/cmd/control" // Switch command
#define LIGHT_STATUS_address  "channel/widget4_0/data/light" // Switch status
#define ITENSITY_DATA_address "channel/widget4_0/data/lightsensor"
#define LEDPIN1    D1    // Define bulb control pins
#define LEDPIN2    D2
#define LEDPIN3    D3
#define LEDPIN4    D5
#define CHECKIN1   A0
#define CHECKIN2   D4
```

```cpp
int autostate = 2;
int light_state = 2;

void buttons_function(uint8_t *payload, uint32_t len) // Auto & Watering Buttons
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
            SerialUSB.println("Automatic mode turned on");
            autostate = 1;
            IntoRobot.publish(LIGHT_STATUS_address, "1");
        }
        else
        {
            SerialUSB.println("Automatic mode turned off");
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
            SerialUSB.println("Manual mode turned on");
            light_state = 1;
            IntoRobot.publish(LIGHT_STATUS_address, "1");
        }
        else
        {
            SerialUSB.println("Manual mode turned off");
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
    digitalWrite(LEDPIN1, HIGH); // Turn on the light bulb
    digitalWrite(LEDPIN2, HIGH); // Turn on the light bulb
    digitalWrite(LEDPIN3, HIGH); // Turn on the light bulb
    digitalWrite(LEDPIN4, HIGH); // Turn on the light bulb
}

void light_half_up()
{
    analogWrite(LEDPIN1, 80); // Turn on the light bulb (at half intensity)
    analogWrite(LEDPIN2, 80); // Turn on the light bulb (at half intensity)
    analogWrite(LEDPIN3, 80); // Turn on the light bulb (at half intensity)
    analogWrite(LEDPIN4, 80); // Turn on the light bulb (at half intensity)
}
```

```cpp
void lightdown()
{
    digitalWrite(LEDPIN1, LOW);
    digitalWrite(LEDPIN2, LOW);
    digitalWrite(LEDPIN3, LOW);
    digitalWrite(LEDPIN4, LOW);
}

int getlight()
{
    int k = analogRead(CHECKIN1);
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
    if (getlight() >= 400)
    {
        IntoRobot.publish(LIGHT_STATUS_address, "1");
        if (get_IR_data() == 0)
            lightup();
        else
            light_half_up();
    }
    else
    {
        IntoRobot.publish(LIGHT_STATUS_address, "0");
        lightdown();
    }
}

void HUMIDITY_print_function(uint8_t *payload, uint32_t len)
{
}

void setup()
{
    pinMode(D4, INPUT);
    SerialUSB.begin(115200);
    SerialUSB.println("hello world");
    pinMode(LEDPIN1, OUTPUT);    // Initialize
    pinMode(LEDPIN2, OUTPUT);    // Initialize
    pinMode(LEDPIN3, OUTPUT);    // Initialize
    pinMode(LEDPIN4, OUTPUT);    // Initialize

    // Device receives light switch commands from the cloud platform
    IntoRobot.subscribe(BUTTONS_address, NULL, buttons_function);
    IntoRobot.subscribe(ITENSITY_DATA_address, NULL, HUMIDITY_print_function);
}

void loop()
{
    int a = map(getlight(), 0, 1024, 100, 0);
    IntoRobot.publish(LIGHT, a);
    SerialUSB.println(getlight());

    if (autostate == 0)
    {
        if (light_state == 1)
            lightup();
        else
            lightdown();
    }
    else if (autostate == 1)
    {
        SerialUSB.println("state=1");
        automode();
    }
    delay(100);
}
```

**FAQ**

Q: Will there be follow-ups to the project in the later stages?
A: Currently, there are no plans for further follow-ups. The project shows great innovation, but its commercial application value remains to be validated.

**Conclusion**

We did not win any awards in this competition. However, the competition improved our ability to rush code and present, allowed us to experience the feeling of overtime work and going live in advance, and introduced us to many people. We also received many souvenirs.

**References and Acknowledgments**

- Team Members: Lin Peijie, Huang Yuefeng, Zhang Ziyi
- [IntoRobot Cloud Platform](https://www.intorobot.com/)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
