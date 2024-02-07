import barcode
import cups
import qrcode
from reportlab.pdfgen import canvas
from pystrich.datamatrix import DataMatrixEncoder
from pdf417 import encode, render_image

from config.config_parser import config
# from .database import db

prnt_folder_path = config.get("Output", "print_output_folder")
# print(prnt_folder_path)

class PrintBarcode:
    @staticmethod
    def print_barcode_data(barcode_data, unique_identifier,printer_data, label_width=150, label_height=75):
        print("baroce",barcode_data)
        conn = cups.Connection()
        printer = printer_data['printer_type']
        code128 = barcode.get("code128", barcode_data, writer=barcode.writer.ImageWriter())
        code128.save(f"{prnt_folder_path}barcode", options={"write_text": False})
        c = canvas.Canvas(f"{prnt_folder_path}barcode.pdf", pagesize=(label_width, label_height))
        # Barcode image
        c.drawImage(f"{prnt_folder_path}barcode.png", 0, 55, width=145, height=15)
        # Font and size for the barcode data
        c.setFont("Helvetica-Bold", 9)
        # Barcode data
        c.drawString(10, 45, barcode_data)
        # Font and size
        c.setFont("Helvetica-Bold", 20)
        # Unique Identifier
        c.drawString(10, 25, unique_identifier)
        # Save the PDF
        c.showPage()
        c.save()
        conn.printFile(printer, f"{prnt_folder_path}barcode.pdf", 'BAR Code Printing', {'page-ranges': '1'})

    @staticmethod
    def print_qrcode_data(data,label_width=150, label_height=75):
        # breakpoint()
        conn = cups.Connection()
        printer = data['printer_type']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_code_data1 = ''
        delimitr = data['printerDelimiter']
        sorted_priority_data = sorted(data["priority"], key=lambda x: x['priority'])
        # breakpoint()
        for item in sorted_priority_data:
                    value = item['value']
                    qr_code_data1 += f"{data[value]}{delimitr}"
        qr.add_data(qr_code_data1)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((70, label_height))
        img.save(f"{prnt_folder_path}qrcode.png")
        c = canvas.Canvas(f"{prnt_folder_path}qrCode.pdf", pagesize=(label_width, label_height))
        # QR code image
        c.drawImage(f"{prnt_folder_path}qrcode.png", 0, 6)
        # # Font and size for the QR code data
        c.setFont("Helvetica-Bold", 9) 
        # # QR code data
        c.drawString(70, label_height - 15, data["barcode"])
        # # Font and size for Unique identifier
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(70, label_height - 25,"UID: "+data["uniqueIdentifier"])
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(70, label_height - 35,"Location: "+data["partLocation"])
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(70, label_height - 45,"FPN:"+data["internal_pn"])
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(70, label_height - 55,"Batch:"+data["lotNumber"])
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(70, label_height - 65, "RN: "+data["receiptNumber"] )
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(8, label_height - 73,"MPN: "+data["partNumber"])
        c.showPage()
        c.save()
        conn.printFile(printer, f"{prnt_folder_path}qrCode.pdf", 'QR Code Printing', {'page-ranges': '1'})
        print("Printing...")
        # conn.printFile(printer, f"{prnt_folder_path}qrCode.pdf", 'QR Code Printing', {'page-ranges': '1'})
        print("Printing done.")

    @staticmethod
    def print_datamatrix_data(data, label_width=150, label_height=75):
        print("data")
        conn = cups.Connection()
        printer = data['printer_type']
        data_matrix_data = ''
        delimitr = data['printerDelimiter']
        sorted_priority_data = sorted(data["priority"], key=lambda x: x['priority'])
        
        for item in sorted_priority_data:
                    value = item['value']
                    data_matrix_data += f"{data[value]}{delimitr}"
        
        encoder = DataMatrixEncoder(data_matrix_data)
        encoder.save( f"{prnt_folder_path}datamatrix.png" )
        c = canvas.Canvas(f"{prnt_folder_path}datamatrix.pdf", pagesize=(label_width, label_height))
        # Draw the DataMatrix
        c.drawImage(f"{prnt_folder_path}datamatrix.png", 3, 10,width=60, height=60)
        # Font and size for the DataMatrix data
        c.setFont("Helvetica-Bold", 9)  
        # dataMatrixUniqueId data 
        # Unique identifier data 
        c.drawString(70, label_height - 25,"UID: "+data["uniqueIdentifier"])
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(70, label_height - 35,"Location:")
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(70, label_height - 45,"FPN:"+data["internal_pn"])
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(70, label_height - 55,"Batch:"+data["lotNumber"])
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(70, label_height - 65, "RN: "+data["receiptNumber"] )
        c.setFont("Helvetica-Bold", 8) 
        # Unique identifier data 
        c.drawString(8, label_height - 73,"MPN: "+data["partNumber"])
        c.showPage()
        c.save()
        print("Printing...")
        conn.printFile(printer, f"{prnt_folder_path}datamatrix.pdf", 'DataMatrix Printing', {'page-ranges': '1'})
        print("Printing done.")


    @staticmethod
    def print_pdf417_data(data,label_width=150, label_height=75):
        conn = cups.Connection()
        printer = data['printer_type']
    
        pdf417_dta = ''
        delimitr = data['printerDelimiter']
        sorted_priority_data = sorted(data["priority"], key=lambda x: x['priority'])
        print(sorted_priority_data)
        for item in sorted_priority_data:
                    value = item['value']
                    pdf417_dta += f"{data[value]}{delimitr}"
        print(pdf417_dta , "pdf417_dta")
        text = pdf417_dta
        codes = encode(text)       
        image = render_image(codes) 
        image.save(f"{prnt_folder_path}pdf417.png")
        # pdf417 image(pdf image)
        c = canvas.Canvas(f"{prnt_folder_path}pdf417.pdf", pagesize=(label_width, label_height))
        # Pdf417 image
        c.drawImage(f"{prnt_folder_path}pdf417.png", 0, 47, width=145, height=30)
        # Font and size for the pdf417UniqueId data
        c.setFont("Helvetica-Bold", 9) 
        # pdf417UniqueId data 
        c.drawString(5, 43, data["barcode"])
        # Font and size for the pdf417UniqueIdentifier data
        c.setFont("Helvetica-Bold", 15) 
        # Draw the pdf417UniqueIdentifier data 
        c.drawString(5, 30, data["uniqueIdentifier"])
        c.setFont("Helvetica-Bold", 9) 
        # Unique identifier data 
        c.drawString(5, 21, "MPN: "+data["partNumber"])
        c.setFont("Helvetica-Bold", 9) 
        # Unique identifier data 
        c.drawString(5, 12, "FPN: "+data["internal_pn"])
        c.setFont("Helvetica-Bold", 9) 
        # Unique identifier data 
        c.drawString(70, label_height - 63, "RN: "+data["receiptNumber"])
        c.showPage()
        c.save()
        conn.printFile(printer, f"{prnt_folder_path}pdf417.pdf", 'PDF417 Printing', {'page-ranges': '1'})
        print("Printing done.")

    @staticmethod
    def print_bin_qrcode(data,label_width=150, label_height=75):
        conn = cups.Connection()
        for i in data:
            printer = i['printer_type']
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr_code_data1 = i['barcode']
            qr.add_data(qr_code_data1)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((70, label_height))
            img.save(f"{prnt_folder_path}qrcode.png")
            c = canvas.Canvas(f"{prnt_folder_path}qrCode.pdf", pagesize=(label_width, label_height))
            c.drawImage(f"{prnt_folder_path}qrcode.png", 0, 2)
            c.setFont("Helvetica-Bold", 15) 
            c.drawString(70, label_height - 25, i["rackName"])
            c.setFont("Helvetica-Bold", 35) 
            c.drawString(70, label_height - 55, i["slotNo"])
            c.showPage()
            c.save()
            conn.printFile(printer, f"{prnt_folder_path}qrCode.pdf", 'QR Code Printing', {'page-ranges': '1'})
            print("Printing done.")


