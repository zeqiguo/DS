# -*- coding: utf-8 -*-


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderList:

    def __init__(self):
        self.head = None

    def add_(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def size_(self):
        curr = self.head
        num = 0
        while curr:
            num += 1
            curr = curr.get_next()
        return num

    def search(self, item):
        curr = self.head
        found = False
        while curr and not found:
            if curr.get_data() == item:
                found = True
            else:
                curr = curr.get_next()
        return found
    
    def remove_(self, item):
        pass



ul = UnorderList()
ul.add_(1)
ul.add_(2)
print(ul.search(1))
# print(ul.size_())



