__author__ = 'Supi'
# @Time    : 2018/9/11 20:12

import Data.Common.environment as environment
def geturl():
    #return "https://prereleaseapi.scf56.com"
    url = environment.enviroment("master")[1]
    jurl = environment.enviroment("master")[3]
    return (url,jurl)
# def getpreurl():
#     return "https://prereleasejqiyun.scf56.com"


def get_sessionkey():
    return "SessionKey4Test_Customer"