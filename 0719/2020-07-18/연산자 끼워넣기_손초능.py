import sys

def dfs(idx, value):
    global nums, cal, min_value, max_value, n
    if idx == n:
        min_value = min(min_value, value)
        max_value = max(max_value, value)
    else:
        for i in range(4):
            if cal[i]:
                cal[i] -= 1
                if i == 0: dfs(idx+1, value+nums[idx])
                elif i == 1: dfs(idx+1, value-nums[idx])
                elif i == 2: dfs(idx+1, value*nums[idx])
                else:
                    if value >= 0: dfs(idx+1, value//nums[idx])
                    else: dfs(idx+1, -(abs(value)//nums[idx]))
                cal[i] += 1

input = sys.stdin.readline

n = int(input())
min_value = float('inf')
max_value = -float('inf')
nums = list(map(int, input().split()))
cal = list(map(int, input().split()))

dfs(1, nums[0])

print(max_value)
print(min_value)
