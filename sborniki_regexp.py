import re

import text_recognition


def vectorize(text):
    data = []
    for i in text:
        if not i:
            continue
        string = re.sub("['} ]+|.*'text':", ' ', i['text']).strip()
        data.append(string)
    return "\r\n".join(data)


def sbornik(text):
    authors = re.search(r"(?<=коллегия:)(\r\n)*.+(?=[/(\r\n)])", text).group(0).strip()
    name = re.search(r"[А-Я][а-я]+?.+?(?=\.\s[\-–—]\s[А-Я])", text).group(0).strip()
    isbn = set(re.findall(r"\s[\d\-–—]{13}\s|\s[\d\-–—]{17}\s", text))
    pages = re.search(r"(?<= [\-–—] )\d{2,3}(?= с\.)", text).group(0).strip()
    year = re.search(r"\d{4}(?=\.? [\-–—] )", text).group(0).strip()

    return [isbn, year, pages]


def ucheb_posobia(text):
    isbn = set(re.findall(r"\s[\d\-–—]{13}\s|\s[\d\-–—]{17}\s", text))

    pages = re.search(r"(?<= [\-–—] )\d{2,3}(?= с\.)", text).group(0).strip()
    year = re.search(r"\d{4}(?=\.? [\-–—] )", text).group(0).strip()
    pass


if __name__ == "__main__":
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Инфомационные_технологии_в_исседований_биоразнообразия\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Проблемы_теоретической_и_экспериментальной_химии__Сборник\2.jpg"
    data_path = r"C:\coding\python\BookCoverRecognition\training_data\Физика_космоса\1.jpg"
    data = sbornik(vectorize(text_recognition.read_paragraphs_from_picture(data_path)))
    print(10)
