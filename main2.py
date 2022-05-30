import monography_parser
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


path = "D:\\Programming\\Python\\BookCoverRecognition\\training_data"
answ = {}
for _, dirs, _ in os.walk(path):
    for dir_ in dirs:
        try:
            text = read_paragraphs_from_picture(f"{path}\\{dir_}\\2.jpg")
            text = monography_parser.vectorize(text)
            res = []
            if "монограф" in text:
                res1 = monography_parser.collective(text)
                res2 = monography_parser.regular(text)
                # res = res2 if none_count(res1) <= none_count(res2) else res1

                answ[dir_] = join(res1, res2)

        except:
            print(f"{dir_}\\2.jpg")

print(answ)
for i in answ:
    print(i, ":", answ[i])
