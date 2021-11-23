import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
import random
from time import time
import time
from datetime import datetime as dt
from datetime import datetime
import datetime
from vk_api.keyboard import VkKeyboard, VkKeyboardColor





class MyVkBotLongPoll(VkBotLongPoll):
        def listen(self):
            while True:
                try:
                    for event in self.check():
                        yield event
                except Exception as e:
                    print('Вк опять перезагрузился:', e)

def main():
    token_api = 'Ваш код сообщества'

    vk_session = vk_api.VkApi(token = token_api)

    
    groupId = 'Id Вашей группы'
    longpoll = MyVkBotLongPoll(vk_session, group_id=groupId)

    vk = vk_session.get_api()
    id=1
    i=0

    t=0



    members_id=vk.groups.getMembers(group_id=groupId)['items']
    members_count=vk.groups.getMembers(group_id=groupId)['count']

    #vk.groups.edit(group_id='189863854', description='т е с т')
    #vk.groups.ban(group_id='189863854', user_id='486259400')

    test_message='''while members_count>=t:
        try:
            vk.messages.send(user_id=members_id[t], message='', random_id=get_random_id())
        except Exception as e:
            print('Не удалось отправить сообщение данному пользователю.')
        t+=1'''

    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Расписание на сегодня', color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()  # Переход на новую строку
    keyboard.add_button('Расписание на завтра', color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на новую строку
    keyboard.add_button('Расписание на послезавтра', color=VkKeyboardColor.DEFAULT)

    p=0


    #расписание на 2 разные недели

    timetable2={0:'''''',
               1:'''''',
               2:'''''',
               3:'''''',
               4:'''''',
               5:'''''',
               6:''''''}

    timetable1={0:'''''',
               1:'''''',
               2:'''''',
               3:'''''',
               4:'''''',
               5:'''''',
               6:''''''}

    r=0

    def dab():
        if  p==0:
            x='в понедельник'
        elif p==1:
            x='во вторник'
        elif p==2:
            x='в среду'
        elif p==3:
            x='в четверг'
        elif p==4:
            x='в пятницу'
        elif p==5:
            x='в субботу'
        elif p==6:
            x='в воскресенье'

    def when():
        sub = event.message.text[6:]
        p = datetime.datetime.today().weekday()



    for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.message.text.lower().find('привет') != -1:
                    vk.messages.send(user_id=event.message.peer_id, message='Привет, '+ vk.users.get(access_token = token, user_ids = event.message.peer_id)[0]['first_name']+'! &#128075;', random_id=get_random_id())
                elif event.message.text.lower().find('пока') != -1:
                    vk.messages.send(user_id=event.message.peer_id, message=vk.users.get(access_token = token, user_ids = event.message.peer_id)[0]+', не уходи! &#128546;', random_id=get_random_id())
                elif event.message.text.lower().find('мудрость') != -1:
                    vk.messages.send(user_id=event.message.peer_id, message='Уроки Синёва самые лучшие.', random_id=get_random_id())
                elif event.message.text.lower().find('спам') != -1:
                    while r<500:
                        vk.messages.send(user_id=event.message.peer_id, message='спам', random_id=get_random_id())
                        time.sleep(5)
                        r+=1
                elif event.message.text.lower().find('когда') != -1:
                    vk.messages.send(user_id=event.message.peer_id, message=event.message.text[6:]+' ближе чем кажется', random_id=get_random_id())
                elif event.message.text.lower() == 'расписание на сегодня':
                    if int(datetime.datetime.today().isocalendar()[1])%2 == 0:
                        i = datetime.datetime.today().weekday()
                        vk.messages.send(user_id=event.message.peer_id, message=timetable2[i], random_id=get_random_id())
                    else:
                        i = datetime.datetime.today().weekday()
                        vk.messages.send(user_id=event.message.peer_id, message=timetable1[i], random_id=get_random_id())
                elif event.message.text.lower() == 'расписание на завтра':
                    if int(datetime.datetime.today().isocalendar()[1])%2 == 0:
                        if datetime.datetime.today().weekday() == 6:
                            i = 0
                            vk.messages.send(user_id=event.message.peer_id, message=timetable1[i], random_id=get_random_id())
                        else:
                            i = datetime.datetime.today().weekday()
                            i+=1
                            vk.messages.send(user_id=event.message.peer_id, message=timetable1[i], random_id=get_random_id())
                    else:
                        if datetime.datetime.today().weekday() == 6:
                            i = 0
                            vk.messages.send(user_id=event.message.peer_id, message=timetable2[i], random_id=get_random_id())
                        else:
                            i = datetime.datetime.today().weekday()
                            i+=1
                            vk.messages.send(user_id=event.message.peer_id, message=timetable1[i], random_id=get_random_id())
                elif event.message.text.lower() == 'расписание на послезавтра':
                    if int(datetime.datetime.today().isocalendar()[1])%2 == 0:
                        if datetime.datetime.today().weekday() == 5 or datetime.datetime.today().weekday() == 6:
                            if datetime.datetime.today().weekday() == 5:
                                i = 0
                                vk.messages.send(user_id=event.message.peer_id, message=timetable1[i], random_id=get_random_id())
                            elif datetime.datetime.today().weekday() == 6:
                                i = 1
                                vk.messages.send(user_id=event.message.peer_id, message=timetable1[i], random_id=get_random_id())
                        else:
                            i = datetime.datetime.today().weekday()
                            i+=2
                            vk.messages.send(user_id=event.message.peer_id, message=timetable2[i], random_id=get_random_id())
                    else:
                        if datetime.datetime.today().weekday() == 5 or datetime.datetime.today().weekday() == 6:
                            if datetime.datetime.today().weekday() == 5:
                                i = 0
                                vk.messages.send(user_id=event.message.peer_id, message=timetable2[i], random_id=get_random_id())
                            elif datetime.datetime.today().weekday() == 6:
                                i = 1
                                vk.messages.send(user_id=event.message.peer_id, message=timetable2[i], random_id=get_random_id())
                        else:
                            i = datetime.datetime.today().weekday()
                            i+=2
                            vk.messages.send(user_id=event.message.peer_id, message=timetable1[i], random_id=get_random_id())
                else:
                    vk.messages.send(user_id=event.message.peer_id, attachment='photo-196388979_457239026', random_id=get_random_id())



if __name__ == '__main__':
    main()
