class Vertex(object):
    def __init__(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
class Graph(object):
    def __init__(self, num_vertex):
        self.adj_matrix = [[0] * num_vertex for _ in range(num_vertex)]
        self.num_vertex = num_vertex
        self.vertices = []
        for i in range(0, num_vertex):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)
    def set_vertex(self, vtx, id):
        if 0 <= vtx < self.num_vertex:
            self.vertices[vtx].set_id(id)
    def get_vertex(self, n):
        for vertxin in range(0, self.num_vertex):
            if n == self.vertices[vertxin].get_id():
                return vertxin       
        return -1
    def add_edge(self, frm, to, weight=0): 
        if self.get_vertex(frm) != -1 and self.get_vertex(to) != -1:
            self.adj_matrix[self.get_vertex(frm)][self.get_vertex(to)] = weight
            # 有向グラフの場合は別
            self.adj_matrix[self.get_vertex(to)][self.get_vertex(frm)] = weight  
    
    def get_vertices(self):
        vertices = []
        for vertxin in range(0, self.num_vertex):
            vertices.append(self.vertices[vertxin].get_id())
        return vertices
  
    def print_matrix(self):
        for u in range(0, self.num_vertex):
            row = []
            for v in range(0, self.num_vertex):
                row.append(self.adj_matrix[u][v])
            print(row)  
  
    def get_edges(self):
        edges = []
        for v in range(0, self.num_vertex):
            for u in range(0, self.num_vertex):
                if self.adj_matrix[u][v] != 0:
                    vid = self.vertices[v].get_id()
                    wid = self.vertices[u].get_id()
                    edges.append((vid, wid, self.adj_matrix[u][v]))
        return edges
        
if __name__ == '__main__':
    graph = Graph(5)
    # graph = Graph(4)
    
    graph.add_edge('a', 'e', 10)  
    graph.add_edge('a', 'c', 20)
    graph.add_edge('c', 'b', 30)
    graph.add_edge('b', 'e', 40)
    graph.add_edge('e', 'd', 50)
    print('隣接行列')
    graph.print_matrix()      
    print('ノード')
    print(graph.get_vertices())
    print('エッジ')
    print(graph.get_edges())    
    print('-----------------------')

    # 隣接行列
    # [0, 0, 20, 0, 10]
    # [0, 0, 30, 0, 40]
    # [20, 30, 0, 0, 0]
    # [0, 0, 0, 0, 50]
    # [10, 40, 0, 50, 0]
    # ノード
    # ['a', 'b', 'c', 'd', 'e']
    # エッジ
    # [('a', 'c', 20), ('a', 'e', 10), ('b', 'c', 30), ('b', 'e', 40), ('c', 'a', 20), ('c', 'b', 30), ('d', 'e', 50), ('e', 'a', 10), ('e', 'b', 40), ('e', 'd', 50)]
    # -----------------------

    # graph.add_edge('a', 'b', 3)  
    # graph.add_edge('b', 'c', 2)
    # graph.add_edge('c', 'd', 1)
    # #graph.add_edge('b', 'e', 4)
    # #graph.add_edge('d', 'a', 5)
    # print('隣接行列')
    # graph.print_matrix()      
    # print('ノード')
    # print(graph.get_vertices())
    # print('エッジ')
    # print(graph.get_edges())    
    # print('-----------------------')
