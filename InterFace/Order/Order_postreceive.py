__author__ = 'Supi'
# @Time    : 2018/8/22 17:22

import Data.Common.request_method  as request_method
import Data.Common.get_url as get_url
import json
HostUrl = get_url.geturl()[0]

class Order_postreceive :
    def GetOrderNums(self,sessionkey,sessionID,OrderType):
        url = HostUrl+"/ORD/v2/GetOrderNums"
        params = {
            "sessionkey":sessionkey,
            "OrderType":OrderType
        }
        headers = {"sessionID":sessionID}
        getordernums = request_method.common_API().getmethod(url=url,headers=headers,params=params)
        return getordernums

    def PostOrderList(self,sessionkey,sessionID,datavalue):
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2/PostOrderList?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        postorderlist = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return postorderlist

    def PostOrderDetail(self,sessionkey,sessionID,datavalue):
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2_3/PostOrderDetail?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        postorderdetail = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return postorderdetail

    def PostCityData(self,sessionkey,sessionID,datavalue):
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/SYS/V2/PostCityData?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        postcitydata = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return postcitydata

    def GetChargeRelationCredit(self,sessionkey,sessionID,OrderID):
        url = HostUrl+"/ORD/V2_1/GetChargeRelationCredit"
        params = {
            "sessionkey":sessionkey,
            "OrderID":OrderID}
        headers = {"sessionID":sessionID}
        getchargerelationcredit = request_method.common_API().getmethod(url=url,headers=headers,params=params)
        return getchargerelationcredit