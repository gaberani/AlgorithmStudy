# 크기가 a by b인 행렬과 크기가 b by c 인 행렬이 있을 때,
# 두 행렬을 곱하기 위해서는 총 a x b x c 번 곱셈해야합니다.

# 행렬의 개수가 3개 이상일 때는 연산의 순서에 따라서
# 곱하기 연산의 횟수가 바뀔 수 있습니다.
# 예를 들어서 크기가 5 by 3인 행렬 A,
# 크기가 3 by 10인 행렬 B,
# 크기가 10 by 6인 행렬 C가 있을 때,
# 순서대로 A와 B를 먼저 곱하고,
# 그 결과에 C를 곱하면 A와 B행렬을 곱할 때 150번을,
# AB 에 C를 곱할 때 300번을 연산을 해서 총 450번의 곱하기 연산을 합니다.
# 하지만, B와 C를 먼저 곱한 다음 A 와 BC를 곱하면
# 180 + 90 = 270번 만에 연산이 끝납니다.

# 행렬의 개수는 3이상 200이하의 자연수입니다.
# 각 행렬의 행과 열의 크기는 200이하의 자연수 입니다.
# 계산을 할 수 없는 행렬은 입력으로 주어지지 않습니다.
import sys
def solution(matrix_sizes):
    # 모든 행렬을 곱하기 위한 최소 곱셈 연산의 수를 return
    answer = 200**3
    # 큰 수를 가운데에 놔서 연산 수를 작게 만드는 것이 핵심
    # 행렬이 4개라면 AB, CD로 연산한뒤 그 둘의 결과를 연산하는 것도
    # 가능해야함

    def dfs(cnt, i, visit, result):
        if cnt == i:
            return result
        else:
            for j in range(L-1):
                if visit[j] == 0:
                    if matrix_sizes[j][1] == matrix_sizes[j+1][0]:
                        visit[j], visit[j+1] = 1, 1
                        dfs(cnt+1, L, visit, result+matrix_sizes[j][0]*matrix_sizes[j][1]*matrix_sizes[j+1][1])
                        visit[j], visit[j+1] = 0, 0

                    if matrix_sizes[j+1][1] == matrix_sizes[j][0]:
                        visit[j], visit[j + 1] = 1, 1
                        dfs(cnt+1, L, visit, result+matrix_sizes[j+1][0]*matrix_sizes[j+1][1]*matrix_sizes[j][1])
                        visit[j], visit[j + 1] = 0, 0

    L = len(matrix_sizes)
    answer = min(dfs(0, L-1, [0]*L, 0), answer)

    return answer





# def sol(cnt, N, visit, mat, Max):
#     if cnt == N:
#         return 0
#     if str(cnt)+str(N) in visit:
#         return visit[str(cnt) + str(N)]
#     result = Max
#     for a in range(cnt, N):
#         result = min(result, sol(cnt, a, visit, mat, Max) + sol(a + 1, N, visit, mat, Max) + mat[cnt][0] * mat[a][1] * mat[N][1])
#     visit[str(cnt) + str(N)] = result
#     return result
#
# def solution(matrix_sizes):
#     mat = matrix_sizes
#     visit = {}
#     N = len(matrix_sizes)
#     answer = sol(0, N-1, visit, matrix_sizes, 200*200*200*N)
#     return answer