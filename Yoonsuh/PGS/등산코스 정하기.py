##### 다익스트라 알고리즘 템플릿 #####

import heapq

def solution(n, paths, gates, summits):
    hiking = [[] for _ in range(n+1)]
    dist = [float('inf')] * (n + 1)
    for path in paths:
        i, j, w = path
        hiking[i].append((j, w))
        hiking[j].append((i, w))
    
    pq = []
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        dist[gate] = 0
    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u]:
            continue
        if u in summits:    # summit 도달하면 탐색 중단
            continue
        for v, w in hiking[u]:
            new_cost = max(cost, w)
            if new_cost < dist[v]: 
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
                
    summits.sort()  # 번호 작은 것부터 확인
    
    result_summit = 0
    result_intensity = float('inf')
    
    for summit in summits:
        if dist[summit] < result_intensity:
            result_intensity = dist[summit]
            result_summit = summit
    
    return [result_summit, result_intensity]
"""
import heapq

def dijkstra(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    pq = [(0, start)] # 거리, 노드

    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u]:
            continue

        for v, w in graph[u]:
            new_cost = cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return dist
"""