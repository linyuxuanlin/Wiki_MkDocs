# Parámetros de CC

Probar los parámetros de CC es esencialmente medir la resistividad del silicio. Pueden ser probados mediante el método de CC, con la corriente forzada de CCVI/PPMU y luego midiendo el voltaje, o forzando el voltaje y luego midiendo la corriente. Se comparará el valor medido con el valor especificado por el probador y luego se concluirá un resultado de prueba como APROBADO o FALLIDO. Los elementos que pueden ser probados mediante el método de CC son los siguientes:

- [**Prueba de Corriente de Suministro de Energía (IDD)**](3) (Prueba de DC-IDD)
  - Prueba Bruta de IDD
  - Prueba de IDD Estática
  - Prueba de IDD Dinámica
  - Prueba de IDD Quiescente (IDDQ)
- [**Prueba de Fuga**](3) (Prueba de Fuga)
  - Prueba de Fuga de Entrada (IIL y IIH)
  - Prueba de Fuga de Tristate de Salida (IOZL e IOZH)
- [**Prueba de Umbral de Nivel**](3) (Prueba de Umbral de Nivel)
  - Prueba de Umbral de Nivel de Salida (VOL/IOL y VOH/IOH)
  - Prueba de Umbral de Nivel de Entrada (VIL y VIH)
- Pruebas opcionales
  - Abrazadera de Entrada (VI)
  - Prueba de Corriente de Cortocircuito de Salida (IOS)
  - Prueba de Entradas Resistivas
  - Prueba de Fanout de Salida

Los parámetros de CC también pueden ser probados con un método funcional digital, se compararán con el valor especificado mediante un comparador de voltaje dentro del PE (Pin Electrónico) durante el procedimiento de prueba funcional y se concluirá un resultado de prueba de APROBADO/NO APROBADO sin valores específicos.

Se menciona que la corriente se define como positiva cuando fluye hacia el DUT y como negativa cuando fluye fuera del DUT.

## Referencias y Reconocimientos

- *Los Fundamentos de la Prueba de Semiconductores Digitales*
- *Fundamentos de la Prueba Utilizando ATE*

> Original: <https://wiki-power.com/>
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), y debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.