from string import ascii_uppercase

def solution(msg):
    answer = []
    dic = list(ascii_uppercase)
    i = 0
    idx = 1
    while 1:
        idx += 1
        # dic에 없는거 찾을 때까지 while
        if msg[i:i+idx] not in dic:
            dic.append(msg[i:i+idx])                 # 없는거 dic에 추가
            answer.append(dic.index(msg[i:i+idx-1])+1)  # 가장 최근 출력을 answer에 추가
            i += idx-1
            idx = 0
        else:
            if i == len(msg)-idx:
                answer.append(dic.index(msg[i:])+1)
                break
    return answer


# from string import ascii_uppercase
#
# def solution(msg):
#     answer = []
#     dic = list(ascii_uppercase)
#     i = 0
#     idx = 1
#     while 1:
#         idx = 1
#         # dic에 없는거 찾을 때까지 while
#         while msg[i:i+idx] in dic:
#             idx += 1
#         dic.append(msg[i:i+idx])                    # 없는거 dic에 추가
#         answer.append(dic.index(msg[i:i+idx-1])+1)  # 가장 최근 출력을 answer에 추가
#         i += idx-1
#         if i >= len(msg)-idx:
#             print(msg[i:])
#             answer.append(dic.index(msg[i:])+1)
#             break
#     print(dic[26:])
#     return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))