import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.config import settings
from datetime import datetime
from app.core.database.rabbitmq_kombu import RabbitMQ
from app.core import constants
import asyncio
import logging

logger = logging.getLogger(f'{__name__}')

loop = asyncio.get_event_loop()

connection = RabbitMQ()

emails_sent_in_day = {}

class SendEmailNotiPasswordExp():
    htype = constants.HTYPE_MAPPING_CLASS_SEND_EMAIL
    
        
    def handler(self, body, message):
        if type(body) != dict:
            logger.critical(f'Body must be a Dict')        
            message.ack()
            return
        else :                
            self.password_notification(body, message)

        
    def password_notification(self,body ,message, **kwargs):
        try:
            
            email = body.get('email')
            if emails_sent_in_day and email in emails_sent_in_day.get(str(datetime.utcnow().date())):
                logger.critical(f'Sent email for {email} in day -> dont send again')
                message.ack()
                return
            time_exp = body.get('time_exp')
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
            if emails_sent_in_day.get(str(datetime.utcnow().date())):
                emails_sent_in_day.get(str(datetime.utcnow().date())).append(email)
            else:
                emails_sent_in_day[str(datetime.utcnow().date())] = [email]
            message.ack()
                
        except Exception as e:
            logger.error(f'{__name__} got error {e}')
            logger.error(f'Sent email fail')
            message.ack()



    
    
    