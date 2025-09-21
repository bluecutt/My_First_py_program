# 数值类型

# 1.int整型（常用）：任意大小的整数
num1 = 1
#检测数据类型的方法 type()
print(type(num1))
# <class 'int'>

# 2.float浮点数：小数
num2 = 1.5
print(type(num2))
# <class 'float'>

# 3.bool布尔型（重点）通常用于判断
# <class 'bool'>
#有固定写法，一个为True(真)，一个为False（假）,严格区分大小写
print(type(True))
#布尔值可以当作整型来对待，True相当于整数1，False相当于整数0
print(True + False)  # 1 + 0 = 1

# 4.complex复数型(了解即可)
# 固定写法 ： z = a + bj  ---a是实部，b是虚部，j是虚数单位