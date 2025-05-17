N, K = map(int, input().split())

A = list(map(int, input().split()))

# print(N, K, A)

value = 1
for i in range(N):
  # print("value", value)
  # print("str", str(value))
  # print("len", len(str(value)))
  if len(str(value*A[i])) > K:
    value = 1
  else:
    value *= A[i]

print(value)