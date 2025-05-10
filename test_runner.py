import subprocess
import sys
import os

def run_tests(problem_path):
    # 問題のディレクトリからファイル名を取得
    base_name = os.path.basename(problem_path)
    py_file = os.path.join(problem_path, f"{base_name}.py")
    input_file = os.path.join(problem_path, "input.txt")
    
    if not os.path.exists(py_file):
        print(f"エラー: {py_file} が見つかりません")
        return
    
    if not os.path.exists(input_file):
        print(f"エラー: {input_file} が見つかりません")
        return
    
    # input.txtを読み込む
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
    
    # テストケースを実行
    passed = 0
    for i, (test_input, expected) in enumerate(test_cases):
        print(f"テストケース {i+1}:")
        print(f"入力:")
        print(test_input)
        print()
        
        # Pythonスクリプトを実行
        result = subprocess.run(
            [sys.executable, py_file],
            input=test_input,
            text=True,
            capture_output=True
        )
        
        actual = result.stdout.strip()
        print(f"出力:")
        print(actual)
        print()
        
        print(f"期待される出力:")
        print(expected)
        print()
        
        if actual == expected:
            print("結果: ✓ 正解")
            passed += 1
        else:
            print("結果: ✗ 不正解")
        
        print("-" * 50)
    
    print(f"合計: {passed}/{len(test_cases)} 正解")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python test_runner.py ABC403/A")
        sys.exit(1)
    
    problem_dir = sys.argv[1]
    run_tests(problem_dir)