S = str(input())

komozi_str = "abcdefghijklmnopqrstuvwxyz"
komozi_list = list(komozi_str)
nyuryoku_list = list(S)
# print(komozi_list)
# print(nyuryoku_list)

tukatta_list:list = []
tukattenai_list:list = list(komozi_str)

for i in komozi_list:
    for j in nyuryoku_list:
        if i == j:
            # print(i)
            tukatta_list.append(i)

tukatta_set = set(tukatta_list)
tukatta_list = list(tukatta_set)
for i in komozi_list:
    for j in tukatta_list:
        if i == j:
            tukattenai_list.remove(i)

# print(tukatta_list)
# print(tukattenai_list)

print(tukattenai_list[0])