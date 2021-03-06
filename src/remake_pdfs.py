import os

import pdf2image
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2image import convert_from_path


path = "/working_data"
pdf_files = []
for dir_path, _, filenames in os.walk(path):
    for items in filenames:
        file_full_path = os.path.abspath(os.path.join(dir_path, items))
        if file_full_path.lower().endswith(".pdf"):
            pdf_files.append(file_full_path)
pdf_files.sort(key=str.lower)

for file_path in pdf_files:
    writer = PdfFileWriter()
    reader = PdfFileReader(file_path)
    left_page = reader.getPage(0)
    try:
        right_page = reader.getPage(1)
    except:
        print("lol")
    # page.scaleBy(0.1)
    writer.addPage(left_page)
    writer.addPage(right_page)
    with open(f"{file_path}", "wb") as output:
        writer.write(output)

    image = convert_from_path(file_path)
    folder_name, file_ext = os.path.splitext(file_path)
    folder_name = folder_name.replace(" ", "_")
    folder_name = folder_name.replace(".", "_")
    folder_name = folder_name.replace(",", "_")
    os.makedirs(folder_name)
    number = 1
    for i in image:
        i.save(f"{folder_name}/{number}.jpg", "JPEG")
        print(folder_name + "\\" + str(number) + " has been converted to jpeg")
        number += 1


def convert_pdf_to_png(pdf_file, pages_to_convert=2):
    pages = []
    image = pdf2image.convert_from_bytes(pdf_file)
    if len(image) < pages_to_convert:
        raise Exception(f"Not enough pages to convert. Contains: {len(image)}, requested: {pages_to_convert}")
    for i in range(pages_to_convert):
        pages.append(image[i])

    return pages
