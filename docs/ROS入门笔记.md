---
id: ROS入门笔记
title: ROS入门笔记
---

本教程基于 ROS2 Foxy，Ubuntu20.04。

## ROS 环境安装

### 设置 UTF-8 编码

```shell
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### 设置软件源

```shell
sudo apt update && sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

```shell
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
```

### 安装 ROS2

```shell
sudo apt update
sudo apt install ros-foxy-desktop
```

### 设置环境变量

```shell
source /opt/ros/foxy/setup.bash
```

### 安装自动补全工具

```shell
sudo apt install python3-argcomplete
```

### 安装成功后的测试

运行 Talker：

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_cpp talker
```

打开一个新的命令行窗口，运行 Listener：

```shell
source /opt/ros/foxy/setup.bash
ros2 run demo_nodes_py listener
```

### 如果想卸载 ROS

```shell
sudo apt remove ros-foxy-* && sudo apt autoremove
```

随后检查～/.bashrc 　以及／opt / 目录是否有 ros 文件夹存在。

## ROS2 环境配置

```shell
source /opt/ros/foxy/setup.bash
```

设置完成后的检查：

```shell
printenv | grep -i ROS
```

## 小海龟仿真器

### 安装

```shell
sudo apt update
sudo apt install ros-foxy-turtlesim
```

检查是否安装成功：

```shell
ros2 pkg executables turtlesim
```

### 启动海龟模拟器

```shell
ros2 run turtlesim turtlesim_node
```

想要让小海龟动起来，可以打开一个新的命令行窗口，输入命令：

```shell
ros2 run turtlesim turtle_teleop_key
```

按命令行中的提示即可实现操控。

### 安装 rqt 工具

```shell
sudo apt update
sudo apt install ~nros-foxy-rqt*
```

### 启动 rqt 工具

首先，要确保有一只小海龟在后台运行。在命令行输入：

```shell
rqt
```

唤醒 rqt 工具，依次打开 `Plugins > Services > Service Caller`，点击刷新按钮，即可看到所有服务。

选择 `/spawn` 服务，填写小海龟的名字（例如 `'GuaiGuai'`）和位置，就可以多生成一只海龟。如果要修改其轨迹的颜色形状，可以修改 `/set_pen` 服务的内容。

控制新生成海龟的运动，可以通过以下命令（注意海龟的名字）：

```shell
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=guaiguai/cmd_vel
```

## 参考与致谢

- [ROS2 入门教程 ——2. Ubuntu20.04 安装 ROS2 Foxy](https://www.guyuehome.com/10226)
- [ROS2 入门教程 ——3. ROS2 环境配置](https://www.guyuehome.com/10243)
- [ROS2 入门教程 ——4. 小海龟仿真器基础使用](https://www.guyuehome.com/10386)
