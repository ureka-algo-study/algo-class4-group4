# 효율성 테스트 - 시간 초과로 실패한 코드

# linked list 사용 없이 스택만을 사용해 풀이

def solution(n, k, cmd):
    stack = []
    size = n

    for command in cmd:
        c = command[0]

        if c == 'U':
            k -= int(command[2:])
        elif c == 'D':
            k += int(command[2:])
        elif c == 'C':
            stack.append(k)
            size -= 1
            if k == size:
                k -= 1
        elif c == 'Z':
            if stack.pop() <= k:
                k += 1
            size += 1

    result = ['O'] * size

    while stack:
        result.insert(stack.pop(), 'X')

    return ''.join(result)