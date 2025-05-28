N = int(input())

# N行の文字列を受け取り、各文字を個別の要素として2次元リストに格納
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]

# print("A:", A)
# print("B:", B)

for i in range(N):
    if A[i] != B[i]:
        # print("No")
        # print("A:", A[i])
        # print("B:", B[i])
        # 単語を一文字ずつ比較
        for j in range(N):
            if A[i][j] != B[i][j]:
                # print(f"Mismatch at ({i}, {j}): A = {A[i][j]}, B = {B[i][j]}")
                print(i + 1, j + 1)
