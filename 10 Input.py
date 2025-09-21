# 1.Input输入函数
#input(__prompt=)
name = input("请输入你的名字:")

# 2.转义字符
# 2.1 \t 制表符 通常表示空四个字符，也称缩进
#如
print('Blue\tsky')
#输出结果为
# Blue	sky

# 2.2 \n 换行符
# 如
print('哈哈\n嘻嘻')
#输出结果为:
'''嘻嘻
   哈哈'''


# 2.3 \r 回车 表示当前位置移到本行开头
# 如
print('six\rstar')
# 输出结果为:
# star

# 2.4 \\ 反斜杠符号
# 如:
print('six\tstar')
# 输出结果为:
# six	star
print('six\\tstar')
# 输出结果为:
# six\tstar

# 注意：原生字符 r 可使得括号内所有转义字符失效
# 如:
print(r'six\tstar')
# 输出结果为:
# six\tstar
