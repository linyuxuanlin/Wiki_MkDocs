# Acelerando el servicio de Pages con Vercel

Hace un tiempo, mi blog (alojado en GitHub Pages) fue bloqueado. Como la mayoría de mi audiencia es de China, esto fue un gran problema. Por lo general, la solución es comprar un servidor o migrar a OSS. Pero ambos métodos son complicados y costosos. Afortunadamente, encontré esta herramienta llamada Vercel. Ahora puedo escribir mi blog felizmente de nuevo.

## Ventajas de Vercel

- Dominio personalizado gratuito con soporte HTTPS
- Servicio Serverless
- Nodos de Google Cloud y AWS, con nodos en Hong Kong y Taiwán, lo que permite una velocidad de acceso decente desde China
- 20 GB de cuota gratuita, suficiente para la mayoría de los sitios web
- Sin límite en la cantidad de sitios y API Serverless
- Serverless compatible con Node.js, Go, Python y Ruby
- Compatible con la CLI now.sh, GitHub, GitLab y Bitbucket para importar y desplegar

## Cómo usarlo

La configuración es sencilla, así que solo proporcionaré una breve explicación en texto.

1. Inicia sesión con tu cuenta de GitHub
2. Importa tu sitio web (importa directamente desde el repositorio de GitHub)
3. Configura las instrucciones de despliegue (para la plataforma VuePress, se puede dejar en blanco)
4. Configura la ruta de salida (para VuePress, es `docs/.vuepress/dist`)
5. Asegúrate de establecer la rama de producción como `gh-pages` en la configuración
6. Asocia tu dominio

## Notas

Asegúrate de escribir un mensaje de commit de más de 1 carácter, de lo contrario, no se desplegará.

## Referencias y agradecimientos

- [Vercel](https://vercel.com/)
- [ZEIT (Vercel) now.sh Free Deployment of Blog Websites, Supporting Serverless Python Go Node.js](https://wivwiv.com/post/zeit-use-guide/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.