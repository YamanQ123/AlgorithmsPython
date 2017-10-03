from MinPQ import MinPQ
from UnionFind import WeightedQuickUnion
import collections


class Edge:
    def __init__(self, v, w, weight):
        self.__v = v
        self.__w = w
        self.__weight = float(weight)

    def weight(self):
        return self.__weight

    def either(self):
        return self.__v

    def other(self, v):
        if v == self.__v:
            return self.__w
        elif v == self.__w:
            return self.__v
        else:
            return None

    def compare_to(self, edge):
        if edge.weight > self.__weight:
            return -1
        elif edge.weight < self.__weight:
            return +1
        else:
            return 0

    def same_edge(self, edge):
        v1 = self.either()
        v2 = edge.either()
        w1 = self.other(v1)
        w2 = edge.other(v2)
        weight1 = self.weight()
        weight2 = edge.weight()
        if v1 == v2 and w1 == w2 and weight1 == weight2:
            return True
        elif w1 == v2 and v1 == w2 and weight1 == weight2:
            return True
        else:
            return False

    def to_string(self):
        return "(v: "+str(self.__v)+", w: "+str(self.__w)+", weight: "+ str(self.__weight)+")"


# e = Edge(2,1,0.5)
# x = Edge(1,2,0.5)
# print e.same_edge(x)
# f = Edge(2, 3, 0.6)
# print f.same_edge(e)
# x = Edge(1,2,0.5)
# print e.to_string()
# print e.weight
# print e.either()
# print e.other(2)
# print e.compare_to(f)


class EdgeWeightedGraph:
    def __init__(self, file_name = None):
        self.__vertices = list()
        self.__edges = list()
        self.__graph = dict()
        if file_name:
            self.file_name = file_name
            file_handler = open(self.file_name)
            for line in file_handler:
                l = list()
                l = line.split()
                edge = Edge(l[0], l[1], float(l[2]))
                self.add_edge(edge)

    def vertices_no(self):
        return len(self.__vertices)

    def edges_no(self):
        return len(self.__edges)

    def get_vertices(self):
        return self.__vertices

    def add_edge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self.__edges.append(edge)
        if v not in self.__vertices:
            self.__vertices.append(v)
        if w not in self.__vertices:
            self.__vertices.append(w)
        if self.__graph.get(v):
            self.__graph[v].append(edge)
        else:
            self.__graph[v] = list()
            self.__graph[v].append(edge)
        if self.__graph.get(w):
            self.__graph[w].append(edge)
        else:
            self.__graph[w] = list()
            self.__graph[w].append(edge)

    def adj(self, v):
        if v in self.get_vertices():
            return self.__graph.get(v)

    def edges(self):
        return self.__edges

    def to_string(self):
        string = '{'
        for vertex in self.__vertices:
            if self.__vertices.index(vertex) != 0:
                string += " " + str(vertex) + ": " + "["
            else:
                string += str(vertex)+": "+"["
            for edge in self.adj(vertex):
                if self.adj(vertex).index(edge) == len(self.adj(vertex)) - 1:
                    string += edge.to_string()
                else:
                    string += edge.to_string() + ", "
            if self.__vertices.index(vertex) == len(self.__vertices) - 1:
                string += ']}'
            else:
                string += '],\n'

        return string


g = EdgeWeightedGraph('tinyEWG.txt')
# print g.get_vertices()

# min_pq = MinPQ()
# for edge in g.edges():
#     min_pq.insert(edge.weight(), edge)
# min_pq.output()
# print min_pq.del_min().to_string()


class MST:
    def __init__(self, edge_weighted_graph):
        self.__EWG = edge_weighted_graph
        self.__MST_vertices = dict()
        self.__MST_edges = list()
        self.__min_pq = MinPQ()
        for vertex in self.__EWG.get_vertices():
            self.__MST_vertices[vertex] = False
        self.__build()

    def __build(self):
        print 'hello'

    def edges(self):
        return self.__MST_edges

    def weight(self):
        total_weight = 0
        for edge in self.__MST_edges:
            total_weight += edge.weight()
        return total_weight


