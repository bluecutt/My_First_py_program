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
A1 = A.encode('utf-8')
print(A1)
A2 = A1.decode('utf-8')
print(A2)