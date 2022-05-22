import tensorflow
from keras.models import Sequential
from keras.layers import Dense
from keras import utils
from keras.preprocessing.sequence import *
import numpy as np
import fs
import matplotlib.pyplot as plt
from text_recognition import *
from vectorize_text import *

# data_path = "D:\\Programming\\Python\\BookCoverRecognition\\training_data\\1__Русский_язык_коронавирусной_эпохи__2021\\1.jpg"
data_path = "D:\\Programming\\Python\\BookCoverRecognition\\training_data\\2__СМИ_как_медиатор_коммуникативно-культурной_памяти\\1.jpg"
path = "D:\\Programming\\Python\\BookCoverRecognition\\training_data"
paragraphs = []
for _, dirs, _ in os.walk(path):
    for dir_ in dirs:
        for _, _, files in os.walk(f"{path}\\{dir_}"):
            for file in files:
                paragraphs.append(vectorize(read_paragraphs_from_picture(f"{path}\\{dir_}\\{file}")))

# data = utils.pad_sequences([vectorize(read_paragraphs_from_picture(data_path))], maxlen=50,
#                            padding='post')
# print(data)

for p in paragraphs:
    print(len(p))

0
