#程序媛：JY子
'''
一个回合制游戏，
每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''
def fight():#定义一个打斗方法
    # 定义四个变量，存放你和我的 血量还有攻击力
    my_hp=100#定义我的血量
    my_power=200#定义我的攻击力
    empty_hp=10#定义敌人的血量
    empty_power=200#定义敌人的攻击力
    my_final_hp=my_hp-empty_power#定义我最后的血量是我的血量减去敌人的攻击力
    empty_final_hp=empty_hp-my_power#定义敌人最后的血量是敌人的血量减去我的攻击力
    print(my_final_hp)#输出我最后的血量
    print(empty_final_hp)#输出敌人最后的血量
    if my_final_hp>empty_final_hp:#做比较，如果我的血量多，我赢
        print("我赢了✌️")
    elif my_final_hp<empty_final_hp:#如果敌人的血量多，我输
        print("你赢了")
    elif my_final_hp==empty_final_hp:#最后平局的场景
        print("平局")
#调用fight函数，才会有返回结果
fight()
