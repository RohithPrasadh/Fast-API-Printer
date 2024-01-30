# import json,logging,cv2,requests
# from datetime import date
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import JSONResponse
# from bson import json_util,ObjectId
# # from django.http import HttpResponse, JSONResponse
# # from django.shortcuts import render,redirect
# # from django.views.decorators.csrf import csrf_exempt
# from config.config_parser import config
# from .camera import Camera
from .extraction import Extraction as IE
# # from master_datasheet import master_datasheet as ED
# from utils.response import UserResponse
# from utils.database import db
# from utils.index import notify_extraction_completed
# from utils.json_load import json_file_read

# logger = logging.getLogger(__name__)
# collection_reelstock = config.get("MongoDb", "collection_reelstock")
# # collection_original_data = config.get("MongoDb", "collection_original_data")
# # collection_extractedSticker = config.get("MongoDb", "collection_extractedSticker")
# collection_printer = config.get("MongoDb", "collection_printer")
# sticker_folder_path = config.get("Output", "sticker_output_folder")   
# collection_print_setting = db[collection_printer]
# collection_reelstock = db[collection_reelstock]
# # collection_original_data = db[collection_original_data]
# # collection_extractedSticker = db[collection_extractedSticker]  
# # collection_invoicedata = config.get("MongoDb", "collection_invoice_data")
# # csv_data_path = config.get("CSVData", "csv_data_path")
# # invoice_data_file = config.get("ExcelData","invoice_data_path")
# # collection_invoicedata = db[collection_invoicedata]

# table_row_num = config.getint("TableList", "max_row")
# json_file_load = json_file_read()

# def capture_image():
#     projection = {
#         "extractedSticker": 0,
#     }
   
#     x=0
#     final_extract = {
#             "partNumber": 'Not Available',
#             "quantity": 'Not Available',
#             "lotNumber": 'Not Available',
#             "manufDate": date.today().strftime("%d/%m/%Y"),
#             "companyName": 'Not Available',
#             "dateOfReceipt": date.today().strftime("%d/%m/%Y"),
#             "interpn_number": 'Not Available',
#             # "receiptNumber":inv_number
#         }
#     try:
#         try:
#             camera = Camera()
#             img_response = IE.capture_raw_image(camera)
#         except Exception as e:
            
#             logger.error(f"Camera Device Error:{str(e)}")
#             img_response = UserResponse()
#             img_response.has_errors = True 
#             img_response.error = "Camera Device Not Connected"
#             return img_response.error

#         if img_response.has_errors:
#             return JSONResponse(img_response.json)

#         sticker_response = IE.identify_sticker(camera, img_response.image)
#         if sticker_response.has_errors:
#             return JSONResponse(sticker_response.json)

#         try:
#             aligned_images = IE.get_sticker_images(sticker_response.detected_stickers)
#             print(len(aligned_images),"aligned_images")
#             for idx, img in enumerate(aligned_images): 
#                 cv2.imwrite(f"{sticker_folder_path}save"+str(x).zfill(3)+".jpg",img)
#                 print(f"Running for {idx}")
#                 final_extract= IE.get_bar_code_details(img, idx,final_extract)  
#                 print(final_extract ,"final_extract")
#                 x+=1
  
#             item_response = IE.get_extracted_item(final_extract, sticker_response.reel_image)       
#             if item_response.has_errors:
#                 return JSONResponse(item_response.has_errors)
#             response = UserResponse()
            
#             IE.json_data_dump(item_response.item)
#             notify_extraction_completed()
                
#             # Print barcode
#             # barcode_scanner = collection_print_setting.find_one({"id": 1})
#             # IE.print_bar_code(item_response.item, barcode_scanner)

#             # Inserting data to database
#             # print(item_response.item,"item_response")    # print("scanner ................")
#     # extracted_info = CR()
#     # return {"data": extracted_info}

#             # origina_data = collection_original_data.insert_one(item_response.item["original_data"])
#             # extracted_sticker_result = collection_extractedSticker.insert_one(item_response.item["extracted_sticker"])

#             # collection_reelstock.insert_one(item_response.item)
#             # if '_id' in item_response.item:
#             #     item_response.item.pop('_id')
#             return item_response.item

#         except Exception as e:
#             logger.error(f"Error: {str(e)}")    # print("scanner ................")
#     # extracted_info = CR()
#     # return {"data": extracted_info}
#             response = UserResponse()
#             response.error = f"Error: {str(e)}"
#             camera.release()
#             return JSONResponse(response.json)
        
#     except Exception as e:
        
#         logger.error(f"Error: {str(e)}")
#         return JSONResponse({"error": "Internal Server Error"}, status=500)
    
def print_barCode(final_data):
    IE.print_bar_code(final_data)