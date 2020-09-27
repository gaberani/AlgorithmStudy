# 모든 수가 0 또는 1로 이루어진 2차원 배열 a가 주어집니다.
# b의 모든 원소는 0 아니면 1입니다.
# a의 행/열의 개수와 b의 행/열의 개수가 같습니다. (= a와 b의 크기가 같습니다.)
# i = 1, 2, ..., (a의 열의 개수)에 대해서 a의 i번째 열과 b의 i번째 열에 들어 있는 1의 개수가 같습니다.
# b의 각 행에 들어 있는 1의 개수가 짝수입니다. (0도 짝수입니다.)

from itertools import combinations

# 모든 경우의 수 체크
def solution(a):
    # 조건을 모두 만족하는 [2차원 배열 b의 경우의 수%(107 + 19)]로 return
    answer = 0
    L_row, L_col = len(a), len(a[0])
    # a의 각 열에 있는 1의 개수 세기
    a_one = []
    for col in list(zip(*a)):
        a_one.append(col.count(1))

    # 각 열마다 조합 뽑기
    possible_lst = combinations(list(range(L_row*L_col)), sum(a_one))
    for one_possible in possible_lst:
        b = [[0] * L_col for _ in range(L_row)]
        flag = 1
        for idx in one_possible:
            # print(idx, '/ i, j:', idx//L_col, idx%L_col)
            b[idx//L_col][idx%L_col] = 1

        # b의 각 행에 들어 있는 1의 개수가 짝수인지 체크(나머지)
        for b_row in b:
            if b_row.count(1)%2: flag = 0; break

        # a의 i번째 열과 b의 i번째 열에 들어 있는 1의 개수가 같습니다.
        a_one_idx = 0
        for col in list(zip(*b)):
            if a_one[a_one_idx] != col.count(1): flag = 0; break
            a_one_idx += 1

        if flag:
            answer += 1
    return answer

# 가능한 행을 하나하나 짜기
# 파스칼 정리
def solution1(a):
    answer = 0
    return answer




# 6
print(solution([[0,1,0],
                [1,1,1],
                [1,1,0],
                [0,1,1]]))
# 0
print(solution([[1,0,0],
                [1,0,0]]))
# 72
print(solution([[1,0,0,1,1],
                [0,0,0,0,0],
                [1,1,0,0,0],
                [0,0,0,0,1]]))