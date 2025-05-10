# N, M, Q = input().split()
N, M, Q = map(int, input().split())

queries:list = []

for i in range(Q):
  query = input().split()
  # TODO: 簡単なやり方調べておく
  queries.append(query)

# print(N,M,Q)
# print(queries)

user_kengenn:dict[list] = {}
# user_kengen = {"1": ["1", "2"], "2": ["-1"]}

def operation_one(user:str, contest:str):
  # print("one")
  if user in user_kengenn:
    current_kengenn:list = user_kengenn.get(user)
    current_kengenn.append(contest)
    user_kengenn[user] = current_kengenn
  else:
    user_kengenn[user] = list(contest)

  # print("user_kengenn", user_kengenn)

def operation_two(user:str):
  # print("two")
  if user in user_kengenn:
    current_kengenn:list = user_kengenn.get(user)
    current_kengenn.append("0")
    user_kengenn[user] = current_kengenn
  else:
    user_kengenn[user] = list("0")

  # print("user_kengenn", user_kengenn)

def operation_three(user:str, contest:str):
  # print("three")
  if user in user_kengenn:
    user_kengenn_list:list = user_kengenn.get(user)
    for i in user_kengenn_list:
      if i == "0":
        print("Yes")
        break
      elif i == contest:
        print("Yes")
        break
      else:
        print("No")
        break
  else:
    print("No")


for i in range(Q):
  if queries[i][0] == "1":
    operation_one(queries[i][1], queries[i][2])
  elif queries[i][0] == "2":
    operation_two(queries[i][1])
  elif queries[i][0] == "3":
    operation_three(queries[i][1], queries[i][2])