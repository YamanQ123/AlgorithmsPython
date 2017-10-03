from MinPQ import MinPQ


class WeightedDirectedEdge:
    def __init__(self,From, To, weight):
        self.__f = From
        self.__t = To
        self.__weight = float(weight)

    def From(self):
        return self.__f

    def To(self):
        return self.__t

    def weight(self):
        return self.__weight

    def to_string(self):
        return '(' + str(self.__f)  + " -> " + str(self.__t) + ", weight: " + str(self.__weight) + ')'


class EdgeWeightedDigraph:
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
                edge = WeightedDirectedEdge(l[0], l[1], float(l[2]))
                self.add_edge(edge)

    def vertices_no(self):
        return len(self.__vertices)

    def edges_no(self):
        return len(self.__edges)

    def get_vertices(self):
        return self.__vertices

    def adj(self, v):
        if v in self.get_vertices():
            return self.__graph.get(v)

    def edges(self):
        return self.__edges

    def add_edge(self, edge):
        v = edge.From()
        w = edge.To()
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

    def to_string(self):
        string = '{'
        for vertex in self.__vertices:
            if self.__vertices.index(vertex) != 0:
                string += " " + str(vertex) + ": " + "["
            else:
                string += str(vertex) + ": " + "["
            if self.adj(vertex) is not None:
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


class DijkstraSP:
    def __init__(self, edge_weighted_digraph, source):
        self.edge_to = dict()
        self.dist_to = dict()
        self.relaxed_vertices = dict()
        self.min_pq = MinPQ()
        self.EWD = edge_weighted_digraph
        self.source = source
        for vertex in self.EWD.get_vertices():
            self.dist_to[vertex] = float("inf")
        self.dist_to[source] = 0
        self.relax_vertex(self.source)
        self.build()
        for vertex,edge in self.edge_to.items():
            print vertex,' : ',edge.to_string()
        print self.dist_to

    # def has_path_to(self, node):
    #     return
    def build(self):
        while not self.min_pq.is_empty():
            v = self.min_pq.del_min()
            if not self.relaxed_vertices.get(v):
                self.relax_vertex(v)

    def has_path_to(self, vertex):
        return self.dist_to.get(vertex) != float('inf')

    def path_to(self, vertex):
        if self.has_path_to(vertex):
            path = list()
            vertex = str(vertex)
            edge = self.edge_to.get(vertex)
            From = edge.From()
            To = edge.To()
            while From != self.source:
                path.insert(0, To)
                edge = self.edge_to.get(From)
                From = edge.From()
                To = edge.To()
            path.insert(0, To)
            path.insert(0, self.source)
            return path
        else:
            return


    def relax_vertex(self, v):
        self.relaxed_vertices[v] = True
        if self.EWD.adj(v) is not None:
            for edge in self.EWD.adj(v):
                self.relax_edge(edge)

    def relax_edge(self, edge):
        To = edge.To()
        From = edge.From()
        # print edge.weight()+ self.dist_to.get(From)
        # print self.dist_to.get(To)
        if edge.weight()+ self.dist_to.get(From) < self.dist_to.get(To):
            self.edge_to[To] = edge
            self.dist_to[To] = edge.weight() + self.dist_to[From]
            self.min_pq.insert(self.dist_to.get(To),To)
            # print edge.to_string()


g = EdgeWeightedDigraph('tinyEWD.txt')
graph_1 = EdgeWeightedDigraph("tinyEWDAG.txt")
#
d = DijkstraSP(graph_1, '5')
print d.path_to('6')
