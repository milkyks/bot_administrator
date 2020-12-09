from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from config.log.logger import Logger


class Keyboard:
    def __init__(self):
        self.logger = Logger('app').logger
        self.user_keyboard = self.create_user_keyboard()
        self.admin_keyboard = self.create_admin_keyboard()
        self.opportunities_keyboard = self.create_opportunities_keyboard()

    def create_user_keyboard(self):
        self.logger.info('Starting of creating user\'s keyboard')
        keyboard = VkKeyboard(one_time=False)
        # False Если клавиатура должна оставаться открытой после нажатия на кнопку
        # True если она должна закрываться
        keyboard.add_button("Комендант", color=VkKeyboardColor.DEFAULT)
        keyboard.add_button("Кастелянша", color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button("Душ", color=VkKeyboardColor.DEFAULT)
        keyboard.add_button("Постирочная", color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button("Гости", color=VkKeyboardColor.DEFAULT)
        keyboard.add_button("Вопрос", color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button("Спортзал", color=VkKeyboardColor.PRIMARY)
        keyboard.add_button("Учебка", color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()
        keyboard.add_button("Чек", color=VkKeyboardColor.POSITIVE)
        keyboard.add_button("Дежурство", color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button("Актуальное", color=VkKeyboardColor.POSITIVE)

        # keyboard.add_button("Инфо", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
        self.logger.info('Completion of creating user\'s keyboard')

        return keyboard.get_keyboard()

    def create_admin_keyboard(self):
        pass

    def create_opportunities_keyboard(self):
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button("Возможности", color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()
