# Personalización de Sublime Text 3

## Antecedentes

**Sublime Text** es un potente editor de texto. Debido a que en el próximo semestre tendré cursos relacionados con Python y considero que la interfaz de herramientas como Pycharm no es muy atractiva, me gustaría intentar transformar Sublime Text en una poderosa herramienta para el desarrollo en Python.

Imagen del resultado después de la personalización:
![](https://media.wiki-power.com/img/ST3效果.png)

## [Implementación Mínima](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB)

1. Descarga la fuente `Consolas-with-Yahei`, descomprímela e instálala.
2. Descarga **la versión personalizada por mí de** [**Sublime Text 3**](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB) (sin garantía de actualizaciones).
3. Ejecuta directamente el archivo `.exe`. Para obtener información detallada sobre la configuración de parámetros, consulta a continuación.

## Configuración Detallada

### Descarga e Instalación del Software

Puedes descargar Sublime Text 3 desde el [sitio web oficial](http://www.sublimetext.com/) (se recomienda la descarga de la [**versión portátil**](https://download.sublimetext.com/Sublime%20Text%20Build%203176%20x64.zip)). El software es de uso gratuito, pero en ocasiones puede mostrar recordatorios de compra. Como recordatorio, he eliminado el número de serie del artículo. Si lo necesitas, no dudes en ponerte en contacto conmigo.

### Gestor de Paquetes e Instalación de Complementos

Para instalar el gestor de paquetes, ve a `Preferences -> Install Package Control` y, posteriormente, puedes acceder rápidamente al menú del gestor de paquetes con la combinación de teclas `Ctrl + Shift + P`.

Para instalar complementos, abre el menú del gestor de paquetes y escribe `Install Package`, presiona Enter y espera pacientemente. Luego, en el cuadro que aparecerá más adelante, busca el complemento que necesitas y haz clic en "Instalar". En el caso de complementos no publicados, puedes elegir directamente `Preference -> Browser packages`, abrir la carpeta donde se almacenan los complementos y colocarlos allí.

Para desinstalar complementos, abre el menú del gestor de paquetes y escribe `remove package`.

### Adaptación al Chino

1. Traducción al chino: Utiliza `Package Control` para buscar `ChineseLocalizations` y haz clic en "Instalar".
2. Problemas con la entrada en chino: Descarga [IMESupport](https://github.com/zcodes/IMESupport/archive/master.zip), descomprímelo en el directorio de instalación de complementos y reinicia Sublime para resolver el problema de que la ventana de entrada no siga al texto en chino.
3. Fuente en chino: Descarga `Consolas-with-Yahei`, descomprímelo e instálalo, luego sustituye la fuente en la configuración del usuario por `"font_face": "Consolas-with-Yahei",`.

   **Tema**

   Los temas oscuros que uso son los siguientes: Utiliza `Package Control` para buscar `Spacegray` y `Afterglow`, y sustitúyelos en la configuración del usuario por:

   ```json
   "color_scheme": "Packages/Theme - Spacegray/base16-ocean.dark.tmTheme",
   "theme": "Afterglow-green.sublime-theme"
   ```

### Ajustes Detallados

Puedes agregar el siguiente código en la configuración del usuario:

```json
"word_wrap": "true", // Envolver automáticamente cuando se oculta
"fold_buttons": true, // Activar el plegado de código
"fade_fold_buttons": true, // Ocultar automáticamente los botones de plegado
"tab_size": 4, // Tamaño de la sangría de la pestaña
"margin": 4, // Márgenes
"tabs_small": true, // Reducir el tamaño de la barra de pestañas
"trim_trailing_white_space_on_save": true, // Eliminar automáticamente los espacios en blanco al final de las líneas
"ensure_newline_at_eof_on_save": true, // Mantener automáticamente una línea vacía al final del archivo (útil para C)
```

### Complementos Recomendados

[Incluye aquí la lista de complementos recomendados]

A continuación, los complementos que están disponibles para su instalación directa a través de `Package Control`.

**StyleToken**: Muestra el color (RGB) representado por el código.

**FileHeader**: Personaliza las plantillas de archivo. Abre `Preferences -> Package Settings -> FileHeader -> Settings - User`, copia el contenido de `Default` a `User` y modifica la información personal de la siguiente manera:

```json
{
  "Default": {
    "author": "linyuxuanlin",
    "email": "824676271@qq.com",
    "website": "yxrct.com"
  }
}
```

Luego, modifica el contenido de las plantillas en `Preferences -> Browse Packages... -> FileHeader -> template -> header o body`. Efecto:  
![Imagen](https://media.wiki-power.com/img/ST3 模板效果.png)

### Ejecución de Python

Dado que el compilador incorporado no permite la entrada del usuario, se requiere el complemento `SublimeREPL`. Instálalo directamente con `Package Control` y agrega una combinación de teclas para activarlo en `Preferences —> Key Buildings -> User`:

```json
[
  {
    "keys": ["f5"],
    "caption": "SublimeREPL:Python",
    "command": "run_existing_window_command",
    "args": {
      "id": "repl_python_run",
      "file": "config/Python/Main.sublime-menu"
    }
  }
]
```

Después de esto, puedes ejecutar código Python directamente presionando `F5`.

### Formateo automático de código

Instala el complemento `Python PEP8 Autoformat` y agrega la siguiente combinación de teclas en `Key Buildings`:

```json
{ "keys": ["alt+r"], "command": "pep8_autoformat" }
```

De esta manera, podrás formatear tu código Python con `Alt + R`.

## Conclusión

La estética es igual a la productividad. Sublime Text no solo admite Python, sino que casi todos los formatos de archivo se pueden abrir y editar con él. Si se configura adecuadamente, escribir código en una interfaz minimalista y potente puede ser una experiencia bastante romántica.

## Referencias y Agradecimientos

- [Sublime Text 3: Personaliza tu herramienta de desarrollo (Parte 1)](https://www.sheyilin.com/2015/05/sublime_text_3_tiao_jiao_ni_de_si_ren_li_qi_1/)
- [Sublime Text: Uso del complemento FileHeader para generar encabezados de archivo (información de derechos de autor)](https://blog.csdn.net/afei__/article/details/82890493)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
