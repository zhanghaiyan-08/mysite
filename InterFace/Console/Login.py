__author__ = 'Supi'
# @Time    : 2018/9/3 14:37
import Data.Common.request_method as request_method
import Data.Common.get_url as get_url

import json
Hosturl = get_url.geturl()[0]
class LoginAPI():
    def GetRandomStringlogin(self,loginname):  #获取随机字符串
        url = Hosturl+"/SYS/V2/GetRandomString"
        params = {"LoginName":loginname}
        getrandomstringlogin = request_method.common_API().getmethod(url=url,params=params)
        return  getrandomstringlogin

    def PostPCLogin(self,datavalue):   #账号密码登录网页端
        url = Hosturl+"/ORG/V2_2/PostPCLogin"
        headers = {"Content-Type":"application/json"}
        data = json.dumps(datavalue)
        PCLogin = request_method.common_API().postmethod(url=url,data=data,headers=headers)
        return PCLogin

    def PostVerificationLogin(self,datavalue):   #验证码登录网页端
        url = Hosturl+"/ORG/V2_2/PostVerificationLogin"
        headers = {"Content-Type":"application/json"}
        data =json.dumps(datavalue)
        postverificationlogin = request_method.common_API().postmethod(url=url,data=data,headers=headers)
        return postverificationlogin
    #{"Phone":"15070064578","SmsVerifyCode":"9999","CodeType":"login"}

    def PostResetLoginPwd(self,datavalue):   #登录页面忘记密码
        url = Hosturl+"/ORG/V2/PostResetLoginPwd"
        headers = {"Content-Type":"application/json"}
        data = json.dumps(datavalue)
        postresetloginpwd = request_method.common_API().postmethod(url=url,data=data,headers=headers)
        return postresetloginpwd

    def GetUserInfo(self,sessionkey,sessionID):#获取企业用户信息
        url = Hosturl+"/ORG/V2_2/GetUserInfo"
        headers = {"sessionID":sessionID}
        params = {"sessionkey":sessionkey}
        getuserinfo = request_method.common_API().getmethod(url=url,params=params,headers=headers)
        return  getuserinfo


