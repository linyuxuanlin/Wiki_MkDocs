# Configuración y consejos de OrCAD

Nota: Este artículo se basa en Cadence OrCAD Capture CIS.

## Fundamentos

Para dibujar un esquema eléctrico, utiliza OrCAD Capture CIS (Menú Inicio -> Cadence -> Capture CIS). Para diseñar una placa de circuito impreso, usa Allegro PCB Designer (Menú Inicio -> Cadence -> PCB Editor).

Por lo general, un archivo `.DSN` es suficiente para abarcar todo el proyecto. Al abrirlo, se generarán automáticamente archivos de esquemáticos `.opj`. Si utilizas Git para el control de versiones, puedes agregar el siguiente `.gitignore`:

```gitignore
# Desde gitignore original

#############
## Allegro
#############

# Ignorar archivos de registro
*.log
*.log,1
*.log,2
*.log,3

*.dml
*.lst

# Ignorar registros de eventos de Allegro
*.jrl
*.jrl,1

*.tag

# Archivos de informes
*.rpt

*.cfg
*.cfg,1

*.lck

# Archivos de informes
*.txt
*.txt,1
*.txt,2

# Excluir datos XY
!place_txt.txt

# Archivos de importación DXF
*.cnv

# Excluir archivo de parámetros Gerber
!art_param.txt

# Carpeta
# Ignorar carpetas completas
/signoise.run/

#############
## OrCAD
#############
*.dbk
*.opj
*.DRC
*.DSNlck

# Ignorar netlists
allegro/
```

## Configuración adicional

Ajustes de DRC:

![Imagen de configuración DRC](https://media.wiki-power.com/img/20210810134720.png)

Renombrar automáticamente las referencias al copiar componentes:

![Imagen de configuración de renombrado automático al copiar componentes](https://media.wiki-power.com/img/20210810134747.png)

Alinear los caracteres al moverlos cerca de la rejilla:

![Imagen de configuración para mover caracteres cerca de la rejilla](https://media.wiki-power.com/img/20210810134758.png)

Consejo: Si estás utilizando la biblioteca CIP y ves el mensaje "not found in the configured library lists", asegúrate de verificar la codificación de espacios en la ruta.

- **Zoom con la rueda del ratón**: `Opciones` - `Preferencias...` - `Pan y Zoom` - Ajusta ambos valores en `Factor de Zoom` a 1.1.
- **Actualizar el esquema al colocar componentes**: `Opciones` - `Preferencias...` - `Varios` - `Colocar Componente` - Marca la casilla `Actualizar componente al seleccionar`.
- **Configurar el tamaño de la rejilla**: `Opciones` - `Preferencias...` - `Visualización de Rejilla` - `Espaciado de Rejilla` - Ajusta a 1/2.

## Atajos de teclado

- Dibujar cables: `W`
- Cancelar: `ESC`
- Dibujar bus: `F4`
- Colocar etiquetas de red: `N`
- Rotar / reflejar horizontalmente / reflejar verticalmente componentes: `R` / `H` / `V`
- Abrir el panel CIS: `Z`
- Colocar fuentes de alimentación / tierra: `F` / `G`
- No conectar: `X`
- Filtrar: `Ctrl` + `I`
- Seleccionar múltiples elementos: Mantén presionada la tecla `Ctrl` y selecciona.
- Copiar y autoincrementar referencias: Mantén presionada la tecla `Ctrl` y arrastra un componente.
- Mover el esquema con el ratón como centro de gravedad: Mantén presionada la tecla `C` y arrastra el ratón.
- Colocar buses: `E`
- Colocar texto: `T`

## Errores y soluciones

- Incapacidad para arrastrar componentes: En general, reiniciar suele resolver este problema.

## Consejos

### Diferencia entre "off-page" y "port"

"Off-page" se utiliza generalmente en esquemas planos, mientras que "port" se utiliza en esquemas jerárquicos.

### Comprobación de DRC (Design Rule Check)

```markdown
1. Haz clic en la opción "Seleccionar proyecto completo" en el árbol de archivos.
2. En la barra de herramientas, selecciona `Herramientas` - `Verificar Reglas de Diseño...`
3. Marca las casillas de verificación "Ejecutar Reglas Físicas" y "Ver Resultados".
4. Haz clic en "Aceptar", se generará un informe y se abrirá automáticamente.

## Referencias y Agradecimientos

- [Resumen del Inicio Rápido de Cadence](https://blog.csdn.net/ReCclay/article/details/101225359)
- [Tutorial de OrCAD Capture](https://resources.orcad.com/orcad-capture-tutorials)
- [Solución al problema de la fuente borrosa en el software Cadence en pantallas de alta resolución](https://blog.csdn.net/qq_34338527/article/details/108846792)
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
