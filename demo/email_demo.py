import os
import smtplib
import email
from email.mime.text import MIMEText
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

email_host = 'smtp.qq.com'     # 发送者邮箱服务器
email_user = '503160268@qq.com'  # 发送者账号
email_pwd = 'ivbkmhhzfwghbgih'       # 发送者密码(smtp授权码)

def sendmail(maillist, subject, content, attach_files=None):
    
    # 构造MIMEMultipart对象做为根容器  
    main_msg = MIMEMultipart()  

    # 构造MIMEText对象做为邮件显示内容并附加到根容器 
    text_msg = MIMEText(content, 'html', 'utf-8')    # 邮件内容
    main_msg.attach(text_msg)

    if None!=attach_files and len(attach_files)>0:
        # 构造MIMEBase对象做为文件附件内容并附加到根容器  
        contype = 'application/octet-stream'  
        maintype, subtype = contype.split('/', 1)  
        for file_name in attach_files:
            ## 读入文件内容并格式化 [方式2]－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－ 
            with open(file_name, 'rb') as f:
                file_msg = MIMEBase(maintype, subtype)  
                file_msg.set_payload(f.read())  
                email.encoders.encode_base64(file_msg)#把附件编码  
            #－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－  
            ## 设置附件头  
            basename = os.path.basename(file_name)  
            file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头  
            main_msg.attach(file_msg)  

    # 设置根容器属性  
    main_msg['From'] = email_user  
    main_msg['To'] = ','.join(maillist)  
    main_msg['Subject'] = subject
    main_msg['Date'] = email.utils.formatdate( )  

    # smtp = smtplib.SMTP(email_host) # port默认为25
    smtp = smtplib.SMTP_SSL(email_host, 465)
    smtp.login(email_user, email_pwd)
    smtp.sendmail(email_user, maillist, main_msg.as_string())
    smtp.quit() 

# maillist = ['haibo.wang@yulore.com']    # 接收者账号
maillist = ['haibo.wang@yulore.com']    # 接收者账号
# sendmail(maillist, '主题', '内容')
attach_files = []
attach_files.append('C:\\Users\\Li Yujie\\Desktop\\tel_20170816.count')
attach_files.append('C:\\Users\\Li Yujie\\Desktop\\tel_20170816.localtel')
sendmail(maillist, '主题', '内容', attach_files)
