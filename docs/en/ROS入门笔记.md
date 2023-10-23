# ROS Getting Started Notes

This tutorial is based on ROS2 Foxy and Ubuntu 20.04.

## Installing the ROS Environment

### Setting UTF-8 Encoding

```shell
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### Setting Software Sources

```shell
sudo apt update && sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

```shell
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
```

### Installing ROS2

```shell
sudo apt update
sudo apt install ros-foxy-desktop
```

### Setting Environment Variables

```shell
source /opt/ros/foxy/setup.bash
```

### Installing Auto-Completion Tool

```shell
sudo apt install python3-argcomplete
```

### Testing After Successful Installation

Run the Talker:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_cpp talker
```

Open a new terminal window and run the Listener:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_py listener
```

### Uninstalling ROS (If Needed)

```shell
sudo apt remove ros-foxy-* && sudo apt autoremove
```

Afterward, check `~/.bashrc` and the `/opt/` directory for the presence of ROS folders.

## Configuring ROS2 Environment

```shell
source /opt/ros/foxy/setup.bash
```

Check the configuration after setting:

```shell
printenv | grep -i ROS
```

## Turtle Simulator

### Installation

```shell
sudo apt update
sudo apt install ros-foxy-turtlesim
```

Check if the installation was successful:

```shell
ros2 pkg executables turtlesim
```

### Launching the Turtle Simulator

```shell
ros2 run turtlesim turtlesim_node
```

To make the turtle move, open a new terminal window and enter the following command:

```shell
ros2 run turtlesim turtle_teleop_key
```

Follow the prompts in the terminal to control the turtle.

### Installing rqt Tools

```shell
sudo apt update
sudo apt install ~nros-foxy-rqt*
```

### Launching rqt Tools

First, ensure that a turtle is running in the background. In the terminal, enter:

```shell
rqt
```

Launch the rqt tool and, in sequence, open `Plugins > Services > Service Caller`. Click the refresh button to see all services.

Select the `/spawn` service, enter the turtle's name (e.g., `'GuaiGuai'`) and position to create another turtle. If you want to modify its trajectory's color and shape, you can adjust the content of the `/set_pen` service.

To control the movement of the newly generated turtle, you can use the following command (please note the turtle's name):

```shell
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=guaiguai/cmd_vel
```

## References and Acknowledgments

- [ROS2 Beginner's Tutorial - 2. Installing ROS2 Foxy on Ubuntu 20.04](https://www.guyuehome.com/10226)
- [ROS2 Beginner's Tutorial - 3. Setting Up the ROS2 Environment](https://www.guyuehome.com/10243)
- [ROS2 Beginner's Tutorial - 4. Basic Usage of the Turtle Simulator](https://www.guyuehome.com/10386)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.