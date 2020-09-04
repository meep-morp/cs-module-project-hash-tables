# Your code here
import string


def read_file():
    file = open("robin.txt", "r")
    return file.read()


count = {}


def histo(s):
    # remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    words = s.split()

    for w in words:
        w.lower()
        if w not in count:
            count[w] = "#"

        count[w] += "#"


histo(read_file())
i = list(count.items())
i.sort(key=lambda e: e[1], reverse=True)
for item in i:
    n = 30 - len(item[0])
    print(item[0] + " " * n + item[1])
