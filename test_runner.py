import subprocess
import sys
import os
import colorama
from colorama import Fore, Style, Back

# カラー表示を初期化
colorama.init(autoreset=True)

def run_tests(problem_path, variant=None, test_case_num=None):
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
    print(f"実行スクリプト: {variant_display} {os.path.basename(py_file)}\n")
    
    # input_output_pairs.txtを読み込む
    with open(input_file, 'r') as f:
        content = f.read().strip()
    
    # 入力と期待される出力に分割
    test_cases = []
    sections = content.split('\n\n')
    
    i = 0
    while i < len(sections):
        if i+1 < len(sections):
            test_input = sections[i].strip()
            expected = sections[i+1].strip()
            test_cases.append((test_input, expected))
            i += 2
        else:
            break
    
    # 特定のテストケースのみを選択
    if test_case_num is not None:
        try:
            test_num = int(test_case_num)
            if 1 <= test_num <= len(test_cases):
                test_cases = [test_cases[test_num-1]]
            else:
                print(f"{Fore.YELLOW}警告: テストケース {test_num} は範囲外です。全テストケースを実行します。{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.YELLOW}警告: 無効なテストケース番号です。全テストケースを実行します。{Style.RESET_ALL}")
    
    # 結果のサマリー情報
    results_summary = []
    passed = 0
    
    # テストケースを実行
    for i, (test_input, expected) in enumerate(test_cases):
        # コンパクトなヘッダー表示
        test_num = i+1
        print(f"{Back.BLUE}{Fore.WHITE} テストケース {test_num} {Style.RESET_ALL}")
        
        # Pythonスクリプトを実行
        result = subprocess.run(
            [sys.executable, py_file],
            input=test_input,
            text=True,
            capture_output=True
        )
        
        actual = result.stdout.strip()
        is_correct = actual == expected
        
        # コンパクトな表示形式
        if is_correct:
            status = f"{Fore.GREEN}✓ 正解{Style.RESET_ALL}"
            passed += 1
        else:
            status = f"{Fore.RED}✗ 不正解{Style.RESET_ALL}"
        
        # 結果のサマリーを保存
        results_summary.append((test_num, is_correct))
        
        # 詳細表示（折りたたみ可能な形式）
        print(f"  状態: {status}")
        print(f"  {Fore.CYAN}入力{Style.RESET_ALL}: {test_input.split(chr(10))[0]}..." if len(test_input.split(chr(10))) > 1 else f"  {Fore.CYAN}入力{Style.RESET_ALL}: {test_input}")
        print(f"  {Fore.CYAN}出力{Style.RESET_ALL}: {actual}")
        print(f"  {Fore.CYAN}期待{Style.RESET_ALL}: {expected}")
        
        # 不正解の場合は差分を表示
        if not is_correct:
            print(f"  {Fore.YELLOW}差分{Style.RESET_ALL}: 実際の出力と期待される出力が一致しません")
        
        print()
    
    # 結果のサマリー表示
    print(f"{Back.WHITE}{Fore.BLACK} 実行結果サマリー {Style.RESET_ALL}")
    for test_num, is_correct in results_summary:
        status = f"{Fore.GREEN}✓ 正解{Style.RESET_ALL}" if is_correct else f"{Fore.RED}✗ 不正解{Style.RESET_ALL}"
        print(f"  テストケース {test_num}: {status}")
    
    # 最終結果
    total = len(test_cases)
    result_color = Fore.GREEN if passed == total else Fore.RED
    print(f"\n{result_color}合計: {passed}/{total} 正解 ({passed/total*100:.1f}%){Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  標準版で全テストケース実行: python test_runner.py ABC403/A")
        print("  AI版で全テストケース実行: python test_runner.py ABC403/A ai")
        print("  標準版で特定テストケース実行: python test_runner.py ABC403/A - 1")
        print("  AI版で特定テストケース実行: python test_runner.py ABC403/A ai 1")
        sys.exit(1)
    
    problem_dir = sys.argv[1]
    
    # 引数の解析
    variant = None
    test_case_num = None
    
    if len(sys.argv) > 2:
        if sys.argv[2].lower() == 'ai':
            variant = 'ai'
            if len(sys.argv) > 3:
                test_case_num = sys.argv[3]
        elif sys.argv[2] == '-':
            if len(sys.argv) > 3:
                test_case_num = sys.argv[3]
        else:
            test_case_num = sys.argv[2]
    
    run_tests(problem_dir, variant, test_case_num)