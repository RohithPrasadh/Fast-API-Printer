# from config.config_parser import config
# import logging
# from utils.database import db

# logger = logging.getLogger(__name__)
# collection_reelstock_name = config.get("MongoDb", "collection_reelstock")
# collection_reelstock = db[collection_reelstock_name]

# def generate_unique_id():
#     projection = {
#         "extractedSticker": 0,
#     }
#     documents_cursor = collection_reelstock.find({}, projection).sort("_id", -1).limit(1)
#     documents_list = list(documents_cursor)

#     print(documents_list, "documents11111")

#     if documents_list:
#         last_unique_id = documents_list[0]["uniqueIdentifier"]
#         chars_list = list(last_unique_id)

#         # Increment the last character
#         chars_list[-1] = chr(ord(chars_list[-1]) + 1)

#         # Handle carry-over
#         for i in range(len(chars_list) - 1, 0, -1):
#             if chars_list[i] > "9":
#                 chars_list[i] = "0"
#                 chars_list[i - 1] = chr(ord(chars_list[i - 1]) + 1)

#         # Handle the case when the first character is greater than "9"
#         if chars_list[0] > "9":
#             chars_list[0] = "A"

#         new_unique_id = "".join(chars_list)
#         print(new_unique_id)
#         return new_unique_id
#     else:
#         chars_list = ['A', '0', '0', '0']
#         return "".join(chars_list)


