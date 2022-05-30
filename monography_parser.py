from text_recognition import *
import re


def vectorize(text):
    data = []
    for i in text:
        if not i:
            continue
        string = re.sub("['} ]+|.*'text':", ' ', i['text']).strip()
        data.append(string)
    return "\r\n".join(data)


def collective(text):
    isbn = set(re.findall(r"\s[\d\-–—]{13}\s|\s[\d\-–—]{17}\s", text))
    if len(isbn) != 0:
        isbn = ' '.join([i.strip() for i in isbn])
    else:
        isbn = None

    authors = re.search(r"(?<=Авторы:(\r\n)).+?(?=[/(\r\n)])", text)
    if not authors:
        authors = re.search(r"(?<=Авторы:).+?(?=[/(\r\n)])", text)
    if authors:
        authors = authors.group(0).strip()
    if authors == '':
        authors = None

    name = re.search(r".+(?=колл)(?=.*моно)", text, re.IGNORECASE)
    if not name:
        name = re.search(r".+(?=моно)", text, re.IGNORECASE)
    if name:
        name = name.group(0).strip()

    pages = re.search(r"(?<= [\-–—] )\d{2,3}(?= с\.)", text)
    if pages:
        pages = pages.group(0).strip()

    year = re.search(r"\d{4}(?=\.? [\-–—] )", text)
    publisher = None
    if year:
        year = year.group(0).strip()
        publisher_and_other = re.search(rf"(?<=/).+?(?=, {year})", text)
        if publisher_and_other:
            publisher_and_other = publisher_and_other.group(0).strip().split('/')
            publisher = publisher_and_other[len(publisher_and_other) - 1].strip()

    return isbn, authors, name, pages, year, publisher


def regular(text):
    isbn = set(re.findall(r"\s[\d\-—]{13}\s|\s[\d\-—]{17}\s", text))
    if isbn:
        isbn = ' '.join([i.strip() for i in isbn])
    else:
        isbn = None

    authors = re.search(r"(?<=/ ).+(?= [/\-–—])", text)
    if authors:
        authors = authors.group(0).strip()
    if authors == '':
        authors = None

    name = re.search(rf"(?<=\d\d).*(?=/ {authors})", text, re.IGNORECASE)
    if name:
        name = name.group(0).strip()

    pages = re.search(r"(?<= [\-–—] )\d{2,3}(?= с\.)", text)
    if pages:
        pages = pages.group(0).strip()

    year = re.search(r"\d{4}(?=\.? [\-–—] )", text)
    publisher = None
    if year:
        year = year.group(0).strip()
        publisher_and_other = re.search(rf"(?<=/).+?(?=, {year})", text)
        if publisher_and_other:
            publisher_and_other = publisher_and_other.group(0).strip().split('/')
            publisher = publisher_and_other[len(publisher_and_other) - 1].strip()

    return isbn, authors, name, pages, year, publisher


if __name__ == '__main__':
    # regular monography
    data_path = "D:\\Programming\\Python\\BookCoverRecognition\\training_data\\1__Русский_язык_коронавирусной_эпохи__2021\\2.jpg"
    # collective monography
    # data_path = "D:\\Programming\\Python\\BookCoverRecognition\\training_data\\6__Травелог_Теоретико-методологический_анализ\\travelog.jpg"

    paragraphs = read_paragraphs_from_picture(data_path)

    dic = {}
    cnt = 0
    # regular(vectorize(paragraphs))
    regu = regular(vectorize(paragraphs))
    coll = collective(vectorize(paragraphs))
    0
