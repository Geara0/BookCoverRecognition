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
    authors = re.search(r"(?<=Авторы:).+?(?=[/(\r\n)])", text).group(0).strip()
    name = re.search(r".+(?=колл)(?=.*моно)", text, re.IGNORECASE).group(0).strip()
    pages = re.search(r"(?<= [\-–—] )\d{2,3}(?= с\.)", text).group(0).strip()
    year = re.search(r"\d{4}(?=\.? [\-–—] )", text).group(0).strip()
    publisher_and_other = re.search(rf"(?<=/).+?(?=, {year})", text).group(0).strip().split('/')

    for i in isbn:
        print(i.strip(), end=' ')
    print()
    print(authors)
    print(name)
    print(pages)
    print(year)
    print(publisher_and_other[len(publisher_and_other) - 1].strip())


def regular(text):
    isbn = set(re.findall(r"\s[\d\-—]{13}\s|\s[\d\-—]{17}\s", text))
    authors = re.search(r"(?<=/ ).+(?= [\-–—])", text).group(0).strip()
    name = re.search(rf"(?<=\d\d).*(?=/ {authors})", text, re.IGNORECASE).group(0).strip()
    pages = re.search(r"(?<= [\-–—] )\d{2,3}(?= с\.)", text).group(0).strip()
    year = re.search(r"\d{4}(?=\.? [\-–—] )", text).group(0).strip()
    publisher_and_other = re.search(rf"(?<=/).+?(?=, {year})", text).group(0).strip().split('/')
    for i in isbn:
        print(i.strip(), end=' ')
    print()
    print(authors)
    print(name)
    print(pages)
    print(year)
    print(publisher_and_other[len(publisher_and_other) - 1].strip())


if __name__ == '__main__':
    # regular monography
    # data_path = "D:\\Programming\\Python\\BookCoverRecognition\\training_data\\2__СМИ_как_медиатор_коммуникативно-культурной_памяти\\2.jpg"
    # collective monography
    data_path = "D:\\Programming\\Python\\BookCoverRecognition\\training_data\\6__Травелог_Теоретико-методологический_анализ\\travelog.jpg"

    paragraphs = read_paragraphs_from_picture(data_path)

    dic = {}
    cnt = 0
    # regular(vectorize(paragraphs))
    regular(vectorize(paragraphs))
