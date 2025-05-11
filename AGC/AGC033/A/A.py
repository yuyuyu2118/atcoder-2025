import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())

# print(H, W , type(H), type(W))

S:list[list[str]] = [list(input()) for i in range(H)]

# print("S: ", S, type(S), S[0], S[1][2])

dist = [[-1]*W for _ in range(H)]

q = deque()

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            dist[i][j] = 0
            q.append((i, j))

while q:
    x, y = q.popleft()

    # 4方向をチェック
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy

        # 範囲外チェック
        if not (0 <= nx < H and 0 <= ny < W):
            continue

        # 壁か、すでに訪れた場所ならスキップ
        if S[nx][ny] == '.' and dist[nx][ny] == -1:
            S[nx][ny] = '#'
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

ans = max(max(row) for row in dist)
print(ans)
