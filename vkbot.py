import difflib
import random
import time

from config.log.logger import Logger
from config.setup import *
from google.google_sheets import GoogleSheets
from google.google_drive_connector import GoogleDriveConnector
import pandas as pd
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
import vk_api.vk_api

from message_parser import MessageParser
from keyboard import Keyboard


class VkBot:

    def __init__(self, group_id, token, table_name, room_list, service_account_file, vk_bot: str = "bot", ):
        """Creates a new bot with parameters from the setup file"""
        self.logger = Logger('app').logger
        self.logger.info('Start of bot initialization')
        self.vk_bot = vk_bot
        self.group_id = group_id
        self.vk_session = vk_api.VkApi(token=token)
        self.long_poll = VkBotLongPoll(self.vk_session, group_id)
        self.vk = self.vk_session.get_api()
        self.master_id = GOSHA_ID
        self.admins_ids = GOSHA_ID
        self.vk_link = VK_LINK

        self.room_list = room_list
        self.table_name = table_name

        self.gs = GoogleSheets(table_name, service_account_file)
        self.gd = GoogleDriveConnector(service_account_file)
        self.keyboard = Keyboard()

        self.logger.info("Completion of bot initialization")

        self.logger.info('Start of answers download')
        self.mp = MessageParser(self.vk, self.gs)

        self.data_to_upload = {'room': [], 'fullname': [], 'id': []}

        self.logger.info("Completion of answer download")

    def write_about_exception(self, event):
        """Sends an exception message to the user and developer.

        :param event:   Event that caused the exception.
        :return:        None.
        """
        self.write_msg(self.master_id, 'Что-то пошло не так с командой {} от пользователя {}.'.format(event.obj.text, ' '.join(self.mp.get_full_name(event.obj.from_id))),
                       self.keyboard.user_keyboard)

        self.write_msg(event.obj.peer_id,
                       'Что-то пошло не так, попробуйте повторить попытку позднее.', self.keyboard.user_keyboard)
        self.logger.exception('Exception:')

    def write_events(self, event):
        """Specifies the type of event to write to the file.

        :param event:   The event that you want to write to a file.
        :param time:    Time when the event occurred.
        :return:        None.
        """

        if event.type == VkBotEventType.GROUP_JOIN:
            self.logger.info('New user group membership')

        elif event.type == VkBotEventType.GROUP_LEAVE:
            self.logger.info('Leaving a group')

        elif event.type == VkBotEventType.MESSAGE_NEW:
            self.logger.info('New incoming message: "{}" from user {}'.format(event.obj.text,
                                                                             ' '.join(self.mp.get_full_name(event.obj.peer_id))))
            self.logger.info(event.obj)

        elif event.type == VkBotEventType.MESSAGE_REPLY:
            self.logger.info('New outgoing message "{}.." for user {}'.format(event.obj.text[:20],
                                                                              ' '.join(self.mp.get_full_name(event.obj.peer_id))))

    def write_msg(self, peer_id, message, keyboard):
        """Sends a message to the user.

        :param peer_id:  Id of the user to send the message to.
        :param message:  Text of the message to send.
        :return:         None
        """
        self.vk.messages.send(peer_id=peer_id,
                              random_id=get_random_id(),
                              message=message,
                              keyboard=keyboard)

    def send_msg_about_duty(self):
        """"Sends a message to students who are on duty at a certain time today."""
        self.logger.info('Duty thread is started')
        while True:
            if '19.00.00' <= time.strftime("%H.%M.%S", time.localtime()) <= '19.10.00':
                rooms = self.gs.get_duty_room()
                if rooms:
                    self.logger.info('Duty rooms {} detected'.format(rooms))

                    for room in rooms:
                        ids = self.gs.get_duty_ids_by_room(room)
                        for id in ids:
                            self.write_msg(int(id), 'Сегодня дежурит {} комната.'.format(room), self.keyboard.user_keyboard)

                else:
                    self.logger.info('Duty rooms not detected')

            # if self.update_time['begin'] <= time.strftime("%H.%M.%S", time.localtime()) <= self.update_time['end']:

            time.sleep(600)
            self.update_data()

    def update_data(self):
        """Updates information from Google Sheets"""
        self.logger.info('Start of data update')

        self.upload_links()

        self.gs.update_data()

        self.mp.about_commandant = self.gs.get_answer_text('ABOUT_MILENA')[0]
        self.mp.about_castellan = self.gs.get_answer_text('ABOUT_MARGO')[0]
        self.mp.about_gym = self.gs.get_answer_text('ABOUT_GYM')[0]
        self.mp.about_study_room = self.gs.get_answer_text('ABOUT_STUDY_ROOM')[0]
        self.mp.about_guests = self.gs.get_answer_text('ABOUT_GUESTS')[0]
        self.mp.about_shower = self.gs.get_answer_text('ABOUT_SHOWER')[0]
        self.mp.about_laundry = self.gs.get_answer_text('ABOUT_LAUNDRY')[0]
        self.mp.about_duty = self.gs.get_answer_text('REMINDER_ABOUT_DUTY')[0]
        self.mp.question = self.gs.get_answer_text('ABOUT_STUDSOVET')[0]
        self.mp.about_bot = self.gs.get_answer_text('ABOUT_BOT')[0]
        self.mp.parting = self.gs.get_answer_text('PARTING')
        self.mp.opportunities = self.gs.get_answer_text('OPPORTUNITIES')[0]
        self.mp.rude_commands = self.gs.get_answer_text('RUDE_COMMANDS')
        self.mp.good_room = self.gs.get_answer_text('GOOD_ROOM')[0]
        self.mp.bad_room = self.gs.get_answer_text('BAD_ROOM')[0]
        self.mp.unknown_commands = self.gs.get_answer_text('UNKNOWN_COMMANDS')
        self.mp.topical = self.gs.get_answer_text('TOPICAL')[0]
        self.mp.about_invoice = self.gs.get_answer_text('ABOUT_INVOICE')[0]

        self.logger.info('Completion of data update')

    def send_answer(self, event, msg, keyboard):
        try:
            self.write_msg(event.obj.peer_id, msg, keyboard)
        except Exception:
            self.write_about_exception(event)
            self.logger.exception('Answer Exception')

    def upload_links(self):
        self.logger.info('Start of uploading links')

        if len(self.data_to_upload['room']) > 0:
            try:
                for i in range(len(self.data_to_upload['room'])):
                    self.gs.add_student(self.data_to_upload['room'][i],
                                        self.data_to_upload['id'][i],
                                        self.data_to_upload['fullname'][i])
                    self.write_msg(self.data_to_upload['id'][i], self.mp.good_room, self.keyboard.user_keyboard)

            except Exception:
                self.logger.exception('Links are not uploaded')

            else:
                self.logger.info('Links uploaded')
                self.data_to_upload = {'room': [], 'fullname': [], 'id': []}
                self.gs.links_dataframe = pd.DataFrame(self.gs.sheet_links.get_all_records())

    def get_events(self):
        self.write_msg(self.master_id, 'Бот запущен', self.keyboard.user_keyboard)
        self.logger.info('Main thread is started')

        for event in self.long_poll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.write_events(event)
                request = event.obj.text.upper()
                forwarded_request = event.obj.text
                is_answered = False

                if event.obj.peer_id == self.master_id:
                    if request.startswith('НАПИШИ'):
                        try:
                            room = forwarded_request.split()[1]
                            mes = ' '.join(forwarded_request.split()[2:])
                            ids = self.gs.get_duty_ids_by_room(int(room))
                            # print(ids)
                            for id in ids:
                                self.write_msg(int(id), mes, self.keyboard.user_keyboard)
                        except Exception:
                            self.write_about_exception(event)

                        else:
                            if ids:
                                self.write_msg(self.master_id, 'Сделано', self.keyboard.user_keyboard)
                            else:
                                self.write_msg(self.master_id, 'Никого не оказалось', self.keyboard.user_keyboard)
                        is_answered = True
                    if request.startswith("ОБНОВИ"):
                        try:
                            self.write_msg(self.master_id, 'Это займет некоторое время, подождите', self.keyboard.user_keyboard)
                            self.update_data()
                        except Exception:
                            self.write_msg(self.master_id, 'Данные не обновлены, повторите попытку позднее', self.keyboard.user_keyboard)
                            self.logger.exception('Information is not updated')
                        else:
                            self.write_msg(self.master_id, 'Данные успешно обновлены', self.keyboard.user_keyboard)
                            self.logger.info('Information updated')

                        is_answered = True

                if event.obj.reply_message:
                    # print(difflib.SequenceMatcher(None, self.about_studsovet, event.obj.reply_message['text']).ratio())
                    # print(self.about_studsovet)
                    # print(event.obj.reply_message['text'])

                    if difflib.SequenceMatcher(None, self.mp.question, event.obj.reply_message['text']).ratio() >= 0.99:
                        try:
                            self.write_msg(event.obj.peer_id, 'Спасибо за вопрос, я передал его.', self.keyboard.user_keyboard)
                            self.write_msg(self.master_id, '{} спросил:\n{} \nСсылка на страницу: {}{}'.format(
                                ' '.join(self.mp.get_full_name(event.obj.from_id)),
                                forwarded_request,
                                self.vk_link,
                                event.obj.peer_id), self.keyboard.user_keyboard)
                        except Exception:
                            self.write_about_exception(event)
                        is_answered = True

                    elif difflib.SequenceMatcher(None, self.mp.about_duty, event.obj.reply_message['text']).ratio() >= 0.99:
                        if request.isdigit() and int(request) in self.room_list:

                            if len(self.data_to_upload['room']) == len(self.data_to_upload['id']) == len(self.data_to_upload['fullname']):

                                self.data_to_upload['room'].append(request)
                                self.data_to_upload['id'].append(event.obj.peer_id)
                                self.data_to_upload['fullname'].append(' '.join(self.mp.get_full_name(event.obj.from_id)))

                                self.logger.info('Link is added')

                                if len(self.data_to_upload['room']) >= 5:
                                    self.upload_links()
                                else:
                                    self.logger.info('Current length of links is {}. Data is not loaded'.format(len(self.data_to_upload['room'])))

                                self.write_msg(event.obj.peer_id, 'Ты ввел корректную комнату.\n\nОжидай добавления в базу :)', self.keyboard.user_keyboard)
                            else:
                                self.write_msg(self.master_id, 'Нарушение структуры данных для загрузки', self.keyboard.user_keyboard)
                        else:
                            try:
                                self.write_msg(event.obj.from_id, self.mp.bad_room, self.keyboard.user_keyboard)
                            except Exception:
                                self.write_about_exception(event)
                        is_answered = True

                    elif event.obj.reply_message['text'] == self.mp.about_invoice:
                        try:
                            if event.obj.attachments:
                                for i in event.obj.attachments:

                                    from_id = event.obj.from_id
                                    name = self.mp.get_full_name(from_id)
                                    if i['type'] == 'doc' or i['type'] == 'photo':
                                        if i['type'] == 'doc':
                                            ext = i['doc']['ext']
                                            url = i['doc']['url']
                                            filename = "{} {}.{}".format(name[1], name[0], ext)

                                        else:
                                            url = self.mp.get_max_image_url(i['photo']['sizes'])
                                            filename = "{} {}.jpg".format(name[1], name[0])

                                        if self.gd.upload_invoice(url, filename):
                                            self.write_msg(from_id, "Твой чек успешно загружен", self.keyboard.user_keyboard)
                                        else:
                                            self.write_msg(from_id, "Твой чек не загружен. Повтори попытку позднее", self.keyboard.user_keyboard)

                        except Exception:
                            self.write_about_exception(event)
                            self.logger.exception('Invoice is not loaded')
                        is_answered = True

                if not is_answered:
                    command = self.mp.get_msg_type(request)

                    if command == 'duty':
                        self.logger.info('Command "Дежурство" detected')# напоминание о дежурстве
                        room = self.gs.get_room_by_id(event.obj.from_id)
                        # print(room)
                        if room:
                            floor = room // 100

                            if floor < 2:
                                floor = 2

                            # print(floor)
                            try:
                                date = self.gs.get_duty_date_by_room_number(room)
                                # print('date', date)
                                duty_rooms = self.gs.get_duty_room()
                                # print(duty_rooms)
                                # if duty_rooms:
                                for room in duty_rooms:
                                    # print(type(room))
                                    # print(type(floor))
                                    if room // 100 == floor:
                                        if date:
                                            # print(room)
                                            self.write_msg(event.obj.peer_id, 'Сегодня дежурит {} комната.\n\n'
                                                                              'Следующее дежурство твоей команты будет {}.'.format(room, date), self.keyboard.user_keyboard)
                                            is_answered = True
                                        else:
                                            # print(room)
                                            self.write_msg(event.obj.peer_id, 'Сегодня дежурит {} комната.\n\n'
                                                                              'Следующее дежурство твоей комнаты будет в следующем месяце.'.format(room), self.keyboard.user_keyboard)
                                            is_answered = True

                            except Exception:
                                self.write_about_exception(event)
                            if not is_answered:
                                self.write_msg(event.obj.peer_id, 'Пока данных нет, но они скоро появятся!',
                                               self.keyboard.user_keyboard)
                        else:
                            try:
                                self.write_msg(event.obj.peer_id, self.mp.about_duty, self.keyboard.user_keyboard)
                            except Exception:
                                self.write_about_exception(event)

                    else:
                        self.logger.info('Command "{}" detected'.format(command))
                        try:
                            self.send_answer(event, self.mp.get_answer_by_msg_type(command), self.keyboard.user_keyboard)
                        except Exception:
                            self.write_about_exception(event)

                    #
                    # elif command == 'invoice':  # чек
                    #     self.logger.info('Command "Чек" detected')
                    #     # if event.obj.fwd_messages:
                    #     #     from_id = event.obj.fwd_messages[0]['from_id']
                    #     #     name = self.mp.get_full_name(from_id)
                    #     #
                    #     #     # if event.obj.fwd_messages[0]['attachments'][0]['type'] == 'doc':
                    #     #     #     url = event.obj.fwd_messages[0]['attachments'][0]['doc']['url']
                    #     #     #     ext = event.obj.fwd_messages[0]['attachments'][0]['doc']['ext']
                    #     #     #
                    #     #     #     filename = "{} {}.{}".format(name[1], name[0], ext)
                    #     #     #
                    #     #     # elif event.obj.fwd_messages[0]['attachments'][0]['type'] == 'photo':
                    #     #     #
                    #     #     #     url = self.mp.get_max_image_url([msg['photo']['sizes'] for msg in event.obj.fwd_messages[0]['attachments']])
                    #     #     #     filename = "{} {}.jpg".format(name[1], name[0])
                    #     #     #
                    #     #     # self.gd.upload_invoice(url, filename)
                    #     # else:
                    #     self.write_msg(event.obj.peer_id, self.about_invoice, self.keyboard.user_keyboard)
                    #
            elif event.type == VkBotEventType.MESSAGE_REPLY:
                self.write_events(event)

            elif event.type == VkBotEventType.GROUP_JOIN:
                self.write_events(event)
