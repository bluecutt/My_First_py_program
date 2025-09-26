import random
name_input = input("输入参与人员名单（记到要用英文逗号分隔嘞）：")
name_list = name_input.split(",")
name_list = [name.strip() for name in name_list if name.strip()]
while True:
    draw_num = int(input(f"\n当前共{len(name_list)}个幸运儿，输入中奖人数："))
    if 1 <= draw_num <= len(name_list):
        break
    else:
        print(f"请输入1到{len(name_list)}之间的整数，再乱输入打断你的腿！")
random.shuffle(name_list)
selected = name_list[:draw_num]
print(f"\n=== 恭迎队长登基！！！！ ===")
for i, name in enumerate(selected, 1):
    print(f"{i}. {name}")