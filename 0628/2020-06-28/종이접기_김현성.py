# 접힌 가운데는 항상 0
def solution(n):
    answer = []
    for _ in range(n):
        tmp = []
        tmp.append(0)
        for a in answer[::-1]:
            if a == 0:
                tmp.append(1)
            else:
                tmp.append(0)
        answer += tmp
    return answer

# print(solution(1))
# print(solution(2))
# print(solution(4))