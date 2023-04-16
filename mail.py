import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import yaml
import sys

if not os.path.exists("config.yaml"):
    print("您并没有config.yaml，请按照GitHub仓库中的README进行设置！")
    exit()
with open('config.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)['mail']
print(data)
print(sys.argv)

if len(sys.argv) == 1:
    print("缺少主播ID arg或者文件路径arg，请按照GitHub仓库中的README进行运行！")
    exit()
Streamer = sys.argv[1]
FILE_PATH = sys.argv[2]

# 第三方 SMTP 服务
mail_host = data['mail_host']  # SMTP服务器
mail_user = data['mail_user']  # 用户名
mail_pass = data['mail_pass']  # 授权密码，非登录密码

sender = data['sender']  # 发件人邮箱(最好写全, 不然会失败)
receivers = data['receivers']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


def sendEmail(title, content):
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


if __name__ == '__main__':
    seed_content = f'{Streamer}有一个直播录像已完成，还请注意！<br>文件路径为：{FILE_PATH}'
    seed_title = f'{Streamer}有一个直播录像已完成！'  # 邮件主题
    sendEmail(seed_title, seed_content)
