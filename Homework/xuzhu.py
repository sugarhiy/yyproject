#定义一个XuZhu类，继承于童姥。
from Homework.tonglao import Tonglao

#快捷键导入，Shift+Enter
class Xuzhu(Tonglao):
    def __init__(self):
        pass
    # 虚竹宅心仁厚不打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印”阿弥陀佛，罪过罪过，望各位施主不要以命搏命。“
    def read(self):
         print("我不打架，罪过罪过")


xuzhu=Xuzhu()#实例化虚竹这个类
xuzhu.read()#调用read 方法


print("game over")