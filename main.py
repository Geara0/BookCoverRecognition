# from remake_pdfs import *
from text_recognition import *
from vectorize_text import *

data_path = "D:\\Programming\\Python\\BookCoverRecognition\\training_data\\1__Русский_язык_коронавирусной_эпохи__2021\\1.jpg"

paragraphs = read_paragraphs_from_picture(data_path)

vectorize(paragraphs)
0
