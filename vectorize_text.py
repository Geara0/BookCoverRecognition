import re

dic = {}
cnt = 0


def vectorize(text):
    data = []
    for i in text:
        if not i:
            continue
        string = re.sub("['} ]+|.*'text':", ' ', i['text']).strip().split(' ')
        for i in string:
            data.append(__hash(i))
    return data


def __hash(text):
    global dic
    global cnt
    if text in dic:
        return dic[text]
    dic[text] = cnt
    cnt += 1
    return cnt - 1
