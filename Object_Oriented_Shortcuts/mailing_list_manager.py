import smtplib
from email.mime.text import MIMEText
from collections import defaultdict


def send_mail(subject,
            message,
            from_addr,
            *to_addrs,
            host="localhost",
            port=1025,
            headers = None
            ):
    
    if not all([to_addrs,subject,message,from_addr]):
        raise ValueError('Too few args provided')

    headers = headers if headers else {}

    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr,addr, email.as_string())
    sender.quit()

send_mail('nowy temacik','ja@gmail.as','on@tak.sa')
