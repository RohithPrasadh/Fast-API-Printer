
# import csv
# import json
# from config.config_parser import config
# import pandas as pd





# @staticmethod
# def append_json_to_csv(input_data):
#     csv_file_path = "reels_info/csv_files/IINVOICE.csv"
#     column_mapping = {
#             'invoiceNumber': 'Invoice No.',
#         'partNumber': 'MPN',
#         'quantity': 'Invoice Qty',
        
#         # Add other mappings as needed
#     }

#     with open(csv_file_path, mode='a', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=list(column_mapping.values()))

#         # Check if the file already has a header
#         if file.tell() == 0:
#             writer.writeheader()

#         # Extracting specific fields based on the mapping
#         extracted_data = {csv_header: input_data.get(data_key, '') for data_key, csv_header in column_mapping.items()}

#         # Append the data
#         writer.writerow(extracted_data)

#     def analyseInvoice(csv,excel):

#         csv_df=pd.read_csv(csv)
#         excel_df=pd.read_excel(excel)
#         print(csv_df.columns)
#         print(excel_df.columns)
#         csv_df['Invoice Qty'] = pd.to_numeric(csv_df['Invoice Qty'], errors='coerce')
#         aggregated_df = csv_df.groupby(['Invoice No.', 'MPN']).agg({'Invoice Qty': 'sum'}).reset_index()
#         print(aggregated_df)
#         merged_df = pd.merge(excel_df, aggregated_df, how='left', on=['Invoice No.', 'MPN'])
#         merged_df["Completed"]=(merged_df["Invoice Qty_y"]/excel_df['Invoice Qty'])*100
#         final_df = merged_df[['Invoice No.', 'Invoice Date', 'MPN', 'Parts Name', 'Maker', 'Invoice Qty_x', 'Invoice Qty_y', 'Completed']]
#         final_df = final_df.rename(columns={
#                                             'Invoice Qty_x': 'Invoice_Quantity',
#                                             'Captured_Quantity_y': 'Captured_Quantity',
#                                             'Completed': 'Completion_Rate'})
#         final_df = final_df.fillna("Yet to Capture")
#         return final_df

