#程序媛：JY子

# class Cat:#定义类首字母需要大写
#     #属性
#      color="orange"
#     # 方法，在类的方法中，是用def定义的
#      def eat(self):
#         print('猫在吃')
# print(Cat.color)#输出属性
# #类的实例化
# cat=Cat()
# cat.eat()#调用方法

#alt+enter快捷键导入
#文件名。路径名，函数名，变量名，类名，不要和内置关键库冲突
from python_test.game import Game


class houyi(Game):

    # 子类的init构造方法覆盖了父类的构造方法
    def __init__(self):
        self.defense = 100
        # 继承父类的构造方法
        super().__init__(1000, 100)

    def defense(self):
        self.my_final_hp = self.my_hp + self.defense - self.empty_power
        self.empty_final_hp = self.empty_hp - self.empty_power
        if self.my_final_hp > self.empty_power:
            print("后羿的最终血量", self.my_final_hp)
            print("后羿赢了")
        elif self.my_final_hp < self.empty_final_hp:
            print("敌人的最终血量", self.my_final_hp)
            print("后羿输了")

        Houyi = houyi(2000, 23)
        Houyi.fight()  # 继承父类所有的方法
        Houyi.defense()