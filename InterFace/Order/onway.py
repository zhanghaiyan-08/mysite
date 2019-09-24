__author__ = 'Supi'
# @Time    : 2018/9/6 11:11

import Data.Common.request_method  as request_method
import Data.Common.get_url as get_url
import json
HostUrl = get_url.geturl()[0]

class OnwayAPI :

    def PostAllOnWayOrderInfo(self,sessionkey,datavalue):     #获取订单在途信息
        headers = {"Content-Type":"application/json"}
        url = HostUrl+"/ORD/V2_1/PostAllOnWayOrderInfo?sessionkey="+sessionkey
        datavalue = json.dumps(datavalue)
        postallonwayorderinfo = request_method.common_API().postmethod(headers=headers,url=url,data=datavalue)
        return postallonwayorderinfo
