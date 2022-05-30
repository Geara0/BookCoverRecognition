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
answ = []
for _, dirs, _ in os.walk(path):
    for dir_ in dirs:
        for _, _, files in os.walk(f"{path}\\{dir_}"):
            for file in files:
                try:
                    paragraphs.append(vectorize(read_paragraphs_from_picture(f"{path}\\{dir_}\\{file}")))
                    answ.append(dir_)
                except:
                    print(f"{dir_}\\{file}")
answ = [['русский язык коронавирусной эпохи', 'институт лингвистических исследований российской академии наук',
         '978-5-6044839-1-6', '2021'],
        ['ural workshop on group theory and combinatorics сборник','','2020'],
        ['ural workshop on group theory and combinatorics приказ'],
        ['политические модели формирования умных городов'],
        ['сми как медиатор коммуникативно- культурной памяти'],
        ['травелог теоретико- методологический анализ'],
        ['spm and rcwdfm'],
        ['дополнительные главы теории матриц'],
        ['задача маршретизации перемещений с неаддитивным агрегированием затрат'],
        ['информационные технологии в исследований биоразнообразия'],
        [
            'исследование сегнетоэлектрических материалов российскими учеными столетие открытия сегнетоэлектричества сборник'],
        ['молекулярная физика'],
        ['научные школы уральского федерального университета'],
        ['общая теория относительности'],
        ['основы теории некорректных задач'],
        ['проблемы теоретической и экспериментальной химии сборник'],
        ['теория управлений и теория управлений гамильтона якоби сборник'],
        ['труды института математики и механики'],
        ['физика космоса'],
        ['электронные и квантовые волны в магнитном поле'],
        ]
print(answ)
max_len = 300
data = utils.pad_sequences(paragraphs, maxlen=max_len, padding='post')

model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(max_len,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(5, activation='relu'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(paragraphs, )
0
