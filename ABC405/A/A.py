R, X = map(int, input().split())

# print(R, X)
# print(type(R), type(X))

if R >= 1600 and R <= 2999 and X == 1:
  print("Yes")
elif R < 1600 and X == 1:
  print("No")
elif R > 2999 and X == 1:
  print("No")
elif R >= 1200 and R <= 2399 and X == 2:
  print("Yes")
elif R > 2399 and X == 2:
  print("No")
elif R < 1200 and X == 2:
  print("No")
