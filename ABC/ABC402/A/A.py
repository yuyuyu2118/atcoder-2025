S = input()

S_list = list(S)

ans = ""
for s in S_list:
  if s.isupper():
    ans += s

print(ans)