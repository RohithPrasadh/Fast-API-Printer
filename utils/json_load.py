import json
from config.config_parser import config


class json_file_read():
    @staticmethod
    def json_data_load(json_file_url):
        with open(json_file_url) as f:
            data = json.load(f)
        return data
    
    def json_data_write(self, json_file_url, data):
        with open(json_file_url, 'w') as f:
            json.dump(data, f)