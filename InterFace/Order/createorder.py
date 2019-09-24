__author__ = 'Supi'
# @Time    : 2018/9/5 10:18

import Data.Common.request_method  as request_method
import Data.Common.get_url as get_url
import json
HostUrl = get_url.geturl()[0]

class CreateorderAPI :

    def GetCarrierList(self,sessionkey,sessionID):    #获取已添加的承运人列表（双方均通过）
        url = HostUrl+"/ORG/V2/GetCarrierList"
        params = {"sessionkey":sessionkey}
        headers = {"sessionID":sessionID}
        getcarrierlist = request_method.common_API().getmethod(headers=headers,url=url,params=params)
        return getcarrierlist

    def PostTruckList(self,sessionkey,sessionID,datavalue):     #获取车辆列表
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORG/V2/PostTruckList?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        posttrucklist = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return posttrucklist

    def PostCityData(self,sessionkey,sessionID,datavalue):     #获取城市列表
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/SYS/V2/PostCityData?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        postcitydata = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return postcitydata

    def PostOrderRelationCredit(self,sessionkey,sessionID,datavalue):     #获取新增订单时可授信额度#涉及逻辑比较复杂，暂没有处理
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2/PostOrderRelationCredit?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        postorderrelationcredit = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return postorderrelationcredit

    def PostOrder(self,sessionkey,sessionID,datavalue):     #创建订单
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2_3/PostOrder?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        postorder = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return postorder

    def GetChargeRelationCredit(self,sessionkey,sessionID,OrderID):   #请求额外费用可用授信额度，未完成
        url = HostUrl + "/ORD/V2_1/GetChargeRelationCredit"
        params = {
            "sessionkey": sessionkey,
            "OrderID":OrderID
        }
        headers = {"sessionID":sessionID}
        getchargerelationcredit = request_method.common_API().getmethod(url=url, headers=headers,params=params)
        return getchargerelationcredit

    def PostSetOrderCanceled(self,sessionkey,sessionID,datavalue):     #取消订单
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2/PostSetOrderCanceled?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        postsetordercanceled = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return postsetordercanceled

    def PutOrderReceived(self,sessionkey,sessionID,datavalue):     #web接单
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2/PutOrderReceived?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        putorderreceived = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return putorderreceived

    def PutOrderRefused(self,sessionkey,sessionID,datavalue):     #web拒绝接单
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2/PutOrderRefused?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        putorderrefused = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return putorderrefused

    def PostOrderPreConfirm(self,sessionkey,sessionID,datavalue):     #请求确认到货
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2_2/PostOrderPreConfirm?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        postorderpreconfirm = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return postorderpreconfirm

    def PutOrderConfirmed(self,sessionkey,sessionID,datavalue):     #确认到货
        url = HostUrl+"/ORD/V2_1/PutOrderConfirmed?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        putorderconfirmed = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return putorderconfirmed


    def GetRandomString(self,sessionkey,sessionID):     #获取随机字符串
        url = HostUrl + "/SYS/V2/GetRandomString"
        params = { "sessionkey": sessionkey}
        headers = {"sessionID":sessionID}
        getrandomstring = request_method.common_API().getmethod(url=url,headers=headers,params=params)
        return getrandomstring


    def PostOrderCharge(self,sessionkey,sessionID,datavalue):     #添加额外费用
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2_1/PostOrderCharge?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        postordercharge = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return postordercharge

    def GetOrderInfoQrCode(self,sessionkey,sessionID,datavalue):     #获取待接单的二维码
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2/GetOrderInfoQrCode?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        getorderinfoqrcode = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return getorderinfoqrcode


