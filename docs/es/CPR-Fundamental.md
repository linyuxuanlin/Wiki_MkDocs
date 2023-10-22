# CPR - Fundamentos

**CPR** representa **Reducción de Potencia Central**, una **tecnología de gestión de energía adaptativa** que determina el voltaje óptimo del producto, permitiendo la compensación en bucle cerrado del voltaje CC, la variación de temperatura, el proceso y la degradación debida al envejecimiento, con el fin de optimizar la potencia y el rendimiento del dispositivo.

El núcleo de CPR consta de un controlador y varios sensores integrados en el SoC para controlar el nivel de VDD de un chip. Los sensores están formados por múltiples osciladores de anillo para estimar la velocidad de funcionamiento del chip. Luego, el controlador proporciona un resultado de comando de modificación de VDD al PMIC, que puede programarse mediante software.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.