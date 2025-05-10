"""
N M
A1 B1
A2 B2
...
AM BM
の入力を受取る
 """

N, M = map(int, input().split())
A = []
B = []

for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# print(A)
# print(B)

"""
サイクルグラフの条件:
1. 全ての頂点の次数が2である
2. グラフが連結している
3. ちょうど1つのサイクルが存在する
"""

def is_cycle_graph(N, M, A, B):
    # グラフの初期化（隣接リスト形式）
    graph = {i: [] for i in range(1, N + 1)}
    
    # グラフの構築
    for a, b in zip(A, B):
        graph[a].append(b)
        graph[b].append(a)
    
    # 条件1: すべての頂点の次数が2であることを確認
    for vertex in range(1, N + 1):
        if len(graph[vertex]) != 2:
            return False
    
    # 訪問済みの頂点
    visited = set()
    
    # DFSで連結性とサイクル数を確認
    def dfs(node, parent):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
                
            if neighbor in visited:
                # サイクルを発見
                return True
                
            if dfs(neighbor, node):
                return True
                
        return False
    
    # 条件2と3: グラフが連結で1つのサイクルを持つ
    # サイクルの存在確認
    cycle_exists = dfs(1, -1)
    
    # 全ての頂点が訪問済みかつサイクルが存在する
    return cycle_exists and len(visited) == N

# 結果出力
print("Yes" if is_cycle_graph(N, M, A, B) else "No")