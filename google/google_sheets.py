import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from config.log.logger import Logger


class GoogleSheets:

    def __init__(self, table_name, service_account_file):
        self.logger = Logger('app').logger

        # self.table_name = 'Дежурство-5б'
        self.table_name = table_name
        self.logger.info('Start of google sheets initialization')
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(service_account_file, self.scope)
        self.client = gspread.authorize(self.creds)

        self.sheet_duty2 = pd.DataFrame(self.client.open(self.table_name).get_worksheet(0).get_all_records())
        self.sheet_duty3 = pd.DataFrame(self.client.open(self.table_name).get_worksheet(1).get_all_records())
        self.sheet_duty4 = pd.DataFrame(self.client.open(self.table_name).get_worksheet(2).get_all_records())
        self.sheet_duty5 = pd.DataFrame(self.client.open(self.table_name).get_worksheet(3).get_all_records())

        self.sheet_links = self.client.open(self.table_name).get_worksheet(4)
        # self.sheet_answers = self.client.open('Дежурство').get_worksheet(5)

        self.links_dataframe = pd.DataFrame(self.sheet_links.get_all_records())
        self.answers_dataframe = pd.DataFrame(self.client.open(self.table_name).get_worksheet(5).get_all_records())
        self.duty_dataframe = pd.concat([self.sheet_duty2, self.sheet_duty3, self.sheet_duty4, self.sheet_duty5], ignore_index=True)

        self.first_empty_cell_index = self.find_first_empty_cell()

        self.logger.info("Completion of google sheets initialization")

    def update_data(self):
        self.sheet_duty2 = pd.DataFrame(self.client.open(self.table_name).get_worksheet(0).get_all_records())
        self.sheet_duty3 = pd.DataFrame(self.client.open(self.table_name).get_worksheet(1).get_all_records())
        self.sheet_duty4 = pd.DataFrame(self.client.open(self.table_name).get_worksheet(2).get_all_records())
        self.sheet_duty5 = pd.DataFrame(self.client.open(self.table_name).get_worksheet(3).get_all_records())
        self.duty_dataframe = pd.concat([self.sheet_duty2, self.sheet_duty3, self.sheet_duty4, self.sheet_duty5], ignore_index=True)
        self.links_dataframe = pd.DataFrame(self.sheet_links.get_all_records())
        self.answers_dataframe = pd.DataFrame(self.client.open(self.table_name).get_worksheet(5).get_all_records())

    def get_duty_date_by_room_number(self, room):
        for row in self.duty_dataframe.values:
            if row[1] == room and row[0] > datetime.date.today().strftime("%d.%m.%Y"):
                return row[0]

    def get_duty_room(self):
        """Used to determine the number of rooms that are on duty on each floor of the dormitory.

        :return:        List of duty rooms.
        """
        today = datetime.date.today().strftime("%d.%m.%Y")
        return [room[1] for room in self.duty_dataframe.values if room[0] == today]

    def get_room_by_id(self, id):
        # print(self.links_dataframe.values)
        for row in self.links_dataframe.values:
            if row[1] == id:
                return row[0]

    def get_duty_ids_by_room(self, room):
        """Used to identify people who live in the specified room.

        :param room:    Room number.
        :return:        List of User ID in Vkontakte social network.
        """
        return [row[1] for row in self.links_dataframe.values if row[0] == room]

    def get_answer_text(self, cmd):
        """searches the table for a text by variable name.

        :param cmd:     Command Name.
        :return:        None.
        """
        answers = []
        for answer in self.answers_dataframe.values:
            if answer[0] == cmd:
                answers.append(answer[1])

        return answers

    def find_first_empty_cell(self):
        self.logger.info('Start searching for empty cell')
        for i in range(2, 300):
            if not self.sheet_links.cell(i, 1).value and not self.sheet_links.cell(i, 2).value and not self.sheet_links.cell(i, 3).value:
                self.logger.info('Empty cell is found')
                return i

    def add_student(self, room, id, fullname):
        """Adds information about the user to the sheet.

        :param room:    Room number.
        :param id:      User ID in Vkontakte social network.
        :return:        None.
        """

        self.sheet_links.update_cell(self.first_empty_cell_index, 1, room)
        self.sheet_links.update_cell(self.first_empty_cell_index, 2, id)
        self.sheet_links.update_cell(self.first_empty_cell_index, 3, fullname)

        self.first_empty_cell_index += 1

        self.links_dataframe = pd.DataFrame(self.sheet_links.get_all_records())


if __name__ == "__main__":
    gs = GoogleSheets()
    # room = gs.get_room_by_id(str(184541442))
    # print(gs.get_duty_date_by_room_number(324))
    # print(gs.get_duty_room())
    print(gs.get_room_by_id(135059353))
    # print(gs.answers_dataframe.iloc[1:3, :]
    # print(pd.concat([gs.sheet_duty2, gs.sheet_duty3, gs.sheet_duty4, gs.sheet_duty5], ignore_index=True))
    # print(gs.get_duty_room())
    # print(gs.sheet_duty3.cell(2,2))
