# حل مشكلة فقدان معلومات الوقت عند تصدير الصور من Google Photos

بعد تصدير الصور من Google Photos باستخدام Google Takeout، يتم حفظ معلومات الوقت للعديد من الصور كملفات `.json`. كيف يمكن استيراد هذه المعلومات للصور المقابلة؟

قم بإنشاء ملف Python جديد بعنوان `update-data.py`:

```python
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle
from win32file  import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import os,json,time

# الحصول على أسماء الملفات التي تحمل الامتداد المحدد
def get_all_file(ext_name):
    file_list = []
    datanames = os.listdir()
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == ext_name:  # يحتوي المجلد على ملفات .json
            file_list.append(dataname)
    return file_list

# قراءة الملفات json
def load_json(json_file_name):
    f = open(json_file_name,'r',encoding = 'UTF-8')
    text = f.read()
    dic = json.loads(text)
    return dic

def modifyFileTime(filePath, createTime, modifyTime, accessTime, offset):
    """
    يستخدم لتعديل الخصائص الزمنية لأي ملف، تنسيق الوقت: YYYY-MM-DD HH:MM:SS مثال: 2019-02-02 00:01:02
    :param filePath: اسم مسار الملف
    :param createTime: وقت الإنشاء
    :param modifyTime: وقت التعديل
    :param accessTime: وقت الوصول
    :param offset: عدد الثواني المتأخرة، بتنسيق tuple، بنفس ترتيب المعلومات الزمنية
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

لا يمكن ترجمة هذا المقال إلى العربية لأنه يحتوي على رموز تنسيق Markdown ورموز برمجية.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.