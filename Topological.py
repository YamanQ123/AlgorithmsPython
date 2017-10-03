from EdgeWeightedDirectedGraphs import EdgeWeightedDigraph
graph = EdgeWeightedDigraph("tinyDAG.txt")
graph_1 = EdgeWeightedDigraph("tinyEWDAG.txt")


class Topological:
    def __init__(self, directed_acyclic_graph, node=None):
        self.dag = EdgeWeightedDigraph()
        self.dag = directed_acyclic_graph
        self.stack = list()
        self.queue = list()
        self.visited = dict()
        self.sort()
        self.node = node

    def topological_order(self):
        return self.queue

    def sort(self):
        nodes = self.dag.get_vertices()
        nodes_int = list()
        for node in nodes:
            nodes_int.append(int(node))

        nodes_int = sorted(nodes_int)
        # print 'nodes',nodes_int
        for node in nodes_int:
            if not self.visited.get(str(node)):
                self.visited[str(node)] = True
                self.__dfs(str(node))
                self.stack.append(str(node))
                self.queue.insert(0, str(node))


                # print 'sorted',self.stack

    def __dfs(self, node):
        # print 'current node', node
        if self.dag.adj(node) is not None:
            # print self.visited
            # print node
            for adjacent in self.dag.adj(node):
                if not self.visited.get(adjacent.To()):
                    self.visited[adjacent.To()] = True
                    self.__dfs(adjacent.To())
                    # print adjacent.From(),adjacent.To()
                    self.stack.append(adjacent.To())
                    self.queue.insert(0,adjacent.To())
                    # print 'sorted currently after: ', self.stack


class TopologicalSingleSource:
    def __init__(self, directed_acyclic_graph, node=None):
        self.dag = EdgeWeightedDigraph()
        self.dag = directed_acyclic_graph
        self.stack = list()
        self.queue = list()
        self.visited = dict()
        self.node = node
        self.sort()

    def topological_order(self):
        return self.queue

    def sort(self):
        self.visited[str(self.node)] = True
        self.__dfs(str(self.node))
        self.stack.append(str(self.node))
        self.queue.insert(0, str(self.node))



    def __dfs(self, node):
        # print 'current node', node
        if self.dag.adj(node) is not None:
            # print self.visited
            # print node
            for adjacent in self.dag.adj(node):
                if not self.visited.get(adjacent.To()):
                    self.visited[adjacent.To()] = True
                    self.__dfs(adjacent.To())
                    # print adjacent.From(),adjacent.To()
                    self.stack.append(adjacent.To())
                    self.queue.insert(0, adjacent.To())
                    # print 'sorted currently after: ', self.stack




t = Topological(graph)
print t.topological_order()
t_1 = TopologicalSingleSource(graph_1, '5')
print t_1.topological_order()