def solution(board, aloc, bloc):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    INF = int(1e9)
    
    # 캐릭터들이 보드 범위 안에 있는지를 확인한다.
    def in_board(board, y, x):
        if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]):
                return False
        return True        
    
    # 이동할 수 있는 칸이 없으면 True
    def check(board, y, x):        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if in_board(board, ny, nx) and board[ny][nx]:
                return False
        return True            
    
    # dfs 알고리즘을 사용해 각 플레이어가 이길 수 있다면 최대한 빠르게, 질 수 밖에 없다면 최대한 오래 버티도록 플레이한다. 
    # (y1, x1)이 현재 턴 캐릭터, (y2, x2)가 상대 캐릭터
    def dfs(board, y1, x1, y2, x2):
        # 현재 턴 캐릭터가 이동할 곳이 없으면 패배
        if check(board, y1, x1):
            return [False, 0]
        # 두 캐릭터가 같은 발판 위에 있을 때, 현재 캐릭터가 이동해 발판이 사라지면 상대가 같은 칸에 남아있으므로 현재 플레이어가 승리
        # (이동 횟수 1번)
        if y1 == y2 and x1 == x2:
            return [True, 1]
        
        min_cnt = INF  # 이길 때 최소 이동 횟수
        max_cnt = 0   # 질 때 최대 이동 횟수 
        win = False
        
        for i in range(4):
            ny = y1 + dy[i]
            nx = x1 + dx[i]
            
            if not in_board(board, ny, nx) or not board[ny][nx]:
                continue
            
            # 다음 칸으로 이동한 후, 상대의 턴으로 재귀 호출
            # dfs 인자 순서를 (y2, x2) → (ny, nx)로 바꿔 턴 교체
            board[y1][x1] = 0
            result = dfs(board, y2, x2, ny, nx)
            board[y1][x1] = 1

            # 상대가 졌다면(result[0] = False), 현재 플레이어가 승리한다.
            if not result[0]:
                win = True
                min_cnt = min(min_cnt, result[1])
            # 상대가 이겼고 아직 승리 경우가 없다면, 최대한 오래 버틴다.
            elif not win:
                max_cnt = max(max_cnt, result[1])
                
        turn = min_cnt if win else max_cnt
        # 이동 횟수 1번(현재 캐릭터 이동) 추가 
        # (turn은 상대 기준 횟수)   
        return [win, turn+1]   
        
    
    return dfs(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]     