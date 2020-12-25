import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import main_token
from datetime import  datetime
import random
import time

vk_session = vk_api.VkApi(token=main_token)
longpoll = VkLongPoll(vk_session)
badwords = ['говно','негр','негры','пидорасы','блять','хуй','мудила','ебать','пизда','ебанный','негры пидорасы']

def sender(id, text):
    vk_session.method('messages.send', {'chat_id' : id, 'message': text, 'random_id': 0})


# while True:
#     for event in longpoll.listen():
#         if event.type == VkEventType.MESSAGE_NEW:
#             print("Message send in: " + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
#             print("Text in message: " + str(event.text))
#             print(event.user_id)
#             msg = event.text.lower()
#             if event.from_user and not (event.type_id):
#                 id = event.chat_id
#                 if msg == "hello":
#                     sender(id, "Meow< sweety :3")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text.lower()
                id = event.chat_id
                print("Message send in: " + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print("Text: " + msg)
                if msg == 'hello':
                    sender(id,'Мeow,sweety')
                elif msg == 'ping':
                    sender(id,'pong')
                if msg in badwords:
                    sender(id, 'Осуждаю,быдло!')

#             print("Message send in: " + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
#             print("Text in message: " + str(event.text))
#             print(event.user_id)