from collections import deque

def solution(m, n, h, w, drops):
    answer = []
    # 끝까지 비가 오지 않는 칸의 시간
    INF = len(drops) + 1
    
    # 각 칸이 몇 번째로 비를 맞는지 순서를 기록한다.
    time = [[INF] * n for _ in range(m)]
    for i in range(len(drops)):
        a, b = drops[i]
        time[a][b] = i + 1  
        
        
    width = n - w + 1
    row_min = [[0] * width for _ in range(m)]
    
    for i in range(m):
        # d에 최솟값 인덱스를 넣어준다.
        d = deque()
        for j in range(n):
            # 새로 들어오는 값보다 기존 deque 내 값들이 같거나 더 큰 경우, 해당 값들은 앞으로도 최솟값이 될 수 없으므로 pop해서 제거한다. 
            while d and time[i][d[-1]] >= time[i][j]:
                d.pop()
            d.append(j)            
            # 현재 격자 범위를 벗어난 인덱스 제거
            while d and d[0] <= j - w:
                d.popleft()
            # 범위가 다 차는 순간(인덱스가 w-1 되는 순간) 이후부터 deque의 맨 앞 최솟값을 결과에 기록
            if j >= w - 1:
                row_min[i][j - w + 1] = time[i][d[0]]
                
                
    height = m - h + 1
    rect_min = [[0] * width for _ in range(height)]
    
    # 행 방향이 아니라 열 방향으로도 같은 작업을 반복한다.
    for j in range(width):
        d = deque()
        for i in range(m):
            while d and row_min[d[-1]][j] >= row_min[i][j]:
                d.pop()
            d.append(i)            
            while d and d[0] <= i - h:
                d.popleft()
            if i >= h - 1:
                rect_min[i - h + 1][j] = row_min[d[0]][j]      
    
    
    # 선인장 구역에 대하여 가장 먼저 비를 맞는 시간(최솟값)을 다 구했으므로 이 중에서 가장 늦은 시간(최댓값)을 구하면 된다.
    maximum = -1
    answer = [0, 0]
    
    for i in range(height):
        for j in range(width):
            if rect_min[i][j] > maximum:
                # 가장 늦게 비를 맞는 시간(최댓값)을 계속 업데이트하고, 그때의 왼쪽 위칸의 좌표를 answer에 저장한다. 
                maximum = rect_min[i][j]
                answer = [i, j]
    
    
    return answer



"""

입출력 예 #1 진행 과정

m = 4, n = 5, h = 2, w =2
len(drops) = 8

width = n - w + 1 = 5 - 2 + 1 = 4
height = m - h + 1 = 4 - 2 + 1 = 3



1) 행 방향 탐색 for문

i = 0, j = 01234 :
time[i][j] = 1 -> 9 -> 9 -> 9 -> 8
deque = [0] -> [0,1] -> [0,2] -> [0,3] -> [4]
row_min[i][j - w + 1] = time[i][d[0]] = - -> 1 -> 1 -> 1 -> 8

i = 1, j = 01234 :
time[i][j] = 9 -> 5 -> 9 -> 3 -> 9
deque = [0] -> [1] -> [1,2] -> [3] -> [3,4]
row_min[i][j - w + 1] = time[i][d[0]] = - -> 5 -> 5 -> 3 -> 3

i = 2, j = 01234 :
time[i][j] = 9 -> 9 -> 6 -> 7 -> 4
deque = [0] -> [1] -> [2] -> [2,3] -> [4]
row_min[i][j - w + 1] = time[i][d[0]] = - -> 9 -> 6 -> 6 -> 4

i = 3, j = 01234 :
time[i][j] = 9 -> 2 -> 9 -> 9 -> 9
deque = [0] -> [1] -> [1,2] -> [3] -> [4]
row_min[i][j - w + 1] = time[i][d[0]] = - -> 2 -> 2 -> 9 -> 9



2) 열 방향 탐색 for문

j = 0, i = 0123 :
row_min[i][j] = 1 -> 5 -> 9 -> 2
deque = [0] -> [0,1] -> [1,2] -> [3]
rect_min[i-h+1][j] = row_min[d[0]][j] = - -> 1 -> 5 -> 2

j = 1, i = 0123 :
row_min[i][j] = 1 -> 5 -> 6 -> 2
deque = [0] -> [0,1] -> [1,2] -> [3]
rect_min[i-h+1][j] = row_min[d[0]][j] = - -> 1 -> 5 -> 2

j = 2, i = 0123 :
row_min[i][j] = 1 -> 3 -> 6 -> 9
deque = [0] -> [0,1] -> [1,2] -> [2,3]
rect_min[i-h+1][j] = row_min[d[0]][j] = - -> 1 -> 3 -> 6

j = 3, i = 0123 :
row_min[i][j] = 8 -> 3 -> 4 -> 9
deque = [0] -> [1] -> [1,2] -> [2,3]
rect_min[i-h+1][j] = row_min[d[0]][j] = - -> 3 -> 3 -> 4



3) 최종 탐색 (마지막 for문)
rect_min 행렬 :
1 1 1 3
5 5 3 3
2 2 6 4

rect_min 행렬의 최댓값 6을 처음 만났을 때 answer이 갱신된다. 이 때의 인덱스 : (2, 2)
따라서 result = [2, 2]


"""