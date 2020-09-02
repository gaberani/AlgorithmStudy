def solution(gems):
    answer = [] # === 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간
    L = len(gems)
    only_gems = (set(gems))
    answerLength = len(only_gems)
    # 답의 길이는 최소 모든 종류 1개씩부터 시작
    for n in range(answerLength, L+1):
        for i1 in range(0, L-n):
            for i2 in range(i1+1, L):
                part_gems = gems[i1:i2]
    return answer








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

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
