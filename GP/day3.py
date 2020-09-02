import random
import hashlib
import math

"""

Hash talbles are great in any situation where you need to quickly look something up:
- Calculations 
- Network Access
- Indexing data
- Counting and removing duplicates

"""

# This notation is O(2^n), which is .. bad.
# return fib(n-1) + fib(n - 2)

cache = {}  # This technique is called caching, or top-down-dynamic programming. It is much faster


def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n - 2)

    return cache[n]


# for i in range(100):
#     print(f"{i}: {fib(i)}")


# Bonus material ->
    # Botom Up Dynamic Programming solves this problem in O(1) space


"""

Sorting results in a dictionary ->
1. Cast the dict onto a list 
2. Sort 

----------------------------

If keys are different types, force them to be the same type.

"""
d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

i = list(d.items())

# Comp gives us fine control over how this is sorted, it looks at the first element and compares on that
"""
def comp(e):
    print(e)
    return e[1]

i.sort(key=comp)
"""


# Anon function, same as comp but shorter
i.sort(key=lambda e: e[1])


# print(i)


"""

Lookup Tables -> 
Build a lookup table for inverse square root, for numbers 1 - 1000.

"""

inv_sqrt_table = {}


def inv_sqrt(n):
    if n not in inv_sqrt_table:
        inv_sqrt_table[n] = 1 / math.sqrt(n)

    return inv_sqrt_table[n]


"""

Count the number of occurrences of a letter in a string

"Hello There" - 2 h's, 1 t ...
A hash table is a great way to count

"""


def letter_count(s):
    d = {}

    for c in s:
        if c.isspace():
            continue
        c = c.upper()

        if c not in d:
            d[c] = 0

        d[c] += 1

    return d


print(letter_count("Hello There"))


def letter_count_alt(s):
    mydict = {i: s.count(i) for i in s}
    return mydict


print(letter_count_alt("Hello There"))


"""

->BONUS<-
How full does a hash table have to get before a collision happens?

"""


def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff


def how_many_before_collision(buckets, loops):
    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = random.random()
            index = hash_function(random_key) % buckets

        if index not in tried:
            tried.add(index)
            tried += 16

        else:
            break

        print(
            f"{buckets} buckets, {tries} hashes before collision. ({tries / buckets * 100:.1f}% full)")


# how_many_before_collision(32, 10)
