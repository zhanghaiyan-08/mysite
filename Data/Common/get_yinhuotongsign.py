__author__ = 'Supi'
# @Time    : 2018/9/18 13:52
import time,hashlib
def get_sign(postdata):  # 设置sign参数
    stringsignkey = {
        "api_version": "1.0",
        "sign_type": "MD5",
        "partner_id": "afc3063d10ae438f9f9b878504d88781"
    }
    signkey = "sign_key=blr5k7Pxdn6sWhlN"
    timestamp = "timestamp=" + str(int(round(time.time() * 1000)))
    if postdata == "":
        signvalue = stringsignkey
    else:
        signvalue = dict(stringsignkey, **postdata)  # 连接入参及签名相关参数字典信息
    m = sorted(signvalue.items(), key=lambda d: d[0])  # 对连接后的字典信息进行排序
    m1 = []
    for i in range(len(m)):
        s = m[i][0]
        s1 = m[i][1]
        u = str(s) + "=" + str(s1)
        m1.append(u)
    strsign = "&".join(m1)
    h1 = hashlib.md5()
    h1.update((signkey + "&" + strsign + "&" + timestamp).encode(encoding='utf-8'))
    # print(signkey+"&"+strsign+"&"+timestamp)
    sign = h1.hexdigest().upper()
    return sign