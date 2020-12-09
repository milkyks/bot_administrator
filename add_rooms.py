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

    def add_room(self, room_n):
        curs = self.conn.cursor()
        query = "INSERT INTO bot.rooms (id, floor, alive) " \
                "VALUES ('{}', {}, {})".format(room_n, room_n//100, 1)
        # query = INSERT INTO users(full_name, vk_id, room_number, phone_number, type) VALUES ('abc', 123, 123, '88005553535', 'student')"

        curs.execute(query)
        self.make_commit()
        # student = {'name': '', 'room': '', 'phone': '', 'id': ''}


if __name__ == '__main__':
    db = DataBaseConnector()
    r = [103, 104, 105, 106, 110, 111, 112,
201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219,
301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321,
401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421,
502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519]

    for i in r:
        DataBaseConnector.add_room(db, i)
