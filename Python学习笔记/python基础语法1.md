
### print函数

#### 1. 输出到文件中
~~~python
fp=open('文件路径'，'打开方式')
print('要输入的内容'，file=fp)
fp.close() 
~~~
#### 2. 连续在一行输出多个字符串
```python
print('hello','world','python')
```
---

### 变量定义及使用
```python
print(id(name))              #输出变量name的内存地址
print(type(name))            #输出变量name的数据类型
print(name)                  #输出变量name的值
```
---


### 数据类型转换
##### 1. str() 将其他数据类型转换为字符串
##### 2. int()将其他数据类型转换成整型
    .无法将文字，小数类字符串转化
    .浮点类转化会抹零取整
##### 3. float()将其他类型转化成浮点型
    .文字类无法转化成浮点型



