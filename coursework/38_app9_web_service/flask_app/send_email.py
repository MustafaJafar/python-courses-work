from email.mime.text import MIMEText
import smtplib

def send_email (email , height , avg_height , count ): 
    from_email = "google email" #Don't forget turnning on "Less secure app access" in gmail settings
    from_password = "password"
    to_email = email 

    subject = "Height Data"
    message = "Hey there , your height is <strong>%s</strong>.<br> The average height is <strong>%s</strong> and that is calculated out of <strong>%s</strong> of pepole. <br>Thanks! " %(height ,avg_height , count)

    msg = MIMEText(message , "html")
    msg['Subject'] = subject  
    msg['To'] = to_email
    msg['From'] = from_email 

    gmail = smtplib.SMTP('smtp.gmail.com' , 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email , from_password)
    gmail.send_message(msg)