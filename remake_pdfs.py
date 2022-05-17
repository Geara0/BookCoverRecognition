import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2image import convert_from_path
from pdf2image.generators import uuid_generator

your_target_folder = "training_data"
pdf_files = []
for dirpath, _, filenames in os.walk(your_target_folder):
    for items in filenames:
        file_full_path = os.path.abspath(os.path.join(dirpath, items))
        if file_full_path.lower().endswith(".pdf"):
            pdf_files.append(file_full_path)
pdf_files.sort(key=str.lower)


for file_path in pdf_files:
    writer = PdfFileWriter()
    reader = PdfFileReader(file_path)
    page = reader.getPage(0)
    #page.scaleBy(0.1)
    writer.addPage(page)

    with open(f"{file_path}", "wb") as output:
        writer.write(output)

    image = convert_from_path(file_path)#, None, None, "ppm", None, 1,
    #None, False, False, False, False, None,
    #"C:\\Users\\Gizon\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\poppler_utils-0.1.0.dist-info")
    image[0].save(f"{file_path}.jpg", "JPEG")
    print(file_path+" has been converted to jpeg")