# from . import json_load
# from config.config_parser import config
# json_file_load = json_load.json_file_read()
# data_extractor_file_path = config.get("JsonFiles","data_extractor_file") 

# class FormatNonEciaKeys:
#     def replace_chars(self,key_lists):
#         json_data_file = json_file_load.json_data_load(data_extractor_file_path)
#         pd_replace_chars = json_data_file["replace_chars"]
#         final_list=[]
#         for ele in key_lists:
#             str1 = ''
#             for c in ele:
#                 if c not in pd_replace_chars:
#                     str1+=c
#             final_list.append(str1)
#         return final_list