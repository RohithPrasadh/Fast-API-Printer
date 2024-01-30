# import logging,cv2, json
# import datetime , re
# from typing import Any
# from config.config_parser import config
# from models import UniqueIDGenerator
# # from utils import PrintBarcode, UserResponse, create_unique_id, similar
# # from utils.print_barcode import PrintBarcode
# from utils.response import UserResponse
# from utils.index import create_unique_id
# from utils.index import similar

# from .barcode_reader import BarcodeQRCodeScanner
# from .camera import Camera
# from .classification import ClassificationModel
# from .detection import ConvBase64, DetectionModel
# from .skew_correction import SkewnessCorrection
# from .master_datasheet import MasterDataInfo
# from utils.database import db
from utils.print_barcode import PrintBarcode

# from utils.index import notify_extraction_completed
# from datetime import datetime
# from utils import date_conversion

# logger = logging.getLogger(__name__)
# prefix = config.get("UniqueId", "final_prefix")
# json_file_url = config.get('JsonFile','json_url')
# date_converter = date_conversion.DateFormatConverter()
# logger = logging.getLogger(__name__)
# collection_reelstock = config.get("MongoDb", "collection_reelstock")
# # collection_Original = config.get("MongoDb", "collection_original_data")
# # collection_extractedSticker = config.get("MongoDb", "collection_extractedSticker")

# collection_setting = config.get("MongoDb", "collection_settings")
# sticker_folder_path = config.get("Output", "sticker_output_folder")
# # collection_print_setting = db[collection_setting]

# collection_reelstock = db[collection_reelstock]
# # collection_Original = db[collection_Original]
# # collection_extractedSticker = db[collection_extractedSticker]

# table_row_num = config.getint("TableList", "max_row")
# barcode_type = config.get('Barccode','barcode_type')
# barcode_prefix = config.get("UniqueId", "final_prefix")

print_qrcode = PrintBarcode()

class Extraction:
    # @staticmethod
#     def capture_raw_image(camera: Camera) -> UserResponse:
#         response = UserResponse()
#         response.image = camera.get_image()
#         return response

#     @staticmethod
#     def identify_sticker(camera: Camera, image) -> UserResponse:
#         response = UserResponse()
#         reel, detected_stickers = DetectionModel.detect_object(image)
#         response.reel, response.detected_stickers = reel, detected_stickers

#         if (reel is None) and (len(detected_stickers) != 0):
#             response.alert = "Poor lighting conditions turn the reel/packet"
#             response.has_errors = True
#             return response

#         if detected_stickers is None:
#             logger.error("detection_stickers is None.")
#             response.error = "Placed Oject is Not a Reel"  
#             response.has_errors = True
#             camera.release()
#             return response

#         if reel is None:
#             response.error = "Please Place The Reel/Packet"
#             response.has_errors = True
#             return response

#         response.reel_image = ConvBase64.conv_base64(reel)
#         return response

#     @staticmethod
#     def get_sticker_images(stickers):
#         rotated_images = SkewnessCorrection.correct_perspective(stickers)
#         aligned_images = ClassificationModel.classify_rotation(rotated_images)
#         return aligned_images
    
#     @staticmethod
#     def json_data_dump(data):
#         with open(json_file_url, 'w') as f:
#             json.dump(data, f)
    
    
#     @staticmethod
#     def get_extracted_item(extract: dict, reel_image) -> UserResponse:
#         print("get_extracted_item", extract)
#         response = UserResponse()
#         if (
#             extract["partNumber"] == 'Not Available'
#             or extract["quantity"] == 'Not Available'
#             or extract["partNumber"] == 'Not Available'
#             or extract["quantity"] == 'Not Available'
#         ):
#             print("thi extract")
#             response.has_errors = True
#             response.error = "Mandatory Fields are Missing hence data is not stored"
#         else:
#             print("else")
#             # breakpoint()
#             # manuf_date=extract["manufDate"]
#             # manuf_date=date_converter.date_format_conversion(extract["manufDate"])                                      # NEW 
#             qty = extract["quantity"]

