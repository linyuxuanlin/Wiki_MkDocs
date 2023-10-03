# Notas de introducción a ROS

Este tutorial se basa en ROS2 Foxy y Ubuntu20.04.

## Instalación del entorno ROS

### Configuración de la codificación UTF-8

```shell
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### Configuración de la fuente de software

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

### Configuración de variables de entorno

```shell
source /opt/ros/foxy/setup.bash
```

### Instalación de herramientas de autocompletado

```shell
sudo apt install python3-argcomplete
```

### Prueba después de la instalación exitosa

Ejecutar Talker:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_cpp talker
```

Abrir una nueva ventana de línea de comandos y ejecutar Listener:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_py listener
```

### Si desea desinstalar ROS

```shell
sudo apt remove ros-foxy-* && sudo apt autoremove
```

Luego, verifique si hay una carpeta de ROS en ~ / .bashrc o / opt / directorio.

## Configuración del entorno ROS2

```shell
source /opt/ros/foxy/setup.bash
```

Comprobación después de la configuración:

```shell
printenv | grep -i ROS
```

## Simulador de tortuga pequeña

### Instalación

```shell
sudo apt update
sudo apt install ros-foxy-turtlesim
```

Comprobar si la instalación fue exitosa:

```shell
ros2 pkg executables turtlesim
```

### Iniciar el simulador de tortuga

```shell
ros2 run turtlesim turtlesim_node
```

Para hacer que la tortuga pequeña se mueva, abra una nueva ventana de línea de comandos e ingrese el siguiente comando:

```shell
ros2 run turtlesim turtle_teleop_key
```

Siga las instrucciones en la línea de comandos para controlar la tortuga.

### Instalación de la herramienta rqt

```shell
sudo apt update
sudo apt install ~nros-foxy-rqt*
```

### Iniciar la herramienta rqt

Primero, asegúrese de que una tortuga pequeña esté ejecutándose en segundo plano. En la línea de comandos, ingrese:

```shell
rqt
```

Despierte la herramienta rqt, abra `Plugins > Services > Service Caller` en orden, haga clic en el botón de actualización y podrá ver todos los servicios.

Seleccione el servicio `/spawn`, ingrese el nombre (por ejemplo, `'GuaiGuai'`) y la ubicación de la tortuga pequeña para generar otra tortuga. Si desea modificar la forma y el color de su trayectoria, puede modificar el contenido del servicio `/set_pen`.

Para controlar el movimiento de una nueva tortuga generada, se puede utilizar el siguiente comando (prestar atención al nombre de la tortuga):

```shell
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=guaiguai/cmd_vel
```

## Referencias y agradecimientos

- [Tutorial de introducción a ROS2 - 2. Instalación de ROS2 Foxy en Ubuntu 20.04](https://www.guyuehome.com/10226)
- [Tutorial de introducción a ROS2 - 3. Configuración del entorno de ROS2](https://www.guyuehome.com/10243)
- [Tutorial de introducción a ROS2 - 4. Uso básico del simulador de la tortuga](https://www.guyuehome.com/10386)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.