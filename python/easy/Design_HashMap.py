class MyHashMap:

    def __init__(self):
        self.map_ = {}

    def put(self, key, value):
        self.map_[key] = value

    def get(self, key):
        try:
            return self.map_[key]
        except KeyError:
            return -1

    def remove(self, key):
        try:
            self.map_.pop(key)
        except KeyError:
            return
