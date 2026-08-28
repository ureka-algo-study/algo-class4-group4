from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, maps, n, m):
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1  # 시작점 거리 초기화

    q = deque([(y, x)])

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:  # nx 수정
                if maps[ny][nx] == 1 and dist[ny][nx] == -1:  # 미방문 체크
                    dist[ny][nx] = dist[ey][ex] + 1  # ✅ 거리 누적
                    q.append((ny, nx))

    return dist[n-1][m-1]  # -1이면 도달 불가, 그대로 반환

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    return bfs(0, 0, maps, n, m)