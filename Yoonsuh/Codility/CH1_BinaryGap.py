# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    binN = bin(N)[2:]

    maxv = 0
    cnt = 0
    sw = False
    for ch in binN:
        if ch == "1":
            if sw:
                maxv = max(maxv, cnt)
                sw = False
            else:
                sw = True
        else:
            if sw:
                cnt+=1

    return maxv