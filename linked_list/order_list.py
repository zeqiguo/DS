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


class OrderList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add_(self, item):
        curr = self.head
        prev = None
        stop = False
        while curr and not stop:
            if curr.get_data() > item:
                stop = True
            else:
                prev = curr
                curr = curr.get_next()
        new_node = Node(item)
        if prev == None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(curr)
            prev.set_next(new_node)

    def size_(self):
        curr = self.head
        num = 0
        while curr:
            num += 1
            curr = curr.get_next()
        return num

    def search(self, item):
        curr  = self.head
        found = False
        stop = False
        while curr != None and not found and not stop:
            if curr.get_data() == item:
                found = True
            else:
                if curr.get_data() > item:
                    stop = True
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

    def index_(self, item):
        curr = self.head
        index = 0
        while curr:
            if curr.get_data() == item:
                return index
            curr = curr.get_next()
            index += 1

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



ol = OrderList()
ol.add_(1)
ol.add_(10)
ol.add_(7)
ol.print_()