import mysql

import mysql.connector
from mysql.connector import Error


class DataBaseConnector:
    def __init__(self):
        self.conn = self.get_connection(host='localhost', database='mysql', user='root', password='123')

    def get_connection(self, host, database, user, password):
        try:
            conn = mysql.connector.connect(host=host,
                                           database=database,
                                           user=user,
                                           password=password)
            if conn.is_connected():
                print('Connected to MySQL database')
                return conn

        except Error as e:
            print(e)

    def close_connection(self):
        self.conn.close()

    # def create_answers_array(self, conn, CMD):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT ANSWR FROM Answers WHERE CMD='{}'".format(CMD))
    #     rows = cursor.fetchall()
    #     cursor.close()
    #     return [row[0] for row in rows]

    def make_commit(self):
        self.conn.commit()

    def add_command(self, name):
        curs = self.conn.cursor()
        query = "INSERT INTO bot.commands (main_name, is_active, priority) " \
                "VALUES ('{}', {}, {})".format(name, 1, 1)
        curs.execute(query)
        self.make_commit()


    def add_synonyms(self, labels):
        curs = self.conn.cursor()
        curs.execute("select c.id from bot.commands c where c.main_name = '{}'".format(labels[0]))
        id = curs.fetchall()
        if id != None:
            for i in labels:
                query = "INSERT INTO bot.command_synonyms (synonym, command_id) VALUES ('{}', {});".format(i, id[0][0])
                print(i)
                curs.execute(query)
            self.make_commit()
        # student = {'name': '', 'room': '', 'phone': '', 'id': ''}


if __name__ == '__main__':
    db = DataBaseConnector()
    c =[["Комендант", "КОМЕНДА", "МИЛЕНА", "КОМЕНДАНТ", "МИЛЕНЫ", "КОМЕНДЫ"],
            ["Кастелянша", "БЕЛЬЕ", "КАСТЕЛЯНША", "МАРГАРИТА", "БЕЛЬЯ"],
            ["Спортзал","ТРЕНАЖЕРНЫЙ ЗАЛ", "СПОРТИВНЫЙ ЗАЛ", "СПОРТЗАЛ", "ЗАПИСЬ В СПОРТЗАЛ", "ЗАЛ"],
            ["Учебная комната", "УЧЕБНАЯ КОМНАТА", "УЧЕБКА", "ЗАПИСЬ В УЧЕБКУ"],
            ["Гости", "ГОСТИ", "ГОСТЕЙ", "ГОСТЯМИ"],
            ["Душ", "ДУШ", "МЫТЬСЯ", "ДУШЕВАЯ"],
            ["Стирка", "СТИРК", "ПРАЧК", "ПОСТИРОЧН", "СТИРАТЬ"],
            ["Дежурство", "ДЕЖУРСТВО", "УБОРКА", "КУХНЯ"],
            ["Вопрос", "ВОПРОС", "СТУДСОВЕТ", "ПОДСКАЖИ"],
            ["Приветствие", "ПРИВЕТ", "ПРИВ", "ХАЙ", "ШАЛОМ", "ЗДАРОВА", "ДРАТУТИ", "НАЧАТЬ", "START"],
            ["Прощание", "ПОКА", "ПРОЩАЙ", "ГУДБАЙ", "ЧМОКИ", "ПОКЕДОВА"],
            ["Благодарность", "СПАСИБО", "THX", "THANKS", "THANK YOU", "СПАСИБКИ", "СПС"],
            ["Возможности","УМЕЕШЬ", "ВОЗМОЖНОСТИ", "МОЖЕШЬ", "ИНФО", "ТЫ КТО?", "ИНФОРМАЦИЯ"],
            ["Квитанция",  "ЧЕК", "ОПЛАТА", "ДОЛГИ"],
            ["Актуальное", "АКТУАЛЬНОЕ", "НОВОСТИ"],
            ["Регистрация", "РЕГИСТРАЦИЯ", "ЗАРЕГИСТРИРОВАТЬСЯ", "ЗАРЕГАТЬСЯ"] ]

    for i in c:
        DataBaseConnector.add_command(db, i[0])
        DataBaseConnector.add_synonyms(db, i)
