from collections import deque

Q = int(input())

queries = [input().split() for _ in range(Q)]

# print(Q)

# print(queries)

q = deque()

for query in queries:
  if query[0] == "1":
    q.append(query[1])
  elif query[0] == "2":
    print(q.popleft())
