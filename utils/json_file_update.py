# from utils import json_load
# from config.config_parser import config
# json_file_load = json_load.json_file_read()
# data_extractor_file_path = config.get("JsonFiles","data_extractor_file")

# class UpdateJsonFile :
#     def update_json_data (self , data,new_part_num,new_qty,new_lot_num,new_manuf_data):
#         json_part_num , json_qty, json_lot_num, json_manuf_data = data['partNumber'],data['quantity'],data['lotNumber'],data['manufDate']

#         if new_part_num not in json_part_num and new_part_num != "" and new_part_num != None:
#             json_part_num.append(new_part_num)
            
#         if new_qty not in json_qty and new_qty != "" and new_qty != None:
#             json_qty.append(new_qty)

#         if new_lot_num not in json_lot_num and new_lot_num != "" and new_lot_num != None:
#             json_lot_num.append(new_lot_num)
        
#         if new_manuf_data not in json_manuf_data and new_manuf_data != "" and new_manuf_data != None:
#             json_manuf_data.append(new_manuf_data)
#         pass

#     def write_json_file(self,text_data,replace_chars,delimiters,company_list,ecia_standard_data =[] , non_ecia_standard_data =[]):
#         updated_data = {
#             "text_data": text_data,
#             "ecia_standard_data": ecia_standard_data,
#             "non_ecia_standard_data":non_ecia_standard_data,
#             "replace_chars": replace_chars,
#             "delimiters": delimiters,
#             "company_list": company_list,
#         }
#         json_file_load.json_data_write(data_extractor_file_path, updated_data)
