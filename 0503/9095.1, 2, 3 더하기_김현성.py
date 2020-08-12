def sum(num, N):
    global result
    if num == N:
        result += 1
    elif num < N:
        sum(num+1, N)
        sum(num+2, N)
        sum(num+3, N)

T = int(input())
for _ in range(T):
    result = 0
    N = int(input())
    sum(0, N)
    print(result)