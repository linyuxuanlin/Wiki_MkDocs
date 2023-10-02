# ROS Beginner's Notes

This tutorial is based on ROS2 Foxy and Ubuntu 20.04.

## ROS Environment Installation

### Set UTF-8 Encoding

```shell
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### Set Software Sources

```shell
sudo apt update && sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

```shell
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
```

### Install ROS2

```shell
sudo apt update
sudo apt install ros-foxy-desktop
```

### Set Environment Variables

```shell
source /opt/ros/foxy/setup.bash
```

### Install Autocomplete Tool

```shell
sudo apt install python3-argcomplete
```

### Test After Successful Installation

Run Talker:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_cpp talker
```

Open a new command line window and run Listener:

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_py listener
```

### If You Want to Uninstall ROS

```shell
sudo apt remove ros-foxy-* && sudo apt autoremove
```

Then check if there is a ROS folder in ~/.bashrc and /opt/ directory.

## ROS2 Environment Configuration

```shell
source /opt/ros/foxy/setup.bash
```

Check after setting up:

```shell
printenv | grep -i ROS
```

## Turtle Simulator

### Installation

```shell
sudo apt update
sudo apt install ros-foxy-turtlesim
```

Check if installed successfully:

```shell
ros2 pkg executables turtlesim
```

### Launch Turtle Simulator

```shell
ros2 run turtlesim turtlesim_node
```

To make the turtle move, open a new command window and enter the command:

```shell
ros2 run turtlesim turtle_teleop_key
```

Follow the prompts in the command line to control the turtle.

### Installation of rqt Tool

```shell
sudo apt update
sudo apt install ~nros-foxy-rqt*
```

### Launch rqt Tool

First, make sure a turtle is running in the background. Enter the command in the command line:

```shell
rqt
```

Launch the rqt tool, open `Plugins > Services > Service Caller` in order, click the refresh button, and you can see all services.

Select the `/spawn` service, fill in the name (e.g. `'GuaiGuai'`) and position of the new turtle, and you can generate a new turtle. If you want to modify the color and shape of its trajectory, you can modify the content of the `/set_pen` service.

To control the movement of the newly generated turtle, use the following command (note the name of the turtle):

```shell
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=guaiguai/cmd_vel
```

## References and Acknowledgments

- [ROS2 Beginner's Tutorial ——2. Installing ROS2 Foxy on Ubuntu20.04](https://www.guyuehome.com/10226)
- [ROS2 Beginner's Tutorial ——3. ROS2 Environment Configuration](https://www.guyuehome.com/10243)
- [ROS2 Beginner's Tutorial ——4. Basic Usage of Turtlebot Simulator](https://www.guyuehome.com/10386)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.