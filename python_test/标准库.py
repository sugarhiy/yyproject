#程序媛：JY子

#os模块
# import os  #python环境自带的模块
# # os.mkdir("testdir")#创建一个目录
# import time
#
# print(os.listdir("./"))#目录下有哪些文件和目录
# # os.removedirs("testdir")#删除这个目录
# print(os.getcwd)#打印出当前的绝对路径
#
# os.path.exists("b")#判断当前路径下是否有该文件夹
# if not os.path.exists("b"):
#         os.mkdir("b")
# if not os.path.exists("b/test.txt"):#判断文件夹中有没有这个文本文件
#         f=open("b/test.txt","w")#如果不存在该文件，则打开这个文件，并且开启写的模式,可读可写可修改可编辑
#         f.write("hello,os using")#写文件的内容
#         f.close()  #调用os中的close的方法区关闭这个文件
#
#
# # os.mkdir('test')
# os.removedirs('test')
# print(os.listdir("./"))
# print(os.getcwd())
# os.path.exists('a')
# if not os.path.exists('a'):
#         os.mkdir('a')
# if not os.path.exists('a/test.text'):
#         f=open('a/test.txt','w')
#         f.write('zaoshanghaoachangsha de ')
#         f.close()

#time 模块
# import time
# # print(time.strftime())
# # print(time.time())
# # print(time.localtime())
# # time.strftime()#command+右键进入方法体内
# # #时间戳转化为日期的格式
# # #获取两天现在的时间
# # now_timestamp=time.time()
# # two_days_before=now_timestamp-60*60*24*2#当前的秒数-两天的秒数
# # time_tuple=time.localtime(two_days_before)
# # print(time.strftime("",time_tuple))

#urllib库
import urllib .request
response=urllib.request.urlopen("http://www.baidu.com")
print(response.status)
print(response.read())#去URL中请求的返回值

#math模块
import math
math.acos('100')
math.ceil('5.5')
