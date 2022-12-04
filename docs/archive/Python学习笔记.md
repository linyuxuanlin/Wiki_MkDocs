---
id: Python学习笔记
title: Python 学习笔记
---

## 环境配置

我们首先需要配置以下环境

- Python：<https://www.python.org/>
- VS Code：<https://code.visualstudio.com/>
- Python extension：<https://marketplace.visualstudio.com/items?itemName=ms-python.python>

## 参考与致谢

- [Introduction to Python](https://docs.microsoft.com/en-us/learn/modules/intro-to-python/)

## 基础语法

### Print

基本语法：

```python
print('Hello World')
print("Hello World")
print('Hello' + 'World')
```

让用户输入信息：

```python
name = input('Please enter your name: ')
print(name)
```

打印空白行：

```python
print() # 空白行
print('NaNaNa\n') # 换行符
```

### Comments

```python
# 这是一行注释
# 注释不会作为代码运行
```

### Strings

```python
name = 'power'
print('Hello' + name)
```

格式化：

```python
output = 'Hello, ' + first_name + '' + last_name
output = 'Hello, {} {}'.format(first_name, last_name)
output = 'Hello, {0} {1}'.format(first_name, last_name)
output = f'Hello, {first_name} {last_name}'
```

### Numbers

类型转换

```python
days_in_feb = 30
print(str(days_in_feb) + ' days in February')
```



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

