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
        cur = self.head
        # Special case of deleting head

        if cur.value == value:
            self.head = cur.next
            return cur

        # General case of deleting internal node

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:  # Found it!
                prev.next = cur.next   # Cut it out
                return cur  # Return deleted node
            else:
                prev = cur
                cur = cur.next

        return None  # If we got here, nothing found

# New hash ->


"""
    load_factor = number_of_items / number_of_slots_in_array
    load_factor = 29 / 8 = 3.625
    load_factor = 29 / 256 = 0.113
    When the load factor > 0.7, it's time to increase the number of slots
    When the load factor < 0.2, it's time to decrease the number of slots (down to some minimum)
    "Rehashing"
    -----------
    Make a new array of double the size
    Go through all the elements in the old hash table
    Insert them into the new array
"""


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


def rehash():
    new_table = [None] * (len(table) * 2)
    # pseudocode
    """
    for each slot in table:
        for each element in the linked list in that slot:
            PUT that element in new_table
    """


put("Beej", 3490)
print(get("Beej"))
print(get("jeeB"))


"""
    Algorithm GET:
        Get the index for the key
        Search the linked list at that index for the entry for that key
        Return the value (or None if not found)
    Algorithm PUT:
        Get the index for the key
        Search the list for the key
        If it exists, overwrite the value
        Else, insert the [key,value] at the head of the linked list at that slot
"""
