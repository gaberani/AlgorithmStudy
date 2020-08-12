def solution(n):
    answer = [0]
    for i in range(1, n):
        answer += [0]
        for j in range(len(answer)-2, -1, -1):
            answer += [int(not(answer[j]))]
    return answer

print(solution(20))

# 1 3 7 15