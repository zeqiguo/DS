class Deque:
    def __init__(self):
        self.item = []

    def addFront(self, item):
        self.item.insert(0, item)

    def addRear(self, item):
        self.item.append(item)

    def removeFront(self):
        self.item.pop(0)

    def removeRear(self):
        self.item.pop(-1)

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)
