

"""
내 답안
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    result1 = 1
    result2 = 1
    for i in range(len(A)-3, len(A)):
       result1 *= A[i]
    for i in range(3):
       result2 *= A[i]
    return max(result1, result2)
"""