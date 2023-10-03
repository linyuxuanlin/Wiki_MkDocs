# Esquema de alimentación (LDO) - XC6206

La serie XC6206 es un regulador de voltaje positivo de tres terminales de alta precisión y bajo consumo de energía que proporciona una corriente alta y una diferencia de voltaje mínima. Está compuesto internamente por un circuito limitador de corriente, un transistor de conducción, un voltaje de referencia de precisión y un circuito corrector de error. Esta serie es compatible con capacitores cerámicos de baja ESR. El voltaje de salida se puede seleccionar en incrementos de 0.1V en el rango de 1.2V a 5.0V.

En este artículo, se utiliza la serie XC6206 de TOREX en un paquete SOT-23. Otros fabricantes pueden utilizar el mismo modelo, pero se recomienda verificar los parámetros detallados.

Repositorio del proyecto: [**Collection_of_Power_Module_Design/LDO/XC6206**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/LDO/XC6206)

## Características principales

- Corriente máxima de salida: 200mA (valor típico a 6.0V)
- Diferencia de voltaje: 250mV@100mA (valor típico a 6.0V)
- Voltaje de operación máximo: 6.0V
- Rango de voltaje de salida: 1.2V ~ 5.0V (incrementos de 0.1V)
- Precisión: ±30mV cuando Vout<1.5V; ±2% cuando Vout>1.5V; ±1% cuando Vout>2V
- Bajo consumo de energía: valor típico de 1.0uA
- Circuitos de protección: circuito limitador de corriente incorporado
- Temperatura de operación: -40℃~ +85℃
- Paquetes opcionales: SOT-23, SOT-89, USP-6B

## Selección del modelo

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420102910.png)

## Circuito de aplicación típico

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420102323.png)

## Diagrama de funciones internas

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420102514.png)

Nota: El diodo en el diagrama es un diodo ESD o un diodo parásito.

## Definición de pines

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420103005.png)

| Nombre del pin | Descripción del pin |
| -------- | -------- |
| VSS      | Tierra       |
| Vin      | Entrada de alimentación |
| Vout     | Salida de alimentación |

## Descripción de características

Tabla de parámetros específicos de cada modelo:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420103738.png)

## Referencias y agradecimientos

- [XC6206_Datasheet](https://www.torexsemi.com/file/xc6206/XC6206.pdf)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.