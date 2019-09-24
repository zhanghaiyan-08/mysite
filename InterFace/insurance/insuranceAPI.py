#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
__author__ = 'zhanghaiyan'
import Data.Common.request_method as request_method
import json
import requests
import urllib.parse
Hosturl = "https://textapi.scf56.com"
#创建投保订单


#获取一个投保订单的详情
def  postOrderPolicyDetail(sessionkey,sessionID,data):
    url = Hosturl + "/ORD/V2/PostOrderPolicyDetail?sessionkey=" + sessionkey
    headers = {"sessionID": sessionID, "Content-Type": "application/json; charset=utf-8"}
    datavalue = json.dumps(data)
    req = request_method.common_API().postmethod(url=url, data=datavalue, headers=headers)
    return req

#获取投保订单列表
def  postInsurancePolicyList(sessionkey,sessionID,data):
    url = Hosturl + "/ORD/V2/PostInsurancePolicyList?sessionkey=" + sessionkey
    headers = {"sessionID": sessionID, "Content-Type": "application/json; charset=utf-8"}
    datavalue = json.dumps(data)
    req = request_method.common_API().postmethod(url=url, data=datavalue, headers=headers)
    return req


#根据货品种类获取保险种类信息
def  postRiskListByCategoryID(sessionkey,sessionID,data):
    url = Hosturl + "/ORD/V2/PostRiskListByCategoryID?sessionkey=" + sessionkey
    headers = {"sessionID": sessionID, "Content-Type": "application/json; charset=utf-8"}
    datavalue = json.dumps(data)
    req = request_method.common_API().postmethod(url=url, data=datavalue, headers=headers)
    return req


#计算保费
def postInsuranceFee(sessionkey,sessionID,data):
    url = Hosturl + "/ORD/V2/PostInsuranceFee?sessionkey=" + sessionkey
    headers = {"sessionID": sessionID, "Content-Type": "application/json; charset=utf-8"}
    datavalue = json.dumps(data)
    req = request_method.common_API().postmethod(url=url, data=datavalue, headers=headers)
    return req


#添加投保人和被投保人
def postAddOrgProposerAndInsuresd(sessionkey,sessionID,data):
    url = Hosturl + "/ORD/V2/PostAddOrgProposerAndInsuresd?sessionkey=" + sessionkey
    headers = {"sessionID": sessionID, "Content-Type": "application/json; charset=utf-8"}
    datavalue = json.dumps(data)
    req = request_method.common_API().postmethod(url=url, data=datavalue, headers=headers)
    return req



#发运-订单详情
def postOrderDetail(sessionkey,sessionID,data):
    url = Hosturl + "/ORD/V2_6/PostOrderDetail?sessionkey=" + sessionkey
    headers = {"sessionID": sessionID, "Content-Type": "application/json; charset=utf-8"}
    datavalue=json.dumps(data)
    req = request_method.common_API().postmethod(url=url, data=datavalue,headers=headers)
    return req

#发运-订单列表
def postOrderList(sessionkey,sessionID,data):
    url = Hosturl + "/ORD/V2_3/PostOrderList?sessionkey=" + sessionkey
    headers = {"sessionID": sessionID, "Content-Type": "application/json; charset=utf-8"}
    datavalue=json.dumps(data)
    req = request_method.common_API().postmethod(url=url, data=datavalue,headers=headers)
    return req




def postOrgProposerAndInsuresdList(sessionkey,sessionID):
    url=Hosturl+"/ORD/V2/PostOrgProposerAndInsuresdList?sessionkey="+sessionkey
    headers = {"sessionID": sessionID, "Content-Type": "application/json; charset=utf-8"}
    #datavalue = json.dumps(datavalue)
    req = request_method.common_API().postmethod(url=url, headers=headers)
    return req



 #显示符合条件的可投保订单
def postOrderListForPolicy(sessionkey,sessionID,datavalue):
    url = Hosturl+"/ORD/V2/PostOrderListForPolicy?sessionkey="+sessionkey
    headers = {"sessionID":sessionID,"Content-Type": "application/json"}
    #data=bytes(urllib.parse.urlencode(datavalue), encoding='utf8')
    datavalue = json.dumps(datavalue) #用于将 Python 对象编码成 JSON 字符串
    print(datavalue)
    rep = request_method.common_API().postmethod(url=url,data=datavalue ,headers=headers)
    return rep

    #获取可投保订单的信息和货品类型、打包方式
def PostOrderPolicyItems(sessionkey,sessionID,datavalue):
    url = Hosturl+"/ORD/V2/PostOrderPolicyItems?sessionkey="+sessionkey
    headers = {"sessionID": sessionID,"Content-Type":"application/json"}
    datavalue = json.dumps(datavalue)
    req = request_method.common_API().postmethod(url=url,headers=headers,data=datavalue)
    return req