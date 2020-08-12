def solution(dirs):
    ans, x, y = 0, 0, 0
    V = [[[] for i in range(11)] for j in range(11)]
    for d in dirs:
        # 새로운 점 찾기
        dir = {"U": (x, y+1), "D": (x, y-1), "R": (x+1, y), "L": (x-1, y)}
        # 범위 넘어가면 무시
        if not -5 <= dir[d][0] <= 5 or not -5 <= dir[d][1] <= 5: continue
        # 지점 이동
        x, y = dir[d]
        # 길이 추가 및 중복 확인
        ans += line(5-y, x+5, d, V, ans)
    return ans

def line(y, x, d, V, ans):
    # 중복 없으면 선 추가 : 각 점에 위, 오른쪽 방향 정보 저장
    # "U", "D" => 1, "L", "R" => 2
    if d == "D" and 1 not in V[y-1][x]:
        V[y-1][x].append(1)
    elif d == "U" and 1 not in V[y][x]:
        V[y][x].append(1)
    elif d == "L" and 2 not in V[y][x+1]:
        V[y][x+1].append(2)
    elif d == "R" and 2 not in V[y][x]:
        V[y][x].append(2)
    else: return 0
    return 1


print(solution("ULURRDLLU"))   # 7
print(solution("LULLLLLLU"))   # 7
print(solution("LLLLLLLLL"))   # 5
print(solution("DDDDDDDDD"))   # 5
print(solution("UDUDUD"))      # 1
print(solution("UDUDUDD"))     # 2
print(solution("LR"))          # 1
print(solution("UD"))          # 1