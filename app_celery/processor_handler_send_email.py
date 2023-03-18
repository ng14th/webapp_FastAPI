import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.config import settings
from datetime import datetime
from app.core.database.rabbitmq_kombu import RabbitMQ
import asyncio
import logging

logger = logging.getLogger(f'{__name__}')

loop = asyncio.get_event_loop()

connection = RabbitMQ()

class SendEmailNotiPasswordExp():
    def __init__(self) -> None:
        self.emails_sent_in_day = {}
        
    def send_email(self,body, **kwargs):
        try:
            for data in body:
                email = data.get('email')
                if self.emails_sent_in_day and email in self.emails_sent_in_day.get(datetime.utcnow().date()):
                    logger.critical(f'Sent email for {email} in day -> dont send again')
                    return
                time_exp = data.get('time_exp')
                logger.info(f'Start process send email to {email}')
                sender_email = settings.EMAIL_SENDER
                host = settings.EMAIL_HOST
                pass_word = settings.EMAIL_PASSWORD
                port = settings.EMAIL_PORT
                msg = MIMEMultipart()

                msg['Subject'] = f'[WARNING] - Mật khẩu của bạn đã hết hạn'
                msg['To'] = email
                msg.attach(MIMEText(f'Mật khẩu của bạn sẽ hết hạn vào ngày {time_exp}. Hãy truy cập vào đường link sau để đổi mật khẩu : \n {"http://172.27.230.14:3000/docs#/User/change_password_user_user_change_password_post"}'))
                server = smtplib.SMTP(host=host, port=port)
                server.starttls()
                server.login(user=sender_email, password=pass_word)
                server.send_message(msg=msg, from_addr=sender_email,
                                    to_addrs=[email])
                logger.info(f'Sent email to {email} success')
                if self.emails_sent_in_day.get(datetime.utcnow().date()):
                    self.emails_sent_in_day.get(datetime.utcnow().date()).append(email)
                else:
                    self.emails_sent_in_day[datetime.utcnow().date()] = [email]
                
        except Exception as e:
            logger.error(f'{__name__} got error {e}')
            logger.error(f'Sent email fail')
            pass

handler_email = SendEmailNotiPasswordExp()

def password_notification(body, message):
    message.ack()
    if type(body) == list:
        for data in body:
            if type(data) != dict:
                logger.critical(f'Data in body must be a Dict')        
                # message.ack()
                return
        handler_email.send_email(body)
    else :
        logger.critical(f'Body input must is a LIST')
        # message.ack()
        return
    # message.ack()


    
    
    