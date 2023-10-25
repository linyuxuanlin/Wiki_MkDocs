# حل مشكلة فقدان معلومات وقت تصدير Google Photos

بعد تصدير Google Photos باستخدام Google Takeout ، يتم حفظ معلومات الوقت للعديد من الصور كملفات `.json`. كيف يمكن استيراد هذه المعلومات إلى الصور المقابلة؟

أنشئ ملف Python جديد بالاسم `update-data.py`:

```python
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle
from win32file  import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import os,json,time

# الحصول على أسماء الملفات ذات الامتداد المحدد
def get_all_file(ext_name):
    file_list = []
    datanames = os.listdir()
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == ext_name:  # الملفات التي تحتوي على امتداد .json في الدليل
            file_list.append(dataname)
    return file_list

# قراءة الملف الـ json
def load_json(json_file_name):
    f = open(json_file_name,'r',encoding = 'UTF-8')
    text = f.read()
    dic = json.loads(text)
    return dic

def modifyFileTime(filePath, createTime, modifyTime, accessTime, offset):
    """
    يستخدم لتعديل الخصائص الزمنية لأي ملف ، تنسيق الوقت: YYYY-MM-DD HH:MM:SS على سبيل المثال: 2019-02-02 00:01:02
    :param filePath: مسار الملف
    :param createTime: وقت الإنشاء
    :param modifyTime: وقت التعديل
    :param accessTime: وقت الوصول
    :param offset: عدد الثواني المنقولة ، تنسيق tuple ، الترتيب يتوافق مع وقت الوسائط
    """
    try:
        format = "%Y-%m-%d %H:%M:%S"  # تنسيق الوقت
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
def timeOffsetAndStruct(times, format, offset):
    return time.localtime(time.mktime(time.strptime(times, format)) + offset)

# تحويل التاريخ ، تحويل تاريخ Google إلى قيمة رقمية
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
    file_name_json = get_all_file('.json')                      # الحصول على قائمة أسماء ملفات الصور في الدليل الحالي

    for fnj in file_name_json:
        dic = load_json(fnj)                                        # استخراج معلومات القاموس
        st = dic['creationTime']['formatted']                       # الحصول على تاريخ الملف
        output_format = time_format(st)                             # تحويل تنسيق التاريخ

        file_name = fnj[0:-5]                                       # الحصول على اسم الصورة المقابلة
        print(file_name)
        offset = (0, 1, 2)
        # تعديل تاريخ الملف
        modifyFileTime(file_name, output_format, output_format, output_format,offset)
```

هذا البرنامج النصي يقوم بتعديل تاريخ إنشاء الملف بناءً على JSON واستيراده إلى الصورة ذات الاسم نفسه.

قم بوضع هذا البرنامج النصي مباشرة في دليل كل ألبوم وقم بتشغيله. بعد التنفيذ ، ستعود معلومات الوقت للصور.

## المراجع والشكر

- [مشكلة فقدان الوقت بعد تنزيل Google Photos](https://zhuanlan.zhihu.com/p/356718593)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.