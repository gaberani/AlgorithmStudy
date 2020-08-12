import sys; input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    grape = int(input())
    arr.append(grape)
arr = [0] + arr + [0]
tmp = [0] * (N+2)

tmp[1] = arr[1]
tmp[2] = arr[1] + arr[2]
for i in range(3, N+2):
    tmp[i] = max(tmp[i-3] + arr[i-1] + arr[i], tmp[i-2] + arr[i], tmp[i-1])
print(tmp[N])