import sys
input = sys.stdin.readline
from collections import deque

N, r, c, d = map(int, input().split())
# 1-based 좌표를 0-based 좌표로 설정하기 위해 r, c 값을 -1 해준다
r -= 1
c -= 1
ocean = [list(map(int, input().split())) for _ in range(N)]

# 1 : 상 / 2 : 하 / 3 : 좌 / 4 : 우
# d == 1 : 우선순위 : [1, 3, 4, 2]
# d == 2 : 우선순위 : [2, 4, 3, 1]
# d == 3 : 우선순위 : [3, 2, 1, 4]
# d == 4 : 우선순위 : [4, 1, 2, 3]
up, down, left, right = 1, 2, 3, 4
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
direction = [
    [], [1, 3, 4, 2], [2, 4, 3, 1], [3, 2, 1, 4], [4, 1, 2, 3]
]

visited = [[False] * N for _ in range(N)]
visited[r][c] = True

unvisited_ocean = 0
for i in range(N):
    for j in range(N):
        if ocean[i][j] == 0:
            unvisited_ocean += 1
# 고래가 출발하는 시작점도 방문한 바다로 치기 때문에 남은 미방문 바다 개수에서 -1
unvisited_ocean -= 1
print(r + 1, c + 1)

def to_target(start_r, start_c):
    dist = [[-1] * N for _ in range(N)]
    dist[start_r][start_c] = 0
    queue = deque([(start_r, start_c)])

    # 시작점(start_r, start_c)을 기준으로 탐험 가능한 모든 바다까지의 최단거리를 dist에 넣는다
    while queue:
        curr_r, curr_c = queue.popleft()
        for i in range(1, 5):
            next_r = curr_r + dr[i]
            next_c = curr_c + dc[i]
            # 다음 위치가 바다 밖으로 벗어나지 않으면 / 암초가 아니라 바다면 / 이번 BFS 탐색에서 아직 한 번도 거리를 계산한 적이 없는 칸이면
            # 위 조건들을 다 만족하면 다음 칸(next_r, next_c) 까지의 거리는 현재 칸까지의 거리 + 1
            if 0 <= next_r < N and 0 <= next_c < N and ocean[next_r][next_c] == 0 and dist[next_r][next_c] == -1:
                dist[next_r][next_c] = dist[curr_r][curr_c] + 1
                queue.append((next_r, next_c))

    return dist


while unvisited_ocean > 0:

    # 1단계 : 인접 탐험
    step1 = False
    for next_d in direction[d]:
            next_r = r + dr[next_d]
            next_c = c + dc[next_d]

            if 0 <= next_r < N and 0 <= next_c < N and ocean[next_r][next_c] == 0 and not visited[next_r][next_c]:
                r, c, d = next_r, next_c, next_d
                visited[r][c] = True
                unvisited_ocean -= 1
                print(r + 1, c + 1)
                step1 = True
                break
            
    # 1단계 성공하면 2단계 진행하지 않고 다음 루프로 이동
    if step1:
        continue


    # 2단계 : 가장 가까운 바다로 이동    
    dist = to_target(r, c)
    minimum = float('inf')
    target_r, target_c = -1, -1

    for i in range(N):
        for j in range(N):
            # 목표 지점이 암초가 아니라 바다면 / 아직 방문한 적이 없는 바다면 / 암초에 막히지 않고 실제로 도달할 수 있는 바다면
            if ocean[i][j] == 0 and not visited[i][j] and dist[i][j] != -1:
                # 자격을 만족하는 바다 칸 중에서 현재까지의 최솟값보다 더 짧은 거리를 가진 바다가 있으면 최솟값 갱신
                if dist[i][j] < minimum:
                    minimum = dist[i][j]
                    target_r, target_c = i, j

    # 지도를 다 탐색했고 방문하지 않은 바다가 없으면 탐색 종료
    if target_r == -1:
        break
    target_dist = to_target(target_r, target_c)

    # 목표 지점으로 이동
    while r != target_r or c != target_c:
        curr_d = target_dist[r][c]
        
        # 우선순위 : 좌 - 하 - 우 - 상
        priority = [3, 2, 4, 1]
        for p in priority:
            next_r = r + dr[p]
            next_c = c + dc[p]
            # 목표 지점까지의 거리가 1 줄어드는 방향으로 바다 탐험
            if 0 <= next_r < N and 0 <= next_c < N and target_dist[next_r][next_c] == curr_d - 1:
                r, c, d = next_r, next_c, p
                break

    # 목표 지점 탐험 완료 처리 및 남은 바다의 개수 -1
    visited[r][c] = True
    unvisited_ocean -= 1
    print(r + 1, c + 1)
