class UF:
    def __init__(self, n):
        # N is the number of connected components
        self.N = n
        self.id = list()
        self.size = list()
        for i in range(0, n):
            self.id.append(i)
            self.size.append(1)

    def find(self, p):
        return

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
       return

    def count(self):
        return self.N


class QuickFind(UF):
    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        q_id = self.id[q]
        p_id = self.id[p]
        if not self.connected(p, q):
            for i in range(0, len(self.id)):
                if self.id[i] == p_id:
                    self.id[i] = q_id
            self.N -= 1
        #     print self.id
        #     print self.N
        # else:
        #     print 'connected'


class QuickUnion(UF):
    def root_of(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def union(self,p, q):
        if not self.connected(p, q):
            root_p = self.root_of(p)
            root_q = self.root_of(q)
            self.id[root_p] = root_q
            self.N -= 1

    def find(self,p):
        return self.root_of(p)


class WeightedQuickUnion(QuickUnion):
    def union(self,p, q):
        if not self.connected(p, q):
            root_p = self.root_of(p)
            root_q = self.root_of(q)
            if self.size[root_p] <= self.size[root_q]:
                self.connect_from_to(p, q)
            else:
                self.connect_from_to(q, p)

    def connect_from_to(self, p, q):
        root_p = self.root_of(p)
        root_q = self.root_of(q)
        self.id[root_p] = root_q
        self.size[root_q] += self.size[root_q]
    
        self.N -= 1




# file_name = "tinyUF.txt"
# file_handler = open(file_name)
# uf = WeightedQuickUnion(10)
# for line in file_handler:
#     l = line.split()
#     uf.union(int(l[0]), int(l[1]))
#
# print uf.count()
# print uf.connected(6, 7)
# print uf.size
#


