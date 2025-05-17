N = int(input())

P = list(map(int, input().split()))

# Pを並び替えてできる数列を全て表示

from itertools import permutations
# 全ての順列を生成
perms = permutations(P)
# 重複を除くためにsetに変換
unique_perms = set(perms)
# 各順列をリストに変換
unique_perms = [list(perm) for perm in unique_perms]

# # 各順列を表示
# for perm in unique_perms:
#     print(perm)

for perm in unique_perms:
    # 各順列を表示
    # print(*perm)

    tani = 0
    yama = 0

    for i in range(N-2):
        # 谷部分
        if perm[i] > perm[i+1] and perm[i+1] < perm[i+2]:
            tani += 1
            continue
        elif perm[i] < perm[i+1] and perm[i+1] > perm[i+2]:
            yama += 1
            continue
          
    
    if tani == 1 and yama == 1:
        print("Yes")
        print(*perm)

        