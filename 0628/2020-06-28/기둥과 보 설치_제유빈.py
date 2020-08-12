def solution(n, build_frame):
    beam = [[0]*(n+1) for _ in range(n)]  # 보
    pillar = [[0]*n for _ in range(n+1)]  # 기둥

    # 기둥
    def check_pillar(x, y):
        if not y or pillar[x][y-1] or (x < n and beam[x][y]) or (x > 0 and beam[x-1][y]):
            return 1
        return 0
    # 보
    def check_beam(x, y):
        if pillar[x][y-1] or pillar[x+1][y-1] or (1 <= x < n-1 and beam[x-1][y] and beam[x+1][y]):
            return 1
        return 0

    for x, y, a, b in build_frame:
        if not a:    # 기둥
            if b:    # 설치
                if check_pillar(x, y):
                    pillar[x][y] = 1
            else:   # 해체
                pillar[x][y] = 0
                if x < n and beam[x][y+1] and not check_beam(x, y+1):
                    pillar[x][y] = 1
                elif x and beam[x-1][y+1] and not check_beam(x-1, y+1):
                    pillar[x][y] = 1
                elif y < n-1 and pillar[x][y+1] and not check_pillar(x, y+1):
                    pillar[x][y] = 1
        elif y:
            if b:   # 설치
                if check_beam(x, y):
                    beam[x][y] = 1
            else:   # 해체
                beam[x][y] = 0
                if y < n and pillar[x][y] and not check_pillar(x, y):
                    beam[x][y] = 1
                elif y < n and pillar[x+1][y] and not check_pillar(x+1, y):
                    beam[x][y] = 1
                elif x > 0 and beam[x-1][y] and not check_beam(x-1, y):
                    beam[x][y] = 1
                elif x + 1 < n and beam[x+1][y] and not check_beam(x+1, y):
                    beam[x][y] = 1

    # 결과 저장
    ans = []
    for x in range(n+1):
        for y in range(n+1):
            if y < n and pillar[x][y]:
                ans.append([x, y, 0])
            if x < n and beam[x][y]:
                ans.append([x, y, 1])
    return ans


# [x, y, a, b] - 가로, 세로, 구조물(0-기둥, 1-보), 설치여부(0-삭제, 1-설치)
# 결과물은 [x, y, a]
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]



