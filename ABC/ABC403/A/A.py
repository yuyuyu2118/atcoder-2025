N:int = input()
A:list = list(map(int, input().split()))

sum:int = 0
for i in A[::2]:
  sum += i
  print

print(sum)
