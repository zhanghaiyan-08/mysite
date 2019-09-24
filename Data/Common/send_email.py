__author__ = 'Supi'
# @Time    : 2018/8/16 17:02
import smtplib
from email.header import   Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os

def send_email(newfile):
    #设置邮箱信息（收/发）

    smtpserver = "smtp.qq.com"   #QQ邮箱服务器配置
    user1 = "1009896841@qq.com"
    password1 = "clnulvezmfekbeic"
    sender = "1009896841@qq.com"
    receiver_list = ["1009896841@qq.com"]
    # smtpserver = "smtp.mxhichina.com"   #阿里企业邮箱服务器配置
    # user = "songping@singerdream.com"
    # password = "_sp9410263350616"
    # sender = "songping@singerdream.com"
    # receiver_list = ["2356003194@qq.com","test@singerdream.com","liumaopeng@singerdream.com"]   #

        #邮件主题设置
    msg = MIMEMultipart()
    msg["From"]= "1009896841@qq.com"
    msg["To"]=";".join(receiver_list)
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    subjiect = "自动化测试报告--"+now
    msg["subject"]= Header(subjiect, 'utf-8')

    #邮件正文内容设置
    with  open(newfile,"rb") as file :
        f = file.read()
    mail_body = MIMEText(f,"html","utf-8")
    msg.attach(mail_body)

    #构造附件
    att = MIMEText(open(newfile, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header("Content-Disposition", "attachment", filename=("gbk", "", newfile))#附件名称为中文时写法
    # att["Content-Disposition"] = 'attachment; filename="test.html")'  #附件名称为英文时写法
    msg.attach(att)
    #发送邮件
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(user=user1, password=password1)
        smtp.sendmail(sender, receiver_list, msg.as_string())
        smtp.quit()
        print("发送邮件成功")
    except Exception as e:
        print("发送邮件错误："+e)

def qqemail(path,reportName):
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1009896841@qq.com"  # 用户名
    mail_pass = "ctaolnuzyymdbcjg"  # 口令

    sender = "1009896841@qq.com"
    receivers = ["1009896841@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("测试人员zhy", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = '启运网web端接口自动化测试'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('测试报告见附件', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    mail_path = os.path.join(path, 'report', reportName)  # 获取测试报告路径
    att1 = MIMEText(open(mail_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="测试报告.html"'
    message.attach(att1)
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        # smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")