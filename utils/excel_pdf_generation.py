# from io import BytesIO

# from django.http import HttpResponse
# from openpyxl import Workbook
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
# from reportlab.lib.units import inch
# from reportlab.platypus.flowables import KeepInFrame

# from reels_info.models import Company


# class Download_pdf_excel:
#     def download_excel_file(self, request, all_reels):
#         response = HttpResponse(
#             content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         )
#         response["Content-Disposition"] = 'attachment; filename="Reel History Report.xlsx"'
#         wb = Workbook()
#         ws = wb.active
#         ws.append(
#             [
#                 "#",
#                 "Barcode",
#                 "Unique Identifier",
#                 "Part Number",
#                 "Quantity",
#                 "Lot Number",
#                 "ManufDate",
#                 "Created At",
#             ]
#         )
#         for index, reel in enumerate(all_reels, start=1):
#             ws.append(
#                 [
#                     index,
#                     reel["barcode"],
#                     reel["uniqueIdentifier"],
#                     reel["partNumber"],
#                     reel["quantity"],
#                     reel["lotNumber"],
#                     reel["manufDate"],
#                     reel["updatedAt"],
#                 ]
#             )
#         wb.save(response)
#         return response

#     def download_pdf_file(self, request, all_report):
#         from reportlab.platypus import (
#             Paragraph,
#             SimpleDocTemplate,
#             Spacer,
#             Table,
#             TableStyle,
#         )

#         buffer = BytesIO()
#         doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=0.3 * inch, bottomMargin=0.2 * inch)
#         style = TableStyle(
#             [
#                 ("ALIGN", (0, 0), (-1, -1), "LEFT"),
#                 ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
#                 ("WORDWRAP", (0, 0), (-1, -1), "TRUE"),
#                 ("BACKGROUND", (0, 0), (-1, 0), "#457ab1"),
#                 ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
#                 ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
#                 ("FONTSIZE", (0, 0), (-1, 0), 15),
#                 ("BACKGROUND", (0, 1), (-1, -1), colors.white),
#                 ("GRID", (0, 0), (-1, -1), 1, colors.gray),
#                 ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
#                 ("FONTSIZE", (0, 0), (-1, -1), 9),
#             ]
#         )

#         data = [
#             [
#                 "#",
#                 "Barcode",
#                 "Unique Identifier",
#                 "Part Number",
#                 "Quantity",
#                 "Lot Number",
#                 "ManufDate",
#                 "Created At",
#             ]
#         ]
#         serial_number = 1

#         for report in all_report:
#             part_number_style = ParagraphStyle(
#                 "PartNumberStyle",
#                 parent=getSampleStyleSheet()["Normal"],
#                 fontSize=9,
#                 leading=10,
#                 wordWrap="LTR",
#             )
#             part_number_paragraph = Paragraph(report["partNumber"], part_number_style)
#             wrapped_partNumber = KeepInFrame(
#                 doc.width * 0.17,
#                 50,
#                 [part_number_paragraph],
#                 mode="shrink",
#                 vAlign="TOP",
#             )
#             quantity_style = ParagraphStyle(
#                 "QuantityStyle",
#                 parent=getSampleStyleSheet()["Normal"],
#                 fontSize=9,
#                 leading=10,
#                 wordWrap="LTR",
#             )
#             quantity_paragraph = Paragraph(str(report["quantity"]), quantity_style)
#             wrapped_quantity = KeepInFrame(
#                 doc.width * 0.15,
#                 50,
#                 [quantity_paragraph],
#                 mode="shrink",
#             )
#             lot_number_style = ParagraphStyle(
#                 "LotNumberStyle",
#                 parent=getSampleStyleSheet()["Normal"],
#                 fontSize=9,
#                 leading=10,
#                 wordWrap="LTR",
#             )
#             lot_number_paragraph = Paragraph(report["lotNumber"], lot_number_style)
#             wrapped_lotNumber = KeepInFrame(
#                 doc.width * 0.17,
#                 50,
#                 [lot_number_paragraph],
#                 mode="shrink",
#                 vAlign="TOP",
#             )
#             manuf_Date_style = ParagraphStyle(
#                 "manufDateStyle",
#                 parent=getSampleStyleSheet()["Normal"],
#                 fontSize=9,
#                 leading=10,
#                 wordWrap="LTR",
#             )
#             ManufDate_paragraph = Paragraph(report["manufDate"], manuf_Date_style)
#             wrapped_manufDate = KeepInFrame(
#                 doc.width * 0.17,
#                 50,
#                 [ManufDate_paragraph],
#                 mode="shrink",
#                 vAlign="TOP",
#             )

#             UpdatedAt_style = ParagraphStyle(
#                 "updatedAtStyle",
#                 parent=getSampleStyleSheet()["Normal"],
#                 fontSize=9,
#                 leading=10,
#                 wordWrap="LTR",
#             )
#             UpdatedAt_paragraph = Paragraph(str(report["updatedAt"]), UpdatedAt_style)
#             wrapped_updatedAt = KeepInFrame(
#                 doc.width * 0.17,
#                 50,
#                 [UpdatedAt_paragraph],
#                 mode="shrink",
#                 vAlign="TOP",
#             )

