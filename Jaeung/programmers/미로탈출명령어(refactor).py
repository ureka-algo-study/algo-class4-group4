# 재귀 깊이 초과 에러를 방지
import sys
sys.setrecursionlimit(100000)

def solution(n, m, x, y, r, c, k):
    
    # 사전 순으로 문자열을 배열하기 위해 d,l,r,u 순서대로 방향을 배치한다.
    directions = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0)}
        
    def dfs(curr_x, curr_y, remaining, path):
        dist = abs(r-curr_x) + abs(c-curr_y)
        # (가지치기) 현재 위치에서 목적지까지 최소거리가 남은 횟수보다 크면 불가능
        # (가지치기) 남은 횟수에서 최소거리를 뺀 횟수가 홀수일 경우, 딱 맞게 탈출 불가능
        if dist > remaining or (remaining - dist) % 2 != 0:
            return False
        if remaining == 0:
            return curr_x == r and curr_y == c
        
        for d, (dr, dc) in directions.items():
            next_x, next_y = curr_x + dr, curr_y + dc
            if 0 < next_x <= n and 0 < next_y <= m:
                path.append(d)
                if dfs(next_x, next_y, remaining - 1, path):
                    return True
                path.pop()
        return False
    
    path = []
    if not dfs(x, y, k, path):
        return "impossible"    
    return ''.join(path) 