import webbrowser
import os
import json
from collections import deque
import tempfile

def bfs_visualization(input_str):
    lines = input_str.strip().split('\n')
    H, W = map(int, lines[0].split())
    
    S = [list(lines[i+1]) for i in range(H)]
    
    # BFSの実行過程を記録するためのリスト
    steps = []
    
    dist = [[-1]*W for _ in range(H)]
    
    # 黒マスの位置をキューに入れる
    q = deque()
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                q.append((i, j))
                dist[i][j] = 0
                steps.append({
                    "grid": [row[:] for row in S],
                    "dist": [row[:] for row in dist],
                    "queue": list(q),
                    "current": (i, j),
                    "message": f"黒マス({i}, {j})をキューに追加し、距離を0に設定"
                })
    
    while q:
        x, y = q.popleft()
        current_dist = dist[x][y]
        
        # 現在処理中のセルを記録
        current_step = {
            "grid": [row[:] for row in S],
            "dist": [row[:] for row in dist],
            "queue": list(q),
            "current": (x, y),
            "message": f"現在のマス: ({x}, {y}), 距離: {current_dist}"
        }
        steps.append(current_step)
        
        # 4方向をチェック
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            
            # 範囲外チェック
            if not (0 <= nx < H and 0 <= ny < W):
                continue
            
            # すでに訪れた場所ならスキップ
            if dist[nx][ny] != -1:
                continue
            
            # まだ訪れてない道なら、キューに追加して訪問記録
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
            
            queue_step = {
                "grid": [row[:] for row in S],
                "dist": [row[:] for row in dist],
                "queue": list(q),
                "current": (x, y),
                "next": (nx, ny),
                "message": f"マス({nx}, {ny})をキューに追加、距離を{dist[nx][ny]}に設定"
            }
            steps.append(queue_step)
    
    # 最終的な結果を記録
    final_step = {
        "grid": [row[:] for row in S],
        "dist": [row[:] for row in dist],
        "queue": [],
        "current": None,
        "message": "BFS完了"
    }
    steps.append(final_step)
    
    max_dist = max(max(row) for row in dist)
    
    return {
        "H": H,
        "W": W,
        "grid": S,
        "steps": steps,
        "max_dist": max_dist
    }

