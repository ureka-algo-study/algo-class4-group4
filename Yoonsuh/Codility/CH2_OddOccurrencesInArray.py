# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict
def solution(A):
    arr = defaultdict(int)
    for a in A:
        arr[a]+=1
    for i, num in arr.items():
        if num % 2 == 1:
            return i
    return 0

"""
모범 답안

def solution(A):
    result = 0
    for a in A:
        result ^= a
    return result
"""