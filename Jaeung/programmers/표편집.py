def solution(n, k, cmd):
    info = {i: [i-1, i+1] for i in range(n)}
    answer = ['O' for _ in range(n)]
    tmp = []
    
    for c in cmd:
        c = c.split()
        
        if c[0] == "U":
            for _ in range(int(c[1])):
                k = info[k][0]
                
        elif c[0] == "D":
            for _ in range(int(c[1])):
                k = info[k][1]
                
        elif c[0] == "C":
            prev, nxt = info[k]
            answer[k] = 'X'
            tmp.append((prev, k, nxt))
            
            if nxt == n:
                k = info[k][0]
            else:
                k = info[k][1]
            
            # 삭제된 행 k의 앞뒤를 linked list를 사용해 연결한다.
            if prev == -1:
                info[nxt][0] = prev
            elif nxt == n:
                info[prev][1] = nxt
            else:
                info[nxt][0] = prev
                info[prev][1] = nxt
            
        elif c[0] == "Z":
            prev, now, nxt = tmp.pop()
            answer[now] = 'O'
            
            # 복구된 행 k의 앞뒤를 linked list를 사용해 연결한다.
            if prev == -1:
                info[nxt][0] = now
            elif nxt == n:
                info[prev][1] = now
            else:
                info[nxt][0] = now
                info[prev][1] = now
                
    return ''.join([x for x in answer])           
    