import smtplib

print('{:->59}'.format('-'))
print('{:-^59}'.format("<Hi welcome to straightlearn auto send email>"))
print('{:->59}'.format('-'))
print("[1]Send an email:",'{:^59}'.format('[2]About us:'))

sender_email=input('input your email here:\n ')
rec_email=input('input your receiver email:\n ')
messege=input("type message you want to send:\n")
passwd=input("put your email password to send mail:\n")
server=smtplib.SMTP("smtp.gmail.com",587)

#To start connection
server.starttls()
server.login(sender_email,passwd)
print('login success')
server.sendemail(sender_email,rec_email,message)
print('Your email have been sent.')
