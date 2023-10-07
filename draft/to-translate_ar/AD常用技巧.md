# Consejos útiles de AD

—— Organización y recopilación de algunos consejos prácticos.

## Biblioteca de esquemas

### Subrayado de nombres de pines (activo en bajo)

**Método**: Agregar el símbolo "\" después de cada letra que necesite ser subrayada.  
**Ejemplo**: Agregar subrayado a `RESET` - `R\E\S\E\T`

## Biblioteca de encapsulados de PCB

(pendiente de actualización)

## Esquemas

### Desactivar la operación "Add Room"

**Razón**: La operación Room es útil en la distribución de múltiples canales y permite aplicar la distribución de un canal a otros canales. No es necesario usar Room en un solo canal.  
**Método**:

1. Barra de menú - Proyecto - Selección de proyecto - Pestaña Generación de clase
2. Desmarcar "Generar Room"

## PCB

### Agregar logotipos e identificadores

**Razón**: Si se utiliza la importación directa de imágenes, el logotipo creado no se puede ajustar libremente en tamaño.  
**Método**: Utilice el software de fuentes Font Creator, descargue mi fuente en [GitHub](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/%E4%B8%93%E7%94%A8%E5%AD%97%E4%BD%93) como plantilla y personalice su propia fuente exclusiva. Después de crear la fuente, instale el archivo .ttf y podrá llamar al logotipo correspondiente con los caracteres apropiados en Altium.

El logotipo correspondiente a cada carácter se muestra en la siguiente imagen:  
![](https://f004.backblazeb2.com/file/wiki-media/img/20200207200606.png)

### Distribución automática de componentes en un área designada

**Razón**: Al actualizar el esquema al PCB, algunos componentes pueden moverse lejos.  
**Método**: Seleccionar todo - **TOL** - Seleccionar con un cuadro

### Distribución circular

**Método**:

1. Seleccionar el objeto - Copiar
2. **EA** - Marcar Pegar en la capa actual
3. Hacer clic en Pegar matriz - Establecer la cantidad de objetos y el espaciado

### Perforaciones rápidas y cambio de capa

**Método**: Cambiar con el teclado numérico + / -

### Configuración uniforme de la red de perforaciones

**Método**:

1. Hacer clic con el botón derecho en cualquier perforación sin atributos - Buscar objetos similares - Establecer Net como Same
2. Agregar uniformemente los atributos de la red de perforaciones en el panel de propiedades

### Agregar gotas de lágrima

**Razón**: Las gotas de lágrima mejoran la integridad de la señal, reducen la pérdida y la reflexión de la señal, y reducen el riesgo de rotura del punto de contacto entre el cable y la perforación durante el impacto externo.  
**Método**: Usar el atajo **TE**

### Ventana de cableado

**Razón**: El estañado en la ventana de cableado puede aumentar el flujo de corriente.  
**Método**: Copiar la línea requerida y pegarla en la capa de soldadura superior / inferior correspondiente.

### Operaciones en la vista previa en 3D

**Método**:

- Presionar la tecla "3" para ingresar a la vista previa en 3D
- Presionar la tecla "2" para volver a la edición de PCB
- Presionar la tecla "0" para restaurar la vista predeterminada
- Ctrl + F para voltear
- Ctrl + rueda de desplazamiento para hacer zoom
- Shift + clic derecho para cambiar la perspectiva

### Mantener las propiedades de la red al copiar y pegar

**Razón**: Al copiar y pegar objetos con propiedades eléctricas, se pierden las propiedades de la red.  
**Método**: Copiar objeto - **EA** - Marcar Mantener el nombre de la red - Pegar

### Salida del diagrama de posición de soldadura

(pendiente de actualización)

### Cómo hacer una ranura en el PCB

En la **capa mecánica 1** del PCB, dibuje una figura cerrada para la ranura, selecciónela y use el atajo `T` - `V` - `B` para generar la ranura (es mejor cambiar a la vista 3D para confirmar).

## Referencias y agradecimientos

- [Altium Designer19 Design Compendium: Practical Operation Skills and Problem Solving Methods](https://item.jd.com/12756518.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.