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
        pass
    
    def remove_(self, item):
        pass



