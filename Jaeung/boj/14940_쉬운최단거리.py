import sys
input = sys.stdin.readline
from collections import deque

def bfs(n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if res[nx][ny] == -1 and maps[nx][ny] == 1:
                    res[nx][ny] = res[x][y] + 1
                    queue.append((nx, ny))

n, m = map(int, input().split())
maps = []
res = [[-1] * m for _ in range(n)]
queue = deque()

for i in range(n):
    line = list(map(int, input().split()))
    maps.append(line)

    for j in range(m):
        if line[j] == 2:
            queue.append((i, j))
            res[i][j] = 0
        elif line[j] == 0:
            res[i][j] = 0

bfs(n, m)

for line in res:
    print(*line)