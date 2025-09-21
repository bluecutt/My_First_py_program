# 字符串str
# 特点： 需要加上引号，单引号和多引号都可以，包含了多行内容的时候可以使用三引号
name = world # 报错，没有引号识别为变量名，world没有被赋值
#若为：
name = "world" # 或者name = 'world'  name = """world"""  都一样
print(name)  #不报错，结果为 world



