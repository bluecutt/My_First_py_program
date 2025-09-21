# break :中途退出，结束循环
# continue: 结束当前循环，进入下一循环

# i = 1
# if i<=3:
#     print('我在吃烧烤')
#     break
#运行结果:报错，因为break和continue都只能出现在循环内部

# 1. break
A = 1
while A <= 100:
    print(f'罗丰涛吃了{A}个苹果')
    if A == 99:
        print('嗨嗨，吃饱了嗷')
        break  #结束break所在的这个循环
    else:
        print('不够，爷爷我还要吃一千个')
    A += 1

# 2.countinue
# 作用:退出本次循环，下次循环照样执行

B = 1
while B <= 10:
    print(f'徐海我在吃第{B}个苹果')
    if B == 3:
        print('吃到了一条大虫子，不吃这一个了')
        B += 1
        continue  #在continue之前，一定要修改计数器，否则会陷入死循环
    B += 1