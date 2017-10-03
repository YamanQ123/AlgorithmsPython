# def connected_components(graph, node):
#     connected = dict()
#     connected[node] = True
#     print recursive_connected_components(graph, node, connected)
#     return connected
from BinarySearchTree import BST


def is_there_cycle_in(directed_graph):
    l =list()
    for k in directed_graph.keys():
        l.append(k)
    # print l
    while len(l) != 0:
        node = l[0]
        # print 'node', node
        detection_result = detect_cycle(directed_graph, node)
        is_cycle = detection_result[0]
        connected_components = detection_result[1]
        # print 'bst_list', l
        # print connected_components
        if is_cycle:
            return True
        else:
            for k in connected_components.keys():
                if k in l:
                    l.remove(k)

    print l

    return False


def detect_cycle(graph, node):
    connected = dict()
    connected[node] = True
    path = list()
    path.append(node)
    recursive_connected_components(graph, node, connected, path)
    import copy
    connected_copy = copy.deepcopy(connected)

    if connected.get('cycle'):
        return True, connected_copy
    else:
        return False, connected_copy


def recursive_connected_components(graph,node,connected,path):
    if connected.get('cycle'):
        return
    for adj in graph.get(node):
        if adj not in path:
            connected[adj] = True
            path.append(adj)
            recursive_connected_components(graph, adj, connected, path)
            path.pop()
        else:
            connected['cycle'] = True



# def find_all_paths(graph, start, end):
#     solution = list()
#     visited = list()
#     visited.append(start)
#     path = list()
#     path.append(start)
#     recursive_find_all_paths(graph, start, end, path, visited, solution)
#     return solution
#
# def recursive_find_all_paths(graph, start, end, path, visited, solution):
#     for adj in graph.get(start):
#         if adj not in visited:
#             visited.append(adj)
#             path.append(adj)
#             start = adj
#             if adj == end:
#                 sol = list()
#                 for x in path:
#                     sol.append(x)
#                 solution.append(sol)
#             else:
#                 recursive_find_all_paths(graph, start, end, path, visited, solution)
#             path.pop()
#             visited.pop()
# def has_cycle(directed_graph):
graph_1 = {1: [4],
           4: [5],
           2: [1, 6],
           5: [2, 6],
           3: [2, 6],
           6: [10],
           10: [11],
           11: [12],
           12: [6]}
graph_2_acyclic = {0: [1, 5, 6],
                   1: [],
                   2: [0, 3],
                   3: [5],
                   4: [],
                   5: [4],
                   6: [4, 9],
                   7: [6],
                   8: [7],
                   9: [10, 11, 12],
                   10: [],
                   11: [],
                   12: []}

# print connected_components(graph_1, 1)
# print detect_cycle(graph_2_acyclic, 0)
print is_there_cycle_in(graph_1)
