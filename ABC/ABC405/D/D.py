H, W = map(int, input().split())

S: list[list[str]] = [list(input()) for _ in range(H)]

from collections import deque

grid = S

dist = [[-1]*W for _ in range(H)]  # 距離（初期は未訪問）
queue = deque()

# スタート地点をすべて入れる（複数でも可）
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':  # スタート記号
            dist[i][j] = 0
            queue.append((i, j))

# 4方向
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

while queue:
    i, j = queue.popleft()
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W:
            if grid[ni][nj] != '#' and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                queue.append((ni, nj))

print(queue)