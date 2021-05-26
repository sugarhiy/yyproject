class Bicycle:
    def run(self,km):
        print(f"一共骑行了多少{km}km")

class EBicycle(Bicycle):
    def __init__(self,valume):
        self.valume = valume

    def fill_charge(self, vol):
        print(f"电动车已充电{vol}度")
        print(f"充完电之后还有{vol + self.valume}度")

    def run(self,km):
         e_km=self.valume*10
         print(f"电动车骑到的最大公里数是{e_km}公里")
         #当我们要骑的公里数大于最大能骑的公里数，
         if e_km-km<=0:
                print(f"用电一共骑行了{e_km}公里")
         else:
                print(f"用脚一共骑了{km-e_km}公里")

ebike=EBicycle(10000)
ebike.run(1)