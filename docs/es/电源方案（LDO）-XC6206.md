# Esquema de alimentación (LDO) - XC6206

La serie XC6206 es un regulador de voltaje positivo de tres terminales de alta precisión y bajo consumo de energía. Proporciona una corriente alta y una caída de voltaje mínima, y está compuesto internamente por un circuito de limitación de corriente, un transistor de conducción, un voltaje de referencia de precisión y un circuito de corrección. Esta serie es compatible con capacitores cerámicos de baja ESR. El voltaje de salida se puede seleccionar en incrementos de 0.1V en un rango de 1.2V a 5.0V.

En este artículo se utiliza la serie XC6206 de TOREX, con encapsulado SOT-23. Otros fabricantes pueden ofrecer modelos equivalentes, pero se recomienda verificar los parámetros detallados.

Repositorio del proyecto: [**Collection_of_Power_Module_Design/LDO/XC6206**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/LDO/XC6206)

## Características principales

- Corriente máxima de salida: 200mA (valor típico a 6.0V)
- Caída de voltaje: 250mV a 100mA (valor típico a 6.0V)
- Voltaje de operación máximo: 6.0V
- Rango de voltaje de salida: 1.2V ~ 5.0V (incremento de 0.1V)
- Precisión: ±30mV cuando Vout < 1.5V; ±2% cuando Vout > 1.5V; ±1% cuando Vout > 2V
- Bajo consumo de energía: 1.0uA (valor típico)
- Circuitos de protección: circuito de limitación de corriente incorporado
- Temperatura de operación: -40℃ ~ +85℃
- Encapsulados disponibles: SOT-23, SOT-89, USP-6B

## Descripción de la selección

![](https://media.wiki-power.com/img/20220420102910.png)

## Circuito de aplicación típico

![](https://media.wiki-power.com/img/20220420102323.png)

## Diagrama de funciones internas

![](https://media.wiki-power.com/img/20220420102514.png)

Nota: El diodo dentro del diagrama es un diodo ESD o un diodo parásito.

## Definición de pines

![](https://media.wiki-power.com/img/20220420103005.png)

| Nombre del pin | Descripción del pin     |
| -------------- | ----------------------- |
| VSS            | Tierra                  |
| Vin            | Entrada de alimentación |
| Vout           | Salida de alimentación  |

## Descripción de las características

Tabla de parámetros específicos para cada modelo:

![](https://media.wiki-power.com/img/20220420103738.png)

## Referencias y agradecimientos

- [XC6206_Datasheet](https://www.torexsemi.com/file/xc6206/XC6206.pdf)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
