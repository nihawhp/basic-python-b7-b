import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

von = "nihawhp@gmail.com"
with open('receiver.txt', 'r') as file:
    zum = file.read().replace('\n', ',')

 
msg = MIMEMultipart()
 
msg['From'] = von
msg['To'] = zum
msg['Subject'] = "Greetings From ALTERSPACE-145GU21"
 
body = "Hi, thank you so much for reading my email. I hope you are in good health and kept away from all bad things. Congratulations on your acceptance to become one of the leaders in the ALTER3675324 project this time. I hope we can work well together."
 
msg.attach(MIMEText(body, 'plain'))

filename = "ThankYOU.jpg"
attachment = open(r'C:\users\asus\Downloads\thankyou.jpg', 'rb')
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(von, "akusayangnihao")
text = msg.as_string()
server.sendmail(von, zum, text)
server.quit()