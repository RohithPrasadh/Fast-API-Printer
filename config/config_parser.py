from configparser import ConfigParser

config_file_path = "config/config.ini"


config = ConfigParser()
config.read(config_file_path)
