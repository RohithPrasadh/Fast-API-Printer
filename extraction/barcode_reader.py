# from datetime import date
# import zxingcpp ,json
# from paddleocr import PaddleOCR
# from config.config_parser import config
# from utils import json_load ,format_keys,sorter
# import re
# import json

# json_file_load = json_load.json_file_read()
# ocr = PaddleOCR(use_gpu=True,use_angle_cls=False, lang='en',show_log=False)
# data_extractor_file_path = config.get("JsonFiles","data_extractor_file")
# keys_format = format_keys.FormatNonEciaKeys()
# sort_keys=sorter.SortKeys()

# class BarcodeQRCodeScanner:
#     def flat(self, lis):
#         flatList = []
#         for element in lis:
#             if type(element) is list:
#                 for item in element:
#                     flatList.append(item)
#             else:
#                 flatList.append(element)
#         return flatList

#     def decode_barcode(self, image):
#         json_data_file = json_file_load.json_data_load(data_extractor_file_path)
#         delimiters = json_data_file["delimiters"]
#         print(json_data_file,delimiters)
#         decoded_data = []
#         qr_decoded_data = []
#         reader = zxingcpp.read_barcodes(image)
#         if len(reader) == 0:
#             print("\tCould not find any barcode.")
#         else:
#             for result in reader:
#                 print("\t Text:    '{}'\t Format:   {}".format(result.text, result.format))
#                 if (str(result.format) == "BarcodeFormat.Code128") or (
#                     str(result.format) == "BarcodeFormat.Code39"
#                 ):
#                     print(type(result.text),result.text)
#                     decoded_data.append(result.text)
#                 elif (
#                     (str(result.format) == "BarcodeFormat.DataMatrix")
#                 ):
#                     for d in delimiters:
#                         if d in result.text:
#                             d1 = result.text.split(d)
#                             qr_decoded_data.append(self.flat(d1))
#                             break
#                 else:
#                     if(str(result.format) != "BarcodeFormat.QRCode"):
#                         decoded_data.append(result.text)
#                     else:
#                         print("invalid type:", result.format, result.text)

#         decoded_data1 = [s.rstrip('\r') for s in decoded_data]
#         print(decoded_data1,"decoded_data1")
#         return self.flat(decoded_data),self.flat(qr_decoded_data)
    


#     @staticmethod
#     def parse_1Pdecoded_data(decoded_data,final_extract):
#         json_data_file = json_file_load.json_data_load(data_extractor_file_path)
#         json_data_file_ecia_standards = json_data_file["ecia_standard_data"]

#         part_number_list = json_data_file_ecia_standards["partNumber"]
#         quantity_list = json_data_file_ecia_standards["quantity"]
#         lot_list = json_data_file_ecia_standards["lotNumber"]
#         date_list = json_data_file_ecia_standards["manufDate"]
#         delimiter = ","
#         part_no_keys=[]
#         lot_no_keys = []
#         qty_keys = []
#         date_keys = []

#         part_no_keys = sort_keys.sorter(part_number_list)
#         lot_no_keys = sort_keys.sorter(lot_list)
#         qty_keys = sort_keys.sorter(quantity_list)
#         date_keys = sort_keys.sorter(date_list)

#         part_no_keys = keys_format.replace_chars(part_number_list)
#         lot_no_keys = keys_format.replace_chars(lot_list)
#         qty_keys = keys_format.replace_chars(quantity_list)
#         date_keys = keys_format.replace_chars(date_list)

#         delimiter = ","  
#         part_number_concatenated=""
#         part_number_count=0
#         lot_numbers_concatenated = ""   
#         lot_match_count = 0
    
#         for value in decoded_data:
#             print("value:",value,' ',type(value))
#             for pt_no_key in part_no_keys:
#                 print(pt_no_key ,"pt_no_key")
#                 len_pt_no_key = len(pt_no_key)
                
#                 if value[:len_pt_no_key] ==  pt_no_key:
#                     part_number_count += 1
#                     part_number_concatenated = value[len_pt_no_key:]
#                     print(part_number_count,"part_number_count")
#                     if part_number_count > 1:
#                         part_number_concatenated = final_extract["partNumber"].upper()+ delimiter + part_number_concatenated.upper()
#                     final_extract["partNumber"] = part_number_concatenated           

#             for lot_key in lot_no_keys:
#                 print(lot_key, "lot_no_keys")
#                 len_lot_no_key = len(lot_key)
#                 if value[:len_lot_no_key] == lot_key:
#                     lot_match_count += 1
#                     lot_numbers_concatenated = value[len_lot_no_key:]
#                     if lot_match_count > 1:
#                         lot_numbers_concatenated = final_extract["lotNumber"].upper()+ delimiter + lot_numbers_concatenated .upper()
#                     final_extract["lotNumber"] = lot_numbers_concatenated