#             data.append(
#                 [
#                     serial_number,
#                     report["barcode"],
#                     report["uniqueIdentifier"],
#                     wrapped_partNumber,
#                     wrapped_quantity,
#                     wrapped_lotNumber,
#                     wrapped_manufDate,
#                     wrapped_updatedAt,
#                 ]
#             )
#             serial_number += 1

#         header_info = Company.objects.first()
#         # Define ParagraphStyle for larger font size
#         larger_font_style = ParagraphStyle(
#             "LargerFontStyle",
#             parent=getSampleStyleSheet()["Normal"],
#             fontSize=15,  # Customize font size as needed
#             leading=19,
#             wordWrap="LTR",
#         )
#         # Define ParagraphStyle for smaller font size
#         smaller_font_style = ParagraphStyle(
#             "SmallerFontStyle",
#             parent=getSampleStyleSheet()["Normal"],
#             fontSize=10,  # Customize font size as needed
#             leading=14,
#             wordWrap="LTR",
#         )
#         # Create the company information paragraph with adjusted font sizes
#         company_info_paragraph = Paragraph(
#             f"{header_info.companyName}<br/>",
#             style=larger_font_style,
#         )
#         gstin_address_paragraph = Paragraph(
#             f"GSTIN:{header_info.gstin},<br/>"
#             f"CIN:{header_info.cin},<br/>"
#             f"{header_info.address}-{header_info.pinCode}<br/> PH:{header_info.phoneNumber}",
#             style=smaller_font_style,
#         )
#         # Wrap the company information paragraphs in a KeepInFrame objects
#         wrapped_company_info = KeepInFrame(
#             doc.width * 0.8,
#             doc.height,
#             [company_info_paragraph, gstin_address_paragraph],
#             mode="shrink",
#         )
#         # Create the heading table
#         heading_text = Table(
#             [
#                 [
#                     Paragraph(
#                         f'<img src="data:image/png;base64,{header_info.logo}" width="75" height="75"/>'
#                         if header_info.logo
#                         else "<b>Company Logo</b>",
#                         style=ParagraphStyle("ImageStyle", alignment=0, spaceBefore=5),
#                     ),
#                     wrapped_company_info,
#                 ]
#             ],
#             colWidths=[doc.width * 0.3, doc.width * 0.85],
#         )
#         report_heading = Table(
#             [
#                 [
#                     Paragraph(
#                         '<font size="14">Reels History Report</font>',
#                         style=ParagraphStyle("ReportHeadingStyle"),
#                     ),
#                 ]
#             ],
#             colWidths=[doc.width * 1.15],
#         )
#         # Define the styles for the report heading
#         report_heading_style = TableStyle(
#             [
#                 ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#                 ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
#                 ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
#                 ("FONTSIZE", (0, 0), (-1, -1), 16),
#                 ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
#             ]
#         )
#         # Apply the report heading style
#         report_heading.setStyle((report_heading_style))
#         heading_style = [
#             ("ALIGN", (0, 0), (-1, -1), "LEFT"),
#             ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
#             ("FONTSIZE", (0, 0), (-1, 0), 7),
#             ("TEXTCOLOR", (0, 0), (-1, -1), colors.gray),
#             ("GRID", (0, 0), (-1, 0), 1, colors.black),
#         ]
#         # Adjust width and height of the heading table
#         heading_table = Table(
#             [[heading_text]],
#             colWidths=[doc.width * 1.13],
#             rowHeights=[1.3 * inch],
#             repeatRows=0,
#             repeatCols=2,
#         )
#         heading_table.setStyle(TableStyle(heading_style))
#         table = Table(data, colWidths=[24, 84, 75, 75, 60, 75, 60, 59])
#         table.setStyle(style)
#         pdf_elements = [heading_table, Spacer(1, 0.2 * inch), report_heading, Spacer(1, 0.2 * inch), table]
#         doc.build(pdf_elements)
#         buffer.seek(0)
#         response = HttpResponse(buffer, content_type="application/pdf")
#         response["Content-Disposition"] = 'attachment; filename="Reel History Report.pdf"'
#         return response

    
#     def invoice_excel_file(self, request, all_reels):
#         response = HttpResponse(
#             content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         )
#         response["Content-Disposition"] = 'attachment; filename="Invoice Incoming Report.xlsx"'
#         wb = Workbook()
#         ws = wb.active
#         ws.append(
#             [
#                 "#",
#                 "Invoice No",
#                 "Date",
#                 "Part No",
#                 "Part Name",
#                 "Maker",
#                 "Maker",
#                 "Incoming Qty",
#                 "Completed %",
#             ]
#         )
#         for index, reel in enumerate(all_reels, start=1):
#             ws.append(
#                 [
#                     index,
#                     reel["invoice_no"],
#                     reel["invoice_date"],
#                     reel["mpn"],
#                     reel["parts_name"],
#                     reel["maker"],
#                     reel["invoice_quantity"],
#                     reel["captured_quantity"],
#                     reel["completion_rate"],
#                 ]
#             )
#         wb.save(response)
#         return response
