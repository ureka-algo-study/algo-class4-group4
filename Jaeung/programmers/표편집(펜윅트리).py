# linked list 사용 없이 펜윅 트리 알고리즘을 사용해 풀이

def solution(n, k, cmd):
    deleted = []
    size = n

    for c in cmd:
        op = c[0]
        if op == 'C':
            deleted.append(k)
            size -= 1
            if k == size:
                k -= 1
        elif op == 'Z':
            if deleted.pop() <= k:
                k += 1
            size += 1
        elif op == 'U':
            k -= int(c[2:])
        elif op == 'D':
            k += int(c[2:])

    fen = [0] * (n + 1)
    for i in range(1, n + 1):
        fen[i] += 1
        j = i + (i & -i)
        if j <= n:
            fen[j] += fen[i]

    def remove(i):
        while i <= n:
            fen[i] -= 1
            i += i & -i

    LOG = n.bit_length()
    def kth(target):
        pos = 0
        for b in range(LOG, -1, -1):
            nxt = pos + (1 << b)
            if nxt <= n and fen[nxt] < target:
                pos = nxt
                target -= fen[pos]
        return pos + 1

    result = ['O'] * n
    for p in deleted:
        slot = kth(p + 1)
        result[slot - 1] = 'X'
        remove(slot)

    return ''.join(result)