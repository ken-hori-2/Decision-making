import matplotlib.pyplot as plt
import networkx as nx

# Graphオブジェクトの作成
G = nx.Graph()
 
# nodeデータの追加
G.add_nodes_from(["A", "B", "C", "D"])
 
# edgeデータの追加
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D")])

G.add_edge("A", "B", length = 0.8)

G.add_edge("B", "C", length = 0.7)
G.add_edge("C", "D", length = 0.6)

# G.add_edge("A", "X", length = 5)

pos = nx.spring_layout(G)
 
# ネットワークの可視化
# nx.draw(G, with_labels = True)
# plt.show()
# nx.draw(G, with_labels=True, node_color = "red", edge_color = "gray", node_size = 500, width = 5)
# plt.show()


colors = ["green", "red", "magenta", "yellow"]
#nx.draw(G, with_labels=True, node_color = colors)  # 色付きノードとエッジ3



# ネットワーク全体の次数の平均値を計算
average_deg = sum(d for n, d in G.degree()) / G.number_of_nodes()
# ノードの次数に比例するようにサイズを設定
sizes = [300*deg/average_deg for node, deg in G.degree()]
print(sizes)
# [150.0, 450.0, 600.0, 150.0, 150.0, 300.0]
 
# グラフの出力
plt.figure(figsize = (10,5))
plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_color = colors, node_size = sizes, edge_color = "black")
nx.draw_networkx_edge_labels(G, pos)
# plt.show() # ←棒グラフと並べて表示する場合は消します。




# 棒グラフ
# 次数の多い順番でnodeを並び替える
nodes_sorted_by_degree = sorted(G.degree(), key=lambda x: x[1], reverse=True)
print(nodes_sorted_by_degree)
# [('C', 4), ('B', 3), ('F', 2), ('A', 1), ('D', 1), ('E', 1)]
 
# 色のリストを次数順に並び替える
colors_dict = dict(zip(G.nodes(), colors))
colors_sorted = [colors_dict[node] for node, _ in nodes_sorted_by_degree]
print(colors_sorted)
# ['red', 'green', 'yellow', 'lightblue', 'cyan', 'magenta']


# グラフの出力
x, height = list(zip(*nodes_sorted_by_degree))
plt.subplot(122)
plt.xlabel("Number of degrees")
plt.ylabel("Name of node")
plt.barh(x, height, color = colors_sorted)
plt.show()
