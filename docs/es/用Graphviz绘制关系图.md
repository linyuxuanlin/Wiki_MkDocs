# Cómo dibujar un gráfico de relaciones con Graphviz

Una forma de dibujar gráficos de relaciones utilizando código.

## Antecedentes

[Graphviz](http://www.graphviz.org/) es una herramienta muy útil para dibujar gráficos de relaciones. A diferencia de Visio, Graphviz genera los gráficos de forma **automática**, sin necesidad de ajustar manualmente la posición de los elementos. Esto es especialmente útil cuando se trabaja con redes de relaciones complejas, ya que permite **minimizar la cantidad de cruces de líneas**.

![](https://media.wiki-power.com/img/Graphviz.png)

## Instalación

He descubierto un editor en línea muy útil llamado \[GraphvizOnline\]\([http://dreampuf.github.io/GraphvizOnline/\#digraph graph_name { ](http://dreampuf.github.io/GraphvizOnline/#digraph%20graph_name%20{%20) %20%20A-&gt;B\[label%3D"关系"\]%20 }\) que permite renderizar los gráficos de forma instantánea y exportarlos en formatos como `.png` y `.svg`.

Para instalar en macOS, ejecuta el siguiente comando: `brew install graphviz`

## Proceso de creación del gráfico

1. Crea un archivo `xxx.dot`
2. Edita el documento `.dot`
3. Cambia al directorio donde se encuentra el archivo y exporta el gráfico: `dot xxx.dot -T png -o xxx.png`

## Sintaxis básica

```
graph graph_name {
  A--B[label="relación"]
}
```

![](https://media.wiki-power.com/img/20190201140244.png)

## Conclusión

La esencia de Graphviz radica en su capacidad de generar diseños automáticos. Al igual que cuando utilizo la sintaxis de Markdown para crear presentaciones, estas herramientas estandarizan el contenido y permiten que nos centremos en el **contenido en sí, en lugar de en la forma y el diseño**.

## Referencias y agradecimientos

- [Tutorial básico de Graphviz](https://blog.zengrong.net/post/2294.html)
- [Dibujo de gráficos con dot](http://www.graphviz.org/pdf/dotguide.pdf)
- [Instalación y tutorial básico de Graphviz en Windows](https://blog.csdn.net/lanchunhui/article/details/49472949)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
