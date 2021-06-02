import requests
#断言是否考虑业务逻辑校验，取决于公司要求
# 这个脚本的缺点：对每个接口的正常返回值都需要校验，单接口校验健壮性不够，重复代码过多，暴露过多接口信息，断言信息和token耦合了，维护性差
#减少重复代码，用例和接口描述拆分开，设计模式是：po,api object,，PO分了三层，实现思路
#创建，更新，删除部门
#先定义一个类
class TestDepartment:
    #定义一个方法
    def setup(self):
        ID = "ww28c4ec9233bfdb57"
        SECRET = "CUnTkJ-8JNi7IExwePXFSHsKTBVA7EObJDkoswwyd6Y"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        #字典
        params={
            "corpid" :ID,
            "corpsecret" :SECRET
        }
        r=requests.get(url=url, params=params)
        #这里获取的token将来会在各处调用，所以加self
        # print(r.json())
        self.token=r.json()["access_token"]
        self.id=2

    def test_create(self):
        create_url=f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data={
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": self.id
        }
        r=requests.post(url=create_url,json=data)
        print(r.json())
        #获取部门列表接口,获取部门列表信息
        get_list_url=f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list=requests.get(url=get_list_url)
        #通过查询部门列表接口的返回值，实现查看部门是否创建成功
        assert list.json()["errmsg"]=='created'
        assert list.json()['errcode']==0

    def test_update(self):
        update_url=f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data={
                "id": self.id,
                "name": "研发中心",
                "name_en": "GZ",
                "parentid": 1,
                "order": 1
            }
        r=requests.post(url=update_url,json=data)
        print(r.json())
        #获取部门列表
        get_list_url=f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list=requests.get(url=get_list_url)
        assert list.json()["errcode"]==0
        assert list.json()["errmsg"]=="updated"

    def test_delete(self):
        delete_url=f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}"
        r=requests.get(url=delete_url)
        print(r.json())
        #获取部门列表
        get_list_url=f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list=requests.get(url=get_list_url)
        assert len(list.json())["department"]==1



if __name__ == '__main__':
    test_department = TestDepartment()  # 实例化一个对象
    test_department.setup()  # 调用方法
    test_department.test_create()
    test_department.test_update()
    test_department.test_delete()
