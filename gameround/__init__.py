class Bicycle():
    def run(self,km):
        print(f"我骑行了{km}km")

class EBicycle(Bicycle):#继承Bicycle
        def __init__(self,valume):
           self.valume=valume
        def fillcharge(self,vol):
            print(f"一共充了{vol}电量")
        def run(self,km):
            # 每骑行10km消耗1度电
            # 当电量耗尽时调用Bicycle的run方法骑行，通过传入骑行里程数，显示骑行结果
            # 有电的时候能骑到的公里数
            e_km=self.valume*10#骑行的最大公里数
            print(f"电动车骑到的最大公里数是{e_km}公里")
            if e_km-km>0:
                print(f"骑行了{km}km")
            else:
                print(f"用脚骑了{km-e_km}km")
                raise Exception("获取数据失败")
                # 实例化类，并且调用方法
                bike = Bicycle()
                # 实例化后的对象调用方法时，才传入参数
                bike.run(km-e_km)






ebike=EBicycle(1000)
ebike.run(100)
