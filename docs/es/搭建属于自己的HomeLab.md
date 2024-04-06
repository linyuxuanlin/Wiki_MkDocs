# Construye tu propio HomeLab

Homelab se refiere a un entorno de experimentación (y trasteo) que se puede construir en casa para realizar experimentos y aprender. Por lo general, se refiere a una serie de dispositivos de hardware (servidores domésticos, mini PC, computadoras antiguas, teléfonos móviles, Raspberry Pi, etc.) que ejecutan sistemas operativos y software (Linux, máquinas virtuales, Docker, etc.). Homelab tiene muchos usos, como ser un enrutador de software, un host remoto, o desplegar una serie de servicios autohospedados, como una biblioteca personal, una biblioteca de películas y series, un gestor de contraseñas, un sitio web personal, un lector de RSS, un servidor de podcasts, una libreta de notas, etc. No solo es práctico, sino que también puede ser un pasatiempo que añade diversión a la vida.

## Configuración de mi HomeLab

Mi propia configuración de HomeLab consta de un **servidor en la nube ligero** + **mini PC** + **NAS**, cada uno con su propia configuración y uso:

|                | Servidor en la nube ligero (Alibaba Cloud 1C2G) | Mini PC (CPU N100) | NAS (Synology DS220+) |
| -------------- | ----------------------------------------------- | ------------------ | --------------------- |
| IP pública     | Sí                                              | No                 | No                    |
| Almacenamiento | Pequeño                                         | Mediano            | Grande                |
| Rendimiento    | Bajo                                            | Alto               | Bajo                  |

![](https://media.wiki-power.com/img/202304130031463.png)

No es difícil ver que cada uno de ellos tiene sus propias fortalezas, pero cuando trabajan juntos, se convierten en un equipo imbatible. El **servidor en la nube ligero** se inclina hacia el acceso a la red, el **mini PC** se inclina hacia el rendimiento de procesamiento, y el **NAS** se inclina hacia el almacenamiento de espacio.

### Servidor en la nube ligero

El **servidor en la nube ligero** es en realidad el exceso de capacidad de los proveedores de servidores en la nube. Tiene una configuración modesta, pero es asequible en términos de precio. Por ejemplo, el servidor en la nube ligero de Alibaba Cloud que compré solo cuesta 96 CNY al año (si conoces un paquete más barato, házmelo saber).

Debido a que tiene una IP pública (los puertos 80/443 también están abiertos), los servicios que despliego en este servidor en la nube ligero son principalmente un servidor frp, un servidor proxy inverso, un salto para acceder a otras máquinas, un panel de monitoreo de otros hosts, un servicio de sitio web pequeño, y monitoreo de tiempo de actividad del sitio web, entre otros servicios que necesitan ser accesibles directamente desde Internet.

### Mini PC

Para el **mini PC**, elegí un sistema preconfigurado con CPU N100, al que le añadí una memoria RAM DDR5 de 16 GB y un disco duro SSD de 250 GB. En general, me costó alrededor de 1000 CNY. Tiene un consumo de energía diario bajo y puede proporcionar un rendimiento sólido cuando se necesita.

![](https://media.wiki-power.com/img/202304130043744.png)

Las aplicaciones que despliego en el mini PC son principalmente servicios que requieren un consumo de rendimiento, como el editor de código web VS Code, una biblioteca privada de notas, un lector de RSS, un servidor de podcasts, una biblioteca de películas y series, y un navegador de red interna, entre otros.

### NAS

Para el **NAS**, elegí el Synology DS220+, que tiene una arquitectura x86 que facilita la ejecución de entornos Docker. Hace un tiempo, le añadí una memoria RAM de 16 GB para intentar mejorar su rendimiento. Sin embargo, descubrí que el cuello de botella seguía siendo la débil CPU J4025. Aunque Synology es como comprar software y recibir hardware de regalo, vale la pena por la seguridad de los datos.

![](https://media.wiki-power.com/img/202304130053483.png)

En el NAS, despliego principalmente servicios de almacenamiento, como copias de seguridad de dispositivos, sincronización de archivos en la nube, una biblioteca de fotos y una biblioteca de libros, entre otros.

## Cómo desplegar Docker Compose de forma masiva con un solo comando

Con el espíritu de experimentar sin cesar, es inevitable reinstalar el sistema cada dos por tres. Desplegar tantas aplicaciones no significa que tengas que iniciarlas una por una. Aquí tienes un sencillo script de shell que te permite desplegar todas las configuraciones de Docker Compose con un solo comando:

```shell title="compose.sh"
echo "Iniciando compose.sh..."
```

```markdown
# Recorrer las carpetas de primer nivel en el directorio actual

for folder in \*/; do
[ "$folder" != "Archive/" ] # Ignorar la carpeta "Archive"
cd "$folder" # Entrar en la carpeta
docker-compose up -d # Ejecutar el comando "docker compose up -d"
cd .. # Volver al directorio anterior
done

echo "¡Hecho!"
```

Mi estructura de directorios es la siguiente:

```
├── compose
│   ├── code-server
|   |   ├──compose.yaml
|   |   ├──.env
│   ├── frp
|   |   ├──compose.yaml
│   ├── xxx
|   |   ├──compose.yaml
│   ├── ……
│   └── compose.sh
```

Simplemente ejecuta `sh compose.sh` en el directorio "compose" y se iniciarán todos los Docker Compose de forma automática.

## Ventajas de la auto-alojamiento

En comparación con el alojamiento de terceros, donde otros se encargan de tus datos, el **auto-alojamiento (Self-Hosted)** tiene muchas ventajas. Tienes el control total sobre tus datos personales y puedes personalizarlos según tus preferencias. Además, te permite acceder a fuentes de información de alta calidad, como bibliotecas personales, bibliotecas de películas y series, y servicios de RSS. Sin embargo, requiere tiempo, esfuerzo y recursos económicos, así como una mentalidad dispuesta a experimentar.

En los próximos artículos, presentaré algunas configuraciones básicas y servicios interesantes. La combinación de "Iron Triangle" mencionada anteriormente es simplemente una configuración personalizada. Si solo tienes una máquina, también puedes experimentar sin problemas. La mayoría de los contenidos que presentaré se basan en la implementación de Docker y Docker Compose, ya que esta forma de implementación es altamente compatible y se puede utilizar en diferentes configuraciones de máquinas sin problemas. Sin embargo, es importante mencionar que es preferible elegir una máquina con arquitectura X86, ya que algunos contenedores no están adaptados para ARM y deben ser compilados e instalados manualmente.

## Referencias y agradecimientos

- [¿Qué servicios interesantes has implementado en tu NAS?](https://www.v2ex.com/t/901954)
- [Iniciar múltiples contenedores de docker-compose con un solo comando](https://juejin.cn/post/7082842557482270734)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
```
