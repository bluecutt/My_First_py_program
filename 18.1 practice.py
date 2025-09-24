# 用户输入昵称，昵称重复则不能使用
Name_list = ['徐海','杨斐然','罗丰涛','罗春兴']
while True:
    User_name = input('请输入用户名称:')
    if User_name in Name_list:
            print('该名称不可用')

    else:
        Name_list.append(User_name)
        print('储存成功!!!')
        print('您的名称为:%s'%User_name)
        break