#             processed_qty = re.sub(r'\D', '', qty)
#             unique_id = create_unique_id(prefix)
#             current_datetime = datetime.now()

#             # Format datetime strings
#             created_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
#             date_of_receipt = current_datetime.strftime("%Y-%m-%d")
#             # Check if manufDate is 'Not Available' or empty
#             if not extract["manufDate"] or extract["manufDate"] == 'Not Available':
#                 manuf_date = created_date
#             else:
#                 manuf_date = extract["manufDate"] 
#                 manuf_date=date_converter.date_format_conversion(extract["manufDate"] )
#                 print("sdsdfdsfdsfdsfds")

#             # expiryDate = (datetime.datetime.now().date()+ datetime.timedelta(days=365 * 3)).strftime("%m/%d/%Y")
#             unique_identifier = UniqueIDGenerator.generate_unique_id()
#             unique_id = create_unique_id(barcode_prefix)

#             response.item = {
#                 # "manufacturer": extract["manufacturer"],
#                 "barcode": unique_id,
#                 "partNumber": extract["partNumber"],
#                 "quantity": processed_qty,
#                 "manufDate": manuf_date,                                                                                               
#                 "originalData": extract,
#                 "uniqueIdentifier": unique_identifier,
#                 "lotNumber": extract["lotNumber"],
#                 "interpn_number": extract["interpn_number"],
#                 "dateOfReceipt": date_of_receipt,
#                 "extractedSticker": reel_image,
#                 "createdAt": created_date,
#                 "updatedAt": created_date,                                                                          
#                 # "expiryDate": expiryDate,
#                 "entry_preferences": "Automatic",
#                 "is_deleted":False,
#                 # "receiptNumber":extract["receiptNumber"]
#             }
#             print("sdsadasdasdsadasdsawqeq")
#         return response

    @staticmethod
    def print_bar_code(item: dict) -> None:
        # print("print",item)
        data = item["barcode"]
        unique_identifier = item["uniqueIdentifier"]
        print(item["scanner"])
        if item["scanner"] == "1":
            PrintBarcode.print_barcode_data(data, unique_identifier,item)
        elif item["scanner"] == "3":

            PrintBarcode.print_datamatrix_data(
                item
            )
        elif item["scanner"] == "4":
            PrintBarcode.print_pdf417_data(
               item
            )
        else:
           
            PrintBarcode.print_qrcode_data(item 
            )


#     def get_bar_code_details(img, idx,final_extract):
#         print("ytsadsa",img, idx,final_extract)
#         decoded_barcodedata,qr_barcode_data = BarcodeQRCodeScanner().decode_barcode(img)
#         print(decoded_barcodedata,"decoded_barcodedata")
#         if len(qr_barcode_data) > 0:
#             print("QR decoded_barcodedata without formatting :",qr_barcode_data)
#             final_extract = BarcodeQRCodeScanner.parse_1Pdecoded_data(qr_barcode_data,final_extract)
#         elif len(decoded_barcodedata) > 0:
#             print("decoded_barcodedata without formatting :",decoded_barcodedata)
#             final_extract = BarcodeQRCodeScanner.parse_1Pdecoded_data(decoded_baextraction.capturercodedata,final_extract)
#         ocr_data = BarcodeQRCodeScanner.extract_ocr_data(img)
#         print("OCR DATA:" , ocr_data)
#         if len(decoded_barcodedata) > 0:
#             final_extract = BarcodeQRCodeScanner.parse_non1P_data(ocr_data,decoded_barcodedata,final_extract)
#         if len(decoded_barcodedata) > 0:
#             final_extract = BarcodeQRCodeScanner.parse_non1P_data(ocr_data,decoded_barcodedata,final_extract)
        
#         if len(ocr_data) > 0:
#             final_extract=BarcodeQRCodeScanner.parse_textdata(ocr_data,final_extract)
#             final_extract = BarcodeQRCodeScanner.manufacturer_data(final_extract)
#         return final_extract
