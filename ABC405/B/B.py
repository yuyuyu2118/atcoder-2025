N, M = map(int, input().split())
A:list = input().split()
A = [int(a) for a in A]

# print(N, M)
# print(type(N), type(M))
# print(A)
# print(type(A))

# print(A)
# # Aを昇順にソート
# A.sort()
# print(A)

# Aのリストに1~Mまでの整数が含まれるか1,2,3の順番に探していく
no_madeno_count = 0
for i in range(N):
  hukumareru = True
  for j in range(1, M + 1):
      if j not in A:
          hukumareru = False
          break

  # print("Yes" if hukumareru else "No")

  A.pop(-1)
  if hukumareru == True:
     no_madeno_count += 1
  
print(no_madeno_count)
