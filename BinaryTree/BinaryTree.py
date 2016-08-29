class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.r = None
        self.l = None

    def search(self, key):
        if self.key == key:
            return self.value
        elif self.r is None:
            return None
        elif key <= self.r.key:
            return self.r.search(key)
        elif self.l is not None:
            return self.l.search(key)
        return None

    def insert(self, key, value):
        node = Node(key, value)
        if self.r is None:
            self.r = node
        elif key < self.r.key:
            self.r.insert(key, value)
        elif self.l is None:
            self.l = node
        else:
            self.l.insert(key, value)

    def __str__(self):
        return str(self.key)