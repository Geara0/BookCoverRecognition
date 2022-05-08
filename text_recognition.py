import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


# работать мы будем с русскими доками, поэтому пока язык просто русский, потом сделаем чтобы можно было выбирать
# скорее всего на этапе подготовления данных будем язык писать рядом в нужном формате
def read_text_from_file(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(img, lang="rus", config=config)


# возвращает массив со словарями, каждый содержит поля :
# level, page_num, block_num, par_num, line_num, word_num, left,top, width, height, conf, text
# содержимое полей понятно из названия, каждый словарь - 1 слово
def aaa(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    config = r'--oem 3 --psm 6'
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

    return word_data_map