#for testing
#-----------

# @staticmethod
# prnt_folder_path = "fastapi_printer/output/printer_output"
# def print_bin_qrcode(data,label_width=150, label_height=75):
#     conn = cups.Connection()
#     for i in data:
#         printer = i['printer_type']
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr_code_data1 = i['barcode']
#         qr.add_data(qr_code_data1)
#         qr.make(fit=True)

#         img = qr.make_image(fill_color="black", back_color="white")
#         img = img.resize((70, label_height))
#         img.save(f"{prnt_folder_path}qrcode.png")
#         c = canvas.Canvas(f"{prnt_folder_path}qrCode.pdf", pagesize=(label_width, label_height))
#         c.drawImage(f"{prnt_folder_path}qrcode.png", 0, 2)
#         c.setFont("Helvetica-Bold", 15) 
#         c.drawString(70, label_height - 25, i["rackName"])
#         c.setFont("Helvetica-Bold", 35) 
#         c.drawString(70, label_height - 55, i["slotNo"])
#         c.showPage()
#         c.save()
#         conn.printFile(printer, f"{prnt_folder_path}qrCode.pdf", 'QR Code Printing', {'page-ranges': '1'})
#         print("Printing done.")

# data = [{"barcode":"RX1678765434566BIN~0001","rackName":"RXS1-01","slotNo":"0001","printer_type":"TSC_TE210"}]
# print_bin_qrcode(data)