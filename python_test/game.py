#程序媛：JY子
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
class Game:
    def __init__(self,my_hp,empty_hp):
    # 定义四个变量，存放你和我的 血量还有攻击力
        self.my_hp=my_hp
        self.my_power=200
        self.empty_hp=empty_hp
        self.empty_power=200
    # 快捷键 ，往前缩进是tab + shift ，往后缩进是tab
    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.empty_hp  # 我的血量等于我的血量减去敌人的初始攻击力
            self.empty_hp = self.empty_hp - self.my_power  # 敌人的血量等于敌人的血量减去我的初始攻击力
            if self.my_hp <= 0:  # 如果我的血量小于0时
                # pycharm 快捷键， ctrl+D 可以复制当前行
                print("我的剩余血量️", self.my_hp)
                print("你的剩余血量", self.empty_hp)
                print("我输了️")  # 输出我输了
                break
            elif self.empty_hp <= 0:  # 如果敌人的血量小于0时
                print("我的剩余血量️", self.my_hp)
                print("你的剩余血量", self.empty_hp)
                print("你输了")  # 输出敌人你输了
                break

class houyi(Game):

        #子类的init构造方法覆盖了父类的构造方法
        def __init__(self):
            self.defense=100
            #继承父类的构造方法
            super().__init__(1000,100)
        def defense(self):
            self.my_final_hp=self.my_hp+self.defense-self.empty_power
            self.empty_final_hp=self.empty_hp-self.empty_power
            if self.my_final_hp>self.empty_power:
                print("后羿的最终血量",self.my_final_hp)
                print("后羿赢了")
            elif self.my_final_hp<self.empty_final_hp:
                print("敌人的最终血量", self.my_final_hp)
                print("后羿输了")

            Houyi = houyi(2000, 23)
            Houyi.fight()  # 继承父类所有的方法
            Houyi.defense()


#调用fight函数
game=Game(1300,899)
game.fight()
# game.defense(1)