import os
import threading
import time

from config.log.logger import Logger
from vkbot import VkBot

import env
    # env.set_5a_creds()
    # env.set_5b_creds()


class Thread(threading.Thread):

    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        global bot
        if self.counter == 1:
            bot.send_msg_about_duty()
        elif self.counter == 2:
            bot.get_events()


def start_threads():
    global thread1
    global thread2

    thread1 = Thread("Thread1", 1)
    thread2 = Thread("Thread2", 2)

    thread1.start()
    thread2.start()


def start_bot(group_id, token, table_name, room_list, service_account_file):
    global logger
    try:
        bot = VkBot(group_id, token, table_name, room_list, service_account_file)
    except Exception:
        time_before_reboot = 200
        logger.exception('Bot is not created')
        for _ in range(0, 200, 10):
            logger.info('{} seconds before restart'.format(time_before_reboot - _))
            time.sleep(10)
        start_bot(group_id, token, table_name, room_list, service_account_file)
    else:
        return bot


if __name__ == "__main__":
    logger = Logger('app').logger
    logger.info('Start program')

    group_id = os.environ['GROUP_ID']
    service_account_file = f"google/client_secrets_{os.environ['DORM']}.json"
    token = os.environ['GROUP_TOKEN']
    table_name = f"Дежурство{os.environ['DORM']}"

    if os.environ['DORM'] == '5b':
        room_list = [209, 210, 211, 212, 213, 214, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226,
                     306, 309, 310, 311, 312, 313, 314, 315, 316, 318, 319, 320, 321, 322, 323, 324, 325, 326, 328,
                     406, 409, 410, 411, 412, 413, 414, 415, 416, 418, 419, 420, 421, 422, 423, 424, 425, 426, 428,
                     506, 509, 510, 511, 512, 513, 514, 515, 516, 518, 519, 520, 521, 522, 523, 524, 525, 526, 528]

    elif os.environ['DORM'] == '5a':
        room_list = [103, 104, 105, 106, 110, 111, 112,
                     201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219,
                     301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321,
                     401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421,
                     502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519]

    logger.info('Start of bot creation')
    bot = start_bot(group_id, token, table_name, room_list, service_account_file)
    logger.info('Complition of bot creation')

    logger.info('Start of bot\'s threads')
    start_threads()

    while True:
        if not thread1.is_alive():
            logger.error('Duty thread is not alive')
            logger.info('Restarting Duty thread')

            thread1 = Thread("Thread1", 1)
            thread1.start()

        if not thread2.is_alive():
            logger.error('Main thread is not alive')
            logger.info('Restarting main thread')

            thread2 = Thread("Thread2", 2)
            thread2.start()

        time.sleep(5)
