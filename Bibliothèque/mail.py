import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText



def envoieEmail():
#Envoie un email au personnel de securite du musee
        msg = MIMEMultipart()
        msg['From'] = 'protectart34@gmail.com'
        msg['To'] = 'securite.musee34@gmail.com'
        msg['Subject'] = 'Detection d une personne'
        message = 'Probleme de securite : la presence d une personne a ete detecte pres de votre oeuvre d art. '
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('protectart34@gmail.com', 'fastoche')
        mailserver.sendmail('protectart34@gmail.com', 'securite.musee34@gmail.com', msg.as_string())
        mailserver.quit()

envoieEmail() 
