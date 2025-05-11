H, W = map(int, input().split())

# print(H, W , type(H), type(W))

S:list[list[str]] = [list(input()) for i in range(H)]

print("S: ", S, type(S), S[0], S[1][2])

"""
クラスを使って管理する
一つ一つのNodeが上下左右の隣接するマスが# or .かいう情報を持っておく。変数はリストでisBlack, isWhite
自分のNodeが# or .という情報を持っておく。変数はisBlack, isWhite
そのNodeの座標を持っておく。変数はx,y

#の時は、隣接するマスを#に変換する
.の時は、無視
"""

class Node():
  def __init__(self, x:int, y:int, S:list[list[str]]):
    self.S = S
    self.x = x
    self.y = y
    self.isBlack = False
    self.isWhite = False
    self.surrounding = [-1] * 4

    self.isBlack =  True if S[x][y] == "#" else False
    self.isWhite =  True if S[x][y] == "." else False

    self.surrounding[0] = 1 if x + 1 < H and S[x+1][y] == "#" else (0 if x + 1 < H else -1) # 下
    self.surrounding[1] = 1 if x - 1 >= 0 and S[x-1][y] == "#" else (0 if x + 1 < H else -1) # 上
    self.surrounding[2] = 1 if y + 1 < W and S[x][y+1] == "#" else (0 if x + 1 < H else -1) # 右
    self.surrounding[3] = 1 if y - 1 >= 0 and S[x][y-1] == "#" else (0 if x + 1 < H else -1) # 左

  def __str__(self):
    return f"Node({self.x}, {self.y}, {self.S}) isBlack: {self.isBlack}, isWhite: {self.isWhite}, surrounding: {self.surrounding})"

print(Node(1,1,S))