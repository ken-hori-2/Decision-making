import collections

class Graph():
    def __init__(self):
        """ ノードのつながりを辞書型で表現する """
        self.adjacency_dict = {}
    
    def add_vertex(self, v):
        """ ノードを追加する """
        self.adjacency_dict[v] = []
    def add_edge(self, v1, v2):
        """ ノード同士をつなぐ。"""
        # 無向グラフの場合は双方向。もし有向グラフなら片側のみ。
        self.adjacency_dict[v1].append(v2)
        self.adjacency_dict[v2].append(v1)
    def remove_edge(self, v1, v2):
        """ ノード同士のつながりを削除する。"""
        self.adjacency_dict[v1].remove(v2)
        self.adjacency_dict[v2].remove(v1)
    def remove_vertex(self,v):
        """ ノードを削除する。"""
        while self.adjacency_dict[v] != []:
            adjacent_vertex = self.adjacency_dict[v][-1]
            self.remove_edge(v, adjacent_vertex)
        del self.adjacency_dict[v]
    
    def print_graph(self):
        print(self.adjacency_dict)

    

    def bfs(self, start, visited=None):
        # ノードを格納するキュー
        queue = collections.deque([start])
        # 訪れた順番を格納
        visited = []
        while list(queue) != []:
            current_vertex = queue.popleft()
            visited.append(current_vertex)
            for v in self.adjacency_dict[current_vertex]:
                if v not in visited and v not in queue:
                    queue.append(v)
        print(visited)


graph = Graph()
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_vertex('d')
# graph.add_vertex(5)
# graph.add_vertex(6)
graph.add_edge('a', 'b')
#graph.add_edge(1, 5)
graph.add_edge('b', 'c')
#graph.add_edge(2, 5)
graph.add_edge('c', 'd')
# graph.add_edge(4, 5)
# graph.add_edge(4, 6)
graph.print_graph()

# graph.add_vertex(0, 'a')
# graph.add_vertex(1, 'b')
# graph.add_vertex(2, 'c')
# graph.add_vertex(3, 'd')

# print('隣接行列')
# graph.print_matrix() 
# print('ノード')
# print(graph.get_vertices())
# print('エッジ')
# print(graph.get_edges())
# print('-----------------------')

# graph.add_edge('a', 'b', 3)  
# graph.add_edge('b', 'c', 2)
# graph.add_edge('c', 'd', 1)

# print('隣接行列')
# graph.print_matrix()      
# print('ノード')
# print(graph.get_vertices())
# print('エッジ')
# print(graph.get_edges())    
# print('-----------------------')




#幅優先探索
graph.bfs('a')

# # import random
# # num = random.uniform(0,1)
# # print('num = {}'.format(num))
# import numpy as np

# List = [0.5,0.6,0.7,0.8,0.9,1.0]
# sNumbers = np.random.choice(List, 6, p=[0.10,0.15,0.20,0.25,0.30,0.35])
# print(sNumbers)