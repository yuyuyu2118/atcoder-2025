from collections import deque

H, W = map(int, input().split())

# print(H, W , type(H), type(W))

S:list[list[str]] = [list(input()) for i in range(H)]

# print("S: ", S, type(S), S[0], S[1][2])

visited = [[False]*W for _ in range(H)]
print("visited: ", visited, type(visited), visited[0], visited[1][2])

q = deque()
q.append((0, 0))  # スタート位置
visited[0][0] = True  # スタート地点を訪問済みにする

while q:
    x, y = q.popleft()
    print(f"今見るマス: ({x}, {y})")

    # 4方向をチェック
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy

        # 範囲外チェック
        if not (0 <= nx < H and 0 <= ny < W):
            continue

        # 壁か、すでに訪れた場所ならスキップ
        if S[nx][ny] == '#' or visited[nx][ny]:
            continue

        # まだ訪れてない道なら、キューに追加して訪問記録
        visited[nx][ny] = True
        q.append((nx, ny))

    print("キューの中身: ", q)
      

print("visited: ", visited, type(visited), visited[0], visited[1][2])