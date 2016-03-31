import praw
import random
import smtplib, email
from email import encoders
import os 
urls = [];

def get_data_reddit(search):
    eesha = ['politics', 'political', 'fencing', 'juice', 'hilary clinton', 'American University', 'Gilmore Girls', 'puppies', 'foreign relations', 'public policy'];
    sid = ['computer science', 'genetics', 'basketball', 'biology', 'coding', 'hip hop', 'food', 'The Office', 'FIFA', 'math'];
    username="spothecow"
    password="icebluetens"
    r = praw.Reddit(user_agent='Sids script')
    r.login(username,password,disable_warning=True)
    posts=r.search(search, subreddit="news",sort=None, syntax=None,period=None,limit=None)
    title=[]
    for post in posts:
        title.append(post.title)
#	print post.url;
	urls.append(post.url)
    print len(title)


eesha = ['politics', 'political', 'fencing', 'juice', 'hilary clinton', 'American University', 'Gilmore Girls', 'puppies', 'foreign relations', 'public policy'];
sid = ['computer science', 'genetics', 'basketball', 'biology', 'coding', 'hip hop', 'food', 'The Office', 'FIFA', 'math'];
for item in eesha:
	for thing in sid:
		search = item + ' ' + thing  	
		get_data_reddit(search)
		


SMTP_SERVER = 'mail.you-gene.com'
SMTP_PORT = 25
SMTP_USERNAME = 'smurali@you-gene.com'
SMTP_PASSWORD = 'Icebluetens1!'
SMTP_FROM = 'mail.you-gene.com'
SMTP_TO = 'siddharthmurali8@.com'

#TEXT_FILENAME = '/script/output/my_attachment.txt'
MESSAGE = ''
for item in urls:
	MESSAGE = MESSAGE + " " + item; 


# Now construct the message

msg = email.MIMEMultipart.MIMEMultipart()
body = email.MIMEText.MIMEText(MESSAGE)
#attachment = email.MIMEBase.MIMEBase('text', 'plain')
#attachment.set_payload(open(TEXT_FILENAME).read())
#attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(TEXT_FILENAME))
#encoders.encode_base64(attachment)
msg.attach(body)
#msg.attach(attachment)
msg.add_header('From', SMTP_FROM)
msg.add_header('To', SMTP_TO)

# Now send the message
mailer = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# EDIT: mailer is already connected
# mailer.connect()
mailer.login(SMTP_USERNAME, SMTP_PASSWORD)
mailer.sendmail(SMTP_FROM, [SMTP_TO], msg.as_string())
mailer.close()
