#程序媛：JY子

def fight():
    my_hp=1000
    my_power=899
    empty_hp=1000
    empty_power=200
#对打多伦，谁血量少谁输
    while True:
        my_hp=my_hp-empty_power
        empty_hp=empty_hp-my_power

        if my_hp<=0:
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
