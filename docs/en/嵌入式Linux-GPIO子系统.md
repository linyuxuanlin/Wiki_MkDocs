# Embedded Linux - GPIO Subsystem

## References and Acknowledgements

- [8. Controlling Buzzer (GPIO Subsystem)](https://doc.embedfire.com/linux/stm32mp1/linux_base/en/latest/linux_app/gpio_subsystem/gpio_subsystem.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

## Introduction to GPIO Subsystem

GPIO (General Purpose I/O) refers to general-purpose input and output ports. These pins usually have multiple functions, with the most basic being high and low level input detection and output. Some pins are also bound to on-chip peripherals of the main controller and can be used as communication pins for serial ports, I2C, networking, voltage detection, etc.

Similar to the LED subsystem, Linux provides a GPIO subsystem driver framework that exports the CPU's GPIO pins to user space. We can control them by accessing the `/sys` file system. The GPIO subsystem supports using pins for basic input and output functions, with support for interrupt detection in input mode. (More detailed information about the GPIO subsystem can be found in the Linux kernel source code under the `Documentation/gpio` directory)

## GPIO Device Directory

The directory where the GPIO driver subsystem is exported to user space is `/sys/class/gpio`. You can use the following command to view it:

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.