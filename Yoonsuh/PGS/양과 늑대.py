def dfs(idx, sheep, wolf, possible):
    global g_info, answer, graph
    if g_info[idx] == 0: # 0, 즉 양
        sheep += 1
        answer = max(answer, sheep) # 최대 몇 마리인지 구하는 것이므로
    else: # 1, 즉 늑대
        wolf += 1
        
    if wolf >= sheep: # 양의 수보다 늑대의 수가 같거나 더 많아지면 스톱
        return 
    
    possible.extend(graph[idx]) # possible에 추가
    for p in possible:
        dfs(p, sheep, wolf, [i for i in possible if i != p])
    
def solution(info, edges):
    global answer, g_info, graph # 최대 양의 수, 전역으로 정보 배열 사용, 배열
    answer = 0
    g_info = info
    n = len(info)
    graph = [[] for _ in range(n)]
    
    for a, b in edges:
        graph[a].append(b)
        
    
    dfs(0, 0, 0, [])
    return answer

# ##### 개념 공부 #####
# ### 1. 인접 리스트 (Adjacency List) 구현 ###
# adj = [[] for _ in range(5)]
# for parent, child in edges:
#     adj[parent].append(child)

# ### 2. 비트마스킹 (Bitmasking) ###
# """
# 파이썬의 정수는 크기 제한이 유연. 비트 연산이 매우 빠름. 
# 17개 노드 방문 여부를 숫자로 압축하거나 set, dictionary 키 
# 활용 가능하다. 

# 현재 상태에 i번 노드 추가 : state | (1 << i)
# i번 노드 방문 여부 확인 : if state & (1 << i)

# 이유: visited = [False] * (1<<17)처럼 리스트를 만들거나 
# set()에 state를 저장하여 "이미 이 노드 조합으로 탐색한 적이
# 있는가?"를 체크해 중복 연산을 방지.
# """

# ### 3. 비선형 백트래킹과 후보군 전달 ###
# """
# 이 문제의 핵심은 "다음에 갈 수 있는 노드 리스트"를 함수의
# 인자로 계속 넘겨주는 것이다. 일반적인 DFS는 현재 노드의
# 자식만 보지만, 여기서는 지금까지 거쳐온 모든 노드의 자식들을
# 다 후보군에 넣어야 한다. 
# """
# def solution(info, edges):
#     visited = [0] * len(info)
#     answer = []
    
#     def dfs(sheep, wolf):
#         if sheep > wolf:
#             answer.append(sheep)
#         else:
#             return
#         for p, c in edges:
#             if visited[p] and not visited[c]:
#                 visited[c] = 1
#                 if info[c] == 0:
#                     dfs(sheep+1, wolf)
#                 else:
#                     dfs(sheep, wolf+1)
#                 visited[c] = 0
    
#     visited[0] = 1
#     dfs(1, 0)
    
#     return max(answer)