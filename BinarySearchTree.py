class Node:
    def __init__(self, k,v, l = None ,r =None):
        self.key = k
        self.value = v
        self.left = l
        self.right = r


    def set_key(self, k):
        self.key = k

    def get_key(self):
        return self.key

    def set_value(self,v):
        self.value = v

    def get_value(self):
        return self.value

    def set_left(self, l):
        self.left = l

    def get_left(self):
        return self.left

    def set_right(self, r):
        self.right = r

    def get_right(self):
        return self.right


class BST:

    def __init__(self, r=None):
        self.root = r
        self.size = 0
        self.ol = []

    def put(self,k,v):
        if self.size == 0:
            new = Node(k,v,None,None)
            self.root = new

        else:
            self.__recursive_put(k,v,self.root)

        self.size += 1

    def __recursive_put(self, k, v, pointer):
        if pointer is None:
            pointer = Node(k, v, None, None)
        elif k < pointer.get_key():
            pointer.set_left(self.__recursive_put(k, v, pointer.get_left()))
        elif k > pointer.get_key():
            pointer.set_right(self.__recursive_put(k, v, pointer.get_right()))
        return pointer

    def get(self,k):
        return self.__recursive_get(k,self.root)

    def __recursive_get(self,k,pointer):
        if k == pointer.get_key():
            return pointer.get_value()
        elif k < pointer.get_key():
            return self.__recursive_get(k,pointer.get_left())
        elif k > pointer.get_key():
            return self.__recursive_get(k,pointer.get_right())

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def contains(self,k):
        return self.__recursive_contains(k,self.root)

    def __recursive_contains(self,k,pointer):
        if pointer is None:
            return False
        elif k == pointer.get_key():
            return True
        elif k < pointer.get_key():
            return self.__recursive_contains(k,pointer.get_left())
        elif k > pointer.get_key():
            return self.__recursive_contains(k,pointer.get_right())

    def max(self):
        return self.__recursive_max(self.root)

    def __recursive_max(self, pointer):
        if pointer.get_right() is None:
            return pointer.get_key()
        else:
            return self.__recursive_max(pointer.get_right())

    def min(self):
        return self.__recursive_min(self.root)

    def __recursive_min(self, pointer):
        if pointer.get_left() is None:
            return pointer.get_key()
        else:
            return self.__recursive_min(pointer.get_left())

    def delete_max(self):
        return self.__recursive_delete_max(self.root)

    def __recursive_delete_max(self, pointer):
        if pointer.get_right() is None:
            pointer = None
        else:
            pointer.set_right(self.__recursive_delete_max(pointer.get_right()))
        return pointer

    def delete_min(self):
        return self.__recursive_delete_min(self.root)

    def __recursive_delete_min(self, pointer):
        if pointer.get_left() is None:
            pointer = None
        else:
            pointer.set_left(self.__recursive_delete_min(pointer.get_left()))
        return pointer

    def floor(self, k):
        f = 0
        f = self.__recursive_floor(k, f, self.root)
        return f

    def __recursive_floor(self, k, f, pointer):
        if pointer is None:
            return f
        key = pointer.get_key()
        if k == key:
            return k
        elif key < k:
            f = key
            f = self.__recursive_floor(k, f, pointer.get_right())
        elif key > k:
            f = self.__recursive_floor(k, f, pointer.get_left())
        return f

    def ceiling(self, k):
        c = 0
        c = self.__recursive_ceiling(k, c, self.root)
        return c

    def __recursive_ceiling(self, k, c, pointer):
        if pointer is None:
            return c
        key = pointer.get_key()
        if k == key:
            return c
        elif key > k:
            c = key
            c = self.__recursive_ceiling(k, c, pointer.get_left())
        elif key < k:
            c = self.__recursive_ceiling(k, c, pointer.get_right())
        return c

    def delete(self,k):
        if k == self.root.get_key():
            if self.root.get_right() is None and self.root.get_left() is None:
                self.root = None
            elif self.root.get_left() is None:
                self.root = self.root.get_right()
            elif self.root.get_right() is None:
                self.root = self.root.get_left()
            else:
                connect_from = self.root.get_right()
                connect_to = self.root.get_left()
                self.root = self.__recursive_connect_left(connect_from, connect_to)
        else:
            self.root = self.__recursive_delete( k, self.root)
        self.size -= 1

    def __recursive_delete(self, k, pointer):
        if k > pointer.get_key():
            if pointer.get_right().get_key() == k:
                if pointer.get_right().get_left() is None:
                    pointer.set_right(pointer.get_right().get_right())
                elif pointer.get_right().get_right() is None:
                    pointer.set_right(pointer.get_right().get_left())
                else:
                    connect_to = pointer.get_right().get_left()
                    connect_from = pointer.get_right().get_right()
                    self.__recursive_connect_left(connect_from, connect_to)
                    pointer.set_right(connect_from)
            else:
                pointer = self.__recursive_delete(k, pointer.get_right())

        else:
            if k < pointer.get_key():
                if pointer.get_left().get_key() == k:
                    if pointer.get_left().get_right() is None:
                        pointer.set_left(pointer.get_left().get_left())
                    elif pointer.get_left().get_left() is None:
                        pointer.set_left(pointer.get_left().get_right())
                    else:
                        connect_to = pointer.get_left().get_right()
                        connect_from = pointer.get_left().get_left()
                        self.__recursive_connect_right(connect_from, connect_to)
                        pointer.set_left(connect_from)
            else:
                pointer = self.__recursive_delete(k, pointer.get_left())
        return pointer

    def __recursive_connect_left(self, pointer, connect_to):
        if pointer.get_left() is None:
            pointer.set_left(connect_to)
        else:
            pointer = self.__recursive_connect_left(pointer.get_left(), connect_to)
        return pointer

    def __recursive_connect_right(self, pointer, connect_to):
        if pointer.get_right() is None:
            pointer.set_right(connect_to)
        else:
            pointer = self.__recursive_connect_right(pointer.get_right(), connect_to)
        return pointer

    def ordered_list(self):
        self.__recursive_ordered_list(self.ol,self.root)
        return self.ol

    def __recursive_ordered_list(self,ol, pointer):
        #if pointer.get_left() is None or pointer.get_right() is None:
        if pointer is None:
            return
        self.__recursive_ordered_list(ol, pointer.get_left())
        ol.append(pointer.get_key())
        self.__recursive_ordered_list(ol,pointer.get_right())

