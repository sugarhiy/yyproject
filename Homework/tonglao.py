#程序媛：JY子
'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''
class Tonglao():#定义天山童姥类
    # 定义童姥血量和武力值属性（通过传入的参数得到）
    def __init__(self,hp,power):
        self.hp=hp#血量
        self.power=power#武力值
    # 定义童姥see_people的方法 需要传入一个name参数
    def see_people(self,name):
        if name=="WYZ":
            print("师弟")
        elif name=="李秋水":
            print("贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    # 定义一个fight_zms方法（天山折梅手）调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍
    def fight_zms(self,enemy_hp,enemy_power):#需要传入敌人的hp，power
    # 调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍
        self.hp=hp/2
        self.power=power*10
    # 需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
        self.hp=self.hp-enemy_power
        enemy_hp=enemy_hp-self.power
    # 定义一个if判断语句，如果童姥使用折梅手后的血量>敌人的血量则打印“天山童姥赢！”
        if self.hp>enemy_hp:
            print(f"童姥的最终血量是{self.hp}")
            print("天山童姥万岁哈哈哈哈")
        elif self.hp<enemy_hp:
            print(f"敌人的最终血量是{self.hp}")
            print("天山童姥拜拜您嘞")
        else:
            raise Exception("平局结束")

# 童姥实例化,
tonglao =Tonglao(1000,66)
# 传入童姥的血量和武力值参数
hp, power = (1000, 200)
# see_people的方法 传入name参数为“丁春秋”
tonglao.see_people("WYZ")
# 使用折梅手的方法传入敌人的血量和武力值
tonglao.fight_zms(30, 30)



