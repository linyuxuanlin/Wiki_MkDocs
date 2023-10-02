# Embedded Linux - GPIO Subsystem

## References and Acknowledgements

- [8. Control Buzzer (GPIO Subsystem)](https://doc.embedfire.com/linux/stm32mp1/linux_base/en/latest/linux_app/gpio_subsystem/gpio_subsystem.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

## Introduction to GPIO Subsystem

GPIO (General Purpose I/O) refers to general-purpose input/output ports. These pins usually have multiple functions, with the most basic being high/low level input detection and output. Some pins are also bound to on-chip peripherals of the controller and can be used as communication pins for serial ports, I2C, networking, voltage detection, etc.

Similar to the LED subsystem, Linux provides a GPIO subsystem driver framework that exports the CPU's GPIO pins to user space. We can control them by accessing the `/sys` file system. The GPIO subsystem supports using pins for basic input/output functions, with interrupt detection supported for input functions. (More detailed explanations about the GPIO subsystem can be found in the `Documentation/gpio` directory of the Linux kernel source code.)

## GPIO Device Directory

The directory exported by the GPIO driver subsystem to user space is `/sys/class/gpio`, which can be viewed using the following command:

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.