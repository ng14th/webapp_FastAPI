import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.config import settings
from app.user.models.user import User
from datetime import datetime
from app.core.database.rabbitmq_kombu import RabbitMQ
import asyncio

loop = asyncio.get_event_loop()

connection = RabbitMQ()

class SendEmailNotiPasswordExp():
    def __init__(self) -> None:
        self.emails_sent_in_day = {}
        
    async def send_msg_to_email_worker(self):
        list_user = []
        time_now = datetime.timestamp(datetime.utcnow())
        users = User.find({'password_expr':{'$lte':str(time_now)}})
        async for user in users:
            
            time_user_exp = datetime.utcfromtimestamp(float(user.password_expr)).date()
            time_exp = datetime.utcnow().date() - time_user_exp
            list_user.append({
                "email" : user.email,
                "time_exp" : time_exp.days
            })
        if list_user:
            # server, channel = connection.initialize_rmq()
            # connection.publish_message_exchange(list_user,constants.EXCHANGE_TASK_CELERY,constants.ROUTING_KEY_NOTI_USER)
            # server.close()
            self.send_email_to_list(list_user)


    def send_email_to_list(self,body, **kwargs):
        try:
            for data in body:
                email = data.get('email')
                if self.emails_sent_in_day and email in self.emails_sent_in_day.get(datetime.utcnow().date()):
                    print(f'Sent email for {email} in day -> dont send again')
                    return
                time_exp = data.get('time_exp')
                print(f'Start process send email to {email}')
                sender_email = settings.EMAIL_SENDER
                host = settings.EMAIL_HOST
                pass_word = settings.EMAIL_PASSWORD
                port = settings.EMAIL_PORT
                msg = MIMEMultipart()

                msg['Subject'] = f'[WARNING] - Mật khẩu của bạn đã hết hạn'
                msg['To'] = email
                msg.attach(MIMEText(f'Mật khẩu của bạn sẽ hết hạn trong {time_exp} ngày nữa. Hãy truy cập vào đường link sau để đổi mật khẩu : \n {"http://172.27.230.14:3000/docs#/User/new_employee_user_change_password_post"}'))
                server = smtplib.SMTP(host=host, port=port)
                server.starttls()
                server.login(user=sender_email, password=pass_word)
                server.send_message(msg=msg, from_addr=sender_email,
                                    to_addrs=[email])
                print(f'Sent email to {email} success')
                if self.emails_sent_in_day.get(datetime.utcnow().date()):
                    self.emails_sent_in_day.get(datetime.utcnow().date()).append(email)
                else:
                    self.emails_sent_in_day[datetime.utcnow().date()] = [email]
                    
                print(self.emails_sent_in_day)
                
        except Exception as e:
            print(f'{__name__} got error {e}')
            print(f'Sent email fail')
            pass

handler_email = SendEmailNotiPasswordExp()

def password_notification(body, message):
    if type(body) is list:
        handler_email.send_email(body)
    else :
        a = 1+"qưeqweqweqwe"
        print(f'Body input must is a LIST')
    message.ack()
    
    
    