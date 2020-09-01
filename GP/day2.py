# Handling collisions in Hash tables
# Currently we cannot save keys with the same letters no matter what order they are in, the solution is to handle our collisions.

a = [
    'Alice',
    'Bob',
    'Charlie',
    'Diane'
]

table = [None] * 8
# The collision stems from this hashing function, we will need to add in a better one and then write exceptions.


# def hash(s):
#     byte = s.encode()
#     hash_value = 'a'
#     total = 0

#     for b in byte:
#         total += b

#     return total


# Adding in a linked list -- This will help with collisions
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        cur = self.head

        while cur != None:
            if cur.value == value:
                return cur

            cur = cur.next

        return None

    def delete(self, value):
        if self.head is None:
            return None

        elif value == self.head.value:
            deleted = self.head
            self.head = self.head.next
            return deleted

        else:
            cur = self.head

            while cur.next != None:
                if cur.next.value == value:
                    deleted = cur.next.value
                    cur.next = cur.next.next
                    return deleted

                cur = cur.next

            return None

# New hash ->


def hash(s):
    pass


def get_index(key):
    index_value = hash(key)
    index_value %= len(table)

    return index_value


def put(key, value):
    index = get_index(key)
    print(index)
    table[index] = value


def get(key):
    index = get_index(key)
    return table[index]


def delete(key):
    index = get_index(key)
    table[index] = None


put("Beej", 3490)
print(get("Beej"))
print(get("jeeB"))
