import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import *
import random

score = 0
vk_session = vk_api.VkApi(token=main_token)
longpoll = VkLongPoll(vk_session)

def send_picture(id):
    vk_session.method('messages.send', {'peer_id': id, 'attachment': 'photo-201338515_457239018', 'random_id': 0})
def sender(id, text):
    vk_session.method('messages.send', {'peer_id': id, 'message': text, 'random_id': 0})
def pin_message(id, message):
    vk_session.method('messages.pin', {'peer_id': id, 'message_id': m_ID})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text.lower()
                msg_words = event.text.lower().split()
                id = event.peer_id
                print(msg)
                m_ID = event.message_id

                for i in msg_words:
                    if i in welcome_words:
                        sender(id, 'Мeow,sweety')

                if msg == '/help':
                    sender(id, commands)

                if msg == '/ава':
                    a = random.randint(1, 10)
                    if event.user_id == 511774421:
                        sender(id, 'Это лучшее, что я видел за свои 9 жизней 😻')
                        continue
                    if a > 5:
                        sender(id, 'Это фото весьма неплохо для говорящего куска мяса 👏🏻')
                    if a <= 5:
                        sender(id, 'У меня в миске корм красивее 😺')

                if msg == '/bibametr':
                    a = random.randint(1,100)
                    if a >= 50:
                        smile = ' 👍🏻'
                    else:
                        smile = ' 😭'
                    sender(id, 'Биба ' + str(a) + 'см' + smile)

                if msg == 'ping':
                    sender(id, 'pong')

                if msg == '/пикча_с_котиками':
                    send_picture(id)

                if msg == '!!!cumaндa_нa_cсyдный_дeнь':
                    sender(id, 'WELCOME TO THE CUM ZONE!')
                    sender(id, 'PREPARE FOR HUGE CUM')
                    while True:
                        sender(id, 'CUM')


                if msg == '/нарушители':
                    for i in bad_people_list:
                        sender(id, '@id' + str(i))


                for i in msg_words:
                    if i in badwords:
                        sender(id, 'осуждаю, быдло!')
                        score += 1
                if score > 5:
                        sender(id, 'ОСУЖДАЮ, БЛЯТЬ!')
                        score = 0
                        pin_message(id, m_ID)
                        bad_people_list.append(event.user_id)
