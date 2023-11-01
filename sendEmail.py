#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = "573561243@qq.com"
receiver = "wangxiouzhong001@163.com" 
smtpserver = "smtp.qq.com"
user = '573561243@qq.com'
password = 'breaqfwfnvtxbfgf'
subject = "python邮件发送功能测试完成"#项目标题
content = "使用Python发送邮件测试案例，接收是否能收到邮件"
msg = MIMEText(content,'plain','utf-8')#发送的文本信息
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = user#这句和下面那句话随便加不加都行。
msg['To'] = receiver
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    print("邮箱发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
