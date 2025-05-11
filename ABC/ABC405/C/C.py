N = int(input())

A:list = input().split()

A = [int(a) for a in A]

# print(N)
# print(type(N))
# print(A)
# print(type(A))

# goukei:int = 0
# for i in range(N - 1):
#   for j in range(i+1, N):
#     # print("i, j",i, j)
#     # print("A", A[i], A[j])
#     goukei += A[i] * A[j]
#     # print(goukei)

# print(goukei)

# TLE対策する
# 平方の展開の()内部をシグマにして式変形して考えればいい

sum_nizyou = 0
for i in range(0, N):
  sum_nizyou += A[i]

sum_nizyou = sum_nizyou * sum_nizyou

nizyou_sum = 0
for i in range(0, N):
  nizyou_sum += A[i] * A[i]

ans = (sum_nizyou - nizyou_sum) // 2

print(ans)