#程序媛：JY子
import requests
#接口描述
class Department:
    def create_department(self,token,department_id):
        create_url =f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}"
        data = {
            "id": department_id,
            "name": "测试中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        # 所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码
        # 所以在传请求体的时候，尽量使用json格式
        r = requests.post(url=create_url, json=data)
        return r.json()

    def update_department(self,token,department_id):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}"
        data = {
            "id": department_id,
            "name": "心心相印",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.post(url=update_url, json=data)
        return r.json()

    def delete_department(self,token,department_id):
        delete_url =f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id={department_id}"
        r = requests.get(url=delete_url)
        return r.json()

    def get_department_list(self,token):
        get_department_list_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}'
        list = requests.get(url=get_department_list_url)
        return list.json()


