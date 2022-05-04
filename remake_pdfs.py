import os
from PyPDF2 import PdfFileReader, PdfFileWriter

your_target_folder = "training_data"
pdf_files = []
for dirpath, _, filenames in os.walk(your_target_folder):
    for items in filenames:
        file_full_path = os.path.abspath(os.path.join(dirpath, items))
        if file_full_path.lower().endswith(".pdf"):
            pdf_files.append(file_full_path)
pdf_files.sort(key=str.lower)

writer = PdfFileWriter()

for file_path in pdf_files:

    reader = PdfFileReader(file_path)
    page = reader.getPage(0)
    page.scaleBy(0.1)
    writer.addPage(page)

with open("CombinedFirstPages.pdf", "wb") as output:
    writer.write(output)
