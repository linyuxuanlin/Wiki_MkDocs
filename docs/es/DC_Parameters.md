# Parámetros DC

> Este artículo solo está disponible en inglés.

La prueba de parámetros DC es esencialmente la medición de la resistividad del silicio. Pueden ser probados mediante el método DC, con corriente forzada DCVI/PPMU y luego midiendo el voltaje, o forzando el voltaje y midiendo la corriente. Se comparará el valor medido con el valor de especificación fuera del probador, luego se concluirá un resultado de prueba con PASA o FALLA. Los elementos que se pueden probar bajo el método DC son los siguientes:

- [**Prueba de corriente de suministro de energía (IDD)**](https://wiki-power.com/DC-IDD_Test)
  - Prueba bruta de IDD
  - Prueba estática de IDD
  - Prueba dinámica de IDD
  - Prueba de IDD quiescente (IDDQ)
- [**Prueba de fugas**](https://wiki-power.com/Leakage_Test/)
  - Prueba de fuga de entrada (IIL y IIH)
  - Prueba de fuga de tristate de salida (IOZL y IOZH)
- [**Prueba de umbral de nivel**](https://wiki-power.com/Level_Threshold_Test/)
  - Prueba de umbral de nivel de salida (VOL/IOL y VOH/IOH)
  - Prueba de umbral de nivel de entrada (VIL y VIH)
- Pruebas opcionales
  - Abrazadera de entrada (VI)
  - Prueba de corriente de cortocircuito de salida (IOS)
  - Prueba de entradas resistivas
  - Prueba de fanout de salida

Los parámetros DC también se pueden probar con el método funcional digital, se compararán con el valor de especificación mediante el comparador de voltaje dentro del PE (Pin Electronic) durante el procedimiento de prueba funcional, y se concluirá un resultado de prueba de Go/No-Go sin valores específicos.

Se menciona que la corriente se define como positiva cuando fluye hacia el DUT y negativa cuando fluye fuera del DUT.

## Referencias y agradecimientos

- *Los fundamentos de la prueba de semiconductores digitales*
- *Fundamentos de la prueba utilizando ATE*

> Original: <https://wiki-power.com/>  
> Este artículo está protegido por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducido con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.