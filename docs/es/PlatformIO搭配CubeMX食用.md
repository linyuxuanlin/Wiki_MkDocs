# Plataforma PlatformIO junto con CubeMX

## Antecedentes

En el [**artículo anterior**](https://wiki-power.com/PlatformIO—una herramienta de desarrollo embebido todo en uno), pudimos apreciar que el uso de PlatformIO es mucho más elegante que Keil. Como es bien sabido, en el contexto de STM32, la biblioteca HAL es más conveniente que la biblioteca estándar (cuando se combina con la potente herramienta CubeMX). Sin embargo, la compatibilidad oficial de PlatformIO con CubeMX no es perfecta (requiere conversión de código a través de middleware Python).

En este artículo, presentaré un enfoque único para que PlatformIO funcione de manera más armoniosa junto con CubeMX.

## Inicialización del Proyecto

Si no tienes tiempo para leer todo esto, puedes encontrar la carpeta de proyecto creada con los siguientes pasos en [**este repositorio**](https://github.com/linyuxuanlin/Template_of_PlatformIO_with_CubeMX) y simplemente clonarla.

### Operaciones de Inicialización de CubeMX

1. Crea un nuevo proyecto.
2. Selecciona el modelo de MCU.
3. Configura Pinout y Configuración.
   1. Configura RCC (elige entre reloj externo o interno, según corresponda).
   2. Configura SYS (cambia la opción DEBUG de 'No Debug' a 'Serial Wire' según sea necesario).
4. Configura la Configuración del Reloj.
5. Configura el Administrador de Proyectos.
   1. Página de Proyecto
      1. Ingresa el nombre del proyecto (Project Name), por ejemplo, `Template_of_PlatformIO_with_CubeMX`.
      2. Modifica la ubicación del proyecto (Project Location), por ejemplo, `D:/Desktop`.
      3. Cambia la herramienta (Toolchain / IDE) a 'Other Toolchains'.
   2. Página del Generador de Código
      1. Selecciona la opción de paquete de biblioteca de software (STM32Cube Firmware Library Package) como 'Copy only the necessary library files'.
      2. Marca la opción 'Generate peripheral initialization as a pair of '.c/.h' files per peripheral' en la sección de archivos generados (Generated files).

Finalmente, después de configurar todo, haz clic en 'Generate Code' en la esquina superior derecha para generar el código.

### Operaciones de Inicialización de PlatformIO

1. Abre la página principal de PlatformIO.
2. Haz clic en 'New Project' para crear un nuevo proyecto.
   1. Ingresa el nombre del proyecto. ¡Importante! Debe ser el mismo que el configurado en CubeMX (por ejemplo, `Template_of_PlatformIO_with_CubeMX`).
   2. Selecciona la placa o el modelo de MCU. Puedes elegir directamente el modelo del MCU (por ejemplo, STM32F103C8) o seleccionar una placa (por ejemplo, BluePill F103C8). ¡Asegúrate de que coincida con la configuración de CubeMX!
   3. En el marco de código (Framework), selecciona 'STM32Cube'.
   4. Desmarca la casilla 'Use default location' en la sección de ubicación (Location) y personaliza la ubicación. ¡Asegúrate de que coincida con la configuración de CubeMX (por ejemplo, `D:/Desktop`).
3. Abre el archivo `platformio.ini` en el proyecto y agrega las siguientes líneas:

   ```ini
   [platformio]
   include_dir=Inc
   src_dir=Src
   ```

   Esto se debe a que las carpetas de estructura predeterminada generadas por PlatformIO y CubeMX son diferentes. Para garantizar la compatibilidad, seguimos la estructura de CubeMX.

4. Puedes eliminar la carpeta 'include' del proyecto. Además, debido a que Windows no distingue entre mayúsculas y minúsculas en los nombres de archivos, la carpeta 'src' se convierte automáticamente en 'Src'.

¡Ahora puedes disfrutar plenamente de tu proyecto!

En el proyecto, los archivos con extensión `.c` se encuentran en la carpeta `Src`, mientras que los archivos con extensión `.h` se ubican en la carpeta `Inc`.

Todo el código que esté comprendido entre las etiquetas `/* USER CODE BEGIN */` y `/* USER CODE END */` se mantendrá sin cambios a lo largo del proceso de generación posterior realizado por CubeMX, y no será sobrescrito.

En PlatformIO, puedes compilar con el atajo `Ctrl + Alt + B`, compilar y cargar con `Ctrl + Alt + U`, y comenzar la depuración con `F5`.

El siguiente paso en nuestra exploración es aprender acerca de la biblioteca HAL. Continuará...

## Referencias y Agradecimientos

- [STM32CubeMX Serie de Tutoriales 03 - Creación y Generación de Proyectos de Código](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B03_%E5%88%9B%E5%BB%BA%E5%B9%B6%E7%94%9F%E6%88%90%E4%BB%A3%E7%A0%81%E5%B7%A5%E7%A8%8B.html)
- [STM32CubeMX Serie de Tutoriales 06 - Detalles del Gestor de Proyectos](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B06_Project%20Manager%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E5%99%A8%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E.html)
- [Utilizando VS Code como Plataforma de Desarrollo STM32 (PlatformIO)](https://www.jianshu.com/p/49cfa03d6164)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.