def solution(info, edges):
    answer = 0
    
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        
    # q = [(현재 위치, 양의 수, 늑대의 수, 방문 가능한 노드 집합)]
    q = [(0, 1, 0, set())]
    
    while q:
        current, sheep, wolf, visit = q.pop()
        answer = max(answer, sheep)
        # 현재 노드의 자식 노드들을 방문 가능한 노드 집합에 추가한다.
        visit.update(graph[current])
        
        for next in visit:
            if info[next] == 1:
                # 다음 노드에 방문해도 '양 > 늑대' 조건이 지켜지는 경우에만 탐색 진행
                if sheep- wolf > 1:
                    q.append((next, sheep, wolf + 1, visit - {next}))
            elif info[next] == 0 :
                q.append((next, sheep + 1, wolf, visit - {next}))
                
    return answer