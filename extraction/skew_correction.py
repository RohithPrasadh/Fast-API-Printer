# import logging ,imutils ,cv2,math
# import numpy as np

# logger = logging.getLogger(__name__)

# class SkewnessCorrection:
#     @staticmethod
#     def correct_perspective(input_images):
#         rotated_images = []
#         for r in input_images:
#             rotated_ = None
#             h, w = r.shape[:2]
#             assert type(r) == np.ndarray
#             kernel = np.ones((4, 4), np.uint8)
#             gray_image = cv2.dilate(r, kernel, iterations=3)
#             edges = cv2.Canny(gray_image, 30, 100, apertureSize=3)
#             lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=350, maxLineGap=10)
#             # print("hougue line created 350:",lines)
#             if lines is None:
#                 lines = cv2.HoughLinesP(
#                     edges, 1, np.pi / 180, threshold=100, minLineLength=300, maxLineGap=10
#                 )
#                 # print("hougue line created 300:",lines)
#                 if lines is None:
#                     lines = cv2.HoughLinesP(
#                         edges, 1, np.pi / 180, threshold=100, minLineLength=250, maxLineGap=10
#                     )
#                     # print("hougue line created 250:",lines)
#                     if lines is None:
#                         lines = cv2.HoughLinesP(
#                             edges, 1, np.pi / 180, threshold=100, minLineLength=200, maxLineGap=10
#                         )
#                         # print("hougue line created 200:",lines)
#                         if lines is None:
#                             lines = cv2.HoughLinesP(
#                                 edges, 1, np.pi / 180, threshold=100, minLineLength=150, maxLineGap=10
#                             )
#                             # print("hougue line created 150:",lines)
#                             if lines is None:
#                                 lines = cv2.HoughLinesP(
#                                     edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10
#                                 )
#                                 # print("hougue line created 100:",lines)
#                                 if lines is None:
#                                     lines = cv2.HoughLinesP(
#                                         edges,
#                                         1,
#                                         np.pi / 180,
#                                         threshold=50,
#                                         minLineLength=100,
#                                         maxLineGap=10,
#                                     )
#             parallel_lines_image = r.copy()
#             parallel_line_distance = 10
#             angle = 0
#             angle1 = 0
#             angle2 = 0
#             dy = 0
#             dx = 0
#             if lines is not None:
#                 for line in lines:
#                     x1, y1, x2, y2 = line[0]
#                     if (x2 - x1 != 0) and (y2 - y1 != 0):
#                         slope = (y2 - y1) / (x2 - x1)
#                         parallel_x1 = int(x1 - parallel_line_distance)
#                         parallel_y1 = int(y1 - parallel_line_distance * slope)
#                         parallel_x2 = int(x2 - parallel_line_distance)
#                         parallel_y2 = int(y2 - parallel_line_distance * slope)
#                         cv2.line(
#                             parallel_lines_image,
#                             (parallel_x1, parallel_y1),
#                             (parallel_x2, parallel_y2),
#                             (0, 0, 255),
#                             2,
#                         )
#                         point1, point2 = (
#                             (parallel_x1, parallel_y1),
#                             (parallel_x2, parallel_y2),
#                         )
#                         dx = point2[0] - point1[0]
#                         dy = point2[1] - point1[1]
#                         angle = math.degrees(math.atan2(dy, dx))
#                         angle1 = angle * -1
#                         angle2 = (angle * -1) + 180
#                         break
#                     elif y2 - y1 == 0:
#                         angle1 = 90
#                     elif x2 - x1 == 0:
#                         angle1 = 90
#                 if (abs(dx) > abs(dy)) and (h > w):
#                     angle1 += 90
#                 elif abs(dy) > abs(dx) and (w > h):
#                     angle1 += 90
#                 elif (abs(dx) != 0) and (abs(dy) != 0):
#                     if abs(dy) == abs(dx) and (h > w):
#                         angle1 += 90
#                 elif (angle1 and angle2) == 0:
#                     if (dx and dy) == 0:
#                         angle1 = 180
#                 rotated_ = imutils.rotate_bound(r, angle1)
#                 rotated_images.append(rotated_)
#         return rotated_images
