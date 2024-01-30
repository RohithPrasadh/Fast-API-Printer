# import calendar
# import datetime
# import time
# from difflib import SequenceMatcher
# import pygame
# from .database import db
# # from .excel_pdf_generation import Download_pdf_excel
# # from .print_barcode import PrintBarcode
# from .response import UserResponse

# def create_unique_id(prefix: str) -> str:
#     gmt = time.gmtime()
#     ts = calendar.timegm(gmt)
#     current_timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
#     custom_timestamp = prefix + str(ts)
#     return custom_timestamp

# def notify_extraction_completed():
#     pygame.mixer.init()
#     pygame.mixer.music.load(r"polaroid-camera-take-picture-01.wav")
#     pygame.mixer.music.play()


# def similar(str1, str2):
#     return SequenceMatcher(None, str1, str2).ratio()
