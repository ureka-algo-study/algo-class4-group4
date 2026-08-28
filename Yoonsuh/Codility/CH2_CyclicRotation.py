def solution(A, K):
    if not A:
        return A
    N = len(A)
    K = K % N        # K가 N보다 크면 실제 이동량으로 축소
    return A[-K:] + A[:-K]

"""
나의 풀이
from collections import deque 
def solution(A, K):     
    newA = deque(A)     
    for i in range(K):         
        if A:             
            item = newA.pop()             
            newA.appendleft(item)     
    arr = []     
    for a in newA:         
        arr.append(a)     
    return arr
"""