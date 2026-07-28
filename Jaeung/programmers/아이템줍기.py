from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    d = deque()
    
    for r in rectangle:
        # 이차원 배열에서 bfs 탐색을 진행하면 테두리를 따라가지 않고, 바로 옆에 붙어있는 점으로 더 빠르게 이동하는 문제가 생긴다.
        # 이를 방지하기 위해 모든 좌표를 2배해서 bfs 탐색을 진행한 후, 2를 나누어 최종 답으로 반환한다. 
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                
                # 테두리 내부 좌표는 0으로 채운다.
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                # 테두리 좌표는 1로 채운다. 
                elif graph[i][j] != 0:
                    graph[i][j] = 1  
    
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2   
    d.append((cx, cy))    
    
    while d:
        x, y = d.popleft()
        
        if x == ix and y == iy:
        	# 최종 답을 반환할 때 2로 나누어 반환한다.
            answer = visited[x][y] // 2
            break   
        for k in range(4):
            nx, ny = x + direction[k][0], y + direction[k][1]            
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                d.append((nx, ny))
    
    return answer