bst = BST()
# bst.put(15,15)
# bst.put(10,10)
# bst.put(14,14)
# bst.put(7,7)
# bst.put(8,8)
# bst.put(3,3)
# bst.put(5,5)
# bst.put(12,12)
# bst.put(16,16)
# bst.put(2,2)
# bst.put(9,9)
# bst.put(13,13)
# bst.put(11,11)
# bst.put(20,20)
# bst.put(19,19)
# bst.put(25,25)
# bst.put(22,22)
# print bst.get(5)
# print bst.is_empty()
# print bst.get_size()
# print bst.contains(100)
# print bst.min()
# print bst.min()
# bst.delete_min()
# print bst.min()
# print bst.floor(7)
# print bst.floor(2.5)
# print bst.floor(13)
# print bst.floor(14)
# print bst.contains(22)
# print bst.floor(22)
# print bst.ceiling(6)
# print bst.ceiling(21)
# l = [52, 92, 10, 74, 50, 8, 96, 70, 82, 95, 5 ,47 ,98, 9, 61, 77, 4, 60, 40, 48, 20, 83, 65, 73, 44, 87, 23]
# for i in range(0, len(l)):
#     bst.put(l[i],l[i])
# bst.put(5,5)
# bst.put(3,3)
# bst.put(6,6)
# bst.delete(5)
# print bst.contains(5)
# print bst.contains(3)
# print bst.contains(6)
# bst.delete(92)
# print bst.contains(96)
# print bst.contains(92)
# print bst.contains(10)
# print bst.contains(52)
# bst.delete(10)
# print bst.contains(10)
# print bst.contains(8)
# print bst.contains(50)
# ol =  bst.ordered_list()
# print bst.get_size()
# print len(ol)
# print ol