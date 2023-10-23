# TheExec (التنفيذي) 🚧

**TheExec (التنفيذي)** هو أحد الكائنات على أعلى مستوى، والذي يمنح الوصول إلى خصائص التنفيذ التجريبي ذات الصلة.

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

- **resultVal** (مطلوب): القيمة التي سيتم كتابتها كنتيجة.
- **lowVal**, **hiVal**: الحدود السفلى والعلوية. القيمة الافتراضية هي lowVal <= resultVal <= hiVal.
- **unit**: وحدة القياس
  - `unitAmp` `unitVolt` `unitDb` `unitHz` `unitTime`.
- **TName**: اسم الاختبار الذي سيتم تسجيله في السجل. إذا ترك فارغًا، سيتم استخدام اسم مثيل الاختبار.
- **pinName**: اسم الدبوس الذي سيتم تسجيله في السجل.
- **forceVal**, **forceunit**: قيمة وحدة الاختبار.
- **ForceResults**: ما إذا كان سيتم فرض نجاح أو فشل أو استخدام الحدود المحددة في جدول التدفق.

على سبيل المثال:

```vbscript
TheExec.Flow.TestLimit  resultVal:=Vout_Measure, _
                        unit:=unitVolt, _
                        Tname:="Output_Voltage", _
                         pinName:=vout_pin, _
                         forceval:=vin_pin_voltage, _
                         forceunit:=unitVolt, _
                         forceresults:=tlForceFlow, _
                         lowval:=VOT_LowLimit, _
                         hival:=VOT_HiLimit
```

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.