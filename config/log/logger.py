from logging import getLogger, config
import yaml
import os


class Logger:
    def __init__(self, *args):
        self.name = 'logger_config.yaml'
        self.path_to_config_file = self.find_path('.')
        if args:
            self.mode = args[0]
        self.logger = self.create_logger()

    def create_logger(self):
        with open(self.path_to_config_file, 'r') as f:
            log_cfg = yaml.safe_load(f.read())
        config.dictConfig(log_cfg)
        if self.mode:
            return getLogger(self.mode)
        return getLogger()

    def find_path(self, path):
        for root, dirs, files in os.walk(path):
            if self.name in files:
                return os.path.join(root, self.name)
