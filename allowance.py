import math

BASE  = 2000          # 最低保証額
A     = 8622.2188802  # 上乗せ最大
H     = 36.31882688   # スケール
BETA  = 4.0           # 鋭さ

def allowance(rank: int) -> int:
    """順位 (1～271) を渡すと支給額を返す"""
    return round(BASE + A * math.exp(-((rank - 1)/H) ** BETA))


if __name__ == "__main__":
    input_rank = int(input("順位を入力してください (1-271): "))
    if 1 <= input_rank <= 271:
        allowance = allowance(input_rank)
        print(f"順位 {input_rank} のお小遣いは {allowance} 円です。")
    else:
        print("順位は1から271の間で入力してください。")