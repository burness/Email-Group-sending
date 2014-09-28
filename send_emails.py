from sender import Mail
import time

# in email_server_config.txt, you enter your email information in this format: smtp.example.com,25,username,password

with open('./email_server_config.txt','r') as f:
	config_content=[]
	for line in f.readlines():
		config_content=line.split(",")
		smtp_server=config_content[0]
		smtp_server_port=config_content[1]
		smtp_server_username=config_content[2]
		smtp_server_password=config_content[3]
		mail=Mail(smtp_server,port=smtp_server_port,username=smtp_server_username,password=smtp_server_password,\
			use_tls=False,use_ssl=False,debug_level=None)

from sender import Message
with open('./to_email_list.txt','r') as f:
	for line in f.readlines():
		msg=Message("email subject",fromaddr=("burness","dss_1990@sina.com"),to=line)
		msg.body = "this is a msg plain text body"
		msg.date = time.time()
		msg.charset = "utf-8"
		msg.extra_headers = {}
		msg.mail_options = []
		msg.rcpt_options = []
		from sender import Attachment
		with open("to_email_list.txt") as f:
			attachment=Attachment("to_email_list.txt","text/txt",f.read())
		msg.attach(attachment)
		mail.send(msg)

print 'To check in your email that ensure it is ok'