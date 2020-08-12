import sys; input = sys.stdin.readline
from itertools import permutations

# 1.
def process(arr):
    global numbers, minV, maxV
    answer = numbers[0]
    for i in range(1, len(numbers)):
        if arr[i-1] == 1:
            answer += numbers[i]
        elif arr[i-1] == 2:
            answer -= numbers[i]
        elif arr[i-1] == 3:
            answer *= numbers[i]
        else:
            if answer < 0 or numbers[i] < 0:
                answer = -(abs(answer) // abs(numbers[i]))
            else:
                answer //= numbers[i]
    if minV > answer:
        minV = answer

    if maxV < answer:
        maxV = answer


N = int(input())
numbers = list(map(int, input().split()))
# 1: 덧셈, 2: 뺄셈, 3: 곱셈, 4: 나눗셈
tmp = list(map(int, input().split()))
operator = []
minV = 10 ** 9
maxV = -10 ** 9
for i in range(len(tmp)):
    for _ in range(tmp[i]):
        operator.append(i+1)
for arr in permutations(operator, N-1):
    process(arr)
print(maxV)
print(minV)

# 2.
def process(cnt, ans, add, sub, mul, div):
    global minV, maxV
    if cnt == N-1:
        if ans > maxV:
            maxV = ans
        if ans < minV:
            minV = ans
    if add:
        process(cnt+1, ans+numbers[cnt+1], add-1, sub, mul, div)
    if sub:
        process(cnt+1, ans-numbers[cnt+1], add, sub-1, mul, div)
    if mul:
        process(cnt+1, ans*numbers[cnt+1], add, sub, mul-1, div)
    if div:
        if ans < 0 or numbers[cnt+1] < 0:
            process(cnt+1, -(abs(ans)//abs(numbers[cnt+1])), add, sub, mul, div-1)
        else:
            process(cnt + 1, ans//numbers[cnt+1], add, sub, mul, div-1)

N = int(input())
numbers = list(map(int, input().split()))
# 1: 덧셈, 2: 뺄셈, 3: 곱셈, 4: 나눗셈
tmp = list(map(int, input().split()))
operator = []
minV = 10 ** 9
maxV = -10 ** 9
process(0, numbers[0], tmp[0], tmp[1], tmp[2], tmp[3])
print(maxV)
print(minV)
