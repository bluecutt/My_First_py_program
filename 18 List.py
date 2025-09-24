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
# append()  extend() insert()
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