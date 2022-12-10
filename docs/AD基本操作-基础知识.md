---
id: AD基本操作-基础知识
title: AD 基本操作 - 基础知识
---

—— Altium Designer 系列教程

## 背景

配置完软件运行环境，在开始画板子之前，我们务必先熟悉一些 Altium Designer 及电路设计的基本知识。

## 库文件安装

库相当于把每个分立元件（如电阻、电容等）的原理图 / PCB 封装起来，方便直接调用。不一定每个元器件的原理图库 / 封装库都必须自己画，但 **整理自己的库是必须的**。假想你的项目内每个元器件用的都是别人的（且不同的库有自己的规则），那么越往后你将越受制于人。拥有自己的库，这不仅方便迁移、提高效率，也有利于知识的体系化。适合自己的规则与体系，从时间轴上看，知识将呈指数型增长。刚开始曲线增长虽然缓慢，但到了后期，将不会有重复性的工作，那时候你需要做的，只是学习新知识，并将其归纳到体系中了。

温馨提示：自己的项目所需的所有元器件，尽量全部从自己整理的原理图库 / 封装库中提取。

### 可参考的库

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium)：我自己整理的库。封装库齐全，原理图库仅包含我的项目所需要的元器件型号。不断更新中。
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary)：一个较为齐全的库。
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github)：挺齐全的一个库，还包含一些单片机方案板。
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB)：嘉立创提供的标准集成库，包含嘉立创可以 SMT 贴片的所有元件，直接用这个集成库，打板 / SMT 的时候兼容性会比较好。
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library)：彬哥整理的原理图库 / 封装库，涵盖队内硬件所需的大部分元器件。

如何安装库文件：参考 [**Altium Designer 安装库文件**](https://wiki-power.com/AltiumDesigner安装库文件)

### 不常见的元器件

以上提供的库，已经涵盖市面上 95% 以上的元器件型号了。如果真的找不到所需元器件，可以尝试以下方法：

AD 插件：

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/)：这个用起来真的超级方便

搜索引擎：[**原理图与封装下载 · Power's NAV**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## 快捷键

于 Altium Designer 而言，熟练掌握常用的快捷键，可以很大程度提高效率。Altium Designer 的系统快捷键都是根据菜单下命令中有下划线的字母组合而成，例如 **Place-Line** 的快捷键为 **P-L** （先按 P 再按 L）

### 原理图

- 显示 Library 面板：**PP**
- 绘制导线：**Ctrl + W**
- 绘制网络标签：**PN**
- 复制元件并自动更新位号：**按住 Shift + 拖动**
- 给图纸编号：**TAT**
- 元件自动编号：**TAA**
  - Reset All：复位所有元件标号，使其变成 " 字母 + ? " 的格式
  - Update Change List：对元件列表进行标号变更
  - Accept Changes（Create ECO）：表示接受编号变更，实现原理图的变更
- 生成 BOM 表：**RI**
- 更新 PCB：**DU**
- 左对齐（右）：**AL**（**AR**）

### PCB

- 把原理图的变更导入 PCB：**DI**
- 把 PCB 的变更覆盖回原理图：**DU**
- 切换单位（英寸/毫米）：**Q**
- 旋转元器件（任意角度）：**EMO**
- 把元件放置在底层：**拖动同时按 L**
- 自动布局：**框选 + TOL**
- 设置坐标原点：**EOS**
- 设置栅格：**G**
- 自动布线：**UAA**
- 清除布线：**UUA**
- 高亮接线：**按住 Shift + 光标移至线**
- 高亮节点所对应连线：**按住 Ctrl + 左键单击**
- 水平翻转：**Ctrl + F**
- 测量：**Ctrl + M**
- 切换视图（二维 / 三维）：**2 / 3**
- 三维视图中旋转：**按住 Shift + 拖动**
- 清除过滤器：**Shift + C**
- 切换单层/多层显示：**Shift + S**
- 过孔盖油（可略，打板时可直接选择）
  1. 单击某一过孔
  2. 右键 - 查找相似对象
  3. 选择大小属性为 Same，确定以激活选择所有过孔
  4. 在属性中的 Solder Mask Expansion 中把顶层和底层都勾选上
- 设置布线规则
  1. **UAA**
  2. 新建策略并编辑规则
  3. 一般修改 Routing 中的规则（新建规则）
     - Width：设置线的粗细
     - Routing Via Style ：设置过孔规则
     - 铺铜：？

### 原理图库

待补充……

### 封装库

- 测量距离：**Ctrl + N**
- 切换单位（英寸/毫米）：**Q**

## 流程及规范

一块电路板从无到有设计出来，基本流程如下：

1. 初始化
   1. 新建项目
   2. 在项目内创建原理图和 PCB 文件
2. 绘制原理图
   1. 完成后确保编译通过
3. 绘制 PCB
   1. 从原理图导入变更
   2. 隐藏元件 Designator 标识
      1. 打开右侧 **Properties** 面板
      2. 点击 **Designator** 旁边的 **眼睛** 标志，即可关闭
   3. 绘制板形
      - 切换 90°/45° 走线（**Shift+Space**）
      - 以所画形状定义板子（**DSD**）
      - **设置板框属性为机械层 1**
      - 固定孔
        - M3 螺孔：内 **3.1** mm、外 **4** mm
   4. 排布元件
      - 跳转文章 [**PCB 元件布局规范**](https://wiki-power.com/PCB%E5%85%83%E4%BB%B6%E5%B8%83%E5%B1%80%E8%A7%84%E8%8C%83)
   5. 布线
      - 设置布线规则
        - 参考 [**PCB 布线规范**](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
      - **不要开启自动布线！**
      - **开启泪滴功能**
   6. 字体标识（引脚标识 / 版权 / 迷惑性文字）
      - 放置于丝印层（顶层 / 底层）
      - 放底层要先镜像
   7. 敷铜（**PG**）
      - 参考 [**PCB 布线规范**](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
4. 打板
   1. 保存项目
   2. 将 **.pcb** 文件压缩（这样做似乎不太对，可以的话导出 Gerber）
   3. 上传至 **嘉立创下单助手**
   4. （可选 SMT）

## 其他知识

### 元件属性

- **Designator**：元件位号，是元件的唯一标识，用来标识原理图中的不同的元件
  - **R**：电阻
  - **RN**：排阻
  - **C**：电容
  - **J**：接口/跳线
  - **X**：晶振
  - **D**：二极管
  - **Q** 或 **T**：三极管
  - **FB**：磁珠
  - **U**：芯片
  - **TP**：测试点
- **Comment**：元件大小参数，如电阻的阻值、电容的容值、IC 芯片型号等
- **Description**：用于填写元件的功能描述

### Logo 添加

跳转文章 [**Logo 添加**](https://seujxh.wordpress.com/2018/10/03/logo%E6%B7%BB%E5%8A%A0/) 。

### 使用 Git 管理项目

详见 [**AD 使用 Git 的注意事项**](https://wiki-power.com/AD%E4%BD%BF%E7%94%A8Git%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)

## 总结

以上是 Altium Designer 及电路设计的基本知识。  
下一章，我们将着手开始原理图的设计。

## 参考与致谢

- [Altium 公司 Altium Designer 专栏](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [嘉立创 SMT 贴片 可贴列表 PADS 集成库 \（正式版)](http://club.szlcsc.com/article/details_2757_1.html)
- [Altium Designer 使用 Git 构想](https://blog.csdn.net/weifengdq/article/details/78406438)
- [Using Version Control](https://www.altium.com/documentation/altium-designer/using-version-control-ad)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

