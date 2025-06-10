# # このhistoryのように初期コミットが必要です
# git init
# git config user.email
# git config user.name
# git config user.email "yuyuyu2118@gmail.com"
# git config user.name "yuyuyu2118"
# $env:GIT_AUTHOR_DATE="2024-11-24 12:00:00"
# $env:GIT_COMMITTER_DATE="2024-11-24 12:00:00"
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/yuyuyu2118/(リポジトリ名).git
# git push -u origin main

# カスタム入力関数の定義
function Read-Input {
    param (
        [string]$Prompt
    )
    Write-Host $Prompt -NoNewline
    $input = ""
    while ($true) {
        $key = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        if ($key.VirtualKeyCode -eq 27) { # ESCキー
            Write-Host "`nESCが押されました。スクリプトを終了します。"
            exit
        }
        elseif ($key.VirtualKeyCode -eq 13) { # Enterキー
            Write-Host ""
            break
        }
        elseif ($key.VirtualKeyCode -eq 8) { # Backspaceキー
            if ($input.Length -gt 0) {
                $input = $input.Substring(0, $input.Length - 1)
                Write-Host "`b `b" -NoNewline
            }
        }
        else {
            $input += $key.Character
            Write-Host $key.Character -NoNewline
        }
    }
    return $input
}

# 日付の入力を受け取る（年と月を固定）
$dayInput = Read-Input "コミットする日付を入力してください（例: 1）："
# 入力が数値かどうかを確認
if ($dayInput -notmatch '^\d+$') {
    Write-Host "無効な日付です。数字を入力してください。スクリプトを終了します。"
    exit
}

$dateInput = "2025-6-${dayInput}"

# コミットメッセージの入力を受け取る
$commitMessage = Read-Input "コミットメッセージを入力してください："

# コミットする対象を選択（デフォルトは 'file'）
$choice = Read-Input "特定のファイルをコミットする場合は 'file'、ディレクトリ全体をコミットする場合は 'dir' を入力してください："
if ([string]::IsNullOrWhiteSpace($choice)) {
    $choice = 'file'
}

# ランダムな時間を生成（6時から17時59分まで）
$randomHour = Get-Random -Minimum 6 -Maximum 23
$randomMinute = Get-Random -Minimum 0 -Maximum 60
$commitDateString = "$dateInput ${randomHour}:${randomMinute}:00"

# 日付文字列のフォーマットを確認
try {
    $commitDate = Get-Date $commitDateString -ErrorAction Stop
} catch {
    Write-Host "日付のフォーマットが正しくありません：$commitDateString"
    exit
}

# コミット日付を環境変数に設定
$env:GIT_AUTHOR_DATE = $commitDate.ToString("yyyy-MM-dd HH:mm:ss")
$env:GIT_COMMITTER_DATE = $commitDate.ToString("yyyy-MM-dd HH:mm:ss")

# Gitコマンドを実行
if ($choice -eq "file") {
    $fileInput = Read-Input "コミットするファイル名をカンマで区切って入力してください（例: .vscode/settings.json, .vscode/launch.json）："
    $fileList = $fileInput -split ",\s*"
    foreach ($file in $fileList) {
        git add $file
    }
} elseif ($choice -eq "dir") {
    $dirInput = Read-Input "コミットするディレクトリを入力してください（例: .vscode）："
    git add "$dirInput/*"
} else {
    Write-Host "無効な選択です。スクリプトを終了します。"
    exit
}

git commit -m $commitMessage

# 環境変数を削除
Remove-Item Env:GIT_AUTHOR_DATE
Remove-Item Env:GIT_COMMITTER_DATE