class PrimMSTLazy:
    def __init__(self, edge_weighted_graph):
        self.__EWG = edge_weighted_graph
        self.__MST_vertices = dict()
        self.__MST_edges = list()
        self.__min_pq = MinPQ()
        for vertex in self.__EWG.get_vertices():
            self.__MST_vertices[vertex] = False
        self.__build()

    def edges(self):
        return self.__MST_edges

    def weight(self):
        total_weight = 0
        for edge in self.__MST_edges:
            total_weight += edge.weight()
        return total_weight

    def __build(self):
        v = self.__EWG.get_vertices()[0]
        # v = '0'
        self.__MST_vertices[v] = True

        # print self.__EWG.adj(v)
        for adjacent in self.__EWG.adj(v):
            self.__min_pq.insert(adjacent.weight(), adjacent)
        while not self.__min_pq.is_empty():
            edge = self.__min_pq.del_min()
            v = edge.either()
            w = edge.other(v)
            if self.__MST_vertices.get(v) and not self.__MST_vertices.get(w):
                self.__MST_vertices[w] = True
                self.__MST_edges.append(edge)
                for adjacent in self.__EWG.adj(w):
                    if not adjacent.same_edge(edge):
                        self.__min_pq.insert(adjacent.weight(), adjacent)
            elif self.__MST_vertices.get(w) and not self.__MST_vertices.get(v):
                self.__MST_vertices[v] = True
                self.__MST_edges.append(edge)
                for adjacent in self.__EWG.adj(v):
                    if not adjacent.same_edge(edge):
                        # filter

                        self.__min_pq.insert(adjacent.weight(), adjacent)


class PrimMSTEager:
    def __init__(self, edge_weighted_graph):
        self.__EWG = edge_weighted_graph
        self.__distance_to = dict()
        self.__edge_to = dict()
        self.__min_pq = MinPQ()
        self.__mst_vertices = dict()
        for v in self.__EWG.get_vertices():
            self.__mst_vertices[v] = False
        self.__build()

    def weight(self):
        sum = 0
        for distance in self.__distance_to.values():
            sum += distance
        return sum

    def edges(self):
        return self.__edge_to.values()

    def __build(self):
        v = self.__EWG.get_vertices()[0]
        # v = '0'
        self.__distance_to[v] = 0
        self.__mst_vertices[v] = True
        for adjacent in self.__EWG.adj(v):
            w = adjacent.other(v)
            self.__min_pq.insert(adjacent.weight(), adjacent)
            self.__distance_to[w] = adjacent.weight()
            self.__edge_to[w] = adjacent
        while not self.__min_pq.is_empty():
            edge = self.__min_pq.del_min()
            if not self.__mst_vertices.get(edge.either()):
                v = edge.either()
                self.__mst_vertices[v] = True
            elif not self.__mst_vertices.get(edge.other(edge.either())):
                v = edge.other(edge.either())
                self.__mst_vertices[v] = True
            if v is None:
                continue
            for adjacent in self.__EWG.adj(v):
                w = adjacent.other(v)
                if w == self.__EWG.get_vertices()[0]:
                    continue
                weight = adjacent.weight()
                if not self.__distance_to.get(w):
                    self.__distance_to[w] = weight
                    self.__edge_to[w] = adjacent
                    self.__min_pq.insert(weight, adjacent)
                elif weight < self.__distance_to.get(w) and not self.__mst_vertices.get(w):
                    self.__distance_to[w] = weight
                    self.__edge_to[w] = adjacent
                    self.__min_pq.insert(weight, adjacent)


class Kruskal:
    def __init__(self, edge_weighted_graph):
        self.__EWG = edge_weighted_graph
        self.__distance_to = dict()
        self.__edge_to = dict()
        self.__min_pq = MinPQ()
        self.__mst_vertices = dict()
        self.__edges = list()
        for v in self.__EWG.get_vertices():
            self.__mst_vertices[v] = False
        for edge in self.__EWG.edges():
            self.__min_pq.insert(edge.weight(), edge)

        self.__vertices_no = len(self.__mst_vertices.keys())
        self.__uf = WeightedQuickUnion(self.__vertices_no)
        self.__build()

    def weight(self):
        sum = 0
        for edge in self.__edges:
            sum += edge.weight()
        return sum

    def edges(self):
        return self.__edges

    def __build(self):
        while len(self.__edges) < self.__vertices_no - 1:
            edge = self.__min_pq.del_min()
            v = edge.either()
            w = edge.other(v)
            if not self.__uf.connected(int(v), int(w)):
                self.__uf.union(int(v), int(w))
                self.__edges.append(edge)




# g.add_edge(e)
# g.add_edge(f)
# for x in g.edges:
#     print x.to_string()
# print g.get_vertices()
# for el in g.adj(e.other(e.either())):
#     print el.to_string()
# print g.to_string()
# mst = PrimMSTEager(g)
# for edge in mst.edges():
#     print edge.to_string()
mst = Kruskal(g)
for edge in mst.edges():
    print edge.to_string()

