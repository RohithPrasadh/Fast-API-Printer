# import base64,cv2,logging
# from ultralytics import YOLO
# from config.config_parser import config

# logger = logging.getLogger(__name__)
# reel_detection_model_path = config.get("YOLO", "bestpt_detect")
# reel_detection_model = YOLO(reel_detection_model_path)


# class DetectionModel:
#     @staticmethod
#     # def detect_object(image):
#     #     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     #     results = reel_detection_model.predict(image,conf =0.7)#save_crop=True
#     #     stickers = []
#     #     reel = None
#     #     for r in results:
#     #         boxes = r.boxes
#     #         for box in boxes:
#     #             if (box.cls == 0) or (box.cls == 1):
#     #                 x1, y1, x2, y2 = box.xyxy[0].cpu().detach().numpy().round().astype(int)
#     #                 reel = image[y1:y2, x1:x2]
#     #         for box in boxes:
#     #             if box.cls == 2:

#     #                 sx1, sy1, sx2, sy2 = box.xyxy[0].cpu().detach().numpy().round().astype(int)                   
#     #                 if ((sx1>x1) and (sx2<x2)) and ((sy1>y1) and (sy1<sy2)):
#     #                     print("am inside the reeel")
#     #                     sticker=image[sy1:sy2, sx1:sx2]
#     #                     stickers.append(sticker)
#     #         return reel, stickers
#     def detect_object(image):
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         results = reel_detection_model.predict(image,save_crop=True) 
#         print(results) # device=0 (only for cuda) ,save_crop=True
#         stickers = []
#         reel = None
#         for r in results:
#             boxes = r.boxes
#             for box in boxes:
#                 if box.cls == 2:
#                     x1, y1, x2, y2 = box.xyxy[0].cpu().detach().numpy().round().astype(int)
#                     sticker = image[y1:y2, x1:x2]
#                     stickers.append(sticker)
  
#                 if (box.cls == 0) or (box.cls==1):
#                         x1, y1, x2, y2 = box.xyxy[0].cpu().detach().numpy().round().astype(int)
#                         reel = image[y1:y2, x1:x2]
#                         print("I am detected packet/reel")
#         print(len(stickers))
#         return reel,stickers

# class ConvBase64:
#     @staticmethod
#     def conv_base64(image):
#         try:
#             _, buffer = cv2.imencode(".jpg", image)
#             reel_base64 = base64.b64encode(buffer).decode("utf-8")
#             return reel_base64
#         except Exception as e:
#             logger.error(f"Base-64 Conversion Error: {str(e)}", exc_info=True)
#             return None
