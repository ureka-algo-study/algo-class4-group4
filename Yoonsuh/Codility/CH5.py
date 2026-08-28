##### CH5 : Prefix Sums 강의 #####
"""
1. 핵심 아이디어
배열의 특정 구간 합을 매번 계산하면 O(N). 만약 질문이
m개면 O(n*m)이 돼서 타임아웃

>> prefix sum을 미리 만들어두면 구간 합을 O(1)로 계산

2. Prefix Sum 정의
배열 A = [a0, a1, a2, ..., an-1] 에 대해:
P[0] = 0
P[1] = a0
P[2] = a0 + a1
P[3] = a0 + a1 + a2
...
P[k] = a0 + a1 + ... + a(k-1)

P의 크기는 A보다 1 크게 만들어. P[0]=0 을 앞에 둬야 함.

4. 구간 합 O(1) 계산
def count_total(P, x, y):
    return P[y + 1] - P[x]

P[y+1] = a0 + a1 + ... + ax-1 + ax + ... + ay
P[x]   = a0 + a1 + ... + ax-1
-----------------------------------------
P[y+1] - P[x] =              ax + ... + ay 

A = [2, 3, 7, 5, 1, 3, 9]
P = prefix_sums(A)

# A[2]~A[4] 합 = 7+5+1 = 13
print(count_total(P, 2, 4))   # 13

# A[0]~A[6] 합 = 전체 합
print(count_total(P, 0, 6))   # 30

# A[5]~A[6] 합 = 3+9 = 12
print(count_total(P, 5, 6))   # 12

5. 실습: 버섯 채집 문제
문제 요약:
    버섯이 도로 위에 배열로 놓여있어
    k번 위치에서 시작, m번 이동 기능
    방향은 최대 한 번만 바꿀 수 있어
    최대한 많은 버섯 수집

핵심 관찰 - 최적 이동 패턴:
방향을 최대 한 번만 바꾸니까 두 가지 경우만 존재
"""

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n+1):
        P[k] = P[k-1] + A[k-1]
    return P

def count_total(P, x, y):
    return P[y+1] - P[x]

def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)

    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n-1, max(k, k+m))
        result = max(result, count_total(pref, left_pos, right_pos))
    
    for p in range(min(m+1, n-k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2*p)))
        reesult = max(result, count_total(pref, left_pos, right_pos))


    return result