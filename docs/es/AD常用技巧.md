# Consejos útiles de AD

—— Aquí se han recopilado algunos consejos prácticos.

## Sección de la biblioteca de esquemas

### Subrayado de nombres de pines (activo en bajo)

**Método**: Agregar el símbolo "\" detrás de cada letra que se deba subrayar.  
**Ejemplo**: Subrayar `RESET` - `R\E\S\E\T`

## Sección de la biblioteca de encapsulados de PCB

(Pendiente de actualización)

## Sección del esquema

### Desactivar la función "Add Room"

**Razón**: La función de Room es útil en el enrutamiento de múltiples canales, ya que permite aplicar directamente el enrutamiento de un canal a otros canales. No es necesario utilizar Room en un solo canal.  
**Método**:

1. Barra de menú - Proyecto - Selección de Proyecto - Pestaña Generación de Clases
2. Desmarcar "Generar Room"

## Sección de PCB

### Agregar logotipos y marcas

**Razón**: Si se importa una imagen directamente, el logotipo creado no se puede ajustar libremente en cuanto a tamaño.  
**Método**: Utilizar el software de creación de fuentes Font Creator, descargue mi fuente personalizada como plantilla en [GitHub](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/%E4%B8%93%E7%94%A8%E5%AD%97%E4%BD%93) y, una vez creada la fuente, instalar el archivo .ttf para usar el logotipo correspondiente en Altium.

La relación de caracteres y logotipos es la siguiente:  
![](https://img.wiki-power.com/d/wiki-media/img/20200207200606.png)

### Colocación automática de componentes en una zona designada

**Razón**: Al actualizar el esquema al PCB, algunos componentes pueden alejarse mucho.  
**Método**: Seleccionar todo - **TOL** - Selección de caja

### Disposición en matriz circular

**Método**:

1. Seleccionar objeto - Copiar
2. **EA** - Marcar "Pegar en la capa actual"
3. Hacer clic en "Pegar matriz" - Configurar cantidad de objetos y espaciado

### Atajos para hacer pasajes y cambiar de capa

**Método**: Utilizar las teclas + / - del teclado numérico al enrutamiento

### Establecer propiedades de red de pasajes de forma uniforme

**Método**:

1. Hacer clic con el botón derecho en cualquier pasaje sin propiedades - Encontrar objetos similares - Establecer la Red como "Igual"
2. En el panel de propiedades, establecer las propiedades de red de pasajes de forma uniforme

### Agregar vias de lágrima

**Razón**: Las vias de lágrima aumentan la integridad de la señal, reducen la pérdida de señal y las reflexiones, y disminuyen el riesgo de rotura del punto de contacto de la pista y la via de paso ante impactos externos.  
**Método**: Utilizar el atajo **TE**

### Ventanas de estañado de pistas

**Razón**: Estañar las pistas puede aumentar la capacidad de corriente.  
**Método**: Copiar el trazado necesario y pegarlo de manera especial en la capa Top / Bottom Solder correspondiente

### Operaciones en la vista 3D

**Método**:

- Presionar la tecla numérica "3" para entrar en la vista 3D
- Presionar la tecla numérica "2" para volver a la edición del PCB
- Presionar la tecla numérica "0" para restaurar la vista predeterminada
- Ctrl + F para voltear
- Ctrl + rueda del ratón para hacer zoom
- Shift + clic derecho para cambiar la vista

### Mantener las propiedades de red al copiar y pegar

**Razón**: Al copiar y pegar objetos con propiedades eléctricas, se pierden las propiedades de red.  
**Método**: Copiar el objeto - **EA** - Marcar "Mantener nombre de red" - Pegar

### Generación de diagramas de pines

(Pendiente de actualización)

### Cómo crear ranuras en el PCB

Dibuje una forma cerrada en la **capa Mecánica 1** del PCB, selecciónela y utilice el atajo `T` - `V` - `B` para crear la ranura (se recomienda cambiar a la vista 3D para confirmar).

## Referencias y agradecimientos

- [Altium Designer19 Design Handbook: Practical Techniques and Problem Solving Methods](https://item.jd.com/12756518.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.