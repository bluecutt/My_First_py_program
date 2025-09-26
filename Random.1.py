import random
def random_draw():
    name_input = input("请输入参与人员名单（英文逗号分隔）：")
    name_list = name_input.split(",")
    name_list = [name.strip() for name in name_list if name.strip()]
    while True:
        try:
            draw_num = int(input(f"\n当前共{len(name_list)}人，请输入要抽取的人数："))
            if 1 <= draw_num <= len(name_list):
                break
            else:
                print(f"请输入1到{len(name_list)}之间的整数！")
        except ValueError:
            print("输入错误，请输入整数！")
    random.shuffle(name_list)
    selected = name_list[:draw_num]
    print(f"\n=== 随机抽取结果 ===")
    for i, name in enumerate(selected, 1):
        print(f"{i}. {name}")
if __name__ == "__main__":
    random_draw()