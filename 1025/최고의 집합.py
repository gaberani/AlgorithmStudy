# 자연수 n 개로 이루어진 중복 집합(multi set, 편의상 이후에는 집합으로 통칭) 중에
# 다음 두 조건을 만족하는 집합을 최고의 집합이라 함.
# 1. 각 원소의 합이 S가 되는 수의 집합
# 2. 위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합

# 런타임 에러???
# 집합의 원소의 개수 n과 모든 원소들의 합 s
def solution(n, s):
    # 최고의 집합이 존재하지 않는 경우 -1을 채워서 return
    answer = []

    maxMulCnt = 1
    # 최고의 집합을 return
    def dfs(SumCnt, MulCnt, tmp):
        nonlocal answer
        if len(tmp) == n:
            if SumCnt == s and maxMulCnt < MulCnt:
                answer = tmp
                print(tmp)
        else:
            for num in range(s):
                tmp.append(num)
                dfs(SumCnt+num, MulCnt*num, tmp)
                tmp.pop()

    dfs(0, 1, [])

    return answer

print(solution(2, 9)) # [4, 5]
print(solution(2, 1)) # [-1]
print(solution(2, 8)) # [4, 4]