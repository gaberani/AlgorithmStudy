def solution(gems):
    answer = []
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
