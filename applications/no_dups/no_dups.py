def no_dups(s):
    new_s = ""
    word_list = s.split()

    for w in word_list:
        if w not in new_s:
            if new_s == "":
                new_s += w
            else:
                new_s += f" {w}"
        else:
            continue

    return new_s


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
