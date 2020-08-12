# 좌표평면의 경계를 넘어가는 명령어는 무시

def solution(dirs):
    answer = 0
    def move(position, d):
        i, j = position[0], position[1]
        if d == 'D' and i != -5:
            i -= 1
        elif d == 'U' and i != 5:
            i += 1
        elif d == 'L' and j != -5:
            j -= 1
        elif d == 'R' and j != 5:
            j += 1
        return [i, j]

    si, sj, visit = 0, 0, []
    for dir in dirs:
        di, dj = move([si, sj], dir)
        if [[si, sj, di, dj]] not in visit and [[di, dj, si, sj]] not in visit and (si != di or sj != dj):
            visit.append([[si, sj, di, dj]])
            visit.append([[di, dj, si, sj]])
            answer += 1
        si, sj = di, dj
    # print(visit)
    return answer



print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))