class Node(object):
    def __init__(self, d, p=None, n=None):
        self.data = d
        self.next = n
        self.prev = p

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, d):
        self.data = d

    def set_next(self, n):
        self.next = n

    def set_prev(self, n):
        self.prev = n


class LinkedList(object):
    def __init__(self, h=None):
        self.head = h
        if h is None:
            self.size = 0
        else:
            self.size = 1

    def add_node(self, d):
        n = Node(d, None, self.head)
        self.head = n
        if self.head.get_next():
            self.head.get_next().set_prev(n)
        self.size += 1

    def remove_node_front(self):
        self.head = self.head.next #
        self.head.prev = None
        self.size -= 1

    def remove_node(self, d):
        current = self.head
        while current:
            if current.data == d: #
                if current.get_prev() is None:
                    self.remove_node_front()
                    print('====')
                else:
                    current.prev.next = current.next #
                    current.next.prev = current.prev
                    self.size -= 1
                return True
            else:
                current=current.next #
        return False

    def find(self, d):
        current = self.head
        while current:
            if current.get_data()==d: ####
                return True
            else:
                current=current.next #
        return False

    def get_size(self):
        return self.size
