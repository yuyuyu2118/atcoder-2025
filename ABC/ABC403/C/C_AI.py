"""
WAtCoderの権限管理システム問題解法

問題ポイント:
- N人のユーザーとM個のコンテストページがある
- 初期状態では誰も閲覧権限を持っていない
- 3種類のクエリを処理する:
  1. ユーザXにコンテストページYの閲覧権限を付与
  2. ユーザXに全コンテストページの閲覧権限を付与
  3. ユーザXがコンテストページYを閲覧できるか判定

解法のポイント:
- ユーザーごとに権限情報を管理する
- 全閲覧権限はフラグで効率的に表現する
- 個別権限はセット（集合）で管理して検索を高速化
"""

# 入力を受け取る
N, M, Q = map(int, input().split())

# ユーザーの権限管理データ構造
# - has_all_access[user] = ユーザーが全権限を持つかどうか (True/False)
# - specific_access[user] = ユーザーが個別に持つ権限のセット
has_all_access = [False] * (N + 1)  # 1-indexedのためN+1
specific_access = [set() for _ in range(N + 1)]

# クエリを処理
for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        # ユーザーXにコンテストページYの閲覧権限を付与
        user, contest = query[1], query[2]
        specific_access[user].add(contest)
        print("specific_access", specific_access)
    
    elif query[0] == 2:
        # ユーザーXに全コンテストページの閲覧権限を付与
        user = query[1]
        has_all_access[user] = True
    
    else:  # query[0] == 3
        # ユーザーXがコンテストページYを閲覧できるか判定
        user, contest = query[1], query[2]
        
        if has_all_access[user] or contest in specific_access[user]:
            print("Yes")
        else:
            print("No")