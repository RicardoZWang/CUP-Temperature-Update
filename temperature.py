#-*- coding:gb2312 -*-
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

url = 'https://reserve.25team.com/wxappv1/yi/addReport'
token = '&���Լ��� token'

headers = {
    'Host': 'reserve.25team.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/json',
    'token': token ,
    'Referer': 'https://servicewechat.com/wxd2bebfc67ee4a7eb/83/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br',
}

post_data = {"content":{"0":"�ھ���У-����ס��","1":"&���Լ�������¥","2":"","3":"","4":"","5":"","6":"&��ϸ��ַ","7":"��","8":"37.3��C����","9":"����","10":"��","11":"","12":"","13":"��","14":"","15":"��","16":"������","17":"��","18":"��","19":"","20":"","21":"��","22":"��","23":"��","24":"��","25":"&��Ľ��ֵ�һ��ʱ��","26":"","27":"��","28":"&��Ľ��ֵڶ���ʱ��","29":"","30":"��","31":"&��ĵ��������ʱ��","32":"","33":"","34":""},"version":20,"stat_content":{},"location":{"country":"�й�","province":"������","city":"������","longitude":"","latitude":""},"sick":"","accept_templateid":""}

info = post_data

r = requests.post(url, headers=headers, data=json.dumps(post_data),verify=False)
print(r)
if r.status_code == 200:
    r_json = r.json()
    print(r_json)
    my_sender='&��� QQ �����ַ'    # �����������˺�
    my_pass = '&��� QQ ������Ȩ��'              # ��������������
    my_user='����ռ������ַ'      # �ռ��������˺ţ�����߷��͸��Լ�
    def mail():
        ret=True
        try:
            msg=MIMEText('��д�ʼ�����','plain','utf-8')
            msg['From']=formataddr(["&�������ǳ�",my_sender])  # ������Ķ�Ӧ�����������ǳơ������������˺�
            msg['To']=formataddr(["&�ռ����ǳ�",my_user])              # ������Ķ�Ӧ�ռ��������ǳơ��ռ��������˺�
            msg['Subject']="���¶��ˣ�"                # �ʼ������⣬Ҳ����˵�Ǳ���
     
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # �����������е�SMTP���������˿���25
            server.login(my_sender, my_pass)  # �����ж�Ӧ���Ƿ����������˺š���������
            server.sendmail(my_sender,[my_user,],msg.as_string())  # �����ж�Ӧ���Ƿ����������˺š��ռ��������˺š������ʼ�
            server.quit()  # �ر�����
        except Exception:  # ��� try �е����û��ִ�У����ִ������� ret=False
            ret=False
        return ret
     
    ret=mail()
    if ret:
        print("�ʼ����ͳɹ�")
    else:
        print("�ʼ�����ʧ��")