# Notas de Introducción a ROS

Este tutorial se basa en ROS2 Foxy y Ubuntu 20.04.

## Instalación del Entorno de ROS

### Configuración de la codificación UTF-8

```shell
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### Configuración de Repositorios

```shell
sudo apt update && sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

```shell
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
```

### Instalación de ROS2

```shell
sudo apt update
sudo apt install ros-foxy-desktop
```

### Configuración de Variables de Entorno

```shell
source /opt/ros/foxy/setup.bash
```

### Instalación de la Herramienta de Autocompletado

```shell
sudo apt install python3-argcomplete
```

### Prueba de Instalación

Para ejecutar el Talker:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_cpp talker
```

Abre una nueva ventana de la terminal y ejecuta el Listener:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_py listener
```

### Desinstalación de ROS (si es necesario)

```shell
sudo apt remove ros-foxy-* && sudo apt autoremove
```

Luego, verifica si hay una carpeta de ROS en ~/.bashrc y en el directorio /opt/.

## Configuración del Entorno de ROS2

```shell
source /opt/ros/foxy/setup.bash
```

Verificación después de la configuración:

```shell
printenv | grep -i ROS
```

## Simulador de Tortuga Pequeña

### Instalación

```shell
sudo apt update
sudo apt install ros-foxy-turtlesim
```

Verifica si la instalación fue exitosa:

```shell
ros2 pkg executables turtlesim
```

### Iniciar el Simulador de Tortuga

```shell
ros2 run turtlesim turtlesim_node
```

Para hacer que la pequeña tortuga se mueva, abre una nueva ventana de la terminal e ingresa el siguiente comando:

```shell
ros2 run turtlesim turtle_teleop_key
```

Sigue las instrucciones en la terminal para controlar la tortuga.

### Instalación de la Herramienta rqt

```shell
sudo apt update
sudo apt install ~nros-foxy-rqt*
```

### Iniciar la Herramienta rqt

Asegúrate de que una tortuga pequeña esté ejecutándose en segundo plano. En la terminal, ingresa:

```shell
rqt
```

Abre la herramienta rqt, ve a `Plugins > Services > Service Caller`, haz clic en el botón de actualización y verás todos los servicios disponibles.

Selecciona el servicio `/spawn`, ingresa el nombre de la tortuga (por ejemplo, `'GuaiGuai'`) y su posición para crear una nueva tortuga. Si deseas modificar el color y la forma de su trayectoria, puedes cambiar el contenido del servicio `/set_pen`.

Controlar el movimiento de la nueva tortuga generada se puede lograr mediante el siguiente comando (ten en cuenta el nombre de la tortuga):

```shell
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=guaiguai/cmd_vel
```

## Referencias y Agradecimientos

- [Tutorial de Inicio de ROS2 - 2. Instalación de ROS2 Foxy en Ubuntu 20.04](https://www.guyuehome.com/10226)
- [Tutorial de Inicio de ROS2 - 3. Configuración del Entorno en ROS2](https://www.guyuehome.com/10243)
- [Tutorial de Inicio de ROS2 - 4. Uso Básico del Simulador de la Pequeña Tortuga](https://www.guyuehome.com/10386)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.