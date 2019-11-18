# -*- coding: utf-8 -*-


class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self, data):
        self.item.append(data)

    def pop_(self):
        return self.item.pop()

    def peak(self):
        return self.item[-1]

    def size(self):
        return len(self.item)

    def print_stack(self):
        print(self.item)

# l1 = [0,1,2,3,4]
# stack = Stack()
# stack.push(0)
# stack.push(1)
# print(stack.peak())
# # print(stack.pop_())
# # stack.print_stack()
# print(stack.isEmpty())



