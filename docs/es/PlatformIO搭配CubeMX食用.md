# PlatformIO con CubeMX

## Antecedentes

En el [**artículo anterior**](https://wiki-power.com/PlatformIO—一站式嵌入式开发工具), pudimos ver que PlatformIO es mucho más elegante que Keil.  
Es bien sabido que en el modo de apertura de STM32, la biblioteca HAL es más conveniente y fácil de usar que la biblioteca estándar (en combinación con la herramienta CubeMX), pero la compatibilidad de PlatformIO con CubeMX no es perfecta (se requiere la conversión de código a través de middleware Python).

En este artículo, presentaré un método único para hacer que la combinación de PlatformIO y CubeMX sea aún más deliciosa.

## Inicialización del proyecto

Resumen: he colocado la carpeta del proyecto creado con los siguientes pasos en [**este repositorio**](https://github.com/linyuxuanlin/Template_of_PlatformIO_with_CubeMX), simplemente clónalo.

### Inicialización de CubeMX

1. Crear un nuevo proyecto
2. Seleccione el modelo de MCU
3. Configure Pinout & Configuration
   1. Configure RCC (seleccionar reloj externo / interno, según sea necesario)
   2. Configure SYS (cambie la opción DEBUG de `No Debug` a `Serial Wire`)
4. Configure Clock Configuration
5. Configure Project Manager
   1. Página del proyecto
      1. Escriba el nombre del proyecto (Project Name) por ejemplo `Template_of_PlatformIO_with_CubeMX`
      2. Cambie la ubicación del proyecto (Project Location) por ejemplo `D:/Desktop`
      3. Cambie la cadena de herramientas (Toolchain / IDE) a `Other Toolchains`
   2. Página del generador de código
      1. Seleccione la opción del paquete de biblioteca de firmware STM32Cube (STM32Cube Firmware Library Package) como `Copy only the necessary library files`
      2. Seleccione la opción de generación de archivos (Generated files) y marque `Generate peripheral initialization as a pair of '.c/.h' files per peripheral`

Finalmente, haga clic en `Generate Code` en la esquina superior derecha para generar el código.

### Inicialización de PlatformIO

1. Abra la página principal de PlatformIO
2. Haga clic en `New Project` para crear un nuevo proyecto
   1. Escriba el nombre del proyecto. ¡Importante! ¡Debe ser el mismo que el configurado en CubeMX! (por ejemplo, `Template_of_PlatformIO_with_CubeMX`)
   2. Seleccione la placa / modelo de MCU. Puede seleccionar directamente el modelo de MCU (por ejemplo, STM32F103C8) o la placa (por ejemplo, BluePill F103C8). ¡Importante! ¡Debe ser el mismo que el configurado en CubeMX!
   3. Seleccione el marco de código `Framework` como `STM32Cube`
   4. Desmarque la opción `Use default location` en la ruta `Location` y personalice la ruta. ¡Importante! ¡Debe ser el mismo que el configurado en CubeMX! (por ejemplo, `D:/Desktop`)
3. Abra el archivo `platformio.ini` en el proyecto y agregue las siguientes líneas:

   ```ini
   [platformio]
   include_dir=Inc
   src_dir=Src
   ```

   Esto se debe a que los marcos de carpetas generados por defecto de PlatformIO y CubeMX son diferentes. Para garantizar la compatibilidad, seguimos a CubeMX.

4. Puede eliminar la carpeta `include` del proyecto. Debido a que los nombres de archivo de Windows no distinguen entre mayúsculas y minúsculas, la carpeta `src` se convierte en `Src`.

### ¡Disfrútalo al máximo!

En el proyecto, los archivos `.c` se encuentran en la carpeta `Src` y los archivos `.h` en `Inc`. Todo el código entre `/* USER CODE BEGIN */` y `/* USER CODE END */` se mantendrá sin cambios durante el proceso de generación de CubeMX y no será sobrescrito.

PlatformIO puede ser utilizado para compilar con la combinación de teclas `Ctrl + Alt + B`, compilar y cargar con `Ctrl + Alt + U` y para iniciar la depuración con `F5`.

El siguiente paso es aprender sobre la biblioteca HAL. ¡Continuará!

## Referencias y agradecimientos

- [STM32CubeMX Tutorial 03_Creating and Generating Code Project](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B03_%E5%88%9B%E5%BB%BA%E5%B9%B6%E7%94%9F%E6%88%90%E4%BB%A3%E7%A0%81%E5%B7%A5%E7%A8%8B.html)
- [STM32CubeMX Tutorial 06_Project Manager Detailed Description](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B06_Project%20Manager%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E5%99%A8%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E.html)
- [Using VS Code as STM32 Development Platform (PlatformIO)](https://www.jianshu.com/p/49cfa03d6164)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.