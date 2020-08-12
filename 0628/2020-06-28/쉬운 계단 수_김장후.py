import sys; input = sys.stdin.readline

N = int(input())
mod = 10**9
arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
answer = arr[:]
start = 1
while start < N:
    for i in range(10):
        if not i:
            answer[0] = arr[1]
        elif i == 9:
            answer[9] = arr[8]
        else:
            answer[i] = arr[i-1] + arr[i+1]
    start += 1
    arr = answer[:]
print(sum(answer)%mod)