def solution(info, edges):
    visited = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        # 양의 수가 늑대의 수보다 더 많을 때만 DFS 탐색을 수행한다.
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep + 1, wolf)
                elif info[child] == 1:
                    dfs(sheep, wolf + 1)
                # DFS 탐색 이후, 상태를 초기화한다. 
                # 이전에 탐색한 노드를 다른 경로에서도 탐색 가능하게 해준다.
                visited[child] = 0
    
    # 루트 노드에는 항상 양이 있으므로 양 1마리, 늑대 0마리의 상태로 시작한다.
    visited[0] = 1
    dfs(1, 0)
    
    return max(answer)   