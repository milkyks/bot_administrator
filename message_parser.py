import difflib
import random

from config.log.logger import  Logger
from config.setup import *

class MessageParser:
    def __init__(self, vk, gs):
        self.vk = vk
        self.logger = Logger('app').logger

        self.about_commandant = gs.get_answer_text('ABOUT_MILENA')[0]
        self.about_castellan = gs.get_answer_text('ABOUT_MARGO')[0]
        self.about_gym = gs.get_answer_text('ABOUT_GYM')[0]
        self.about_study_room = gs.get_answer_text('ABOUT_STUDY_ROOM')[0]
        self.about_guests = gs.get_answer_text('ABOUT_GUESTS')[0]
        self.about_shower = gs.get_answer_text('ABOUT_SHOWER')[0]
        self.about_laundry = gs.get_answer_text('ABOUT_LAUNDRY')[0]
        self.about_duty = gs.get_answer_text('REMINDER_ABOUT_DUTY')[0]
        self.question = gs.get_answer_text('ABOUT_STUDSOVET')[0]
        self.about_bot = gs.get_answer_text('ABOUT_BOT')[0]
        self.parting = gs.get_answer_text('PARTING')
        self.opportunities = gs.get_answer_text('OPPORTUNITIES')[0]
        self.rude_commands = gs.get_answer_text('RUDE_COMMANDS')
        self.good_room = gs.get_answer_text('GOOD_ROOM')[0]
        self.bad_room = gs.get_answer_text('BAD_ROOM')[0]
        self.unknown_commands = gs.get_answer_text('UNKNOWN_COMMANDS')
        self.topical = gs.get_answer_text('TOPICAL')[0]
        self.about_invoice = gs.get_answer_text('ABOUT_INVOICE')[0]
        self.unknown_commands = gs.get_answer_text('UNKNOWN_COMMANDS')

    def get_full_name(self, from_id):
        """Returns the first and last name of the person who initiated the event."""
        user = self.vk.users.get(user_id=from_id)
        return user[0]['first_name'], user[0]['last_name']

    @staticmethod
    def get_max_image_url(paths):
        max_h = 0
        for path in paths:
            if path['height'] > max_h:
                max_h = path['height']
                url = path['url']
        return url

    @staticmethod
    def get_msg_type(text):
        for number_dict, (name, values) in enumerate(COMMANDS.items()):
            for number_arr, word in enumerate(values):
                if difflib.SequenceMatcher(None, text, word).ratio() >= 0.8 or word in text:
                    return name

    def get_answer_by_msg_type(self, msg_type):
        return {
            'commandant':       self.about_commandant,
            'castellan':        self.about_castellan,
            'gym':              self.about_gym,
            'study_room':       self.about_study_room,
            'guests':           self.about_guests,
            'shower':           self.about_shower,
            'laundry':          self.about_laundry,
            'question':         self.question,
            'parting':          random.choice(self.parting),
            'gratitude':        'Обращайтесь:)',
            'opportunities':    self.opportunities,
            'rude_command':     random.choice(self.rude_commands),
            'invoice':          self.about_invoice,
            'topical':          self.topical,
        }.get(msg_type, random.choice(self.unknown_commands))

