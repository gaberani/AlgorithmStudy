# X
import copy
def combination(arr, r):
    # 1.
    tmp = []
    arr = sorted(arr)
    # 2.
    def generate(chosen):
        if len(chosen) == r:
            tmp.append(copy.deepcopy(chosen))
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])
    return tmp

def solution(relation):
    answer = 0
    C = len(relation[0])    # 4: column 개수
    R = len(relation)       # 6: data 개수
    exclude = []
    for c in range(1, C+1):
        com_lst = combination(list(range(C)), c)    # 조합 리스트 짜기
        # print(com_lst)
        for num_lst in com_lst:
            test_lst = []
            for _ in range(1, len(num_lst)+1):
                test_lst += combination(num_lst, _)
            tmp_lst = []        # 조합별 테이블
            for r in range(6):
                tmp_one = ''    # 데이터 하나
                for num in num_lst:
                    tmp_one += relation[r][num]
                tmp_lst.append(tmp_one)
            if len(list(set(tmp_lst))) == R:
                if len(exclude) != 0:
                    flag = 1
                    # print(exclude)
                    for ex in exclude:
                        if ex in test_lst:
                            flag = 0
                    if flag:
                        exclude.append(num_lst)
                        answer += 1
                else:
                    exclude.append(num_lst)
                    answer += 1
    return answer

# 조합 짜기
# 1로 성공한 애들은 그 이후에 다른 거 추가해봤자 최소성 위반이므로 바로 return
# 2도 마찬가지
# 성공 안한애들은 return이 아니라 이후 조합 찾으러 가야함

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],
                ["300","tube","computer","3"],["400","con","computer","4"],
                ["500","muzi","music","3"],["600","apeach","music","2"]]))


# def combi(arr, cnt, V, visit, relation):
#     global C, R, answer
#     if cnt == V:
#         print(arr)
#         for c in range(len(arr)):
#             if arr[c] == 1:
#                 tmp_lst = []
#                 for r in range(R):
#                     tmp_lst.append(relation[r][c])
#                 if R == len(list(set(tmp_lst))):
#                     answer += 1
#                     print(tmp_lst)
#     else:
#         for c in range(C):
#             if arr[c] == 0 and visit[c] == 0:
#                 arr[c] = 1
#                 combi(arr, cnt+1, V, visit, relation)
#                 arr[c] = 0