def create_html(bfs_data):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>BFS Visualization - AtCoder AGC033 A</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            .container {
                display: flex;
                flex-wrap: wrap;
            }
            .grid-container {
                margin-right: 20px;
            }
            .info-container {
                min-width: 300px;
            }
            .grid {
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            .grid td {
                width: 30px;
                height: 30px;
                text-align: center;
                border: 1px solid #ccc;
                font-size: 12px;
            }
            .black {
                background-color: #333;
                color: white;
            }
            .current {
                background-color: #ff6347;
                color: white;
            }
            .next {
                background-color: #4caf50;
                color: white;
            }
            .queued {
                background-color: #3498db;
                color: white;
            }
            .controls {
                margin-bottom: 20px;
            }
            button {
                padding: 5px 10px;
                margin-right: 5px;
            }
            .step-indicator {
                margin-bottom: 10px;
            }
            .message {
                margin-bottom: 10px;
                padding: 10px;
                background-color: #f5f5f5;
                border-radius: 5px;
            }
            .queue-container {
                margin-bottom: 20px;
            }
            .queue-item {
                display: inline-block;
                width: 40px;
                height: 20px;
                text-align: center;
                background-color: #3498db;
                color: white;
                margin-right: 5px;
                padding: 5px;
                border-radius: 3px;
            }
        </style>
    </head>
    <body>
        <h1>BFS可視化 - AtCoder AGC033 A</h1>
        
        <div class="controls">
            <button id="prevBtn">前へ</button>
            <button id="nextBtn">次へ</button>
            <button id="playBtn">再生</button>
            <button id="pauseBtn">停止</button>
            <span id="playSpeed">
                速度: 
                <select id="speedSelect">
                    <option value="2000">遅い (2秒)</option>
                    <option value="1000" selected>普通 (1秒)</option>
                    <option value="500">速い (0.5秒)</option>
                    <option value="200">超速い (0.2秒)</option>
                </select>
            </span>
        </div>
        
        <div class="step-indicator">
            ステップ: <span id="currentStep">0</span> / <span id="totalSteps">0</span>
        </div>
        
        <div class="message" id="message"></div>
        
        <div class="container">
            <div class="grid-container">
                <h2>グリッド</h2>
                <table class="grid" id="gridTable"></table>
                
                <h2>距離</h2>
                <table class="grid" id="distTable"></table>
            </div>
            
            <div class="info-container">
                <h2>キューの状態</h2>
                <div class="queue-container" id="queue"></div>
                
                <h2>統計</h2>
                <div id="stats">
                    <p>グリッドサイズ: <span id="gridSize"></span></p>
                    <p>最大距離: <span id="maxDist"></span></p>
                    <p>処理済みのセル: <span id="processedCells">0</span></p>
                </div>
            </div>
        </div>

        <script>
            const bfsData = BFSDATA;
            let currentStepIndex = 0;
            let playInterval = null;
            let playSpeed = 1000; // デフォルトは1秒
            
            // HTML要素の初期化
            document.getElementById('gridSize').textContent = `${bfsData.H} × ${bfsData.W}`;
            document.getElementById('maxDist').textContent = bfsData.max_dist;
            document.getElementById('totalSteps').textContent = bfsData.steps.length - 1;
            
            // グリッドの初期化
            function initializeGrid() {
                const gridTable = document.getElementById('gridTable');
                const distTable = document.getElementById('distTable');
                
                gridTable.innerHTML = '';
                distTable.innerHTML = '';
                
                for (let i = 0; i < bfsData.H; i++) {
                    const gridRow = gridTable.insertRow();
                    const distRow = distTable.insertRow();
                    
                    for (let j = 0; j < bfsData.W; j++) {
                        const gridCell = gridRow.insertCell();
                        gridCell.id = `grid-${i}-${j}`;
                        gridCell.textContent = bfsData.grid[i][j];
                        if (bfsData.grid[i][j] === '#') {
                            gridCell.classList.add('black');
                        }
                        
                        const distCell = distRow.insertCell();
                        distCell.id = `dist-${i}-${j}`;
                    }
                }
            }
            
            // ステップを表示
            function showStep(stepIndex) {
                if (stepIndex < 0 || stepIndex >= bfsData.steps.length) return;
                
                const step = bfsData.steps[stepIndex];
                
                // キューの更新
                updateQueue(step.queue);
                
                // 現在のセルとマークアップを更新
                updateCells(step);
                
                // メッセージの更新
                document.getElementById('message').textContent = step.message;
                
                // ステップ表示の更新
                document.getElementById('currentStep').textContent = stepIndex;
                
                // 処理済みセル数の更新
                let processed = 0;
                for (let i = 0; i < bfsData.H; i++) {
                    for (let j = 0; j < bfsData.W; j++) {
                        if (step.dist[i][j] !== -1) processed++;
                    }
                }
                document.getElementById('processedCells').textContent = processed;
            }
            
            // セルの更新
            function updateCells(step) {
                // すべてのセルクラスをリセット
                for (let i = 0; i < bfsData.H; i++) {
                    for (let j = 0; j < bfsData.W; j++) {
                        const gridCell = document.getElementById(`grid-${i}-${j}`);
                        const distCell = document.getElementById(`dist-${i}-${j}`);
                        
                        // グリッド表示の更新（黒マスは維持）
                        if (bfsData.grid[i][j] !== '#') {
                            gridCell.className = '';
                        }
                        
                        // 距離表示の更新
                        distCell.textContent = step.dist[i][j] === -1 ? '-' : step.dist[i][j];
                        distCell.className = '';
                    }
                }
                
                // 現在のセルをマーク
                if (step.current) {
                    const [x, y] = step.current;
                    const gridCell = document.getElementById(`grid-${x}-${y}`);
                    if (bfsData.grid[x][y] !== '#') {
                        gridCell.classList.add('current');
                    }
                    const distCell = document.getElementById(`dist-${x}-${y}`);
                    distCell.classList.add('current');
                }
                
                // 次に追加されるセルをマーク
                if (step.next) {
                    const [nx, ny] = step.next;
                    const gridCell = document.getElementById(`grid-${nx}-${ny}`);
                    gridCell.classList.add('next');
                    const distCell = document.getElementById(`dist-${nx}-${ny}`);
                    distCell.classList.add('next');
                }
                
                // キューに入っているセルをマーク
                for (const [qx, qy] of step.queue) {
                    const gridCell = document.getElementById(`grid-${qx}-${qy}`);
                    if (!gridCell.classList.contains('current') && bfsData.grid[qx][qy] !== '#') {
                        gridCell.classList.add('queued');
                    }
                    const distCell = document.getElementById(`dist-${qx}-${qy}`);
                    if (!distCell.classList.contains('current')) {
                        distCell.classList.add('queued');
                    }
                }
            }
            
            // キューの表示を更新
            function updateQueue(queue) {
                const queueContainer = document.getElementById('queue');
                queueContainer.innerHTML = '';
                
                if (queue.length === 0) {
                    queueContainer.textContent = '空';
                    return;
                }
                
                for (const [x, y] of queue) {
                    const queueItem = document.createElement('div');
                    queueItem.className = 'queue-item';
                    queueItem.textContent = `(${x},${y})`;
                    queueContainer.appendChild(queueItem);
                }
            }
            
            // イベントリスナーの設定
            document.getElementById('prevBtn').addEventListener('click', () => {
                pausePlayback();
                if (currentStepIndex > 0) {
                    currentStepIndex--;
                    showStep(currentStepIndex);
                }
            });
            
            document.getElementById('nextBtn').addEventListener('click', () => {
                pausePlayback();
                if (currentStepIndex < bfsData.steps.length - 1) {
                    currentStepIndex++;
                    showStep(currentStepIndex);
                }
            });
            
            document.getElementById('playBtn').addEventListener('click', startPlayback);
            document.getElementById('pauseBtn').addEventListener('click', pausePlayback);
            
            document.getElementById('speedSelect').addEventListener('change', (e) => {
                playSpeed = parseInt(e.target.value);
                if (playInterval) {
                    pausePlayback();
                    startPlayback();
                }
            });
            
            function startPlayback() {
                if (playInterval) return;
                
                playInterval = setInterval(() => {
                    if (currentStepIndex < bfsData.steps.length - 1) {
                        currentStepIndex++;
                        showStep(currentStepIndex);
                    } else {
                        pausePlayback();
                    }
                }, playSpeed);
            }
            
            function pausePlayback() {
                if (playInterval) {
                    clearInterval(playInterval);
                    playInterval = null;
                }
            }
            
            // 初期化
            initializeGrid();
            showStep(0);
        </script>
    </body>
    </html>
    """
    
    # bfsDataをJSON形式に変換して挿入
    json_data = json.dumps(bfs_data, ensure_ascii=False)
    html = html.replace('BFSDATA', json_data)
    
    return html

if __name__ == "__main__":
    # テスト入力（コメントアウト）
    # test_input = """3 3
# ...
# .##
# ..."""
    
    # 標準入力から読み込む
    test_input = ""
    H, W = map(int, input().split())
    test_input = f"{H} {W}\n"
    for _ in range(H):
        test_input += input() + "\n"
    
    # BFS実行
    bfs_data = bfs_visualization(test_input)
    
    # HTML生成
    html_content = create_html(bfs_data)
    
    # HTMLファイルとして保存して開く
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f:
        f.write(html_content.encode('utf-8'))
        temp_path = f.name
    
    print(f"HTMLファイルを作成しました: {temp_path}")
    webbrowser.open('file://' + temp_path)
    
    # 結果の表示
    print(f"最大距離: {bfs_data['max_dist']}")