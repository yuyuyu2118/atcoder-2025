T:str = input()
U:str = input()

"""
まず、TとUを順番に比較して?の所は仮で〇とする
なぜなら?はa-zまでの文字のなんでもいれれるので、位置さえあえば〇だから

そして、全部がtrueならOK
"""

check:list[bool] = [False] * len(U)
flag:bool = False
for i in range(len(T)-len(U)+1):
  # print("i:", i)
  for j in range(len(U)):
    # print("j:", j)

    # print("T[i + j]: ", T[i + j])
    # print("U[j]: ", U[j])
    if T[i + j] == U[j]:
      check[j] = True

    if T[i + j] == "?":
      check[j] = True
  
  answer:str = "Yes"
  for i in check:
    if i == False:
      answer = "No"

  if answer == "Yes":
    print(answer)
    flag = True
    break
  check:list[bool] = [False] * len(U)

if flag == False:
  print("No")