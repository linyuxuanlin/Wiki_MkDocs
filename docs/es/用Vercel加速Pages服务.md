# Acelera tu servicio de Pages con Vercel

Hace un tiempo, mi blog (alojado en GitHub Pages) fue bloqueado en China. Esto fue un gran problema ya que la mayoría de mi audiencia se encuentra en ese país. 
Por lo general, la solución sería comprar un servidor o migrar a un servicio de almacenamiento en la nube. Sin embargo, estos métodos son complicados y costosos.
Afortunadamente, descubrí esta increíble herramienta llamada Vercel. Ahora puedo seguir escribiendo mi blog sin preocupaciones.

## Ventajas de Vercel

- Personalización gratuita de dominios con soporte para HTTPS.
- Servicio Serverless.
- Nodos de Google Cloud y AWS disponibles, incluyendo nodos en Hong Kong y Taiwán, lo que garantiza una buena velocidad de acceso desde China.
- Límite gratuito de 20 GB, más que suficiente.
- Sin límite en la cantidad de sitios y APIs Serverless.
- Serverless es compatible con Node.js, Go, Python y Ruby.
- Soporte para importar/desplegar desde now.sh CLI, GitHub, GitLab y Bitbucket.

## Cómo utilizarlo

La configuración de Vercel es bastante sencilla, por lo que solo necesitarás seguir estos pasos:

1. Inicia sesión directamente con tu cuenta de GitHub.
2. Importa tu sitio (directamente desde tu repositorio de GitHub).
3. Configura las instrucciones de despliegue (para la plataforma VuePress puedes dejarlo en blanco).
4. Configura la ruta de salida (para VuePress sería `docs/.vuepress/dist`).
5. Asegúrate de establecer la rama de producción como `gh-pages` en la configuración.
6. Asocia tu dominio.

## Consideraciones

Recuerda que cada mensaje de commit debe tener más de 1 caracter, de lo contrario no se realizará el despliegue.

## Referencias y agradecimientos

- [Vercel](https://vercel.com/)
- [ZEIT (Vercel) now.sh Free Deployment for Blog Websites, Supports Serverless Python Go Node.js](https://wivwiv.com/post/zeit-use-guide/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.