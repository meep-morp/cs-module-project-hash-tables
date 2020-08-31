"""

Hash tables
----------------------------------------------------------------

What problems are we solving with this structure? -> A way to quickly get values from a key.
A hashing function returns that string as a number.

A python dictionarty is basically a hash table, it is generally known as a 'key value store'.

"""

a = [
    'Alice',
    'Bob',
    'Charlie',
    'Diane'
]

table = [None] * 8


def hash(s):
    """
    This function is very naive -- do not use. The spread of numbers is not even enough.
    """
    # Takes a string and returns it as a 'byte'
    byte = s.encode()
    hash_value = 'a'

    total = 0

    # O(n) over the size of the key, but O(1) over the size of the table.
    for b in byte:
        total += b

    return total


def get_index(key):
    index_value = hash(key)
    index_value %= len(table)

    return index_value


def put(key, value):
    # Which slot is the value going in?
    index = get_index(key)
    print(index)

    # Store the value in that slot
    table[index] = value


def get(key):
    index = get_index(key)
    return table[index]


def delete(key):
    index = get_index(key)
    table[index] = None


put("Beej", 3490)
print(get("Beej"))  # 3490
print(get("jeeB"))  # 3490
#  why? -- They have the same letters and they attach at the same slot. This is called a collision. Tuesday problem.
