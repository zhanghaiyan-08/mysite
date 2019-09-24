__author__ = 'Supi'
# @Time    : 2018/9/12 8:51
import Data.Common.request_method as request_method
import Data.Common.get_url as get_url
import json
Hosturl = get_url.geturl()[0]

class RegisterAPI():
    def PostRegister(self,datavalue):
        url = Hosturl+"/ORG/V2/PostRegister"
        headers = {"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        postregister = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return postregister

    def PostORGAuthentication(self,sessionkey,sessionID,datavalue):

        url = Hosturl+"/ORG/V2/PostUserLogo?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        postuserlogo = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return postuserlogo



