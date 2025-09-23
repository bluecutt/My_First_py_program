# 1.字符串编码
# 本质上就是二进制数据与语言文字的一一对应关系

# 1.1 Unicode: 所有字符都是2个字节
# 好处:字符与数字之间转换速度更快一些
# 坏处:占用空间大

# 1.2 UTF-8:精准，对不同字符的不同长度表示
# 好处:节省空间
# 坏处:字符与数字的转换速度，较慢，每次都需要计算字符需要计算字符要多少个字节来表示

# 2 字符串编码转换
a = 'hello world'
print(type(a))  #str 字符串是以字符为单位进行处理
print(a)
A = a.encode()  # 编码
print(A)
print(type(A))  # bytes,以字节为单位进行处理
a2 = A.decode()
print(type(a2)) # 回归字符串类型

#对于bytes，只需要知道它跟字符串之间的转换关系

A = '罗春兴是我的儿子'
A1 = A.encode('utf-8')  # 编码
print(A1)
A2 = A1.decode('utf-8')  # 解码
print(A2)

# 3 字符串常见操作
# 3.1 + 字符串拼接
print('10'+'10')
# 结果为1010，字符串相加，+是字符串拼接
name1 = '天气'
name2 = '之子'
print(name1 + name2)
print(name1,name2,sep='')
# 结果都为:天气之子

# 3.2 重复输出
print('好好学习，天天向上\n'*5)

# 4 成员运算符
# 作用:检查字符串中是否包含了某个子字符串(即某个字符或多个字符)
# in:如果包含的话，返回Ture,不包含返回False
# not in:如果不包含的话返回Ture,包含返回False
name = '杨斐然'
print('杨'in name)  # 结果为Ture
print('王'in name)  # 结果为False
print('杨'not in name)  #结果为False

# 5 下标
# Python中下表从0开始
# 作用:通过下标可以快速找到对应的数据
# 格式:字符串名[下标值]
name = 'YFR'
# 从左往右数，下表从0开始
print(name[0])  # 输出结果为:Y
print(name[1]) # 输出结果为:F

# print(name[7])  # 报错，取值时候不要超出范围

# 从右往左数，下标从-1开始
print(name[-1])  # 结果为:R

# 6 切片
# 含义:只对操作对象截取一部分的操作
# 语法:[开始位置:结束位置:步长]
# 包前不包后:即从起始位置开始，到结束位置前一位结束(不包含结束位置本身)
A = 'ABCDEFG'
print(A[0:4])  # ABCD
print(A[3:7])  # DEFG
print(A[3:])
# 从右往左取
print(A[-3:])
# 步长:表示选取间隔，不写步长，则默认是1
# 步长的绝对值大小决定切取的间隔，正负号决定切取方向
# 正数表示从左往右取值，复数表示从右往左取值
print(A[-1:-5:-1])  # 结果为:GFED
print(A[0:5:2])  # 结果为:ACE

