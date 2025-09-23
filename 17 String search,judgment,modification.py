# 一 查找:
# 1 查找
# find:检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，否则就返回-1
# find(子字符串，开始位置下标，结束位置下标)
# 注意:开始和结束位置下标可以神略，表示在整个字符串中查找
name = 'bingbing'
print(name.find('i'))  # 第一个i的下表为2
print(name.find('bing')) # 检测到第一个’bing‘ ，’b‘的下标为0
print(name.find('b',3)) # 4
print(name.find('b',5)) # -1  --超出范围，不包含返回-1
print(name.find('b',3,5)) #--在下标3-5位置范围内寻找
# 包前不包后
print(name.find('b',3,4)) # -1

# 2 index():检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，否则就会报错
# index(子字符串，开始位置下标，结束位置下标)
# 注意:开始和结束位置下标可以神略，表示在整个字符串中查找
# name = '我命由我不由天'
# print(name.index('命'))
# print(name.index('命',2))  #报错，从下标2开始找，没有找到
# 依旧包前不包后
# 与find的区别:find没找到，返回-1，而index直接报错

# 3 count():返回某个字符串在整个字符串中出现的次数，没有就返回0
# 注意:开始和结束位置下标可以神略，表示在整个字符串中查找
name = 'bingbing'
print(name.count('b')) # 2
print(name.count('a')) # 0
print(name.count('b',1)) # 1
print(name.count('b',1,3))  # 0
# 依旧包前不包后

# 二 判断:
# 1 startswith():是否以某个字符串开头，是的话就返回Ture,不是的话就返回False,如果设置开始和结束位置下标，则在指定范围内检查
# startswith(子字符串，开始位置下标，结束位置下标)
st ='sixstar'
print(st.startswith('six'))  #Ture
print(st.startswith('x'))  #False
print(st.startswith('s',2,4)) #Ture

# 2 endswith():是否以某个字符串结尾，是的话就返回Ture,不是的话就返回False,如果设置开始和结束位置下标，则在指定范围内检查
st ='sixstar'
print(st.endswith('six'))
print(st.endswith('six'))
print(st.endswith('s',2,4))

# 3 isupper(): 检测字符串中所有的字母是否都为大写，是则返回Ture
st ='sixstar'
print(st.isupper())

# 三 修改元素
# 1 replace():替换
# replace (旧内容，新内容，替换次数)
# 注意，替换次数可以省略，默认全部替换
name = '好好学习，天天向上'
print(name.replace('天','时',1))  # 结果:好好学习，时天向上

# 2 split:指定分隔符来切割字符串:
st = 'hello,Python'
print(st.split(','))  # ['hello', 'Python']  --以列表的形式返回
# 如果字符串中不包含分割内容，就不进行分割而是作为一个整体
print(st.split('a'))  # ['hello,Python']
print(st.split('o'))  #['hell', ',Pyth', 'n']
print(st.split('o',1))  # ['hell', ',Python'] --指定只分割一次

# 3 capitalize():第一个字符大写，其他都小写
st = 'sixStar'
print(st.capitalize())  # Sixstar

# 4 lower():大写字母转为小写
st = 'BBBAAaaa'
print(st.lower())  # bbbaaaaa

# 5 upper():小写字母转为大写
print(st.upper())  #BBBAAAAA