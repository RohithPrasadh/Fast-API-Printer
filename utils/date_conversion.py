# from dateutil import parser
# from datetime import datetime, timedelta

# class DateFormatConverter:
#     @staticmethod
#     def date_format_conversion(input_date_string):
#         if len(input_date_string) == 4:
#             year = int(input_date_string[:2]) + 2000
#             week_number = int(input_date_string[2:])
#             first_day_of_week = datetime.fromisocalendar(year, week_number, 1)
#             formatted_date = first_day_of_week.strftime('%y/%m/%d')
#             print(formatted_date, "first_day_of_week")
#             return formatted_date

#         elif len(input_date_string) == 6:
#             input_date_string = input_date_string[0:4]
#             print(input_date_string)
#             year = int(input_date_string[:2]) + 2000
#             week_number = int(input_date_string[2:])
#             first_day_of_week = datetime.fromisocalendar(year, week_number, 1)
#             formatted_date = first_day_of_week.strftime('%y/%m/%d')
#             print(formatted_date, "first_day_of_week")
#             return formatted_date

#         else:
#             if '+' in input_date_string:
#                 parts = input_date_string.split('+')
#                 base_year = int(parts[0])
#                 years_to_add = int(parts[1])
#                 target_date = datetime(base_year, 1, 1) + timedelta(days=years_to_add * 365)
#                 formatted_date = target_date.strftime('%y/%m/%d')
#                 print(formatted_date, "formatted_date")
#                 return formatted_date
#             else:
#                 input_date_string = input_date_string.replace('-', '/')
#                 formatted_date = parser.parse(input_date_string, dayfirst=True)
#                 formatted_date_str = formatted_date.strftime('%d/%m/%y')
#                 print(formatted_date_str, "formatted_date")
#                 return formatted_date_str