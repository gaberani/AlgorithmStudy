def solution(dartResult):
    anyone = ['S','D','T','*','#']
    parts = [0, 0, 0]
    visit = [0, 0, 0]
    num_idx = -1
    next = 0
    flag = 0
    for i in dartResult:
        next += 1
        if not flag:
            if i == 'S':
                parts[num_idx] **= 1
            elif i == 'D':
                parts[num_idx] **= 2
            elif i == 'T':
                parts[num_idx] **= 3
            elif i == '*':
                visit[num_idx] = 1
                parts[num_idx] *= 2
                if num_idx-1 != -1:
                    parts[num_idx-1] *= 2
            elif i == '#':
                visit[num_idx] = 1
                parts[num_idx] *= -1
            else:
                num_idx += 1
                parts[num_idx] = int(i)
                if dartResult[next] not in anyone:
                    parts[num_idx] = 10
                    flag = 1
        else:
            flag = 0
    answer = sum(parts)
    return answer