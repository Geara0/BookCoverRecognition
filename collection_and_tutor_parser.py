import re


def collections(text):
    authors = re.search(r"(?<=коллегия:)(\r\n)*.+(?=[/(\r\n)])", text)
    if authors:
        authors = authors.group(0).strip()

    name = re.search(r"[А-Я][а-я]+?.+?(?=\.\s[\-–—]\s[А-Я])", text)
    if name:
        name = name.group(0).strip()

    isbn = set(re.findall(r"\s[\d\-–—]{13}\s|\s[\d\-–—]{17}\s", text))
    if isbn:
        isbn = ' '.join([i.strip() for i in isbn])
    else:
        isbn = None

    pages = re.search(r"(?<= [\-–—] )\d{2,3}(?= с\.)", text)
    if pages:
        pages = pages.group(0).strip()

    year = re.search(r"\d{4}(?=\.? [\-–—] )", text)
    if year:
        year = year.group(0).strip()

    publisher = re.search(r"((\s:\s)|[А-Я][а-я]+:\s)[А-Яа-я-. ]+(?=,)", text)
    if publisher:
        publisher = publisher.group(0).strip()

    return isbn, authors, name, pages, year, publisher


def tutorial(text):
    isbn = set(re.findall(r"\s[\d\-–—]{13}\s|\s[\d\-–—]{17}\s", text))
    if isbn:
        isbn = ' '.join([i.strip() for i in isbn])
    else:
        isbn = None

    authors = re.findall(r"[А-Я]\.\s[А-Я]\.\s[А-Я][а-я]+(?=[,.\s])|(?:[А-Я][а-я]+[\s,]){3}|[А-Я][а-я]+,(?:\s[А-Я].){2}",
                         text)
    if authors:
        authors = " ".join([i.strip() for i in isbn])

    name = re.search(r"[А-Я][а-я ]+\s(?=:)|[А-Яа-я\s:.]+(?=:\sУч)", text)
    if name:
        name = name.group(0).strip()

    pages = re.search(r"(?<=\s)[\d]{1,3}(?=\sс.)", text)
    if pages:
        pages = pages.group(0).strip()

    year = re.search(r"(?<=\s)[\d]{4}(?=\.)", text)
    if year:
        year = year.group(0).strip()

    publisher = re.search(r"((?:[А-Я][а-я-\s]+\s:\s)|(?:[А-Я]\.:\s))[А-Яа-я-. ]+(?=,)", text)
    if publisher:
        publisher = publisher.group(0).strip()

    return isbn, authors, name, pages, year, publisher


# if __name__ == "__main__":
#     data_path = r"C:\coding\python\BookCoverRecognition\training_data\Инфомационные_технологии_в_исседований_биоразнообразия\2.jpg"
#     # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Проблемы_теоретической_и_экспериментальной_химии__Сборник\2.jpg"
#     # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Физика_космоса\2.jpg"
#     t = vectorize(text_recognition.read_paragraphs_from_picture(data_path))
#     data = collections(t)

    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Молекулярная_физика\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\978-5-7996-1371-6_2014\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\978-5-7996-1454-6\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\978-5-7996-1561-1_2015\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\978-5-7996-2171-1_2017\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\978-5-7996-1561-1_2015\2.jpg"
    # data_path = r"C:\coding\python\BookCoverRecognition\training_data\Электроннные_и_квантовые_волны_в_магнитном_поле\2.jpg"

    # t = vectorize(text_recognition.read_paragraphs_from_picture(data_path))
    # data = tutorial(t)
