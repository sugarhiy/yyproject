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
def fight():#定义一个打斗的方法
    my_hp=1000#我的初始血量
    my_power=899#我的初始攻击力
    empty_hp=1000#敌人的初始血量
    empty_power=200#敌人的初始攻击力
    # 对打多轮，谁的血量先小于等于0，谁就输了
    while True:
        my_hp=my_hp-empty_power#我的血量等于我的血量减去敌人的初始攻击力
        empty_hp=empty_hp-my_power#敌人的血量等于敌人的血量减去我的初始攻击力

        if my_hp<=0:#如果我的血量小于0时
            # pycharm 快捷键， ctrl+D 可以复制当前行
            print("我的剩余血量️",my_hp)
            print("你的剩余血量",empty_hp)
            print("我输了️")#输出我输了
            break
        elif empty_hp<=0:#如果敌人的血量小于0时
            print("我的剩余血量️", my_hp)
            print("你的剩余血量", empty_hp)
            print("你输了")#输出敌人你输了
            break

#调用fight函数
fight()
