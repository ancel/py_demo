
import smtplib

from email.mime.text import MIMEText
from email.header import Header


def sendmail(maillist, subject, content):
    email_host = 'smtp.qq.com'     # 发送者邮箱服务器
    email_user = '503160268@qq.com'  # 发送者账号
    email_pwd = 'ivbkmhhzfwghbgih'       # 发送者密码(smtp授权码)

    msg = MIMEText(content, 'html', 'utf-8')    # 邮件内容
    msg['Subject'] = subject    # 邮件主题
    msg['From'] = email_user    # 发送者账号
    msg['To'] = ','.join(maillist)    # 接收者账号

    # smtp = smtplib.SMTP(email_host) # port默认为25
    smtp = smtplib.SMTP_SSL(email_host, 465)
    smtp.login(email_user, email_pwd)   # 发送者的邮箱账号，密码
    smtp.sendmail(email_user, maillist, msg.as_string()) # 参数分别是发送者，接收者，邮件内容
    smtp.quit() 
    print ('email send success.')

maillist = ['haibo.wang@yulore.com']    # 接收者账号
sendmail(maillist, '主题', '内容')
