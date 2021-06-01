#程序媛：JY子
import json
#字典
dict_test={
    "a":[1,2,3],
    "name":["a","b","c"]
}
#将dict转化为json字符串并存入文件当中,文件名是"data.json",加一个写的权限
#在data.json中传入python object数据
with open("data.json","w") as f:
#def open(file, mode='r'默认是只读权限, buffering=None, encoding=None, errors=None, newline=None, closefd=True): # known special case of open
#def dump(obj：python的对象格式, fp：文件流, *, skipkeys=False, ensure_ascii=True, check_circular=True,

#json.dump表示把python对象写入在文件中
    json.dump(dict_test, f, ensure_ascii=False)

#json.dumps表示把python对象,转化成字符串，dump+string=dumps
print(type(dict_test))
print(type(json.dumps(dict_test)))

#load将json对象转回python对象
json_load=json.load(open("data.json"))
print("使用json_load数据为：",type(json_load))

#loads是将json流转回python对象

