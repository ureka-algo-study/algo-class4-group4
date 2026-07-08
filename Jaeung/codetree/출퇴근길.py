n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
S, T = map(int, input().split())

# Please write your code here.
import sys
input = sys.stdin.readline
from collections import deque

def solution(n, edges, S, T):
    graph = [[] for _ in range(n+1)] 
     # graph의 모든 간선 방향을 뒤집은 그래프 (i→T 도달 가능 여부를 T에서부터 역으로 계산하기 위함)
    tmp_graph = [[] for _ in range(n+1)] 

    for x, y in edges:
        graph[x].append(y)
        tmp_graph[y].append(x)

    # start에서 시작하고, block_node(정점 T 또는 S)를 만나면 bfs 확장을 멈춘다.
    # block_node의 기본값을 0으로 설정하면 정점은 1번부터 시작하므로 bfs 탐색에 영향을 주지 않는다.
    def bfs(start, near, block_node=0):
        visited = [False] * (n+1)
        visited[start] = True
        q = deque([start])
        while q:
            node = q.popleft()
            if node == block_node:
                continue
            for nxt in near[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
        return visited

    # 출근길에 사용되는 경로 조건
    A = bfs(S, graph, block_node=T)
    reachT = bfs(T, tmp_graph)

    # 퇴근길에 사용되는 경로 조건
    B = bfs(T, graph, block_node=S)
    reachS = bfs(S, tmp_graph)

    count = 0
    for i in range(1, n+1):
        if i == S or i == T:
            continue
        # 출근길에서는 S->i->T로 가는 경로 찾기 (중간에 T를 거치지 않는)
        # 퇴근길에서는 T->i->S로 가는 경로 찾기 (중간에 S를 거치지 않는)
        if A[i] and reachT[i] and B[i] and reachS[i]:
            count += 1    
    return count

print(solution(n, edges, S, T))