N = str(input())

# N*Nの2次元配列の入力を取得
S = [list(input()) for _ in range(int(N))]
T = [list(input()) for _ in range(int(N))]

# Sの中身は「#」と「.」が入っているので、それぞれを1, 0に変換
for i in range(int(N)):
    for j in range(int(N)):
        if S[i][j] == "#":
            S[i][j] = 1
        else:
            S[i][j] = 0
        if T[i][j] == "#":
            T[i][j] = 1
        else:
            T[i][j] = 0

"""
N * Nの座標において、90度回転されるとは、
座標が
(0,0) → (0,3)
(0,1) → (1,3)
(0,2) → (2,3)
(1,2) → (2,2)
(2,3) → (3,1)
(3,3) → (3,0)
xy座標が逆になり、
(X,Y) → (Y,4-X-1)
"""

def rotation(S:list, N:int) -> list:
    """
    S: 2次元配列
    N: 2次元配列のサイズ
    """
    # 回転後の座標を格納するリスト
    rotated = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            rotated[j][N - 1 - i] = S[i][j]
    
    return rotated

# Sと座標を入力して、該当位置の値を1→0、0→1に反転する
def hanten(S:list, N:int) -> list:
    """
    S: 2次元配列
    N: 2次元配列のサイズ
    """
    # 反転後の座標を格納するリスト
    hanten = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                hanten[i][j] = 0
            else:
                hanten[i][j] = 1
    
    return hanten

# rotationとhantenを使って、S=Tにするときの最小値を求める
"""
事前に 4回の回転をして、それぞれの回転で1,0が異なる座標の数を求めておく
1,0が異なる座標の数 = hantenを使う回数となる
"""

def main(S:list, T:list, N:int) -> int:
    """
    S: 2次元配列
    T: 2次元配列
    N: 2次元配列のサイズ
    """
    # 回数の最小値を格納する変数
    min_count = 0

    # 回転後の座標を格納するリスト
    rotated = [S]
    
    # 4回の回転をして、rotatedに格納する
    for i in range(N):
        rotated.append(rotation(rotated[i], N))

    # 各回転ごとに、1,0がSとTで異なる座標の数を求める
    ans = []
    for i in range(N):
        count = 0
        for j in range(N):
            for k in range(N):
                if rotated[i][j][k] != T[j][k]:
                    count += 1
        ans.append(count)

    # ansの0~N-1に対して、それぞれrotationの数を操作回数として足す
    for i in range(N):
        ans[i] = ans[i] + i

    # 最小値
    min_count = min(ans)
    print(min_count)


if __name__ == "__main__":
    main(S, T, int(N))