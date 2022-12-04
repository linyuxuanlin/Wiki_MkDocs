---
id: 解决Google相册导出时间信息丢失问题
title: 解决 Google 相册导出时间信息丢失问题
---

在 Google Takeout 导出 Google 相册后，很多照片的时间信息都被另存为 `.json` 文件。如何将其导入对应照片呢？

新建一个 Python 文件 `update-data.py`：

```python
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle
from win32file  import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import os,json,time

# 获取指定后缀的文件名
def get_all_file(ext_name):
    file_list = []
    datanames = os.listdir()
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == ext_name:  #目录下包含.json的文件
            file_list.append(dataname)
    return file_list

# 读取json
def load_json(json_file_name):
    f = open(json_file_name,'r',encoding = 'UTF-8')
    text = f.read()
    dic = json.loads(text)
    return dic

def modifyFileTime(filePath, createTime, modifyTime, accessTime, offset):
    """
    用来修改任意文件的相关时间属性，时间格式：YYYY-MM-DD HH:MM:SS 例如：2019-02-02 00:01:02
    :param filePath: 文件路径名
    :param createTime: 创建时间
    :param modifyTime: 修改时间
    :param accessTime: 访问时间
    :param offset: 时间偏移的秒数,tuple格式，顺序和参数时间对应
    """
    try:
        format = "%Y-%m-%d %H:%M:%S"  # 时间格式
        cTime_t = timeOffsetAndStruct(createTime, format, offset[0])
        mTime_t = timeOffsetAndStruct(modifyTime, format, offset[1])
        aTime_t = timeOffsetAndStruct(accessTime, format, offset[2])

        fh = CreateFile(filePath, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
        createTimes, accessTimes, modifyTimes = GetFileTime(fh)

        createTimes = Time(time.mktime(cTime_t))
        accessTimes = Time(time.mktime(aTime_t))
        modifyTimes = Time(time.mktime(mTime_t))
        SetFileTime(fh, createTimes, accessTimes, modifyTimes)
        CloseHandle(fh)
        return 0
    except:
        return 1


def timeOffsetAndStruct(times, format, offset):
    return time.localtime(time.mktime(time.strptime(times, format)) + offset)

#日期转换，将谷歌的日期转化为数值
def time_format(data_string):
    print(data_string)
    year = data_string.split('年')[0]
    month = data_string.split('年')[1].split('月')[0]
    day = data_string.split('年')[1].split('月')[1].split('日')[0]
    add_flag = data_string.split('年')[1].split('月')[1].split('日')[1].find('下午')
    hour = data_string.split('年')[1].split('月')[1].split('日')[1].split('午')[1].split(':')[0]
    minute = data_string.split('年')[1].split('月')[1].split('日')[1].split('午')[1].split(':')[1]
    second = data_string.split('年')[1].split('月')[1].split('日')[1].split('午')[1].split(':')[2]
    if add_flag > 0:
        hour = str(int(hour)+12)
    return year + '-' + month + '-' +day +' ' + hour + ':'+ minute + ':' + second


if __name__ == '__main__':
    file_name_json = get_all_file('.json')                      #获取当前目录下所有文件图片文件名list

    for fnj in file_name_json:
        dic = load_json(fnj)                                        #提取字典信息
        st = dic['creationTime']['formatted']                       #获取文件日期
        output_format = time_format(st)                             #转换日期格式

        file_name = fnj[0:-5]                                       #获取对应文件的照片名字
        print(file_name)
        offset = (0, 1, 2)
        #修改文件日期
        modifyFileTime(file_name, output_format, output_format, output_format,offset)
```

这个脚本的作用是根据 json 修改文件创建日期，并将其导入同名的照片。

直接将此脚本放入每个相册的目录中运行即可。执行过后，照片的时间信息就回来了。

## 参考与致谢

- [谷歌相册下载后的时间丢失问题](https://zhuanlan.zhihu.com/p/356718593)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