#             for dt_key in date_keys:
#                 print(dt_key ,"date_keys")
#                 len_dt_key = len(dt_key)
#                 if value[:len_dt_key] ==  dt_key:
#                     final_extract['manufDate'] = value[len_dt_key:]
#                     print("Match found for", value[len_dt_key:] + dt_key)


#             for qty in qty_keys:
#                print(qty ,"qty_keys")
#                len_qty = len(qty)
#                if value[:len_qty] == qty:
#                     final_extract['quantity'] = value[len_qty:]

#         print("final_extract from 1p decoded data:",final_extract)
#         return final_extract

        
#     def parse_non1P_data(ocr_data,decoded_data,final_extract):
#         non_standard_data = json_file_load.json_data_load(data_extractor_file_path)
#         pd_replace_chars = non_standard_data["replace_chars"]
#         non_standard_data = non_standard_data["text_data"]
#         part_number_list = non_standard_data['partNumber']
#         quantity_list = non_standard_data['quantity']
#         lot_list = non_standard_data['lotNumber'] 
#         date_list = non_standard_data['manufDate']
        
#         part_no_keys=[]
#         lot_no_keys = []
#         qty_keys = []
#         date_keys = []

#         part_no_keys = sort_keys.sorter(part_number_list)
#         lot_no_keys = sort_keys.sorter(lot_list)
#         qty_keys = sort_keys.sorter(quantity_list)
#         date_keys = sort_keys.sorter(date_list)

#         part_no_keys = keys_format.replace_chars(part_number_list)
#         lot_no_keys = keys_format.replace_chars(lot_list)
#         qty_keys = keys_format.replace_chars(quantity_list)
#         date_keys = keys_format.replace_chars(date_list)
        
#         for ele in decoded_data:
#             print("running for ele in parse 1p data part number:",ele)
#             ocr_data = ocr_data.upper()
#             if ele in ocr_data:
#                 idx = ocr_data.index(ele)
#                 if final_extract['partNumber'] == 'Not Available':
#                     for part_no in part_no_keys:
#                         len_part_no = len(part_no)
#                         start = idx - len_part_no
#                         compare_part_no = ocr_data[start:idx]
#                         if compare_part_no == part_no:
#                             final_extract['partNumber'] = ele.upper()
#                             break
#                 if final_extract['lotNumber'] == 'Not Available':
#                     for lot_no in lot_no_keys:
#                         len_lot_no = len(lot_no)
#                         start = idx - len_lot_no
#                         compare_lot_no = ocr_data[start:idx]
#                         if compare_lot_no == lot_no:
#                             final_extract['lotNumber'] = ele
#                             break
#                 if final_extract['quantity'] == 'Not Available':
#                     for qty in qty_keys:
#                         len_qty = len(qty)
#                         start = idx - len_qty
#                         compare_qty = ocr_data[start:idx]
#                         if compare_qty == qty:
#                             final_extract['quantity'] = ele
#                             break
#                 if final_extract['manufDate'] == 'Not Available':
#                     for dte in date_keys:
#                         len_date = len(dte)
#                         start = idx - len_date
#                         compare_dte = ocr_data[start:idx]
#                         if compare_dte == dte:
#                             final_extract['manufDate'] = ele
#                             break
#         print("Final Extract from parse_non1P_data:",final_extract)
#         return final_extract
    


#     def extract_ocr_data(img):  
#         json_data_file = json_file_load.json_data_load(data_extractor_file_path)
#         pd_replace_chars = json_data_file["replace_chars"]
#         ocr_data = []
#         ocr_data1 = []
#         result = ocr.ocr(img)
#         if not None in result:
#             for res in result:
#                 for line in res:
#                     ocr_data.append(str(line[1][0]))
#             for ele in ocr_data:
#                 str1 = ''
#                 for c in ele:
#                     if c not in pd_replace_chars:
#                         str1+=c
#                 ocr_data1.append(str1)
#             ocr_data = ' '.join(ocr_data1)
#         return ocr_data   

#     @staticmethod
#     def parse_textdata(ocr_data,final_extract):
#             non_standard_data = json_file_load.json_data_load(data_extractor_file_path)
#             pd_replace_chars = non_standard_data["replace_chars"]
#             non_standard_data = non_standard_data["text_data"]
#             part_number_list = non_standard_data['partNumber']
#             quantity_list = non_standard_data['quantity']
#             lot_list = non_standard_data['lotNumber'] 
#             date_list = non_standard_data['manufDate']
            
#             part_no_keys=[]
#             lot_no_keys = []
#             qty_keys = []
#             date_keys = []

