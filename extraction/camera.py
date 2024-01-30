# from typing import Any
# from pypylon import pylon
# from config.config_parser import config

# class Camera:
#     def __init__(self) -> None:
#         try:
#             self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
#             print("Camera Connected")
#         except Exception as e:
#             print(f"Error initializing the camera: {e}")
#         self.grab_time = config.getint("Camera", "grab_time")
#         self.grab_time = 5000
#         self.grab_result = None

#     def get_image(self) -> Any:
#         self.camera.Open()
#         self.grab_result = self.camera.GrabOne(self.grab_time)
#         return self.grab_result.Array

#     def release(self) -> None:
#         self.grab_result.Release()
#         self.camera.Close()
    
