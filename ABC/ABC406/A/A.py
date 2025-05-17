A, B, C, D = map(int, input().split())

simekiri = A * 60 + B
teisyutu = C * 60 + D

# print(simekiri, teisyutu)

if simekiri > teisyutu:
    print("Yes")
else:
    print("No")
