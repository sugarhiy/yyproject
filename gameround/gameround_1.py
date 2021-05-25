#程序媛：JY子
'''
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''
def fight():
    # 定义四个变量，存放你和我的 血量还有攻击力
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
