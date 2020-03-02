#!/usr/bin/python2.7
#coding:utf-8
import smtplib  
from email.mime.text import MIMEText  
from sys import argv
 
mailto_list=[] 
mail_host="smtp.163.com:25" 
mail_user="18081119007@163.com"     
mail_pass="sao5nian"  
#mail_postfix="163.com" 
debug_level=0      
 
def send_mail(to_list,sub,content):  
    me=mail_user
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.set_debuglevel(debug_level)    
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception as e:  
        print('except:',e)  
        return False  
if __name__ == '__main__':
    try:
        mailto_list=argv[1].split(';')
        sub=argv[2]
        content=argv[3]
    except:
        print("python send_mail.py 'user1@xx.com;user2@xx.com' sub content")
        exit()
 
    if send_mail(mailto_list,sub,content):  
        print("send ok")  
    else:  
        print("send fail")

