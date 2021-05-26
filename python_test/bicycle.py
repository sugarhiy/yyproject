"""
写一个Bicycle(自行车)类,有run(骑行)方法, 调用时显示骑行里程km(骑行里程为传入的数字):
再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性通过，参数传入,
同时有两个方法：
1. fill_charge(vol) 用来充电, vol 为电量
2. run(km) 方法用于骑行,每骑行10km消耗电量1度,
当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""
class Bicycle:
    def run(self,km):#km是个变量
        #字面量插值传入km参数
        print(f"一共骑行了多少{km}km")

#写一个电动自行车的类EBicycle继承Bicycle的类，括号里是父类
class EBicycle(Bicycle):#类的参数不是在定义类的时候去写，是在构造函数中去写
    #构造函数
    def __init__(self,valume):
        #电池电量是valume，
        # 构造方法中定义了参数，在实例化类时的时候需要传参
        self.valume = valume
        #valume想在整个类（作用域）中起作用的话，需要加self，
        #类属性：特征：类体内，在方法之外
        #实例属性：特征：类体中，方法内，并且以self.变量名的方式定义的变量
        #普通属性：类体中，方法内 ；局部变量：不加self的，特征：只在当前的方法内有用

    def fill_charge(self, vol):
        print(f"电动车已充电{vol}度")
        print(f"充完电之后还有{vol + self.valume}度")


    def run(self,km):
         #每骑行10km消耗1度电
         #当电量耗尽时调用Bicycle的run方法骑行，通过传入骑行里程数，显示骑行结果
         # 有电的时候能骑到的公里数
         e_km=self.valume * 10
         print(f"电动车骑到的最大公里数是{e_km}公里")
         #当我们要骑的公里数大于最大能骑的公里数，
         if e_km-km<=0:
                print(f"用电一共骑行了{e_km}公里")
         else:
                print(f"用脚一共骑了{km-e_km}公里")

                # 调用父类的方法，知识点
                # 第一种调用父类的方法，和普通实例化类，调用方法相同
                bike = Bicycle()
                bike.run(km - e_km)
                # # 第二种调用父类的方法
                super().run(km - e_km)

#继承之后子类可以继承父类的属性和方法
Ebike=EBicycle(100)
#实例化类
# 当子类中有和父类重名的方法或者属性，那么首先选择的是子类
Ebike.run(10)
#调用父类的方法
# Ebike.fill_charge(10)
# Bicycle()#实例化类要加括号
# bike=Bicycle()#bike变量来存放实例化后的实例对象
# bike.run(200)#对象可以调用方法，并且传值



