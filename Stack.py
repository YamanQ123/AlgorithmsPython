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


class Stack:
    def __init__(self,r = None):
        self.root = r

    def push(self, d):
        new_node =Node(d, self.root)
        self.root = new_node

    def pop(self):
        data = self.root.get_data()
        self.root = self.root.get_next()
        return data


stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
print stack.pop()
