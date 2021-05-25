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
    my_hp=1000
    my_power=899
    empty_hp=1000
    empty_power=200
    # 对打多轮，谁的血量先小于等于0，谁就输了
    while True:
        my_hp=my_hp-empty_power
        empty_hp=empty_hp-my_power

        if my_hp<=0:
            # pycharm 快捷键， ctrl+D 可以复制当前行
            print("我的剩余血量️",my_hp)
            print("你的剩余血量",empty_hp)
            print("我输了️")
            break
        elif empty_hp<=0:
            print("我的剩余血量️", my_hp)
            print("你的剩余血量", empty_hp)
            print("你输了")
            break

#调用fight函数
fight()
