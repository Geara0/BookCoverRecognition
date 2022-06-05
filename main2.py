import re

import monography_parser
import collection_and_tutor_parser
from text_recognition import *


def none_count(arr):
    c = 0
    for i in arr:
        if i is None:
            c += 1
    return c


def join(a, b):
    res = []
    for i in range(len(a)):
        if not a[i]:
            res.append(b[i])
        else:
            res.append(a[i])
    return res


def vectorize(source_text):
    data = []
    for i in source_text:
        if not i:
            continue
        string = re.sub("['} ]+|.*'text':", ' ', i['text']).strip()
        data.append(string)
    return "\r\n".join(data)


path = r"C:\coding\python\BookCoverRecognition\training_data"
answ = {}
all = 0
success = 0
for _, dirs, _ in os.walk(path):
    for dir_ in dirs:
        try:
            text = read_paragraphs_from_picture(f"{path}\\{dir_}\\2.jpg")
            text = vectorize(text)
            res = []
            if "монограф" in text:
                res1 = monography_parser.collective(text)
                res2 = monography_parser.regular(text)
                # res = res2 if none_count(res1) <= none_count(res2) else res1
                success += 1
                answ[dir_] = join(res1, res2)

            elif "сборник" in text:
                res = collection_and_tutor_parser.collections(text)
                answ[dir_] = res
                success += 1
            elif "пособие" in text or "лабораторный практикум" in text:
                res = collection_and_tutor_parser.tutorial(text)
                answ[dir_] = res
                success += 1
            else:
                print(dir_)

        except:
            print(f"{dir_}\\2.jpg")

        all += 1

print(success/all)
print(answ)
for i in answ:
    print(i, ":", answ[i])
