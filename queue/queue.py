

class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self, data):
        self.item.append(data)

    def dequeue(self):
        self.item.pop(0)

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)



q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
print(q.size())