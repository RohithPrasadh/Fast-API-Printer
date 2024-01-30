# import pandas as pd
# import numpy as np
# from config.config_parser import config
# import csv , json


# # master_data_file = config.get("ExcelData","master_data_path")
# # invoice_data_file = config.get("ExcelData","invoice_data_path")
# # md_file = pd.read_excel(master_data_file)
# # invoice_file = pd.read_excel(invoice_data_file)


# class MasterDataInfo:
#     @staticmethod
#     def master_data_search(part_num):
#         # excel_final_data = {}
#         # if part_num in md_file['Maker Part No'].values:
#         #     matching_row = md_file[md_file['Maker Part No'] == part_num]
#         #     for column in md_file.columns:
#         #         variable_name = column.replace(" ", "_").lower()
#         #         value = matching_row.iloc[0][column]
#         #         if md_file[column].dtype == 'datetime64[ns]':
#         #             value = value.strftime("%d-%m-%Y")
#         #         if pd.isna(value):
#         #             value = "-"
#         #         excel_final_data[column] = value
#         #     print('excel_final_data:',excel_final_data)
#         #     return excel_final_data
#         # else:
#         print(f"Part number  not found in the Excel file.")

#     @staticmethod
#     def invoice_data():
#         print("haos")
#         # invoice_column = next((col for col in invoice_file.columns if 'invoice' in col.lower().replace(" ", "")), None)
#         # invoice_column='Invoice No.'
#         # print(invoice_column,"invoice_column")
#         # if invoice_column is not None:
#         #     unique_options = invoice_file[invoice_column].unique().tolist()
#         #     print(unique_options)
#         #     # index_of_invoice = next((i for i, value in enumerate(unique_options) if 'Invoice No.' in value), None)
#         #     # print('index_of_Invoice No.', index_of_invoice)
#         #     # index_of_invoice = unique_options.index('Invoice No.') if 'Invoice No.' in unique_options else np.nan
#         #     # # index_of_invoice = next((i for i, sublist in enumerate(unique_options) if 'Invoice No.' in sublist), None)
#         #     # print('index_of_Invoice No.',index_of_invoice)
#         #     # unique_invoice_num = unique_options[index_of_invoice+1:] if not np.isnan(index_of_invoice) else []
#         #     return unique_options
#         # else:
#         #     raise KeyError("Column with variations of 'invoice' not found in the DataFrame")



#     @staticmethod
#     def append_json_to_csv(input_data):
#         print("dcfsfsd")
#         # csv_file_path = "reels_info/csv_files/IINVOICE.csv"
#         # column_mapping = {
#         #         'invoiceNumber': 'Invoice No.',
#         #     'partNumber': 'MPN',
#         #     'quantity': 'Invoice Qty',
            
#         #     # Add other mappings as needed
#         # }

#         # with open(csv_file_path, mode='a', newline='') as file:
#         #     writer = csv.DictWriter(file, fieldnames=list(column_mapping.values()))

#         #     # Check if the file already has a header
#         #     if file.tell() == 0:
#         #         writer.writeheader()

#         #     # Extracting specific fields based on the mapping
#         #     extracted_data = {csv_header: input_data.get(data_key, '') for data_key, csv_header in column_mapping.items()}

#         #     # Append the data
#         #     writer.writerow(extracted_data)

#     @staticmethod
#     def analyse_invoice(csv,excel):
#         print("sadsad")
#           # csv_df=pd.read_csv(csv)
#         # excel_df=pd.read_excel(excel)
#         # csv_df['MPN'] = csv_df['MPN'].apply(lambda x: int(x) if isinstance(x, str) and x.isnumeric() else x)
#         # csv_df['Invoice Qty'] = pd.to_numeric(csv_df['Invoice Qty'], errors='coerce')
#         # aggregated_df = csv_df.groupby(['Invoice No.', 'MPN']).agg({'Invoice Qty': 'sum'})
#         # merged_df = pd.merge(excel_df, aggregated_df, how='left', on=['Invoice No.', 'MPN']).reset_index()
#         # print(merged_df)
#         # merged_df["Completed"]=(merged_df["Invoice Qty_y"]/excel_df['Invoice Qty'])*100
#         # final_df = merged_df[['Invoice No.', 'Invoice Date', 'MPN', 'Parts Name', 'Maker', 'Invoice Qty_x', 'Invoice Qty_y', 'Completed']]
#         # final_df = final_df.rename(columns={
#         #     'Invoice No.': 'invoice_no',
#         #     'Invoice Date': 'invoice_date',
#         #     'MPN': 'mpn',
#         #     'Parts Name': 'parts_name',
#         #     'Maker': 'maker',
#         #     'Invoice Qty_x': 'invoice_quantity',
#         #     'Invoice Qty_y': 'captured_quantity',
#         #     'Completed': 'completion_rate'
#         # })
#         # final_df = final_df.fillna(0)
#         # final_df["invoice_date"] = pd.to_datetime(final_df["invoice_date"]).dt.strftime('%Y-%m-%d')
#         # print(final_df)
#         # json_objects = final_df.to_dict(orient='records')
#         # with open('output/output.json', 'w') as json_file:
#         #     json.dump(json_objects, json_file, indent=2)

#         # return final_df

        