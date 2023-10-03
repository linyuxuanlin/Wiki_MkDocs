# Cómo construir tu propio HomeLab

Homelab se refiere a un entorno de experimentación (tinkering) que se puede construir en casa para realizar experimentos y aprender. Por lo general, se refiere a una serie de dispositivos de hardware (servidores domésticos, mini ordenadores, viejos ordenadores portátiles, Raspberry Pi, etc.) que ejecutan sistemas operativos y software (Linux, máquinas virtuales, Docker, etc.). Homelab tiene muchos usos, como ser un enrutador suave, un host remoto, o desplegar una serie de servicios de auto-alojamiento, como una biblioteca personal, una biblioteca de películas, un gestor de contraseñas, un sitio web personal, un lector de RSS, un servidor de podcasts, una libreta de notas, etc. No sólo es práctico, sino que también puede ser un hobby que añade diversión a la vida.

## Mi configuración de Homelab

Mi configuración de Homelab es un **servidor en la nube ligero** + **mini ordenador** + **NAS**, cada uno con su propia configuración y uso:

|          | Servidor en la nube ligero (Alibaba Cloud 1C2G) | Mini ordenador (CPU N100) | NAS (Synology DS220+) |
| -------- | --------------------------------------------- | ------------------------ | --------------------- |
| IP pública | Sí | No | No |
| Espacio de almacenamiento | Pequeño | Mediano | Grande |
| Rendimiento | Bajo | Alto | Bajo |

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304130031463.png)

No es difícil ver que cada uno tiene sus propias fortalezas, pero juntos forman un equipo triangular. El **servidor en la nube ligero** se centra en el acceso a la red, el **mini ordenador** se centra en el procesamiento de rendimiento, y el **NAS** se centra en el almacenamiento de espacio.

### Servidor en la nube ligero

El **servidor en la nube ligero** es en realidad el excedente de los proveedores de servidores en la nube, con una configuración no muy alta, pero con un precio asequible, como el Alibaba Cloud que compré por sólo 96 yuanes al año (si tienes un paquete más barato, házmelo saber).

Debido a que tiene una IP pública (los puertos 80/443 también están abiertos), los servicios que despliego en este servidor en la nube ligero son principalmente un servidor frp, un servidor proxy inverso, un salto para acceder a otras máquinas, un panel de monitorización de otros hosts, un servicio de sitio web de pequeña escala, un monitor de tiempo de actividad del sitio web, etc., que necesitan ser accesibles directamente desde la red pública.

### Mini ordenador

Para el **mini ordenador**, elegí el sistema N100 CPU de Zero-Knowledge, con 16 GB de memoria DDR5 y un disco duro SSD de 250 GB, que en general cuesta alrededor de 1.000 yuanes. El consumo diario de energía no es alto, y puede ser llamado cuando se necesita rendimiento.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304130043744.png)

Los tipos de aplicaciones que despliego en el mini ordenador son principalmente servicios que consumen rendimiento, como el editor de código web VS Code, la biblioteca privada de notas, el lector de RSS, el servidor de podcasts, la biblioteca de películas, el navegador interno de la red local, etc.

### NAS

Para el **NAS**, elegí el Synology DS220+, que tiene una arquitectura X86 que facilita la ejecución del entorno Docker. Hace un tiempo, también le añadí una memoria RAM de 16 GB para intentar mejorar su rendimiento. Pero luego descubrí que el cuello de botella seguía siendo la débil CPU J4025. El Synology blanco es como comprar software y obtener hardware gratis, pero por la seguridad de los datos, todavía vale la pena.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304130053483.png)

Los servicios que despliego en el NAS son principalmente para necesidades de almacenamiento, como la copia de seguridad de datos de dispositivos, la sincronización de la nube, la biblioteca de fotos, la biblioteca de libros, etc.

## Cómo desplegar Docker Compose en un solo paso

Con el espíritu de experimentación, es inevitable que se tenga que reinstalar el sistema cada dos o tres días. Después de desplegar tantas aplicaciones, no es posible que se inicien una por una. Aquí hay un sencillo script de shell que puede desplegar todas las composiciones de Docker en un solo paso:

```shell title="compose.sh"
echo "iniciando compose.sh..."

# Recorre todas las carpetas de primer nivel en el directorio actual
for folder in */; do
  [ "$folder" != "Archive/" ] # Ignora la carpeta Archive
  cd "$folder"  # Entra en la carpeta
  docker-compose up -d # Ejecuta el comando docker compose up -d
  cd .. # Regresa al directorio anterior
done

echo "listo."
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

Simplemente ejecutando `sh compose.sh` en el directorio compose, se pueden iniciar todos los Docker compose con un solo comando.

## Ventajas del autohospedaje

En comparación con el alojamiento de terceros, donde alguien más se encarga de tus datos, el **autohospedaje (Self-Hosted)** tiene muchas ventajas, como el control total sobre tus datos personales, la capacidad de personalizar según tus necesidades y la posibilidad de acceder a más fuentes de información de calidad (biblioteca personal, biblioteca de películas y series, servicios RSS). La única condición es tener tiempo, recursos y la disposición para experimentar.

En los próximos artículos, presentaré algunas configuraciones básicas y servicios interesantes. La combinación de "triángulo de hierro" mencionada anteriormente es solo una configuración personalizada, pero si solo tienes una máquina, también puedes experimentar con ella. La mayoría de los servicios que presentaré se basan en Docker y Docker-compose, ya que son altamente compatibles y se pueden utilizar en diferentes configuraciones de máquinas. Sin embargo, es importante mencionar que es mejor elegir una máquina con arquitectura X86, ya que algunos contenedores no están adaptados para ARM y deben compilarse e instalarse manualmente.

## Referencias y agradecimientos

- [¿Qué servicios interesantes tienes en tu NAS?](https://www.v2ex.com/t/901954)
- [Iniciar varios contenedores de docker-compose con un solo comando](https://juejin.cn/post/7082842557482270734)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.