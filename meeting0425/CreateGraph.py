# 迷路をグラフにする：本質的に深さ優先探索
import itertools as it

def isWall(s):
    return 1 if s == '$' else 0

def getWalls(arr, i, j):
    return isWall(arr[i+1][j]) + isWall(arr[i-1][j]) + isWall(arr[i][j+1]) + isWall(arr[i][j-1])

def getEdge(arr, i, j, edges, v, c):
    for (a,b) in zip([1,-1,0,0], [0,0,1,-1]):
        if isWall(arr[i+a][j+b]) == 0:
            arr[i+a][j+b] = '$'
            if arr[i+2*a][j+2*b] == 0:
                vn = v
                cn = c + 1
            else:
                vn = arr[i+2*a][j+2*b]
                edges.append((v, vn, c))
                cn = 1
            getEdge(arr, i+2*a, j+2*b, edges, vn, cn)

vs = 0
edges = list()
arr = list()
for line in open('maze_input.txt', 'r'):
    arr.append(list(line))
height = len(arr)
width = len(arr[height - 1])
cellidi = range(1,width,2)
cellidj = range(1,height,2)
for i,j in it.product(cellidi, cellidj):
    if getWalls(arr, i, j) == 2:
        arr[i][j] = 0
    elif arr[i][j] == ' ':
        vs += 1
        arr[i][j] = vs

# 今回のデータ用の設定
getEdge(arr, 3, 7, edges, 1, 1)



# 可視化
import networkx as nx
import matplotlib.pyplot as plt
import math

G = nx.Graph()
srcs, dests = zip(* [(fr, to) for (fr, to, d) in edges])
G.add_nodes_from(srcs + dests)

for (s,r,d) in edges:
    G.add_edge(s, r, weight=20/math.sqrt(d))

pos = nx.spring_layout(G)

edge_labels=dict([((u,v,),d)
             for u,v,d in edges])

plt.figure(1)
nx.draw_networkx(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

plt.axis('equal')
plt.show()