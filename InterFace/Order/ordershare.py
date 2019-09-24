__author__ = 'Supi'
# @Time    : 2018/10/23 9:40


import Data.Common.request_method as request_method
import Data.Common.get_url as get_url
import json
Hosturl = get_url.geturl()[1]
class OrderShare():

    def GetShareOrderInfo(self,sessionKey,sessionID,shareFrom,shareParam,sharePlatform,shareType):#在途分享-订单分享链接
        url = Hosturl+"/Share/V3/GetShareOrderInfo"
        headers = {"sessionID":sessionID}
        params = {"sessionKey":sessionKey,
                  "shareFrom":shareFrom,
                  "shareParam":shareParam,
                  "sharePlatform":sharePlatform,
                  "shareType":shareType
                  }
        getsharedorderinfo = request_method.common_API().getmethod(url=url,headers=headers,params=params)
        return getsharedorderinfo

    def GetShareInfo(self,sessionKey,sessionID,shareFrom,shareParam,sharePlatform,shareType):#邀请注册
        url = Hosturl+"/Share/V3/GetShareInfo"
        headers = {"sessionID":sessionID}
        params = {"sessionKey":sessionKey,
                  "shareFrom":shareFrom,
                  "shareParam":shareParam,
                  "sharePlatform":sharePlatform,
                  "shareType":shareType
                  }
        getshareinfo = request_method.common_API().getmethod(url=url,headers=headers,params=params)
        return getshareinfo

    def GetOrderInfoByOrderShare(self,orderSerial,code):#在途分享-查询订单获取订单详情
        url = Hosturl+"/Order/V3/GetOrderInfoByOrderShare"
        params = {"orderSerial":orderSerial,
                  "code":code
                  }
        getorderinfobyordershare = request_method.common_API().getmethod(url=url,params=params)
        return getorderinfobyordershare

    def GetShareStatistics(self,sessionKey,sessionID,datavalue):#查询分享数量
        url = Hosturl+"/Share/V3/GetShareStatistics?sessionKey="+sessionKey
        headers = {"sessionID":sessionID}
        datavalue = json.dumps(datavalue)
        getsharestatistics = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
        return getsharestatistics

    def GetSharedOrderInfo(self,orderBillCode,shareCode):#在途分享-订单信息获取接口
        url = Hosturl+"/Share/V3/GetSharedOrderInfo"
        params = {"orderBillCode":orderBillCode,
                  "shareCode":shareCode
                  }
        getsharedorderinfo = request_method.common_API().getmethod(url=url,params=params)
        return getsharedorderinfo




