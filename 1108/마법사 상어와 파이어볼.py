# 마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사
# 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다.
# 서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.
# 위치 (r, c)는 r행 c열을 의미한다.

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
info_lsts = [list(map(int, input().split())) for _ in range(M)]
fire_info = {}
# i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다.
for ri, ci, mi, si, di in info_lsts:
    fire_info[(ri-1, ci-1)] = [(mi, si, di)]

# 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
#    이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
def move():
    global fire_info, grid
    tmp = []
    for key, values in fire_info.items():
        fi, fj = key
        for val in values:
            fm, fs, fd = val
            tmp.append([(fi+fs*dr[fd])%N, (fj+fs*dc[fd])%N, fm, fs, fd])

    fire_info = {}
    for ni, nj, nm, ns, nd in tmp:
        if fire_info.get((ni, nj)) != None:
            fire_info[(ni, nj)].append((nm, ns, nd))
        else:
            fire_info[(ni, nj)] = [(nm, ns, nd)]

def multifireball():
    global fire_info
    tmp = []
    for key, values in fire_info.items():
        balls_m, balls_s, balls_d = 0, 0, -1
        fi, fj = key
        # 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
        if len(values) > 1:
            # ㄱ. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.

            for val in values:
                fm, fs, fd = val
                if balls_d == -1:
                    if fd%2 == 1: balls_d = 1
                    elif fd%2 == 0: balls_d = 0
                elif balls_d == 0 or balls_d == 1:
                    if fd%2 == 1 and balls_d != 1: balls_d = 7
                    elif fd%2 == 0 and balls_d != 0: balls_d = 7

                balls_m += fm
                balls_s += fs

            #   ㄷ. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
            #       가. 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
            #       나. 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
            nm, ns = balls_m//5, balls_s//len(values)
            #       다. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면,
            #           방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
            nd = [0, 2, 4, 6] if balls_d != 7 else [1, 3, 5, 7]
            # ㄹ. 질량이 0인 파이어볼은 소멸되어 없어진다.
            if nm > 0:
                # ㄴ. 파이어볼은 4개의 파이어볼로 나누어진다.
                for d in nd:
                    tmp.append([fi, fj, nm, ns, d])
        else:
            fm, fs, fd = values[0]
            tmp.append([fi, fj, fm, fs, fd])

    fire_info = {}
    for ni, nj, nm, ns, nd in tmp:
        if fire_info.get((ni, nj)) != None:
            fire_info[(ni, nj)].append((nm, ns, nd))
        else:
            fire_info[(ni, nj)] = [(nm, ns, nd)]

cnt = 0
# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합 구하기
while cnt < K:
    move()
    multifireball()
    cnt += 1

answer = 0
for values in fire_info.values():
    for val in values:
      answer += val[0]
print(answer)