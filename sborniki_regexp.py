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
    authors = re.findall(r"[А-Я]\.\s[А-Я]\.\s[А-Я][а-я]+(?=[,.\s])|(?:[А-Я][а-я]+[\s,]){3}|[А-Я][а-я]+,(?:\s[А-Я].){2}", text)
    name = re.search(r"[А-Я][а-я ]+\s(?=:)|[А-Яа-я\s:.]+(?=:\sУч)", text).group(0).strip()
    pages = re.search(r"(?<=\s)[\d]{1,3}(?=\sс.)", text).group(0).strip()
    year = re.search(r"(?<=\s)[\d]{4}(?=\.)", text).group(0).strip()
    return [isbn, year, pages]


if __name__ == "__main__":
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Инфомационные_технологии_в_исседований_биоразнообразия\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Проблемы_теоретической_и_экспериментальной_химии__Сборник\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Физика_космоса\1.jpg"
    # data = sbornik(vectorize(text_recognition.read_paragraphs_from_picture(data_path)))

    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Молекулярная_физика\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\978-5-7996-1371-6_2014\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\978-5-7996-1454-6\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\978-5-7996-1561-1_2015\2.jpg"
    data_path = r"C:\coding\python\BookCoverRecognition\training_data\978-5-7996-2171-1_2017\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Общая_теория_относительности\2.jpg"

    t = vectorize(text_recognition.read_paragraphs_from_picture(data_path))
    data = ucheb_posobia(t)
    print(10)
