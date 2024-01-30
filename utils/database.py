from pymongo import MongoClient

from config.config_parser import config
print("ojkhg")

db_name = config.get("MongoDb", "data_base")
db_url = config.get("MongoDb", "data_base_url")

client = MongoClient(db_url)
db = client[db_name]
