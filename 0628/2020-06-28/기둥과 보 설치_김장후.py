def solution(n, build_frame):
    def check(x, y, type):
        nonlocal pillar, beam
        if type:
            if pillar[x][y-1] or pillar[x+1][y-1] or (x > 0 and beam[x-1][y] and beam[x+1][y]):
                return 1
        else:
            if y == 0 or beam[x][y] or (x > 0 and beam[x-1][y]) or pillar[x][y-1]:
                return 1
        return 0

    answer = []
    pillar = [[0] * (n+1) for _ in range(n+1)]
    beam = [[0] * (n+1) for _ in range(n+1)]
    for x, y, type, equipment in build_frame:
        if equipment:
            if type:
                if check(x, y, type):
                    beam[x][y] = 1
            else:
                if check(x, y, type):
                    pillar[x][y] = 1
        else:
            if type:
                beam[x][y] = 0
                if x > 0 and beam[x-1][y] and not check(x-1, y, 1):
                    beam[x][y] = 1
                elif beam[x+1][y] and not check(x+1, y, 1):
                    beam[x][y] = 1
                elif pillar[x][y] and not check(x, y, 0):
                    beam[x][y] = 1
                elif pillar[x+1][y] and not check(x+1, y, 0):
                    beam[x][y] = 1
            else:
                pillar[x][y] = 0
                if x > 0 and beam[x-1][y+1] and not check(x-1, y+1, 1):
                    pillar[x][y] = 1
                elif beam[x][y+1] and not check(x, y+1, 1):
                    pillar[x][y] = 1
                elif pillar[x][y+1] and not check(x, y+1, 0):
                    pillar[x][y] = 1


    for i in range(n+1):
        for j in range(n+1):
            if pillar[i][j]:
                answer.append([i, j ,0])
            if beam[i][j]:
                answer.append([i, j, 1])
    return answer




# def check(arr):
#     for x, y, type in arr:
#         if type:
#             if not ([x, y-1, 0] in arr or [x+1, y-1, 0] in arr or ([x-1, y, 1] in arr and [x+1, y, 1] in arr)):
#                 return 0
#         else:
#             if not (y == 0 or [x, y, 1] in arr or [x-1, y, 1] in arr or [x, y-1, 0] in arr):
#                 return 0
#     return 1
#
# def solution(n, build_frame):
#     answer = []
#     for x, y, type, equipment in build_frame:
#         # 설치
#         if equipment:
#             answer.append([x, y, type])
#             if not check(answer):
#                 answer.remove([x, y, type])
#         # 삭제
#         else:
#             answer.remove([x, y, type])
#             if not check(answer):
#                 answer.append([x, y, type])
#
#     answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
#     return answer

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]


