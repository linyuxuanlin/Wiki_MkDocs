# TheExec (The Executive) 🚧

> هذه المقالة متاحة فقط باللغة الإنجليزية.

**TheExec (The Executive)** هو أحد أعلى المستويات الكائنات، والذي يمنح الوصول إلى الخصائص المتعلقة بالتنفيذ الاختباري.

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
- **lowVal**، **hiVal**: الحدود الدنيا والعليا. الافتراضي هو lowVal <= resultVal <= hiVal.
- **unit**: وحدة القياس
  - `unitAmp` `unitVolt` `unitDb` `unitHz` `unitTime` .
- **TName**: اسم الاختبار الذي سيتم تسجيله في الداتالوج. إذا ترك فارغًا، سيتم استخدام اسم مثيل الاختبار.
- **pinName**: اسم الدبوس الذي سيتم تسجيله في الداتالوج.
- **forceVal**، **forceunit**: قيمة وحدة شرط الاختبار.
- **ForceResults**: ما إذا كان يجب إجبار النتيجة على النجاح أو الفشل أو استخدام الحدود المحددة في جدول التدفق.

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