"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


def sumdiff(q):
    # Check base case
    if len(q) < 4:
        return None

    sums = {}
    diffs = {}
    rtn = ""

    # Loop through q
    for i in q:
        sums[i] = {}
        diffs[i] = {}
        for j in q:
            sum_val = f(i) + f(j)
            diff_val = f(i) - f(j)

            sums[i][j] = sum_val

            diffs[i][j] = diff_val

    # Loop through both dictionaries and check if the two values are the same
    for a, sum_dict in sums.items():
        for b, value in sum_dict.items():
            for c, diff_dict in diffs.items():
                for d, value2 in diff_dict.items():
                    if value == value2:
                        str_1 = f"f({a}) + f({b}) = f({c}) + f({d})"
                        str_2 = f"{f(a)} + {f(b)} = {f(c)} - {f(d)}"
                        n = 30 - len(str_1)

                        print(str_1 + " " * n + str_2)


sumdiff(q)
