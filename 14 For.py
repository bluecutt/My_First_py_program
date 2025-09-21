# for循环
# 1.1 for循环基本格式:


# for 临时变量 in 可迭代对象:
#     循环体

# 注意冒号和缩进
str = 'helloworld'  # 定义一个字符串
# 可迭代对象就是要去遍历取值的整体，字符串就是可迭代对象,int整型，浮点型不是可迭代对象
for i in str:
    print(i)
'''运行结果为:
h
e
l
l
o
w
o
r
l
d'''

# 1.2 range()
# 用来记录循环次数，相当于一个计数器
for i in range(1,6):
    print(i)

'''输出结果为:
1
2
3
4
5'''    #取值原则:包前不包后,也就是[)