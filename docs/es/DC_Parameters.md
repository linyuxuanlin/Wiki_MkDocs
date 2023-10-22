# Parámetros de CC

La prueba de los parámetros de CC consiste esencialmente en medir la resistividad del silicio. Se pueden probar mediante el método de CC, aplicando una corriente mediante DCVI/PPMU y luego midiendo el voltaje, o aplicando un voltaje y midiendo la corriente. Luego se comparará el valor medido con el valor especificado en el probador y se llegará a un resultado de prueba que será "APROBADO" o "FALLIDO". Los elementos que se pueden probar mediante el método de CC son los siguientes:

- **Prueba de Corriente de Suministro de Energía (IDD)**](https://wiki-power.com/es/Prueba de CC-IDD
  - Prueba Bruta de IDD
  - Prueba Estática de IDD
  - Prueba Dinámica de IDD
  - Prueba de Corriente en Reposo (IDDQ)
- **Prueba de Fugas**](https://wiki-power.com/es/Prueba de Fugas
  - Prueba de Fugas de Entrada (IIL e IIH)
  - Prueba de Fugas en Tristate de Salida (IOZL e IOZH)
- **Prueba de Umbral de Nivel**](https://wiki-power.com/es/Prueba de Umbral de Nivel
  - Prueba de Umbral de Nivel de Salida (VOL/IOL y VOH/IOH)
  - Prueba de Umbral de Nivel de Entrada (VIL y VIH)
- Pruebas opcionales
  - Abrazadera de Entrada (VI)
  - Prueba de Corriente en Cortocircuito de Salida (IOS)
  - Prueba de Entradas Resistivas
  - Prueba de Fanout de Salida

Los parámetros de CC también se pueden probar mediante el método funcional digital, y se compararán con el valor especificado mediante un comparador de voltaje dentro del PE (Pin Electronic) durante el procedimiento de prueba funcional. Se llegará a un resultado de prueba "Ir/No Ir" sin valores específicos.

Se menciona que la corriente se define como positiva cuando fluye hacia el DUT y negativa cuando fluye fuera del DUT.

## Referencias y Reconocimientos

- *Los Fundamentos de la Prueba de Semiconductores Digitales*
- *Fundamentos de Prueba Utilizando ATE*

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por un acuerdo de [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), y debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.