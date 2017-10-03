class MinPQ:
    def __init__(self):
        self.__heap = list()
        self.__heap_elements = list()

    def __exchange(self, i, j):
        temp = self.__heap[i]
        self.__heap[i] = self.__heap[j]
        self.__heap[j] = temp
        temp = self.__heap_elements[i]
        self.__heap_elements[i] = self.__heap_elements[j]
        self.__heap_elements[j] = temp

    def insert(self, value, element):
        self.__heap.append(value)
        self.__heap_elements.append(element)

        index = len(self.__heap)

        if index == 1:
            return
        if index % 2 != 0:  #odd
            parent = (index - 1) / 2
        else:  #even
            parent = index / 2

        i = index - 1
        p = parent -1
        #print 'index: ',index," parent: ",parent
        #print 'i:    ',i     ," p     :",p
        #  swim
        # here
        while self.__heap[p] >  self.__heap[i]:
            #print 'in loop:'
            #print '__heap[p]:', self.__heap[p], '__heap[i]', self.__heap[i]
            #print '__heap: ', self.__heap
            self.__exchange(i, p)
            #print '__heap: ',self.__heap
            index = parent
            if parent % 2 != 0:
                parent = (parent - 1) / 2
            else:
                parent = parent / 2
            if parent == 0:
                break
            i = index - 1
            p = parent - 1

            #print 'index: ', index, " parent: ", parent
            #print 'i:    ', i, " p     :", p

    def del_min(self):

        self.__exchange(0, len(self.__heap)-1)
        minimum = self.__heap.pop()
        Min = self.__heap_elements.pop()
        if len(self.__heap) > 2:
            #  sink
            i = 0
            index = 1
            p = 1
            parent = 2
            biggest_parent = parent
            bp = p
            if self.__heap[bp + 1] < self.__heap[bp]:
                biggest_parent = biggest_parent + 1
                bp = bp + 1
            while self.__heap[bp] < self.__heap[i]:
                self.__exchange(bp, i)
                index = biggest_parent
                i = bp

                biggest_parent = 2 * index
                bp = 2 * i + 1
                if bp >= len(self.__heap):
                    break
                elif bp + 1 < len(self.__heap):
                    if self.__heap[bp + 1] < self.__heap[bp]:
                        biggest_parent = biggest_parent + 1
                        bp = bp + 1

        return Min

    def is_empty(self):
        if len(self.__heap) == 0:
            return True
        else:
            return False


    def output(self):
        print (self.__heap)


pq = MinPQ()
pq.insert(90,90)
pq.insert(89,89)
pq.insert(70,70)
print(pq.is_empty())
# pq.insert(36,36)
# pq.insert(75,75)
# # pq.insert(63)
# # pq.insert(65)
# # pq.insert(21)
# # pq.insert(18)
# # pq.insert(15)
# # pq.output()
# # x = pq.del_min()
# # pq.output()
# while not pq.is_empty():
#     print pq.del_min()


