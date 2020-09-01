"""
    DAY 1
    Task: Implement a basic hash table without collision resolution.

    Implement a HashTable class and HashTableEntry class.

    Implement a good hashing function.

    Recommend either of:

    DJB2 ->

        unsigned long
        hash(unsigned char *str)
        {
        unsigned long hash = 5381;
        int c;

        while (c = *str++)
            hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

        return hash;
        }
        The magic of number 33 (why it works better than many other constants, prime or not) has never been adequately explained.

    FNV-1 (64-bit)
    You are allowed to Google for these hashing functions and implement from psuedocode.

    Implement the hash_index() that returns an index value for a key.

    Implement the put(), get(), and delete() methods.

    Day 2
    Task: Implement linked-list chaining for collision resolution.

    Modify put(), get(), and delete() methods to handle collisions.
"""


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that starts with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Keep capacity at the minimum
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY

        self.capacity = capacity
        self.table = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash_val = 14695981039346656037
        for x in key:
            hash_val = hash_val ^ ord(x)
            hash_val = (hash_val * 1099411628211)
        return hash_val

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash_val = 5381

        for c in key:
            # Using 33 spreads the numbers evenly
            hash_val = (hash_val * 33) + ord(c)

        return hash_val

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Store index(key) to place value
        index = self.hash_index(key)
        # Check that current index has nothing in it
        if self.table[index] == None:
            # Place value at key
            self.table[index] = HashTableEntry(key, value)
            self.count += 1

        # If spot is taken ->
        else:
            cur = self.table[index]
            # Loop through table
            while cur.next != None and cur.key != key:
                cur = cur.next
            # Check if key == current key, replace it
            if cur.key == key:
                cur.value = value
            # Else, place key before the current index
            else:
                entry = HashTableEntry(key, value)
                entry.next = self.table[index]
                self.table[index] = entry
                self.count += 1
        # Check load factor and double if necessary
        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # Store the key index
        index = self.hash_index(key)

        if self.table[index] is None:
            return None
        else:
            cur = self.table[index]
            prev = None

            # Search for key in a Loop
            while cur.key != key and cur.next is not None:
                prev = cur
                cur = cur.next

            if cur.key == key:
                # if it is the head
                if prev is None:
                    self.table[index] = cur.next
                else:
                    # move to next key
                    prev.next = cur.next

                if self.table[index] is None:
                    self.count -= 1

                # Check load factor ->
                # If decreases below .2, rehash table until it reaches the minimum
                if self.get_load_factor() < .2:
                    if self.capacity/2 > 8:
                        self.resize(self.capacity//2)
                    elif self.capacity > 8:
                        self.resize(8)

                return cur.value
            else:
                # not found
                return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Get the index for the key
        index = self.hash_index(key)
        if self.table[index] is not None and self.table[index].key == key:
            return self.table[index].value
        elif self.table[index] is None:
            return None
        else:
            cur = self.table[index]
            # Search the linked list at that index for the entry for that key
            while cur.next != None and cur.key != key:
                cur = self.table[index].next
            # Return the value (or None if not found)
            if cur == None:
                return None
            else:
                return cur.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.table[:]
        self.capacity = new_capacity
        self.table = [None] * new_capacity
        # for each slot in table:
        for i in range(len(old_table)):
            # for each element in the linked list in that slot:
            if old_table[i] is not None:
                cur = old_table[i]
                # PUT that element in new_table
                self.put(cur.key, cur.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
