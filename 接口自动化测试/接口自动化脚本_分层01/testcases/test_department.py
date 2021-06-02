#程序媛：JY子
from wechat_test.api.department import Department
from wechat_test.api.wework import Wework

#实现了接口具体描述，与测试用例解耦了
#测试用例和断言
#以后需要改接口信息，去改对应的接口信息，测试用例无需改动，增加代码可维护性
class Test_department():
    def setup_class(self):
        wework=Wework()#封装不完美，token是不是不需要传递？？token是不需要通过传值的方式
        self.token=wework.get_token()
        self.department=Department()

    def test_create_department(self):
        self.department.create_department(self.token,3)#第一个测试用例
        #不同的步骤需要不同的断言信息
        list=self.department.get_department_list(self.token)
        assert list['department'][1]["name"] == "测试中心"
        assert list["errmsg"] == 'created'
        assert list['errcode'] == 0

    def update_department(self, token, department_id):
        self.department.update_department(self.token)#第二个测试用例
        list=self.department.get_department_list(self.token)
        assert list['department'][1]["name"] == "心心相印"
        assert list['errmsg'] == "updated"

    def delete_department(self, token, department_id):
        self.department.delete_department(self.token,3)#第三个测试用例
        list=self.department.get_department_list(self.token)
        assert len(list()['department']) == 1

    def get_department_list(self):
        self.department.get_department_list(self.token)


#需要增加断言的灵活性和可维护性！！！！！！！！