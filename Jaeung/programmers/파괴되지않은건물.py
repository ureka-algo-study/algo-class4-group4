def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    # tmp : 변화량을 누적해서 기록하는 배열
    tmp = [[0] * (M+1) for _ in range(N+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            val = -degree
        elif type == 2:
            val = degree
            
        # 2차원 누적합을 기록한다. 이후 행 방향, 열 방향 for문을 돌면서 누적합을 tmp 배열에 기록한다.
        tmp[r1][c1] += val
        tmp[r1][c2 + 1] -= val
        tmp[r2+1][c1] -= val
        tmp[r2+1][c2+1] += val
        
    # 행 방향 누적합
    for r in range(N):
        for c in range(1, M):
            tmp[r][c] += tmp[r][c-1]
    
    # 열 방향 누적합
    for c in range(M):
        for r in range(1, N):
            tmp[r][c] += tmp[r-1][c]
    
    # 누적합을 계산한 tmp 배열을 기존 board 배열과 합쳐서 0보다 큰 건물만 개수를 센다.
    for r in range(N):
        for c in range(M):
            if board[r][c] + tmp[r][c] > 0:
                answer += 1
    
    return answer