# 入力を受け取る
T = input()
U = input()

"""
問題の解き方:
1. Tの各位置からUの長さ分の部分文字列を順に比較
2. Tの「?」はどんな文字にもなれるため、'?'と任意の文字は一致すると考える
3. ある開始位置iからの部分文字列がUと一致する可能性がある場合、「Yes」を出力
4. どの位置からもUと一致する可能性がない場合、「No」を出力
"""

# Uが含まれているかのフラグ
found = False

# Tの各位置からUの長さ分の部分文字列を順に比較
for i in range(len(T) - len(U) + 1):
    match = True
    
    # 現在の開始位置iから、U全体と一致するかチェック
    for j in range(len(U)):
        # 「?」は任意の文字に一致できる
        # それ以外は実際の文字同士が一致する必要がある
        if T[i + j] != '?' and T[i + j] != U[j]:
            match = False
            break
    
    # 一致する可能性がある場合
    if match:
        found = True
        break

# 結果を出力
print("Yes" if found else "No")