def solution(s):
    answer = []
    num_lst = ['0','1','2','3','4','5','6','7','8','9']
    num_stack = []
    score = []
    flag = 0
    num = ''
    for i in range(len(s)):
        if s[i] in num_lst:
            num += s[i]
        elif s[i] == ',' or s[i] == '}':
            if num != '' and int(num) not in num_stack:
                num_stack.append(int(num))
                num = ''
                score.append(1)
            elif num != '' and int(num) in num_stack:
                score[num_stack.index(int(num))] += 1
                num = ''
    for _ in range(len(num_stack)):
        max_idx = score.index(max(score))
        answer.append(num_stack[max_idx])
        score[max_idx] = 0
    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# print(solution("{{20,111},{111}}"))