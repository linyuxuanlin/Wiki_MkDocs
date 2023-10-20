# TheExec (التنفيذي) 🚧

**TheExec (التنفيذي)** هو واحد من أعلى الكائنات المستوى، الذي يمنح الوصول إلى خصائص التنفيذ الاختبارية ذات الصلة.

## التدفق

```vbscript
TheExec.Flow
```

### TestLimit

```vbscript
TheExec.Flow.TestLimit(resultVal, lowVal, hiVal, lowCompareSign,
highCompareSign, scaletype, unit, formatStr, TName, compareMode, pinName,
forceVal, forceunit, customUnit, customForceunit, ForceResults, TNum)
```

المعلمات الأكثر استخدامًا:

- **resultVal** (مطلوب): القيمة التي ستتم كتابتها كنتيجة.
- **lowVal**, **hiVal** : الحدود الدنيا والحدود العليا. الافتراضي هو lowVal <= resultVal <= hiVal.
- **unit**: وحدة القياس
  - `unitAmp` `unitVolt` `unitDb` `unitHz` `unitTime` .
- **TName**: اسم اختبار يجب تسجيله في السجل. إذا ترك فارغًا، سيتم استخدام اسم النسخة الاختبارية.
- **pinName**: اسم الدبوس الذي يجب تسجيله في السجل.
- **forceVal**, **forceunit**: قيمة الشرط الاختباري ووحدته.
- **ForceResults**: ما إذا كان يجب فرض نجاح أو فشل أو استخدام الحدود المحددة في جدول التدفق.

مثال:

```vbscript
TheExec.Flow.TestLimit  resultVal:=Vout_Measure, _
                        unit:=unitVolt, _
                        Tname:="جهد الإخراج", _
                        pinName:=vout_pin, _
                        forceval:=vin_pin_voltage, _
                        forceunit:=unitVolt, _
                        forceresults:=tlForceFlow, _
                        lowval:=VOT_LowLimit, _
                        hival:=VOT_HiLimit
```

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.