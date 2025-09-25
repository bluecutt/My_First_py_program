# 1 列表
# 基本格式:
# 列表名 = [元素一，元素二，元素三..]

# 注意:
# 所有元素放在中括号内，元素与元素之间用逗号隔开
# 元素之间的内容可以各不相同
li = [1,2,3,4,'sss']
print(type(li)) # <class 'list'>
print(li[4]) # sss
print(li[0:3]) # [1, 2, 3]
# 列表亦可以进行切片操作
# 列表是可迭代对象
for i in li:
    print(i)

# 2 列表的常见操作

# 2.1 添加元素
# append()  extend()  insert()
li = ['one','two','three','four','five']
li.append('six')
print(li)  # ['one', 'two', 'three', 'four', 'five', 'six']
# append整体添加

li.extend('我喜欢你')
print(li)
# extend 分散添加，将另外一个类型 中的元素逐一添加

li.insert(4,'我不喜欢你')
print(li)  # 如果指定位置有元素，原有元素就会后移
# 如果不指定下表就会报错

# 2.2 修改元素
# 直接通过下标就可以进行修改
li = [1,2,3]
li[2] = 'a'
print(li)  # [1, 2, 'a']

#2.3 查询元素
# in:如果包含的话，返回Ture,不包含返回False
# not in:如果不包含的话返回Ture,包含返回False
li = ['a','b','c','d']
print('b' in li)  # Ture

# index: 返回指定数据所在位置的下标，如果查找数据不存在就会报错
# count: 统计指定数据在当前列表出现的次数
# 跟字符串中用法相同

# 2.4 删除元素
# del   根据下标来删除
li = ['a','b','c','d']
del li[2]
print(li)  # ['a', 'b', 'd']

# pop:删除指定下标的数据，python3版本指定删除最后一个元素
li = ['a','b','c','d']
li.pop()
print(li)  # ['a', 'b', 'c']  #默认删除d

li = ['a','b','c','d']
li.pop(2)  # 不能指定元素删除。只能根据下标删除
print(li) # ['a', 'b', 'd']
# 下标不可以超出范围

# remove:根据元素的值进行删除
li = ['a','b','c','d','d']
li.remove('a')
print(li)  # ['b', 'c', 'd']
# li.remove('x')     若列表中不存在值就会报错
li.remove('d')  # 若列表中有两个相同的元素，则删除时默认删除最先 出现的指定元素
print(li)

# 2.5 排序
# sort:将列表按特定顺序进行排列
li = [1,88,6999,555,4412,8]
li.sort()
print(li)  # [1, 8, 88, 555, 4412, 6999]  按从小到大的顺序进行排序

#reverse:将列表倒置过来进行排序
li = [1,88,6999,555,4412,8]
li.reverse()
print(li)  # [8, 4412, 555, 6999, 88, 1]




# 3 列表推导式
# 格式一:[表达式 for 变量 in 列表]
# 注意: in后面不仅可以放置列表，还可以放置range()、可迭代对象
li = [1,2,3,4,5,6]
[print(i) for i in li]  # 前面的i是表达式


li = []
for i in range(1,6):
    print(i)
    li.append(i)
print(li)
# 上式与下式等价
[li.append(i) for i in range(1,8)]
print(li)

# 格式二:[表达式 for 变量 in 列表 if 条件]
# 把奇数放进列表里面
li = []
for i in range(1,11):
    if i % 2 ==1:
        li.append(i)
print(li)
# 上下式子等价
li = []
[li.append(i) for i in range(1,10) if i % 2 == 1]
print(li)


# 4 列表嵌套
# 含义:一个列表里面又有一个列表
li = [1,2,3,[4,5,6]]  #4,5,6是里面的列表
print(li[3])  # [4, 5, 6]
# 取出里面的列表
print(li[3][0])  # 4   # 取出嵌套列表中的数