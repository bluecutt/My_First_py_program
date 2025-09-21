# 1.while循环
# 语法格式:

# 定义初始变量
# while 条件 :
#     循环体(满足条件时段做的事情)
#     改变变量


# 死循环
# while True:
#     循环体(要循环做的事情)

A = 1  # 定义一个初始值，记录循环次数。A = 1表示从第一次开始
while A <= 100:
    print('好好学习天天向上')
    A += 1

# while True:    # 条件只写Ture,说明一直为真，程序就会一直执行
#     print(666)
# 只要条件不是False或0.其他单独的值也会是死循环

# 2.while循环的应用

B = 1
C = 0
while B <=100:
    C += B
    B += 1
print('计算结果为: %s' %C )


# 3.while循环嵌套
# 基本格式:

# while 条件一:
#     循环体一
#     while 条件二:
#         循环体二
#         改变变量二
#     改变变量一
i = 1
while i <= 3:
    print(f'这是第{i}次外循环')
    j=1
    while j <= 5:
        print(f'这是第{j}次内循环')
        j += 1
    i += 1
