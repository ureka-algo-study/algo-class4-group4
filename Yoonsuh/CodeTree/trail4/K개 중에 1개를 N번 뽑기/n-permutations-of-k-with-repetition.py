k, n = map(int, input().split())
nums = []

def print_permutation():
    for num in nums:
        print(num, end = " ")
    print()

def find_permutations(cnt):
    if cnt == n:
        print_permutation()
        return

    for i in range(1, k+1):
        nums.append(i)
        find_permutations(cnt+1)
        nums.pop()

find_permutations(0)
