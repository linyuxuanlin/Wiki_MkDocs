# Cómo dibujar gráficos de relaciones con Graphviz

Una forma de dibujar gráficos de relaciones mediante código.

## Contexto

[Graphviz](http://www.graphviz.org/) es una herramienta útil para dibujar gráficos de relaciones. A diferencia de Visio, Graphviz genera gráficos con **distribución automática**, lo que significa que no es necesario ajustar manualmente la posición de los elementos. Cuando una red de relaciones es compleja, la distribución automática puede minimizar **la intersección de líneas**.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/Graphviz.png)

## Instalación

Se ha descubierto un editor en línea muy útil: \[GraphvizOnline\]\([http://dreampuf.github.io/GraphvizOnline/\#digraph graph_name { ](http://dreampuf.github.io/GraphvizOnline/#digraph%20graph_name%20{%20) %20%20A-&gt;B\[label%3D"关系"\]%20 }\) que admite la representación en tiempo real y la exportación en formatos como `.png` y `.svg`.

Para macOS, la instalación es: `brew install graphviz`

## Proceso de dibujo

1. Crear `xxx.dot`
2. Editar el documento `.dot`
3. Cambiar al directorio correspondiente y exportar: `dot xxx.dot -T png -o xxx.png`

## Sintaxis sencilla

```
graph graph_name {
  A--B[label="relación de conexión"]
}
```

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20190201140244.png)

## Conclusión

La distribución automática es la esencia de Graphviz. Al igual que cuando usamos la sintaxis de Markdown para generar presentaciones, estas herramientas estandarizan el contenido, lo que permite que las personas se centren en el **contenido en lugar de la forma y la distribución**.

## Referencias y agradecimientos

- [Tutorial sencillo de Graphviz](https://blog.zengrong.net/post/2294.html)
- [Dibujar gráficos con dot](http://www.graphviz.org/pdf/dotguide.pdf)
- [Instalación y tutorial básico de Graphviz en Windows](https://blog.csdn.net/lanchunhui/article/details/49472949)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.