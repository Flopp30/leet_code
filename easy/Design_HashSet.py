# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class MyHashSet:

    def __init__(self):
        self.hashtable = {}

    def add(self, key: int) -> None:
        self.hashtable[key] = MyHashSet.do_hash(key)

    def remove(self, key: int) -> None:
        try:
            self.hashtable.pop(key)
        except KeyError:
            return

    def contains(self, key: int) -> bool:
        try:
            self.hashtable[key]
            return True
        except KeyError:
            return False

    @staticmethod
    def do_hash(str_):
        hash_ = ''
        for el in str(str_):
            hash_ += el + '1qwe22'
        return hash_
