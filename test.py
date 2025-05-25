import random
import time
from colorama import init, Fore, Back, Style

# coloramaを初期化
init(autoreset=True)  # 自動でリセットするように設定

# プレイヤー情報の設定
player_name = input("あなたの名前を入力してください: ")
player_hp = 50
player_max_hp = 50
player_attack = 5
player_is_defending = False
player_heal_count = 3

# 敵情報の設定
enemy_name = input("倒す相手の名前を入力してください: ")
enemy_hp = 30
enemy_max_hp = 30
enemy_attack = 3
enemy_is_defending = False
enemy_heal_count = 3

# 体力ゲージを表示する関数
def show_hp_gauge(name, current_hp, max_hp):
    gauge_length = 20  # ゲージの長さ
    filled_length = int(gauge_length * current_hp / max_hp)
    empty_length = gauge_length - filled_length
    
    # HPが30%以下なら赤色、70%以下ならオレンジ色、それ以上なら緑色
    if current_hp / max_hp <= 0.3:
        color = Fore.RED
    elif current_hp / max_hp <= 0.7:
        color = Fore.YELLOW
    else:
        color = Fore.GREEN
    
    # ゲージの表示（例: [████████████████    ] 24/30）
    gauge = "[" + color + "█" * filled_length + Style.RESET_ALL + " " * empty_length + "]"
    
    # 名前は青色でハイライト
    if name == player_name:
        name_display = Fore.CYAN + Style.BRIGHT + name + Style.RESET_ALL
    else:
        name_display = Fore.MAGENTA + Style.BRIGHT + name + Style.RESET_ALL
        
    print(f"{name_display}: {gauge} {current_hp}/{max_hp}")

# バトル開始
print(f"\n{Fore.YELLOW + Style.BRIGHT}⚔️  {player_name} VS {enemy_name}のバトル開始！ ⚔️{Style.RESET_ALL}\n")
time.sleep(1)

# バトルループ
while True:
    # 現在の体力ゲージを表示
    show_hp_gauge(player_name, player_hp, player_max_hp)
    show_hp_gauge(enemy_name, enemy_hp, enemy_max_hp)
    print("")
      # プレイヤーの行動選択
    print("\n行動を選択してください:")
    print(f"{Fore.RED}1. 攻撃{Style.RESET_ALL}")
    print(f"{Fore.BLUE}2. 防御 {Fore.CYAN}(相手の攻撃を半分にする){Style.RESET_ALL}")
    print(f"{Fore.GREEN}3. 回復 {Fore.CYAN}(残り{player_heal_count}回 - 10回復する){Style.RESET_ALL}")
    
    while True:
        choice = input("選択 (1-3): ")
        if choice in ["1", "2", "3"]:
            if choice == "3" and player_heal_count <= 0:
                print("回復回数がもうありません！")
            else:
                break
        else:
            print("1から3の数字を入力してください。")
    
    # プレイヤーの防御状態をリセット
    player_is_defending = False
    
    # プレイヤーの行動を実行
    if choice == "1":  # 攻撃
        # たまにクリティカルヒットが出る
        if random.randint(1, 4) == 1:  # 4分の1の確率でクリティカル
            damage = player_attack * 2
            print("クリティカルヒット！")
        else:
            damage = player_attack
        
        # 敵が防御中なら半分のダメージ
        if enemy_is_defending:
            damage = damage // 2
            print(f"{enemy_name}は防御している！ダメージが半減した！")
        
        # 敵の体力を減らす
        enemy_hp -= damage
        
        # 体力が0未満にならないようにする
        if enemy_hp < 0:
            enemy_hp = 0
            
        print(f"{enemy_name}に{damage}ダメージを与えた！")
        time.sleep(0.5)
    
    elif choice == "2":  # 防御
        player_is_defending = True
        print(f"{player_name}は防御の構えをとった！")
        time.sleep(0.5)
    
    elif choice == "3":  # 回復
        if player_heal_count > 0:
            heal_amount = 10
            player_hp += heal_amount
            player_heal_count -= 1
            
            # 最大HPを超えないようにする
            if player_hp > player_max_hp:
                player_hp = player_max_hp
                
            print(f"{player_name}は{heal_amount}ポイント回復した！(残り回復回数: {player_heal_count})")
            time.sleep(0.5)
      # 敵を倒した場合
    if enemy_hp <= 0:
        show_hp_gauge(enemy_name, enemy_hp, enemy_max_hp)
        print(f"\n{enemy_name}に大ダメージを与えた、もう動けないようだ...")
        print(f"{player_name}の勝利！")
        break
    
    # 敵の行動を決定（ランダム）
    enemy_action = random.randint(1, 3)
    
    # 敵の防御状態をリセット
    enemy_is_defending = False
    
    # 敵の行動を実行
    if enemy_action == 1 or (enemy_action == 3 and enemy_heal_count <= 0):  # 攻撃
        print(f"\n{enemy_name}の攻撃！")
        time.sleep(1)
        
        # たまにクリティカルヒットが出る
        if random.randint(1, 5) == 1:  # 5分の1の確率でクリティカル
            damage = enemy_attack * 2
            print("クリティカルヒット！")
        else:
            damage = enemy_attack
        
        # プレイヤーが防御中なら半分のダメージ
        if player_is_defending:
            damage = damage // 2
            print(f"{player_name}は防御している！ダメージが半減した！")
        
        # プレイヤーの体力を減らす
        player_hp -= damage
        
        # 体力が0未満にならないようにする
        if player_hp < 0:
            player_hp = 0
            
        print(f"{player_name}は{damage}ダメージを受けた！")
        time.sleep(0.5)
    
    elif enemy_action == 2:  # 防御
        enemy_is_defending = True
        print(f"\n{enemy_name}は防御の構えをとった！")
        time.sleep(1)
    
    elif enemy_action == 3 and enemy_heal_count > 0:  # 回復
        heal_amount = 10
        enemy_hp += heal_amount
        enemy_heal_count -= 1
        
        # 最大HPを超えないようにする
        if enemy_hp > enemy_max_hp:
            enemy_hp = enemy_max_hp
            
        print(f"\n{enemy_name}は{heal_amount}ポイント回復した！")
        time.sleep(1)
    
    # プレイヤーが倒された場合
    if player_hp <= 0:
        show_hp_gauge(player_name, player_hp, player_max_hp)
        print(f"\n{player_name}はもう戦えない...")
        print(f"{enemy_name}の勝利！")
        break
    
    print("\nバトル続行！")
    time.sleep(1)
        
    print(f"{player_name}は{damage}ダメージを受けた！")
    time.sleep(0.5)
    
    # プレイヤーが倒された場合
    if player_hp <= 0:
        show_hp_gauge(player_name, player_hp, player_max_hp)
        print(f"\n{player_name}はもう戦えない...")
        print(f"{enemy_name}の勝利！")
        break
    
    print("\nバトル続行！")
    time.sleep(1)