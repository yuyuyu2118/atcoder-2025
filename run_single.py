import subprocess
import sys
import os
import colorama
from colorama import Fore, Style, Back

# カラー表示を初期化
colorama.init(autoreset=True)

def run_single(problem_path, variant=None):
    """
    指定されたファイルを実行し、input_output_pairs.txtの最初の入力を与えるだけのシンプルな関数
    """
    # 問題のディレクトリからファイル名を取得
    base_name = os.path.basename(problem_path)
    
    # 実行するスクリプトの決定（AI版または標準版）
    if variant and variant.lower() == 'ai':
        py_file = os.path.join(problem_path, f"{base_name}_AI.py")
    else:
        py_file = os.path.join(problem_path, f"{base_name}.py")
    
    input_file = os.path.join(problem_path, "input_output_pairs.txt")
    
    if not os.path.exists(py_file):
        print(f"{Fore.RED}エラー: {py_file} が見つかりません{Style.RESET_ALL}")
        return
    
    if not os.path.exists(input_file):
        print(f"{Fore.RED}エラー: {input_file} が見つかりません{Style.RESET_ALL}")
        return

    # AI版か通常版かを表示
    variant_display = f"{Fore.MAGENTA}AI版{Style.RESET_ALL}" if variant and variant.lower() == 'ai' else f"{Fore.BLUE}通常版{Style.RESET_ALL}"
    print(f"{Fore.CYAN}実行: {variant_display} {os.path.basename(py_file)}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}")
    
    # input_output_pairs.txtから最初のテストケースだけを読み取る
    with open(input_file, 'r') as f:
        content = f.read().strip()
    
    # 入力部分だけを抽出
    sections = content.split('\n\n')
    if sections:
        test_input = sections[0].strip()
    else:
        print(f"{Fore.RED}エラー: 入力データが見つかりません{Style.RESET_ALL}")
        return
    
    # 入力データを表示
    print(f"{Fore.GREEN}入力データ:{Style.RESET_ALL}")
    print(test_input)
    print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}")
    
    # Pythonスクリプトを実行
    print(f"{Fore.GREEN}実行結果:{Style.RESET_ALL}")
    result = subprocess.run(
        [sys.executable, py_file],
        input=test_input,
        text=True,
        capture_output=False  # 標準出力に直接出力させる
    )
    
    print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}実行終了{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  標準版で実行: python run_single.py ABC403/B")
        print("  AI版で実行: python run_single.py ABC403/B ai")
        sys.exit(1)
    
    problem_dir = sys.argv[1]
    variant = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2].lower() == 'ai' else None
    
    run_single(problem_dir, variant)