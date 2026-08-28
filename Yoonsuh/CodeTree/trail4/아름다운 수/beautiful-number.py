n = int(input())
nums = list()
ans = 0
def beautiful():
    i = 0
    while i < n:
        if i + nums[i] - 1 >= n:
            return False
        for j in range(i, i + nums[i]):
            if nums[j] != nums[i]:
                return False
        i += nums[i]
    return True

def find_permutation(cnt):
    global ans
    if cnt == n:
        if beautiful():
            ans+=1
        return
    for i in range(1, 5):
        nums.append(i)
        find_permutation(cnt+1)
        nums.pop()
find_permutation(0)
print(ans)