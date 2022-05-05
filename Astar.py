"""
2021/01/30
@Yuya Shimizu

A*アルゴリズム：無駄なコストも踏まえたダイクストラ法の発展アルゴリズム
"""
import heapq

def A_star(edges, nodes, Goal):
    """ 経路の表現
            [終点, 辺の値]
            start, A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [float('inf')] * len(nodes)    #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, [0]])

    while len(node_name) > 0:
        #ヒープから取り出し
        _, min_point = heapq.heappop(node_name)
        last = min_point[-1]
        if last == Goal:
            return min_point, node  #道順とコストを出力させている

        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[last]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[last] + cost < node[goal]:
                node[goal] = node[last] + cost     #更新
                #ヒープに登録 ※ここで，nodes[goal]という部分がダイクストラ法と異なる
                heapq.heappush(node_name, [node[last] + cost + nodes[goal], min_point + [goal]])

    return []

if __name__ == '__main__':
    #各ノードのマンハッタン距離をリストとしてまとめるstart, A, B, ..., L, M
    Nodes = [
        10, 14, 10, 10, 9, 9, 5, 0, 9, 8, 6, 4, 7, 3
        ]

    Edges = [
        [[4, 1], [5, 1]],                 # ← 頂点startからの辺のリスト
        [[2, 12], [3, 4], [4, 15]],   # ← 頂点Aからの辺のリスト
        [[1, 12], [9, 2], [11, 6]],   # ← 頂点Bからの辺のリスト
        [[1, 4], [5, 3], [8, 3]],       # ← 頂点Cからの辺のリスト
        [[1, 15], [0, 1], [6, 6]],     # ← 頂点Dからの辺のリスト
        [[0, 1], [3, 3], [6, 4]],       # ← 頂点Eからの辺のリスト
        [[4, 6], [5, 4], [10, 1]],     # ← 頂点Fからの辺のリスト
        [[11, 4], [13, 5]],              # ← 頂点Gからの辺のリスト
        [[3, 3], [9, 1], [10, 5]],     # ← 頂点Hからの辺のリスト
        [[2, 2], [8, 1], [12, 1]],     # ← 頂点Iからの辺のリスト
        [[6, 1], [8, 5], [13, 3]],     # ← 頂点Jからの辺のリスト
        [[2, 6], [7, 4], [12, 5]],     # ← 頂点Kからの辺のリスト
        [[9, 1], [11, 5], [13, 6]],   # ← 頂点Lからの辺のリスト
        [[7, 5], [10, 6], [12, 3]]    # ← 頂点Mからの辺のリスト
        ]

    #今ノード数は14（0, 1~13: start, A~G）
    Goal = 7    #いまはGを目的地とする    
    opt_root, opt_cost = A_star(Edges, Nodes, Goal)    #道順とコストを出力させている


    #以下は結果を整理するためのコード

    #出力を見やすく整理するための変換用辞書型リストの作成
    root_converter = {0: 'start'}
    cost_converter = {0: opt_cost[0]}
    for i in range(1, len(Nodes)):
        root_converter[i] = chr(ord('A') + i - 1)
        cost_converter[i] = opt_cost[i]

    arrow = " → "
    result = ""
    for i in range(len(opt_root)):
        if i > 0:
            result += arrow
        result += f"{root_converter[opt_root[i]]}({cost_converter[opt_root[i]]})"

    print(f"ノード(そこまでのコスト)\n\n{result}")