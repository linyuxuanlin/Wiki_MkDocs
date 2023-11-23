# Parámetros CC

La prueba de los parámetros CC consiste esencialmente en medir la resistividad del silicio. Estos parámetros pueden ser evaluados mediante el método CC, aplicando una corriente forzada con DCVI/PPMU y luego midiendo la tensión, o aplicando una tensión forzada y luego midiendo la corriente. Luego se compara el valor medido con el valor especificado por el probador y se llega a un resultado de prueba que puede ser "APROBADO" o "FALLIDO". Los elementos que pueden ser evaluados mediante el método CC son los siguientes:

- [**Prueba de Corriente de Fuente de Alimentación (IDD)**](https://wiki-power.com/DC-IDD_Test)
  - Prueba Bruta de IDD
  - Prueba Estática de IDD
  - Prueba Dinámica de IDD
  - Prueba de IDD en Reposo (IDDQ)
- [**Prueba de Fugas**](https://wiki-power.com/Leakage_Test/)
  - Prueba de Fugas de Entrada (IIL e IIH)
  - Prueba de Fugas en Estado de Alta Impedancia de Salida (IOZL e IOZH)
- [**Prueba de Umbral de Nivel**](https://wiki-power.com/Level_Threshold_Test/)
  - Prueba de Umbral de Nivel de Salida (VOL/IOL y VOH/IOH)
  - Prueba de Umbral de Nivel de Entrada (VIL y VIH)
- Pruebas opcionales
  - Prueba de Abrazadera de Entrada (VI)
  - Prueba de Corriente de Cortocircuito de Salida (IOS)
  - Prueba de Entradas Resistivas
  - Prueba de Fanout de Salida

Los parámetros CC también pueden ser evaluados con el método funcional digital y se compararán con el valor especificado mediante un comparador de tensión dentro del PE (Pin Electronic) durante el procedimiento de prueba funcional, llegando a un resultado de "Apto" o "No Apto" sin valores específicos.

Es importante mencionar que la corriente se define como positiva cuando fluye hacia el DUT y negativa cuando fluye fuera del DUT.

## Referencias y Agradecimientos

- *Los Fundamentos de la Prueba de Semiconductores Digitales*
- *Fundamentos de Pruebas Utilizando ATE*

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por un acuerdo de [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) y debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.