#             part_no_keys = sort_keys.sorter(part_number_list)
#             lot_no_keys = sort_keys.sorter(lot_list)
#             qty_keys = sort_keys.sorter(quantity_list)
#             date_keys = sort_keys.sorter(date_list)  

#             part_no_keys = keys_format.replace_chars(part_number_list)
#             lot_no_keys = keys_format.replace_chars(lot_list)
#             qty_keys = keys_format.replace_chars(quantity_list)
#             date_keys = keys_format.replace_chars(date_list)
            
            
#             all_keys=part_no_keys+lot_no_keys+qty_keys+date_keys
#             for key in all_keys:
#                 match = re.search(rf'\b{re.escape(key)}\b', ocr_data)
#                 if match:
#                     ocr_data = ocr_data[:match.end() ] + ocr_data[match.end():].lstrip()
#             for ele in part_no_keys:
#                 print("running for ele in text data in part number:",ele)
#                 if ele in ocr_data:
#                     print("found element ",ele)
#                     idx = ocr_data.index(ele)
#                     print(idx)
#                     len_part_no = len(ele)
#                     print(len_part_no)
#                     start = idx+len_part_no
#                     part_no_val = ''
#                     if (final_extract['partNumber'] == 'Not Available') or (len(final_extract['partNumber'].strip())==0):
#                         print("here inside partNumber")
#                         query_string = ocr_data[start:]
#                         for c in query_string:
#                             if c ==  ' ':
#                                 break
#                             else:
#                                 part_no_val+= c
                        
#                         final_extract['partNumber'] = part_no_val.upper()

#             for ele in lot_no_keys:
#                 print("running for ele in text data in lot number",ele)
#                 if ele in ocr_data:
#                     idx = ocr_data.index(ele)
#                     len_lot_no = len(ele)
#                     start = idx+len_lot_no
#                     lot_no_val = ''
#                     if final_extract['lotNumber'] == 'Not Available' or (len(final_extract['lotNumber'].strip())==0):
#                         print("here inside lotNumber")
#                         query_string = ocr_data[start:]
#                         for c in query_string:
#                             if c ==  ' ':
#                                 break
#                             else:
#                                 lot_no_val+= c
#                         final_extract['lotNumber'] = lot_no_val

#             for ele in qty_keys:
#                 print("running for ele in text data in quantity number:",ele)
#                 if ele in ocr_data:
#                     idx = ocr_data.index(ele)
#                     len_qty = len(ele)
#                     start = idx+len_qty
#                     qty_val = ''
#                     if final_extract['quantity'] == 'Not Available' or (len(final_extract['quantity'].strip())==0):
#                         print("here inside quantity")
#                         query_string = ocr_data[start:]
#                         for c in query_string:
#                             if c ==  ' ':
#                                 break
#                             else:
#                                 qty_val+= c
#                         final_extract['quantity'] = qty_val

#             for ele in date_keys:
#                 print("running for ele in text data in manuf date",ele)
#                 if ele in ocr_data:
#                     idx = ocr_data.index(ele)
#                     len_date = len(ele)
#                     start = idx+len_date
#                     date_val = ''
#                     if final_extract['manufDate'] == 'Not Available' or  (len(final_extract['quantity'].strip())==0):
#                         print("here inside manufDate")
#                         query_string = ocr_data[start:]
#                         for c in query_string:
#                             if c ==  ' ':
#                                 break
#                             else:
#                                 date_val+= c
#                         final_extract['manufDate'] = date_val
#             print("Final Extract from parse_textdata",final_extract)
#             return final_extract


#     # @staticmethod
#     def manufacturer_data(final_extract):
#         print("Inside manufacture details")
#         # if final_extract["partNumber"] is not None:
#         #     final_extract=BarcodeQRCodeScanner.update_partNumber(final_extract)
#         # print(results)
#         # final_extract["companyName"]=results["manufacturer"]
#         return final_extract
  
#     @staticmethod
#     def update_partNumber(final_extract):
#         results=map_internal.map_partNumber_internalpartNumber(final_extract)
#         print(results)
#         if results is not None:
#             final_extract["partNumber"]=results["partNumber"]
#         print("checking internalpart number: ",final_extract["partNumber"],results["partNumber"])
#         return final_extract

#     # @staticmethod
#     # # def map_lot_yageo(ocr_data,final_extract):
#     # #     if final_extract["companyName"]=="YAGEO":
#     # #         for i in range(len(ocr_data)):
#     # #             if ocr_data[i:] in final_extract['lotNumber']:
#     # #                 final_extract['lotNumber'] = ocr_data[i:]
#     # #                 break
#     # #     return final_extract

