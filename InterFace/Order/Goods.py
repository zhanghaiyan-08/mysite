__author__ = 'Supi'
# @Time    : 2018/8/27 16:52

import Data.Common.request_method as request_method
import Data.Common.get_url as get_url
import json
Hosturl = get_url.geturl()[0]
class GoodsAPI():
    def GetGoodsList(self,sessionkey,sessionID,datavalue):#获取货品列表
        url = Hosturl+"/ORG/V2/GetGoodsList?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        getgoodslist = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return getgoodslist

    def PostGoods(self,sessionkey,sessionID,datavalue):#添加/编辑货品
        url = Hosturl+"/ORG/V2/PostGoods?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        postgoods = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return postgoods

    def DeleteGoods(self,sessionkey,sessionID,datavalue):#删除货品
        url = Hosturl+"/ORG/V2/DeleteGoods?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        deletegoods = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return deletegoods

    def PostImportGoods(self,sessionkey,sessionID,datavalue):#货品导入
        url = Hosturl+"/ORG/V2/PostImportGoods?sessionkey="+sessionkey
        headers = {"sessionID":sessionID,"Content-Type":"application/json"}
        datavalue = json.dumps(datavalue)
        postimportgoods = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return postimportgoods