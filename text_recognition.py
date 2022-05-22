import os

import pytesseract
import matplotlib.pyplot as plt
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = "D:\Program Files\Tesseract-OCR\\tesseract.exe"


# возвращает массив со словарями, каждый содержит поля :
# level, page_num, block_num, par_num, line_num, word_num, left,top, width, height, conf, text
# содержимое полей понятно из названия, каждый словарь - 1 слово
def read_paragraphs_from_picture(path):
    img = plt.imread(path)
    img = img[..., ::-1]
    return read_paragraphs_from_picture_IMG(img)


def __make_paragraphs(word_data_map, data):
    paragraphs = dict.fromkeys(data["block_num"])
    word_data_map.sort(key=lambda x: x["block_num"])
    par_num = -1
    first_word = {"left": -10, "top": -10}
    last_word = {"left": -9, "top": -9}
    text = [" "]
    for line in word_data_map:
        if par_num == line["block_num"]:
            text.append(line["text"])
            last_word = line
        else:
            if par_num != -1:
                paragraphs[par_num] = {"text": " ".join([str(item) for item in text]),
                                       "top": first_word["top"],
                                       "left": first_word["left"],
                                       "height": last_word["top"] - first_word["top"] + last_word["height"],
                                       "width": last_word["left"] - first_word["left"] + last_word["width"]}
            par_num = line["block_num"]
            text.clear()
            text.append(line)
            first_word = line


    return paragraphs


def read_paragraphs_from_picture_IMG(img):
    config = r'--oem 3 --psm 3'
    data = pytesseract.image_to_data(img, lang="rus", config=config, output_type=Output.DICT)
    word_data_map = []
    for i in range(len(data['text'])):
        if i < 4:
            continue
        word_data_map.append({
            "level": data["level"][i],
            "page_num": data["page_num"][i],
            "block_num": data["block_num"][i],
            "par_num": data["par_num"][i],
            "line_num": data["line_num"][i],
            "word_num": data["word_num"][i],
            "left": data["left"][i],
            "top": data["top"][i],
            "width": data["width"][i],
            "height": data["height"][i],
            "conf": data["conf"][i],
            "text": data["text"][i],
        })

    result = __make_paragraphs(word_data_map, data)

    return list(result.values())
