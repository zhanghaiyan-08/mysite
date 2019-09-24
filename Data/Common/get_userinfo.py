__author__ = 'Supi'
# @Time    : 2018/9/12 9:24
import Data.Common.request_method as request_method
from InterFace.Console.Login import LoginAPI as LoginAPI
import Data.Common.get_url as get_url
import time,hashlib
import Data.Common.connectSQL as connectSQL
import Data.Common.environment as environment
Hosturl = get_url.geturl()[0]


#用于获取登陆的sessionkey和sessionID和orgid
def getuserinfo():
    LoginName = "cjwl2"
    pwd = "123456"
    opensql = connectSQL.open_MySQL()
    #phone = connectSQL.get_MySQLselect("select phone from sys_user where LoginName like '%s'" % LoginName)[0][0]
    #m1  = hashlib.md5()
    #m1.update(str(pwd).encode(encoding='utf-8'))    #对excel文档中pwd进行MD5编码
    #pwd_1 = m1.hexdigest().lower()
    #datavalue2 = {
    #                    "Phone":phone,
    #                   "VerificationCode":"9999",
    #                   "NewPassWord":pwd_1,
    #                   "codeType":"resetPwd"}
    #resetloginpwd = LoginAPI().PostResetLoginPwd(datavalue2)
    #assert resetloginpwd.status_code ==200
    login_randomstring1 = LoginAPI().GetRandomStringlogin(LoginName).json()["code"]
    m1_1  = hashlib.md5()
    m1_1.update(str(123456).encode(encoding='utf-8'))    #对初始密码进行MD5加密
    pwd_1_1 = m1_1.hexdigest().lower()
    m2_1 = hashlib.md5()
    m2_1.update(str(pwd_1_1+login_randomstring1).encode(encoding='utf-8'))    #MD5（MD5（密码）拼接code)
    pwd_2_1 = m2_1.hexdigest().lower()
    datavalue1 ={"IsApp":0,
                "LoginName":LoginName,
                "Pwd":pwd_2_1,
                "Ticket":""}
    postpclogincorrect = LoginAPI().PostPCLogin(datavalue=datavalue1)
    assert postpclogincorrect.status_code ==200, "登录接口状态码返回为："+str(postpclogincorrect.status_code)
    assert postpclogincorrect.json()["error"]["ErrorCode"] == 0,"PostPCLogin接口返回的ErrorCode：%s "%(str(postpclogincorrect.json()["error"]["ErrorCode"]))

    sessionkey = postpclogincorrect.json()["SessionKey"]
    sessionID = postpclogincorrect.json()["SessionID"]
    getinfo = LoginAPI().GetUserInfo(sessionkey,sessionID)
    ORGID=getinfo.json()["userInfo"]["ORGID"]
    userid = getinfo.json()["userInfo"]["UserID"]
    dbjavaurl = environment.enviroment("test")[2]
    closesql = connectSQL.close_MySQL()
    return (sessionkey,sessionID, ORGID , userid,dbjavaurl)

def getOneuserinfo(LoginName,pwd):
    opensql = connectSQL.open_MySQL()
    login_randomstring1 = LoginAPI().GetRandomStringlogin(LoginName).json()["code"]
    m1_1  = hashlib.md5()
    m1_1.update(str(123456).encode(encoding='utf-8'))    #对初始密码进行MD5加密
    pwd_1_1 = m1_1.hexdigest().lower()
    m2_1 = hashlib.md5()
    m2_1.update(str(pwd_1_1+login_randomstring1).encode(encoding='utf-8'))    #MD5（MD5（密码）拼接code)
    pwd_2_1 = m2_1.hexdigest().lower()
    datavalue1 ={"IsApp":0,
                "LoginName":LoginName,
                "Pwd":pwd_2_1,
                "Ticket":""}
    postpclogincorrect = LoginAPI().PostPCLogin(datavalue=datavalue1)
    assert postpclogincorrect.status_code ==200, "登录接口状态码返回为："+str(postpclogincorrect.status_code)
    assert postpclogincorrect.json()["error"]["ErrorCode"] == 0,"PostPCLogin接口返回的ErrorCode为：%s"%(str(postpclogincorrect.json()["error"]["ErrorCode"]))

    sessionkey = postpclogincorrect.json()["SessionKey"]
    sessionID = postpclogincorrect.json()["SessionID"]
    getinfo = LoginAPI().GetUserInfo(sessionkey,sessionID)
    ORGID=getinfo.json()["userInfo"]["ORGID"]
    userid = getinfo.json()["userInfo"]["UserID"]
    orgrole=getinfo.json()["userInfo"]["ORGRole"]
    dbjavaurl = environment.enviroment("test")[2]

    return (sessionkey,sessionID, ORGID , userid,orgrole,dbjavaurl)




s = getuserinfo()