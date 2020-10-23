# 원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어
# 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니다.
# 단, 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.

# 2.
def solution3(sticker):
    answer = 0
    L = len(sticker)
    visit = [0]*L

    def dfs(tmp):
        nonlocal answer
        if visit.count(0) == 0:
            answer = max(answer, tmp)
        else:
            for i in range(L):
                if visit[i] == 0:
                    visit[i-1], visit[i], visit[i+1] = visit[i-1]+1, visit[i]+1, visit[i+1]+1
                    dfs(tmp+sticker[i])
                    visit[i-1], visit[i], visit[i+1] = visit[i-1]-1, visit[i]-1, visit[i+1]-1
    visit[0], visit[1], visit[-1] = 1, 1, 1
    dfs(sticker[0])
    visit[0], visit[1], visit[-1] = 0, 0, 0

    visit[0], visit[-2], visit[-1] = 1, 1, 1
    dfs(sticker[-1])
    visit[0], visit[-2], visit[-1] = 0, 0, 0

    visit[0], visit[-1] = 1, 1
    dfs(0)
    visit[0], visit[-1] = 0, 0
    return answer

print(solution3([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution3([1, 3, 2, 5, 4]))



# 2.
def solution2(sticker):
    answer = 0
    L = len(sticker)
    visit = [0]*L

    def dfs(tmp):
        nonlocal answer
        if visit.count(0) == 0:
            answer = max(answer, tmp)
        else:
            for i in range(L):
                if visit[i] == 0:
                    visit[i-1], visit[i], visit[i+1] = visit[i-1]+1, visit[i]+1, visit[i+1]+1
                    dfs(tmp+sticker[i])
                    visit[i-1], visit[i], visit[i+1] = visit[i-1]-1, visit[i]-1, visit[i+1]-1
    visit[0], visit[1], visit[-1] = 1, 1, 1
    dfs(sticker[0])
    visit[0], visit[1], visit[-1] = 0, 0, 0

    visit[0], visit[-2], visit[-1] = 1, 1, 1
    dfs(sticker[-1])
    visit[0], visit[-2], visit[-1] = 0, 0, 0

    visit[0], visit[-1] = 1, 1
    dfs(0)
    visit[0], visit[-1] = 0, 0
    return answer

print(solution2([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution2([1, 3, 2, 5, 4]))

# 1. 완전탐색 풀이
def solution(sticker):
    answer = 0
    L = len(sticker)
    visit = [0]*L

    def dfs(tmp):
        nonlocal answer
        if visit.count(0) == 0:
            answer = max(answer, tmp)
        else:
            for i in range(L):
                if visit[i] == 0:
                    if i == 0: visit[-1], visit[i], visit[i+1] = visit[-1]+1, visit[i]+1, visit[i+1]+1
                    elif i == L-1: visit[i-1], visit[i], visit[0] = visit[i-1]+1, visit[i]+1, visit[0]+1
                    else: visit[i-1], visit[i], visit[i+1] = visit[i-1]+1, visit[i]+1, visit[i+1]+1
                    dfs(tmp+sticker[i])
                    if i == 0: visit[-1], visit[i], visit[i+1] = visit[-1]-1, visit[i]-1, visit[i+1]-1
                    elif i == L-1: visit[i-1], visit[i], visit[0] = visit[i-1]-1, visit[i]-1, visit[0]-1
                    else: visit[i-1], visit[i], visit[i+1] = visit[i-1]-1, visit[i]-1, visit[i+1]-1

    dfs(0)
    return answer

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))

