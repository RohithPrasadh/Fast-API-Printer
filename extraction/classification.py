# import logging
# import pathlib
# import platform
# import cv2
# from ultralytics import YOLO
# from config.config_parser import config

# logger = logging.getLogger(__name__)
# plt = platform.system()
# if plt == "Linux":
#     pathlib.WindowsPath = pathlib.PosixPath

# classification_model_path = config.get("YOLO", "bestpt_classify")
# classification_model = YOLO(classification_model_path)


# class ClassificationModel:
#     @staticmethod
#     def classify_rotation(images):
#         try:
#             sticker_image = None
#             classified_stickers = []
#             for c in images:
#                 results = classification_model.predict(c) 
#                 if results is not None:
#                     names_dict = results[0].names
#                     probs = results[0].probs.top1
#                     class_name = names_dict[probs]
#                 if class_name == "0":
#                     sticker_image = c
#                     classified_stickers.append(sticker_image)
#                 elif class_name == "90":
#                     sticker_image = cv2.rotate(c, cv2.ROTATE_90_CLOCKWISE)
#                     classified_stickers.append(sticker_image)
#                 elif class_name == "180":
#                     sticker_image = cv2.rotate(c, cv2.ROTATE_180)
#                     classified_stickers.append(sticker_image)
#                 elif class_name == "270":
#                     sticker_image = cv2.rotate(c, cv2.ROTATE_90_COUNTERCLOCKWISE)
#                     classified_stickers.append(sticker_image)
#             return classified_stickers
#         except Exception as e:
#             logger.error(f"Classification Error: {str(e)}", exc_info=True)
