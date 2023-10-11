# Configuración y consejos de OrCAD

Nota: Este artículo se basa en Cadence OrCAD Capture CIS.

## Fundamentos

Para dibujar un esquema, use OrCAD Capture CIS (Menú Inicio -> Cadence -> Capture CIS)
Para dibujar un PCB, use Allegro PCB Designer (Menú Inicio -> Cadence -> PCB Editor)

En general, un archivo `.DSN` es suficiente para todo el proyecto, y al abrirlo se generan automáticamente archivos de esquema como `.opj`. Si utiliza git para el control de versiones, puede agregar lo siguiente a su archivo gitignore:

```gitignore
# Desde el gitignore original

#############
## Allegro
#############

# Ignorar archivo de registro
*.log
*.log,1
*.log,2
*.log,3

*.dml
*.lst

# Ignorar registros de eventos de allegro
*.jrl
*.jrl,1

*.tag

# Archivos de informe
*.rpt

# Archivos de configuración
*.cfg
*.cfg,1

*.lck

# Archivos de informe
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
# Filtrar toda la carpeta
/signoise.run/

#############
## OrCAD
#############
*.dbk
*.opj
*.DRC
*.DSNlck

# Ignorar lista de redes
allegro/
```

## Algunas configuraciones

Configuración de DRC:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134720.png)

Renombrar automáticamente los identificadores al copiar componentes:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134747.png)

Mover caracteres cerca de la cuadrícula:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134758.png)

Truco: Cuando se utiliza la biblioteca CIP, si aparece el mensaje "not found in the configured librarie lists", verifique la codificación de los espacios en blanco en la ruta.

- **Desplazamiento del mouse para hacer zoom**: `Options` - `Preferences…` - `Pan and Zoom` - Configure los dos `Zoom Factor` a 1.1x
- **Actualizar el esquema al seleccionar una parte**: `Options` - `Preferences…` - `Miscellaneous` - `Place Part` – Seleccione `Refresh part on selection`
- **Establecer el tamaño de la cuadrícula**: `Options` - `Preferences…` - `Grid Display` - `Grid Spacing` - Establecer en 1/2

## Atajos de teclado

- Dibujar un cable: `W`
- Cancelar: `ESC`
- Dibujar una línea de bus: `F4`
- Colocar un número de red: `N`
- Rotar / Espejo horizontal / Espejo vertical de componentes: `R` / `H` / `V`
- Abrir el panel CIS: `Z`
- Colocar una fuente de alimentación / tierra: `F` / `G`
- No conectar: `X`
- Filtro: `Ctrl` + `I`
- Selección múltiple de elementos: Mantenga presionada la tecla `Ctrl` mientras selecciona
- Copiar y agregar automáticamente un identificador: Mantenga presionada la tecla `Ctrl` mientras arrastra un componente
- Mover el esquema con el mouse como centro de gravedad: Mantenga presionada la tecla `C` y arrastre el mouse
- Colocar un bus: `E`
- Colocar texto: `T`

## Errores y soluciones

- No se puede mover un componente: En general, reiniciar el programa resuelve el problema.

## Consejos

### Diferencia entre off-page y port

Off-page se utiliza generalmente para esquemas planos, mientras que port se utiliza para esquemas jerárquicos.

### Verificación de DRC

1. En el árbol de archivos, haga clic para seleccionar todo el proyecto.
2. Haga clic en la barra de herramientas `Tools` - `Design Rules Check...`
3. Seleccione `Run Physical Rules` y `View Output`.
4. Haga clic en Aceptar y se generará un informe que se abrirá automáticamente.

## Referencias y agradecimientos

- [【Cadence 快速入门】一文总结版](https://blog.csdn.net/ReCclay/article/details/101225359)
- [OrCAD Capture Tutorial](https://resources.orcad.com/orcad-capture-tutorials)
- [cadence 软件用于高分屏笔记本时候显示字体模糊问题解决](https://blog.csdn.net/qq_34338527/article/details/108846792)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
