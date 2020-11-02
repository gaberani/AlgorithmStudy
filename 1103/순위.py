# n명의 권투선수가 권투 대회 각각 1번부터 n번까지 번호를 받았습니다.
# 만약 A 선수가 B 선수보다 실력이 좋다면 A는 B를 항상 이깁니다.
# 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다.

# 선수의 수 n
# 경기 결과를 담은 2차원 배열 results
# 정확하게 순위를 매길 수 있는 선수의 수를 return
def solution(n, results):
    answer = 0
    L = len(results)
    grid = [[0]*L for _ in range(L)]
    for r1, r2 in results:
        grid[r1][r2] = -1
        grid[r2][r1] = 1
    for i in range(L):
        for j in range(L):
            if grid[i][L]:

            if grid[L][i]:
    return answer

print(solution([[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]], 2))