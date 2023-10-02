# TinyTimelapseCam - 基于 ESP32-S3 的迷你延时相机

这是一个基于 ESP32-S3 的迷你延时相机，你可以用它来拍摄白天的云层飘动、一整晚的斗转星移，也可以用来抓取城市街道上形形色色的人群。

## 部署网络摄像头

请参考 [**摄像头使用**](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12) 章节进行部署，此处不赘述。

## 测试使用 Python 调用推流

```py title="StreamViewer.py"
# 调用 OpenCV 库
import cv2

# 定义摄像头地址
camera_url = "http://192.168.31.203:81/stream"

# 创建VideoCapture对象
cap = cv2.VideoCapture(camera_url)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法连接到摄像头。请检查摄像头地址或网络连接。")
    exit()

while True:
    # 读取帧
    ret, frame = cap.read()

    # 检查帧是否成功读取
    if not ret:
        print("无法获取帧。")
        break

    # 显示预览画面
    cv2.imshow('Camera Preview', frame)

    # 按下 'q' 键退出预览
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
```

需要注意的是，推流的地址是在原 IP 的基础上，加上 `:81/stream` 后缀。你也可以在网页端显示的实时画面上点击右键，复制推流的地址。

## 延时相机

如果前面的推流测试成功，就可以尝试以下延时相机的程序了：

```py title="TimelapseCam.py"
import cv2
import numpy as np
import time
import os

nframes = 500  # 拍摄多少张照片
interval = 0.00001  # 间隔时间（秒）

# 需要改为你的 ESP32 的 IP 地址
cap = cv2.VideoCapture('http://192.168.31.203:81/stream')

print("延时相机启动")
for i in range(nframes):
    # 捕获图像帧
    ret, img = cap.read()
    # 保存图像文件
    if img is None:
        print("无法获取图像")
    else:
        cv2.imwrite('temp_destination/photos/img_' +
                    str(i + 1000).zfill(4) + '.png', img)
    # 等待一段时间
    time.sleep(interval)
    print("照片编号：", i)

# 定义照片文件夹路径
photos_path = "temp_destination/photos/"
# 如果文件夹不存在，则创建文件夹
os.makedirs(photos_path, exist_ok=True)
# 获取照片文件名列表
photos = os.listdir(photos_path)
# 按名称对照片进行排序
photos.sort()
# 创建视频写入对象
video = cv2.VideoWriter("temp_destination/video.avi",
                        cv2.VideoWriter_fourcc(*"MJPG"), 100, (1280, 720))

# 遍历照片
for photo in photos:
    # 读取照片作为图像
    image = cv2.imread(photos_path + photo)
    # 调整图像大小以适应视频帧大小
    image = cv2.resize(image, (1280, 720))
    # 将图像写入视频
    video.write(image)

# 释放视频写入对象
video.release()
print("延时摄影视频生成完成")
```

运行程序后，你可以在 `temp_destination` 文件夹下找到生成的视频。你也可以修改 `nframes` 和 `interval` 参数，使延时相机可以适用于不同的拍摄场景。

## 疑难解答与建议

- 如果网页端可以显示实时画面，但本地无法抓取推流，这是因为同一时间只能开一个推流，请尝试把网页关掉。
- 如果你打算拍一整天的视频，可以把 Python 程序运行在低功耗的服务器或旧手机上，这样就不用一直开着电脑。

## 参考与致谢

- [ESP32-CAM Python stream OpenCV Example](https://www.hackster.io/onedeadmatch/esp32-cam-python-stream-opencv-example-1cc205)
- [Live Security Camera with UNIHIKER & FireBeetle 2 ESP32S3](https://www.hackster.io/pradeeplogu0/live-security-camera-with-unihiker-firebeetle-2-esp32s3-5d478e)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
