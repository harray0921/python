#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

mail_host="smtp.qq.com"
mail_user="841668821@qq.com"
mail_pass="jwbzobiglxfrbfge"

sender = '841668821@qq.com'
receivers = ['1325512053@qq.com']

message = MIMEText('Python test','plain','utf-8')
message['Form'] = Header("Erric",'utf-8')
message['To'] = Header('好运','utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject,'utf-8')

try:
    #smtpObj = smtplib.SMTP()
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com",465)
    #smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"


