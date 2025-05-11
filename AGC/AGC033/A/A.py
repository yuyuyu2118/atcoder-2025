from collections import deque

H, W = map(int, input().split())

# print(H, W , type(H), type(W))

S:list[list[str]] = [list(input()) for i in range(H)]

# print("S: ", S, type(S), S[0], S[1][2])

dist = [[-1]*W for _ in range(H)]
start_x, start_y = 0, 0
dist[start_x][start_y] = 0

q = deque()
q.append((start_x, start_y))  # スタート位置

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
        if S[nx][ny] == '#' or dist[nx][ny] != -1:
            continue

        # まだ訪れてない道なら、キューに追加して訪問記録
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))

    print("キューの中身: ", q)
    print("dist: ", dist)
      
print("dist: ", dist)

max_dist = max(max(row) for row in dist)

print(max_dist)