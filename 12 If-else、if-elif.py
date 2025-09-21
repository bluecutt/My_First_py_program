# 1.if-else基本格式:

# if 条件:
#     满足条件做的事
# else:
#     不满足条件做的事

a=666
if a == 666:
    print('一般')
else:        # else不添加任何条件
    print('你不行啊')

# 结果为：一般，如果a != 666,则结果为：你不行啊

# 正常格式为：
a = 4
b = 5
if a <= b:
    print('a小于等于b')
else:
    print('a大于b')

# 三目运算格式为：
print('a小于等于b') if a <= b else print('a大于b')

# 2.if-elif结构
# if-else二选一  if-elif多选一
# 格式如下:

# if 条件一:
#     满足条件一要做的事情一
# elif 条件二:
#     满足条件二要做的事情二
# elif 条件三:
#     满足条件三要做的事情三
# ......

score = float(input('小朋友你考了多少分啊:'))
if 85 <= score <=100:
    print('有点东西但不多')
elif 60 <= score < 85:
    print('飞舞')
elif 0 <= score < 60:
    print('孩子重开吧')
else:
    print('骗骗哥们得了，别给自己骗了啊')


# 3.if嵌套

# if嵌套基本格式：
# if 条件1:
#     事情1
#     if 条件2:
#         事情2
# else:
#     不满足条件的事情

# 注意: 内层if判断和外层if判断都可以是if-else结构

