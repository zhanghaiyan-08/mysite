__author__ = 'Supi'
# @Time    : 2018/8/27 16:52
import Data.Common.request_method as request_method
import Data.Common.get_url as get_url
import json
Hosturl = get_url.geturl()[0]

class AddressAPI():
    def PostAddressList(self,sessionkey,sessionID,datavalue):#获取地址列表（启运/目的）
        url = Hosturl+"/ORG/V2/PostAddressList?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        postaddresslist = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return postaddresslist

    def AddAddress(self,sessionkey,sessionID,datavalue): #添加/编辑地址（启运/目的）
        url = Hosturl+"/ORG/V2/AddAddress?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        addaddress = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return addaddress

    def DeletePostress(self,sessionkey,sessionID,datavalue): #删除地址（启运/目的）
        url = Hosturl+"/ORG/V2/DeletePostress?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        deletepostress = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return deletepostress

    def PutDefaultPostress(self,sessionkey,sessionID,datavalue): #设置地址为默认地址（启运/目的）
        url = Hosturl+"/ORG/V2/PutDefaultPostress?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        putdefaultpostress = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return putdefaultpostress


