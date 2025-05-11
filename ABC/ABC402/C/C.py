N, M = map(int, input().split())

syokuzi = []
for i in range(M):
  row = list(map(int, input().split()))
  # print(row)
  syokuzi.append(row[1:])

# print("syokuzi", syokuzi)

B = list(map(int, input().split()))

# print(B)

kokuhuku_list = []
for i in range(M):
  kokuhuku_list.append(B[i])
  # print(kokuhuku_list)
  for j in syokuzi:
    print("j:", j)
    if set(kokuhuku_list) & set(j):  # 共通部分があるか？
        print("共通の要素あり")
        print("kokuhuku_list", kokuhuku_list)
    else:
        print("共通の要素なし")

#   for j in range(syokuzi[i][0]):
#     print("syokuzi[i][j]", syokuzi[i][j+1])