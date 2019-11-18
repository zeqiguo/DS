# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def print_node(self):
        print(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def _is_empty(self):
        return self.head is None

    def empty_list(self):
        self.head = None

    # ADD FUNCTINOS
    def insert_head(self, data):
        newNode = Node(data)
        if self.head != None:
            newNode.next = self.head
        self.head = newNode

    def insert_tail(self, data):
        newNode = Node(data)
        if self.head is None:
            self.insert_head()
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def insert_at_index(self, data, index):
        newNode = Node(data)
        curr_index = 0
        current = self.head
        if index < 0:
            return "invalid index"
        if index > self.count_num():
            return "index out of range"
        while current and curr_index<index-1:
            curr_index += 1
            current = current.next
        if  current.next == None:
            current.next = newNode
        else:
            temp = current.next
            current.next = newNode
            newNode.next = temp

    # DELETE FUNCTIONS
    def delete_head(self):
        self.head = self.head.next

    def delete_tail(self):
        temp = self.head
        if self.count_num() <= 1:
            self.delete_head()
        else:
            while temp.next.next:
                temp = temp.next
            temp.next = None

    def delete_at_index(self, index):
        curr_index = 0
        current = self.head
        temp = None
        if index >= self.count_num() or index < 0:
            return "index out fo range"
        while current and curr_index < index:
            temp = current
            current = current.next
            curr_index += 1
        # delete the tail
        if current.next == None:
            temp.next = None
        # delete the head
        elif index == 0:
            self.head = current.next
        # delete other index
        else:
            temp.next = current.next

    #  MODIFY FUNCTIONS
    def reverse(self):
        prev = None
        current = self.head

        while current:
            # store the next node
            next_node = current.next
            # cut the link between current and current next
            current.next = prev
            # reverse the pointer
            prev = current
            # move to next node
            current = next_node
        self.head = prev

    def modify_at_index(self, index, data):
        curr_index = 0
        current = self.head
        if index >= self.count_num():
            return "index out of range"
        if index < 0:
            return "invalid index"
        while current and curr_index < index:
            curr_index += 1
            current = current.next
        current.data = data

    # SEARCH FUNCTIONS
    def find_value_at_index(self, index):
        curr_index = 0
        current = self.head
        if index < 0 or index >= self.count_num():
            return "index out of range"
        while curr_index < index and current:
            curr_index += 1
            current = current.next
        return current.data


    def count_num(self):
        temp = self.head
        num = 0
        while temp:
            temp = temp.next
            num += 1
        return num

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


l1 = Linked_List()
l1.insert_head(1)
l1.insert_tail(2)
# l1.insert_at_index(data=0, index=2)
l1.insert_tail(3)
# l1.print_list()
# l1.reverse()
print(l1.find_value_at_index(index=2))
# l1.print_list()
# print('\n\n\n')
# l1.modify_at_index(index=2, data=0)
# l1.print_list()
# this is first pycharm and git combination

# test





