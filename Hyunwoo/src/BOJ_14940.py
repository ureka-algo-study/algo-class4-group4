from collections import deque
import sys

def bfs (si, sj):
    q = deque([])
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 0 and visited[ni][nj] == 0:
                dist[ni][nj] = dist[ci][cj] + 1
                visited[ni][nj] = 1
                q.append((ni, nj))


input = sys.stdin.readline

N, M = map(int, input().split())
board = [[] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dist = [[0]*M for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))

flag = True
for i in range(N):
    if flag == False:
        break
    for j in range(M):
        if board[i][j] == 2:
            si, sj = i, j
            flag = False
            break

bfs(si, sj)
for i in range(N):
    for j in range(M):
        if dist[i][j] == 0 and board[i][j] == 1:
            dist[i][j] = -1

for i in range(len(dist)):
    print(*dist[i])


