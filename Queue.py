class Node:
    def __init__(self, d, n = None ,p =None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def set_data(self, d):
        self.data = d

    def get_data(self):
        return self.data

    def set_next(self, n):
        self.next_node = n

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def set_prev(self, p):
        self.prev_node = p


class Queue:
    def __init__(self,r=None , l=None):
        self.last = l
        self.root = r
        self.size = 0

    def enque(self, d):
        if self.size == 0:
            new_node = Node(d, self.root, self.last)
            self.root = new_node
            self.last = new_node
            self.size += 1

        else:
            new_node = Node(d, self.root,None)
            self.root.set_prev(new_node)
            self.root = new_node
            self.size += 1

    def deque(self):
            data = self.last.get_data()
            self.last = self.last.get_prev()
            self.size -= 1
            return data

    def get_size(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


q = Queue()
q.enque(5)
q.enque(6)
q.enque(7)

print q.deque()
print q.get_size()
print q.deque()
print q.get_size()
print q.is_empty()
print q.deque()
print q.is_empty()

test = {
    1 :True
}
if not test.get(1):
    print 'hello'
else:
    print 'welcome'
print len(test
          )



