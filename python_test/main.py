# # 程序媛：JY子
# import logging
# from time import sleep, ctime#在一个库中导入多个模块加逗号继续添加就好了
#
# # 加日志,对logging做基本的初始化
# logging.basicConfig(level=logging.INFO)#配置基本参数，日志级别
#
#
# #两个sleep进行简答的打印
# def loop0():
#     logging.info("start loop0 at"+ctime())#ctime是当前时间，python自带的时间函数
#     sleep(4)
#     logging.info("start loop0 at"+ctime())#打印日志，结束时间
#
# def loop1():
#     logging.info("start loop0 at"+ctime())#ctime是当前时间，python自带的时间函数
#     sleep(2)
#     logging.info("start loop0 at"+ctime())#打印日志，结束时间
#
# def main():
#     logging.info("start all at"+ctime())
#     loop0()
#     loop1()#调用函数
#     logging.info("end all at"+ctime())#日志输出

#--------多线程优化，/thread

# 程序媛：JY子
# import _thread
# import logging
# from time import sleep, ctime#在一个库中导入多个模块加逗号继续添加就好了
#
# # 加日志,对logging做基本的初始化
# logging.basicConfig(level=logging.INFO)#配置基本参数，日志级别
#
#
# #两个sleep进行简答的打印
# def loop0():
#     logging.info("start loop0 at"+ctime())#ctime是当前时间，python自带的时间函数
#     sleep(4)
#     logging.info("start loop0 at"+ctime())#打印日志，结束时间
#
# def loop1():
#     logging.info("start loop0 at"+ctime())#ctime是当前时间，python自带的时间函数
#     sleep(2)
#     logging.info("start loop0 at"+ctime())#打印日志，结束时间
#
# def main():
#     logging.info("start all at"+ctime())
#     _thread.start_new_thread(loop0())
#     _thread.start_new_thread(loop1())#调用函数,主线程退出的时候，其他线程全部杀掉，没有守护线程的概念
#     sleep(6)
#     logging.info("end all at"+ctime())#日志输出

#--------优化

import _thread
import logging
from time import sleep, ctime#在一个库中导入多个模块加逗号继续添加就好了

# 加日志,对logging做基本的初始化
logging.basicConfig(level=logging.INFO)#配置基本参数，日志级别


#两个sleep进行简单的打印
loops=[2,4]
def loop(nloop,nsec,lock):#传递nloop参数，用于标示当前loop是第几个；传递nsec参数，展示loop循环时间，lock是锁的概念
    logging.info("start loop0 at"+ctime())#ctime是当前时间，python自带的时间函数
    sleep(nsec)#sleep 改为动态时间
    logging.info("start loop0 at"+ctime())#打印日志，结束时间
    lock.release()#所有loop执行结束，进行解锁操作，锁的概念是让主线程判断是不是结束，释放锁，release是_thread自带的方法



def main():
    logging.info("start all at"+ctime())
    locks=[]#申明一个锁的list,包含所有的锁，main函数会对所有的锁进行频繁检测 ，当locks所有的锁释放后，main就退出
    nloops=range(len())#算出loop值
    #取出nloops中每一个值
    for i in loops:
        lock=_thread.allocate_lock()
        lock.acquire()
    _thread.start_new_thread(loop())
    _thread.start_new_thread(loop())#调用函数,主线程退出的时候，其他线程全部杀掉，没有守护线程的概念
    sleep(6)
    logging.info("end all at"+ctime())#日志输出