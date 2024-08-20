import json


class Config:
    def __init__(self, db_type, db_cfg):
        self.db_type = db_type
        self.db_cfg = db_cfg


class JsonConfigFactory:
    @staticmethod
    def get(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            db_type = data.get('DB_TYPE')
            db_cfg = data.get('DB_CFG')
            return Config(db_type, db_cfg)
