#-*- coding:utf-8 -*-

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from utils.logger import Logger

logger = Logger(logger='SendEmail').get_log()

class SendEmail():

    def send_email(self,to):
        #设置账户和密码
        sender_email = 'amy@mail.com'
        sender_pass = '####'
        logger.info('设置发件邮箱登录账号和密码')
        #设置总的邮件体对象，对象类型为mixed
        msg_root = MIMEMultipart('mixed')
        logger.info('设置总的邮件体对象，对象类型为mixed')
        #邮件添加的头尾信息等
        msg_root['From'] = 'amy@mailcom<amy@mail.com>'
        logger.info('设置发件人的邮箱信息')
        msg_root['To'] = to
        logger.info('设置收件人的邮箱信息')
        #邮件主题，显示在接收邮件的预览页面
        subject = 'python sendmail test successful'
        msg_root['subject'] = Header(subject,'utf-8')
        #构造文本内容
        text_info = 'happy everyday!!'
        text_sub = MIMEText(text_info,'plain','utf-8')
        msg_root.attach(text_sub)
        #构造附件
        html_file = open(r'D:\api\test_report\jetty_report.html','rb').read()
        html = MIMEText(html_file,'base64','utf-8')
        #邮件内容
        html["Content-Type"] = 'application/octet-stream'
        html['Content-Disposition'] = 'attachment;filename="jetty_report.html"'
        msg_root.attach(html)

        #发送邮件
        try:
            sftp_obj = smtplib.SMTP('lsmtp.com',25)
            sftp_obj.login(sender_email,sender_pass)
            sftp_obj.sendmail(sender_email,to,msg_root.as_string())
            sftp_obj.quit()
            print('sendemail successful')
        except Exception as e:
            print('sendemail failed next is the reason')
            print(e)


if __name__ == '__main__':
    to = 'amy@mail.com'
    # to = ['amy23@sfmail.sf-express.com','80004207@sfmail.sf-express.com']
    # to = ''.join(to)
    send = SendEmail()
    send.send_email(to)