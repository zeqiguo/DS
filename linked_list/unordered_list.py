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
        curr = self.head
        prev = None
        found = False
        while not found:
            if curr.get_data() == item:
                found = True
            else:
                prev = curr
                curr = curr.get_next()

        if prev == None:
            self.head = curr.get_next()
        else:
            prev.set_next((curr.get_next()))

    def append_(self, item):
        curr = self.head
        prev = None
        new_node = Node(item)
        while curr:
            prev = curr
            curr = curr.get_next()

        prev.set_next(new_node)

    def index_(self, item):
        curr = self.head
        index = 0
        while curr:
            if curr.get_data() == item:
                return index
            curr = curr.get_next()
            index += 1

    def insert(self, index, item):
        pos = 0
        prev = None
        curr = self.head
        new_node = Node(item)
        if index == 0:
            self.add_(item)
        elif index == self.size_():
            self.append_(item)
        else:
            while curr and index != pos:
                prev = curr
                curr = curr.get_next()
                pos += 1
            prev.set_next(new_node)
            new_node.set_next(curr)

    def pop_(self):
        curr = self.head
        prev = None
        while curr.get_next():
            prev = curr
            curr = curr.get_next()
        prev.set_next(None)
        return curr.get_data()

    def pop_index(self, index):
        curr = self.head
        prev = None
        pos = 0
        while curr and pos != index:
            prev = curr
            curr = curr.get_next()
            pos += 1
        prev.set_next(curr.get_next())
        return curr.get_data()

    def print_(self):
        curr = self.head
        while curr:
            print(curr.get_data())
            curr = curr.get_next()




ul = UnorderList()
ul.add_(1)
ul.add_(2)
ul.append_(0)
# ul.insert(4, 9)
print(ul.pop_index(1))
# ul.print_()
# print(ul.index_(3))
# print(ul.size_())



