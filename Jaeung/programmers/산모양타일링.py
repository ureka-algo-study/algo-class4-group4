def solution(n, tops):
    mod = 10007

    # a[i] : i번째 정삼각형을 3번 방법으로 덮은 경우의 수
    # b[i] : i번째 정삼각형을 1, 2, 4번 방법으로 덮은 경우의 수
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]    
    a[0] = 1
    b[0] = 3 if tops[0] == 1 else 2
    
    for i in range(1, n):
        if tops[i] == 1:
            # 이전 방법의 경우의 수에 대해 모두 3번 적용 가능
            a[i] = a[i-1] + b[i-1]
            # 이전 방법이 3번인 경우 1, 4번 적용 가능 / 이전 방법이 3번이 아닌 경우 1, 2, 4번 적용 가능
            b[i] = a[i-1] * 2 + b[i-1] * 3
        else:
            # 이전 방법의 경우의 수에 대해 모두 3번 적용 가능
            a[i] = a[i-1] + b[i-1]
            # 이전 방법이 3번인 경우 4번 적용 가능 / 이전 방법이 3번이 아닌 경우 2, 4번 적용 가능
            b[i] = a[i-1] + b[i-1] * 2
            
        a[i] %= mod
        b[i] %= mod
        
    return (a[-1] + b[-1]) % mod