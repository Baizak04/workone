from notifiers import get_notifier
import time
from TOKEN import token, chatId

while True:
    what = input('О чем напомнить? \n Для выхода отправьте \'exit\' \n')
    if what == 'exit':
        break
    else:
        t = input('Через сколько минут напомнить? \n')
        t = int(t) * 60
        time.sleep(t)
        telegram = get_notifier('telegram')
        telegram.notify(token=token, chat_id=chatId, message=what)