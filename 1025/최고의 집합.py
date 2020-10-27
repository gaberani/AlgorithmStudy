# 자연수 n 개로 이루어진 중복 집합(multi set, 편의상 이후에는 집합으로 통칭) 중에
# 다음 두 조건을 만족하는 집합을 최고의 집합이라 함.
# 1. 각 원소의 합이 S가 되는 수의 집합
# 2. 위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합

# 최적화
def solution(n, s):
    if n > s:
        return [-1]
    value, remain = s//n, s%n
    answer = [value]*n
    for i in range(remain):
        answer[i] += 1
    answer.sort()
    return answer

# 2. 굳이 절반으로 나누면서 붙일 필요가 없다.
def solution2(n, s):
    answer = []
    if n%2 == 1:
        tmp = s//3
        flag = s%3
        if not flag:
            answer.append(tmp)
            s -= tmp
        if flag:
            answer.append(tmp+1)
            s -= tmp+1
    while len(answer) != n:
        tmp = s//2
        flag = s%2
        if not flag:
            answer.append(tmp)
            answer.append(tmp)
        if flag:
            answer.append(tmp+1)
            answer.append(tmp)
    if answer.count(0):
        answer = [-1]
    answer.sort()
    return answer

# 런타임 에러??? -> RecursionError n의 길이가 10만 이상이므로 dfs가 1000회이상 들감
def dfs(SumCnt, MulCnt, tmp, n, s):
    global answer, MaxMulCnt
    if len(tmp) == n:
        if SumCnt == s and MaxMulCnt < MulCnt:
            MaxMulCnt = MulCnt
            if answer:
                while answer: answer.pop()
            for t in tmp:
                answer.append(t)
    else:
        for num in range(s):
            tmp.append(num)
            dfs(SumCnt+num, MulCnt*num, tmp, n, s)
            tmp.pop()

def solution1(n, s):
    global answer, MaxMulCnt
    # 최고의 집합이 존재하지 않는 경우 -1을 채워서 return
    answer = []
    MaxMulCnt = 1
    # 최고의 집합을 오름차순으로 정렬된 1차원 배열(list, vector) return
    dfs(0, 1, [], n, s)
    if answer == []: answer.append(-1)
    answer.sort()
    return answer


# 처음 짠 dfs
# 집합의 원소의 개수 n과 모든 원소들의 합 s
# def solution1(n, s):
#     # 최고의 집합이 존재하지 않는 경우 -1을 채워서 return
#     answer = []
#     maxMulCnt = 1
#     # 최고의 집합을 return
#     def dfs(SumCnt, MulCnt, tmp):
#         nonlocal answer
#         if len(tmp) == n:
#             if SumCnt == s and maxMulCnt < MulCnt:
#                 answer = tmp
#                 print(tmp)
#         else:
#             for num in range(s):
#                 tmp.append(num)
#                 dfs(SumCnt+num, MulCnt*num, tmp)
#                 tmp.pop()
#     dfs(0, 1, [])
#     return answer

print(solution(2, 9)) # [4, 5]
print(solution(2, 1)) # [-1]
print(solution(2, 8)) # [4, 4]
print(solution(3, 12))
print(solution(3, 13))
# print(solution(10000, 100000))