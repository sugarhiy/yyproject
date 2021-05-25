#程序媛：JY子

def fight():
    my_hp=100
    my_power=200
    empty_hp=10
    empty_power=200
    my_final_hp=my_hp-empty_power
    empty_final_hp=empty_hp-my_power
    print(my_final_hp)
    print(empty_final_hp)
    if my_final_hp>empty_final_hp:
        print("我赢了✌️")
    elif my_final_hp<empty_final_hp:
        print("你赢了")
    elif my_final_hp==empty_final_hp:
        print("平局")

#调用fight函数
fight()
