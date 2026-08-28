# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    ans = set(i for i in range(1, X+1)) # 그냥 리스트로 하면 시간복잡도 O(n)이므로 초과됨. 
    for i, a in enumerate(A):
        if a in ans:
            ans.remove(a)
        if not ans:
            return i
    return -1