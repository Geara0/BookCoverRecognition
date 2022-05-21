def vectorize(text):
    vectors = []
    for i in text:
        for j in i:
            vectors.append(j)

    return vectors
