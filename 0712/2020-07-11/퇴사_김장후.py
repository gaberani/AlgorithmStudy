# 2.
import sys; input = sys.stdin.readline
from collections import deque

def bfs(idx, day, money):
    global answer, todo
    q = deque()
    q.append((idx, day, money))

    while q:
        idx_, day_, money_ = q.popleft()
        if answer < money_:
            answer = money_

        for i in range(idx_+day_, N):
            if i + todo[i][0] <= N:
                q.append((i, todo[i][0], money_+todo[i][1]))


N = int(input())
todo = []
answer = 0
for _ in range(N):
    days, money = map(int, input().split())
    todo.append((days, money))

for i in range(N):
    if i + todo[i][0] <= N:
        bfs(i, todo[i][0], todo[i][1])
print(answer)



# 1.
def check(x):
    global fire, N, maxV
    queue = []
    total = 0
    queue.append((x, fire[x][0], fire[x][1], total)) # 일차, 상담기간, 돈, 총 벌어드린 돈
    maxV = 0 # 총 벌어드린 금액의 최대값
    while queue:
        k, day, money, total = queue.pop(0)
        if k + day <= N+1: # 만약 일차 + 상담기간이 전체 기간을 넘지 않는다면
            total += money # total + money
            for i in range(k+day, N+1): # 상담이후 기간부터 마지막 날까지
                if i + fire[i][0] <= N+1: # 일차 + 상담기간이 마지막 날을 넘기지 않는다면
                    queue.append((i, fire[i][0], fire[i][1], total)) # 정보 추가
            else:
                if maxV < total: # 상담 가능한 마지막 날이라면 maxV와 total을 비교
                    maxV = total
    return maxV

import sys
N = int(sys.stdin.readline())
fire = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
fire = [[0, 0]] + fire
answer = 0
for i in range(1, N+1): # 1일차부터 마지막 날까지 순서대로 탐색
    if answer < check(i):
        answer = check(i)
print(answer)

