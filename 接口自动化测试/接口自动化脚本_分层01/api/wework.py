#程序媛：JY子
import requests
#获取token

class Wework():
    """
    token 的定义
    """
    def get_token(self, corp_id, corp_secret):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": corp_id,
            "corpsecret": corp_secret
        }
        r = requests.get(url=url, params=params)
        return r.json()["access_token "]#获取token

