__author__ = 'Supi'
# @Time    : 2018/10/9 11:21
def enviroment(enviromentitem):
    if enviromentitem=="master":
        dburl = "qiyundata"
        hosturl = "https://qiyun.scf56.com"
        javahosturl = ""
        dbjavaurl = ""
    elif enviromentitem=="prerelease":
        dburl = "qiyundata_release_test"
        hosturl = "https://prereleaseapi.scf56.com"
        javahosturl = "https://prereleasejqiyun.scf56.com/japi/qiyun"
        dbjavaurl = "qiyundata_v3_release_test"
    elif enviromentitem=="test":
        dburl = "qiyundata_test"
        hosturl = "https://textapi.scf56.com"
        javahosturl = "https://textjqiyun.scf56.com/japi/qiyun"
        dbjavaurl = "qiyundata_v3_java_test"

    return (dburl,hosturl,dbjavaurl,javahosturl)

