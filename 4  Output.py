#*values值，表一次性输出多个对象。输出多个值或者多句话时候，需要用”，“隔开
#如
print("HAHAHA","HEHEHE","BIBIBI")
#运行结果为  HAHAHA HEHEHE BIBIBI

#sep用来间隔多个对象，默认值是一个空格
#如
print("HAHAHA","HEHEHE","BIBIBI")
#运行结果为  HAHAHA HEHEHE BIBIBI
#如果添加了sep函数，则为
print("HAHAHA","HEHEHE","BIBIBI",sep='/')
#运行结果为  HAHAHA/HEHEHE/BIBIBI
#sep要设置在内容的后面

#end用来设定以...结尾，默认值是换行符，可以切换成其他字符串
#如
print("hello world")
print("sky")
'''运行结果为   hello world
              sky'''
print("hello world",end='//')
print("sky")
#运行结果为    hello world//sky
