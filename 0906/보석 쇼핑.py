def solution(gems):
    answer = []
    L = len(gems)   # 8, 5
    only_gems = list(set(gems)) # 4, 3
    answerLength = len(only_gems)
    for n in range(answerLength, 0, -1):
        for i1 in range(L-n+1, -1, -1):
            part_gems = gems[i1:i1+n]
            if len((set(part_gems))) is answerLength:
                answer = [i1+1, i1+n]
                # print(part_gems)
    if answer == []:
        for n in range(L, answerLength, -1):
            for i1 in range(L-n+1, -1, -1):
                part_gems = gems[i1:i1+n]
                if len((set(part_gems))) is answerLength:
                    answer = [i1+1, i1+n]
                    # print(part_gems)
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))




# Try 2
# def solution(gems):
#     gemLength, only_gems = len(gems), set(gems)
#     answer = [1, gemLength] # === 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간
#     minLength = len(only_gems)
#     # 시작은 처음 인덱스 부터
#     for i1 in range(0, gemLength-minLength):
#         flag = 0
#         # 답의 길이는 최소 모든 종류 1개씩부터 시작
#         for n in range(minLength, gemLength):
#             for i2 in range(i1+1, i1+n):
#                 # slice 후 중복제거해서 비교 & 길이가 더 짧으면
#                 part_gems = gems[i1:i2]
#                 if len(set(part_gems)) is minLength and (answer[1]-answer[0]) > (i2-i1-1):
#                     answer = [i1+1, i2]
#                     print(answer, part_gems)
#                     flag = 1
#             if flag: break
#     # 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return
#     return answer


# 코테 당시 코드
# def solution(gems):
#     answer = []
#     L = len(gems)   # 8, 5
#     only_gems = list(set(gems)) # 4, 3
#     s_L = len(only_gems)
#     for n in range(s_L, 0, -1):
#         for i1 in range(L-n+1, -1, -1):
#             part_gems = gems[i1:i1+n]
#             if len(list(set(part_gems))) == s_L:
#                 answer = [i1+1, i1+n]
#                 print(part_gems)
#     if answer == []:
#         for n in range(L, s_L, -1):
#             for i1 in range(L-n+1, -1, -1):
#                 part_gems = gems[i1:i1+n]
#                 if len(list(set(part_gems))) == s_L:
#                     answer = [i1+1, i1+n]
#                     print(part_gems)
#     return answer

