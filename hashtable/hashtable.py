"""
Implementation of a Hash Table
In this lecture we will be implementing our own Hash Table to complete our understanding of Hash Tables and Hash Functions!
Make sure to review the video lecture before this to fully understand this implementation!

Keep in mind that Python already has a built-in dictionary object that serves as a Hash Table,
you would never actually need to implement your own hash table in Python.

Map
The idea of a dictionary used as a hash table to get and retrieve items using keys is often referred to as a mapping.
In our implementation we will have the following methods:

HashTable() Create a new, empty map. It returns an empty map collection.
put(key,val) Add a new key-value pair to the map.
    If the key is already in the map then replace the old value with the new value.

get(key) Given a key, return the value stored in the map or None otherwise.

del Delete the key-value pair from the map using a statement of the form del map[key].

len() Return the number of key-value pairs stored
in the map in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
"""
class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] is not None and self.slots[nextslot]!= key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data


    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        found = False
        stop = False
        position = startslot

        while self.slots[position] is not None and found!=True and stop!=True:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    # Special Methods for use with Python indexing
    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

if __name__ == "__main__":
    h = HashTable(5)
    h[1] = 'one'
    h[2] = 'two'
    h[3] = 'three'
    print(h[1])
    h[1] = 'new_one'
    print(h[1])
    print(h[4])
    h[13] = "overlap"
    print(h[13])
    print(h[3])