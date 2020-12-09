import os

import requests
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from config.log.logger import Logger


class GoogleDriveConnector:
    def __init__(self, service_account_file):
        self.logger = Logger('app').logger

        self.logger.info('Start of google drive initialization')

        self.scope = ['https://www.googleapis.com/auth/drive']
        self.service_account_file = service_account_file
        self.credentials = service_account.Credentials.from_service_account_file(self.service_account_file,
                                                                                 scopes=self.scope)
        self.service = build('drive', 'v3', credentials=self.credentials)
        self.folder_id = '19S0Idot_9aRpShBc7ze6i2Y5wstqAVBF'

        self.logger.info("Completion of google drive initialization")

    def upload_invoice(self, url, filename):
        def add_invoice(name):
            try:
                file_path = name
                file_metadata = {
                                'name': name,
                                'parents': [self.folder_id]
                            }
                media = MediaFileUpload(file_path, resumable=True)
                self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            except Exception:
                return False
            else:
                return True

        with open(filename, "wb") as out:
            out.write(requests.get(url).content)

        if add_invoice(filename):
            self.logger.info('Invoice uploaded')
            os.remove(filename)
            return True
        else:
            self.logger.error('Invoice not uploaded')
            return False


if __name__ == '__main__':
    pass
