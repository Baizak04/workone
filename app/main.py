import pywhatkit
import os

def send_message_inst():
    mobile = os.getenv('MOBILE')
    message = input('Введите текст сообщения: ')
   
    pywhatkit.sendwhatmsg(phone_no=mobile, message=message)
    
def send_message():
    mobile = os.getenv('MOBILE')
    message = input('Введите текст сообщения: ')
    hour = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))
    
    pywhatkit.sendwhatmsg(phone_no=mobile, message=message, time_hour=hour, time_main=minutes)
    
def main():
    send_message()
    
if __name__ == '__name__':
    main()