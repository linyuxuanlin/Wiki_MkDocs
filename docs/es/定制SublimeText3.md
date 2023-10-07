# Personalización de SublimeText3

## Antecedentes

**Sublime Text** es un editor de texto muy poderoso. Debido a que el próximo semestre tengo cursos relacionados con Python y las herramientas como Pycharm tienen una interfaz de usuario un poco fea, quiero intentar convertir Sublime Text en una herramienta de desarrollo de Python.

Imagen del resultado personalizado:
![](https://f004.backblazeb2.com/file/wiki-media/img/ST3效果.png)

## [Implementación mínima](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB)

1. Descarga la fuente `Consolas-with-Yahei`, descomprímela e instálala.
2. Descarga **mi versión personalizada** de [**Sublime Text 3**](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB) (sin garantía de actualización).
3. Ejecuta directamente el archivo `.exe`, para obtener una configuración detallada, consulta el siguiente texto.

## Configuración detallada

### Descarga e instalación de software

Sublime Text 3 se puede descargar desde el [sitio web oficial](http://www.sublimetext.com/) (se recomienda descargar la [**versión portátil**](https://download.sublimetext.com/Sublime%20Text%20Build%203176%20x64.zip)). El software se puede utilizar de forma gratuita, pero a veces aparece una ventana emergente de pago. Después de recibir la advertencia, he eliminado el número de serie del artículo. Si lo necesitas, contáctame.

### Instalación de administrador de paquetes y complementos

Instala el administrador de paquetes: `Preferences -> Install Package Control`, luego puedes usar la tecla de acceso rápido `Ctrl + Shift + P` para abrir rápidamente la interfaz del administrador de paquetes.

Instala complementos: abre la interfaz de `Package Control`, escribe `Install Package`, presiona Enter, espera pacientemente y busca el complemento necesario en la ventana emergente y haz clic en instalar. Para los complementos no publicados, simplemente selecciona `Preference -> Browser packages`, abre la carpeta donde se almacenan los complementos y coloca el complemento directamente allí.

Desinstala complementos: abre la interfaz de `Package Control`, escribe `remove package`.

### Adaptación al chino

1. Localización en chino: busca `ChineseLocalizations` en `Package Control` y haz clic en instalar.
2. Problemas de entrada en chino: descarga [IMESupport](https://github.com/zcodes/IMESupport/archive/master.zip), descomprímelo en el directorio de instalación de complementos, reinicia Sublime y resuelve el problema de que el cuadro de entrada no sigue la entrada en chino.
3. Fuente china: descarga `Consolas-with-Yahei`, descomprímela e instálala, y reemplázala en la configuración del usuario con `"font_face": "Consolas-with-Yahei",`.

   **Tema**

El tema oscuro que uso: busca `Spacegray` y `Afterglow` en `Package Control`, y reemplázalo en la configuración del usuario con:

```
"color_scheme": "Packages/Theme - Spacegray/base16-ocean.dark.tmTheme",
"theme": "Afterglow-green.sublime-theme"
```

### Ajustes de detalle

En la configuración del usuario, puedes agregar el siguiente código:

```
"word_wrap": "true", // Envolver automáticamente cuando se oculta
"fold_buttons": true, // Habilitar el plegado de código
"fade_fold_buttons": true, // Los botones de plegado se ocultan automáticamente
"tab_size": 4, // Tamaño de indentación de tabulación
"margin": 4, // Indentación
"tabs_small": true, // Hacer que la barra de pestañas sea más pequeña
"trim_trailing_white_space_on_save": true, // Eliminar automáticamente los espacios en blanco al final de la línea
"ensure_newline_at_eof_on_save": true, // Mantener automáticamente una línea vacía al final del archivo, para C
```

### Complementos recomendados

Los siguientes complementos están disponibles para instalar directamente a través de `Package Control`.

**StyleToken**: muestra el color (RGB) que representa el código. **FileHeader**: plantilla de archivo personalizada. Abre `Preferences -> Package Settings -> FileHeader -> Settings - User`, copia el contenido de `Default` en `User` y modifica la información personal, por ejemplo:

```
{
    "Default": {
        "author": "linyuxuanlin",
        "email": "824676271@qq.com",
        "website": "yxrct.com"
    }
}
```

Modifica el contenido de la plantilla en `Preferences -> Browse Packages... -> FileHeader -> template -> header o body`. Resultado:  
 ![](https://f004.backblazeb2.com/file/wiki-media/img/ST3 模板效果。png)

### Ejecución de Python

Debido a que el compilador incorporado no tiene entrada de usuario, se necesita un complemento: `SublimeREPL`. Instálalo directamente a través de `Package Control` y agrega un atajo en `Preferences —> Key Buildings -> User`:

```
[
    { "keys": ["f5"], "caption": "SublimeREPL:Python",
                      "command": "run_existing_window_command", "args":
                      {
                           "id": "repl_python_run",
                           "file": "config/Python/Main.sublime-menu"
                      }
    },
]
```

Luego, en el código de Python, puedes presionar `F5` para ejecutarlo.

### Formateo automático de código

Instala el complemento `Python PEP8 Autoformat` y agrega el siguiente atajo en `Key Buildings`:

```
{ "keys": ["alt+r"], "command": "pep8_autoformat" },
```

Ahora puedes formatear el código de Python con `Alt + R`.

## Conclusión

La apariencia es importante para la productividad. Sublime Text no solo es compatible con Python, sino que también puede abrir y editar casi todos los formatos de archivo. Si lo configuras correctamente, escribir código en una interfaz minimalista y poderosa puede ser bastante romántico.

## Referencias y agradecimientos

- [Sublime Text 3 调教你的私人利器（上）](https://www.sheyilin.com/2015/05/sublime_text_3_tiao_jiao_ni_de_si_ren_li_qi_1/)
- [Sublime Text 自动生成文件头部注释（版权信息）：FileHeader 插件的使用](https://blog.csdn.net/afei__/article/details/82890493)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.