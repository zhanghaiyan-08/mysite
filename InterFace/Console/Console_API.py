__author__ = 'Supi'
# @Time    : 2018/8/24 9:38
import Data.Common.request_method  as request_method
import json
import Data.Common.get_url as get_url
import Data.Common.get_userinfo as get_userinfo
Hosturl = get_url.geturl()[0]

class Console_API():



    def GetIntegralInfo(self,sessionkey,sessionID):
        url = Hosturl+"/FNS/V2/GetIntegralInfo"
        headers = {"sessionID":sessionID}
        params = {"sessionkey":sessionkey}
        getintegralinfo = request_method.common_API().getmethod(url=url,headers=headers,params=params)
        return getintegralinfo

    def PostMessageNTopList(self,sessionkey,sessionID,datavalue):
        url = Hosturl+"/MSG/V2/PostMessageNTopList?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        data = json.dumps(datavalue)
        postmessagentoplist = request_method.common_API().postmethod(url=url,headers=headers,data=data)
        return  postmessagentoplist


    def PostOrderFinanceDetail(self,sessionkey,sessionID,datavalue):
        url = Hosturl+"/FNS/V2_2/PostOrderFinanceDetail?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        data = json.dumps(datavalue)
        postorderfinancedetail = request_method.common_API().postmethod(url=url,headers=headers,data=data)
        return  postorderfinancedetail

    def PostTotalMoney(self,sessionkey,sessionID,datavalue):
        url = Hosturl+"/RPT/V2/PostTotalMoney?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        data = json.dumps(datavalue)
        posttotalmoney = request_method.common_API().postmethod(url=url,headers=headers,data=data)
        return  posttotalmoney

    def GetOrderSums(self,sessionkey,sessionID):
        url = Hosturl+"/ORD/V2/GetOrderSums"
        headers = {"sessionID":sessionID}
        params = {"sessionkey":sessionkey}
        getordersums = request_method.common_API().getmethod(url=url,headers=headers,params=params)
        return getordersums

    def GetOrgAuthenticateAndCreditInfo(self,sessionkey,sessionID,datavalue):
        url = Hosturl+"/ORG/V2/GetOrgAuthenticateAndCreditInfo?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        data = json.dumps(datavalue)
        getorgauthenticateAndCreditInfo = request_method.common_API().postmethod(url=url,headers=headers,data=data)
        return  getorgauthenticateAndCreditInfo


    def GetCreditMoneySums(self,sessionkey,sessionID):
        url = Hosturl+"/FNS/V2/GetCreditMoneySums"
        headers = {"sessionID":sessionID}
        params = {"sessionkey":sessionkey}
        getcreditmoneysums = request_method.common_API().getmethod(url=url,headers=headers,params=params)
        return getcreditmoneysums

    def GetTodoNums(self,sessionkey,sessionID):
        url = Hosturl+"/ORG/V2/GetTodoNums"
        headers = {"sessionID":sessionID}
        params = {"sessionkey":sessionkey}
        gettodonums = request_method.common_API().getmethod(url=url,headers=headers,params=params)
        return gettodonums

    def postOrgRelationOrderList(self,sessionID,sessionkey,datavalue):
        url = Hosturl+"/ORG/V2/PostOrgRelationOrderList?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        data = json.dumps(datavalue)
        postOrgRelationOrderList = request_method.common_API().postmethod(url=url,headers=headers,data=data)
        return  postOrgRelationOrderList







#
# items = []
# for i in range(3):
#     item = {}
#     item["index"]=i
#     item["nianji"]=i+1
#     items.append(item)
#     print(items)


