def solution(n, k, cmds):
    answer = ''
    prev = [i-1 for i in range(n+1)]
    nxt = [i+1 for i in range(n+1)]
    stack = [] # 삭제한 걸 저장하는 스택. 최근에 삭제한 걸 삭제하기 때문
    
    for cmd in cmds:
        if cmd == 'C': # 현재 선택된 행을 삭제. 바로 아래 행을 삭제
            stack.append(k) # 해당 위치를 스택에 저장
            prev[nxt[k]] = prev[k] # k 다음 행이 이제 k 이전 행을 앞으로 바라보게
            nxt[prev[k]] = nxt[k] # k 이전 행이 k 다음 행을 뒤로 바라보게
            k = nxt[k] if nxt[k] < n else prev[k] # 바로 아래 행을 선택. 단, 마지막 행이면 윗 행을 선택
        elif cmd == 'Z': # 최근에 삭제된 것을 복구
            r = stack.pop() # 삭제 저장소에서 한 개를 뺌. 
            nxt[prev[r]] = r # 연결 복원
            prev[nxt[r]] = r
        else: # U 혹은 D 중 하나입니다. 
            c, X = cmd.split()
            if c == 'U':
                for _ in range(int(X)):
                    k = prev[k] # k의 이전행으로 갱신. 이걸 X만큼 반복.
            elif c == 'D':
                for _ in range(int(X)):
                    k = nxt[k] # # k의 다음 행으로 갱신. 이걸 X만큼 반복.
                    
    deleted = set(stack) # 중복 제거
    for i in range(n): # 삭제 여부 기준으로 정답 문자열 만들기
        if i in deleted:
            answer+='X'
        else:
            answer+='O'
    # answer = ''.join(['X' if i in deleted else 'O' for i in range(n)])
    return answer