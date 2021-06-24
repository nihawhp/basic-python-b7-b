from email.mime.nonmultipart import MIMENonMultipart
import smtplib
from email.mime.text import MIMEText
from email.header import Header

von = 'katnis.everdeen@gmail.com'
zum = 'garykasparov@gmail.com'

msg = MIMENonMultipart()
msg['From'] = von
msg['to'] = zum 
msg['Suject'] = "Enfolg beim Programmieren lernen"

body = "Wie wir wissen, ist die Programmierung einer der ersten Schritte, um ein Gebäude wie ein solides Fundament zu starten.  Auch die Technologie wächst und erfordert, dass wir in der Lage sind, die Technologie zu beherrschen und uns mit ihr anzufreunden."
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP ('smpt.gmail.com', 587)
server.starttls
server.login(von, "okinawa92914")
text = msg.as_string()
server.sendmail(von, zum, text)
server.quit()