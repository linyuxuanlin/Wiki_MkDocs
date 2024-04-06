# Consejos útiles para AD

En esta sección, hemos recopilado algunos consejos prácticos para trabajar con Altium Designer.

## Sección de biblioteca de esquemas

### Subrayado de nombres de pines (activo a nivel bajo)

**Método**: Agregar un símbolo "\" después de cada letra que necesite subrayar.  
**Ejemplo**: `RESET` subrayado - `R\E\S\E\T`

## Sección de biblioteca de encapsulados de PCB

(Próximamente)

## Sección de esquema

### Desactivar la función "Add Room"

**Razón**: La función "Room" es útil en el enrutamiento de múltiples canales, ya que permite aplicar el enrutamiento de un canal directamente a otros canales. No es necesario usar "Room" en un solo canal.  
**Método**:

1. Menú - Proyecto - Selección de Proyecto - Pestaña Generación de Clases
2. Desmarcar la casilla "Generar Room"

## Sección de PCB

### Agregar logotipos e identificaciones

**Razón**: Si importas imágenes directamente, el logotipo creado no se puede redimensionar fácilmente.  
**Método**: Utiliza el software de creación de fuentes "Font Creator". Puedes descargar mi fuente desde [GitHub](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/%E4%B8%93%E7%94%A8%E5%AD%97%E4%BD%93) como plantilla y personalizar tu propia fuente exclusiva. Después de crear la fuente, instala el archivo .ttf y podrás utilizar los caracteres correspondientes en Altium para crear tu logotipo.

La correspondencia de caracteres con el logotipo es la siguiente:  
![Logo](https://media.wiki-power.com/img/20200207200606.png)

### Distribución automática de componentes en un área designada

**Razón**: Cuando actualizas el esquema al PCB, algunos componentes pueden estar dispersos.  
**Método**: Selecciona todo - **TOL** - Seleccionar un área con un marco.

### Disposición en matriz circular

**Método**:

1. Selecciona el objeto - Copiar
2. **EA** - Marca "Pegar en la capa actual"
3. Haz clic en "Pegar matriz" - Configura el número de objetos y el espaciado

### Cambiar de capa y crear perforaciones rápidamente

**Método**: Usa el teclado numérico + / - mientras enrutamos.

### Configuración unificada de propiedades de red de perforación

**Método**:

1. Haz clic derecho en cualquier perforación sin atributos: Buscar objetos similares - Configurar "Red" como "Igual"
2. Agrega las propiedades de la red de perforación en el panel de propiedades.

### Agregar vias de lágrima

**Razón**: Las vias de lágrima mejoran la integridad de la señal, reducen la pérdida de señal y el riesgo de desconexión de los puntos de contacto de las vías cuando se produce un impacto externo.  
**Método**: Usa el atajo de teclado **TE**

### Abrir soldadura en las pistas

**Razón**: Agregar estaño a las pistas puede mejorar la capacidad de corriente.  
**Método**: Copia las pistas necesarias y pégalas en las capas superiores e inferiores de soldadura correspondientes.

### Operaciones en la vista 3D

**Método**:

- Presiona la tecla "3" para ingresar a la vista 3D.
- Presiona la tecla "2" para volver a la edición de PCB.
- Presiona la tecla "0" para restablecer la vista predeterminada.
- Ctrl + F para voltear la vista.
- Ctrl + rueda del ratón para hacer zoom.
- Shift + clic derecho para cambiar la perspectiva.

### Mantener las propiedades de la red al copiar y pegar

**Razón**: Al copiar y pegar objetos con propiedades eléctricas, se pueden perder las propiedades de la red.  
**Método**: Copia el objeto - **EA** - Marca "Mantener nombre de la red" - Pega

### Generar diagrama de pines soldados

(Próximamente)

### Cómo crear ranuras en el PCB

En la capa **Mecánica 1** del PCB, dibuja una forma cerrada de la ranura, selecciónala y usa el atajo de teclado `T` - `V` - `B` para generar la ranura (es recomendable cambiar a la vista 3D para confirmar).

## Referencias y Agradecimientos

- [Altium Designer 19 Guía Práctica: Técnicas de Operación y Solución de Problemas](https://item.jd.com/12756518.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
