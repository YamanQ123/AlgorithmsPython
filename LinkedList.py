class Node:
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n

    def set_data(self, d):
        self.data = d

    def get_data(self):
        return self.data

    def set_next(self, n):
        self.next_node = n

    def get_next(self):
        return self.next_node


class LinkedList:
    def __init__(self ,r = None):
        self.size = 0
        self.root = r

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return True
            else:
                this_node = this_node.get_next()
        return False

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                prev_node.set_next(this_node.get_next())
                self.size -= 1

                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False


myList = LinkedList()
myList.add(5)
myList.add(6)
myList.add(7)
print myList.find(5)
print myList.get_size()
print myList.remove(5)
print myList.find(5)
print myList.get_size()