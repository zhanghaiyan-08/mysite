__author__ = 'Supi'
# @Time    : 2018/8/16 17:16
import requests

class common_API:

    def getmethod(self,url,params='',headers=''):
        requests.packages.urllib3.disable_warnings()#用来解决运行代码时报错：InsecureRequestWarning: Unverified HTTPS requestisbeing made. Adding certificate verificationisstrongly advised.
        response = requests.get(url,params=params,headers=headers,verify=False)
        return response

    def postmethod(self,url,data='',headers=''):
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url,data=data,headers=headers,verify=False)
        return  response
    def deletemethod(self,url,data='',headers=''):
         response = requests.delete(url,data=data,headers=headers,verify=False)
         return  response

