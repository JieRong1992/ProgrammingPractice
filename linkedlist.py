class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next = n

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, d):
        self.data = d

    def set_next(self, n):
        self.next = n


class LinkedList(object):
    def __init__(self, h=None):
        self.head = h
        if h is None:
            self.size = 0
        else:
            self.size = 1
    def add_node(self, d):
        n = Node(d,self.head)
        self.head = n
        self.size += 1

    def remove_node_front(self):
        self.head=self.head.get_next()
        self.size -= 1

    def remove_node(self, d):
        current = self.head
        pre_node=None
        while current:
            if current.get_data() == d:
                if pre_node is None:
                    self.head = self.head.get_next()
                else:
                    pre_node.set_next(current.get_next())
                current = current.get_next()
                self.size -= 1
            else:
                pre_node=current
                current=current.get_next()
        return False
    def find(self,d):
        current=self.head
        while current:
            if current.get_data()==d:
                return True
            else:
                current=current.get_next()
        return False

    def get_size(self):
        return self.size
