# Resolving the issue of missing time information when exporting from Google Photos

After exporting from Google Photos using Google Takeout, the time information of many photos is saved as a `.json` file. How can we import this information back to the corresponding photos?

Create a new Python file called `update-data.py`:

```python
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle
from win32file  import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import os,json,time

# Get all file names with a specific extension
def get_all_file(ext_name):
    file_list = []
    datanames = os.listdir()
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == ext_name:  # Files in the directory with the .json extension
            file_list.append(dataname)
    return file_list

# Read the json file
def load_json(json_file_name):
    f = open(json_file_name,'r',encoding = 'UTF-8')
    text = f.read()
    dic = json.loads(text)
    return dic

def modifyFileTime(filePath, createTime, modifyTime, accessTime, offset):
    """
    Used to modify the time attributes of any file, time format: YYYY-MM-DD HH:MM:SS, for example: 2019-02-02 00:01:02
    :param filePath: File path
    :param createTime: Creation time
    :param modifyTime: Modification time
    :param accessTime: Access time
    :param offset: Time offset in seconds, in tuple format, in the order corresponding to the time parameters
    """
    try:
        format = "%Y-%m-%d %H:%M:%S"  # Time format
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
```

```python
import time

def timeOffsetAndStruct(times, format, offset):
    return time.localtime(time.mktime(time.strptime(times, format)) + offset)

# Date conversion, converting Google's date to a numerical value
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
    file_name_json = get_all_file('.json')                      # Get a list of all file names in the current directory

    for fnj in file_name_json:
        dic = load_json(fnj)                                        # Extract dictionary information
        st = dic['creationTime']['formatted']                       # Get the file date
        output_format = time_format(st)                             # Convert the date format

        file_name = fnj[0:-5]                                       # Get the corresponding photo name of the file
        print(file_name)
        offset = (0, 1, 2)
        # Modify the file date
        modifyFileTime(file_name, output_format, output_format, output_format,offset)
```

This script is used to modify the file creation date based on a JSON file and import it into the corresponding photo with the same name.

Simply place this script in the directory of each album and run it. After execution, the time information of the photos will be restored.

## References and Acknowledgements

- [Google Photos Downloaded Date Loss Problem](https://zhuanlan.zhihu.com/p/356718593)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.