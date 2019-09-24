__author__ = 'Supi'
# @Time    : 2018/8/24 9:08
import time
import datetime
def getdate(date):    #用于将接口返回日期数据中带T的时间转化为数据库中存储的2018-09-10 00:00:00时间格式
    strdate = date
    if strdate is None:
        return str(strdate)
    else:
        return (strdate[0:10]+" "+strdate[11:19])

def getmoney(money):      #用于将接口的money类数据与数据库中的money数据进行匹配，转化为统一类型
    if money =="" or money is None:
        return money
    else:
        return float(money)

def getnullstring(str1):
    if str1 is None:
        str1 = ""
        return str1
    else:
        return str1




#时间格式
def gettime():
    todaytime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))    #获取当前时间日期并进行格式化
    print(todaytime)

    moreday=(datetime.date.today() + datetime.timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S')   #获取当前时间日期+3天并进行格式化
    print(moreday)
    yesterday = (datetime.date.today() - datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')   #获取当前时间日期-3天并进行格式化
    print(yesterday)
    i = datetime.datetime.now()
    print(i)
    print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.year, i.month,i.day ) )
    print((datetime.date.today() - datetime.timedelta(days=365)).strftime('%Y-%m-%d %H:%M:%S'))



#
# s = None
# s1 =""
# print (str(s))
# import time
# print(int(time.time()))


    # def test_base64(self):
    #     with open('H:\全致科技资料\身份证照片\乐丁科2.jpg','rb') as f:
    #         data = f.read()
    #         encodestr = base64.b64encode(data) # 得到 byte 编码的数据
    #         print(str(encodestr,'utf-8'))  # 重新编码数据








