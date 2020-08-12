def solution(key, lock):
    answer = False
    N = len(lock)
    M = len(key)
    # 자물쇠 홈 부분 개수
    homes = 0
    # 자물쇠 홈 부분 대표 좌표
    first_home = tuple()
    # 열쇠 돌기 부분 좌표 집합 (0, 90, 180, 270도 방향)
    keys = [[] for _ in range(4)]
    for i in range(M):
        for j in range(M):
            if key[i][j]:
                keys[0].append((i, j))
    # 90도씩 회전하면서 돌기 좌표 저장
    for i in range(3):
        for m, n in keys[i]:
            keys[i+1].append((M-n-1,m))
    # 자물쇠 홈 부분 개수와 대표 좌표
    for i in range(N):
        for j in range(N):
            if not lock[i][j]:
                homes += 1
                if not first_home:
                    first_home = (i, j)
    # 자물쇠 홈이 있고, 열쇠 돌기가 존재할 때 (이미 자물쇠가 모두 채워져 있을 때 에러 방지)
    if homes and keys[0]:
        # 모든 경우 비교
        for k in keys:
            # 자물쇠 대표 홈과 매칭시킬 열쇠 대표 돌기 구하기
            for si, sj in k:
                # 조정 좌표
                a, b = first_home[0]-si, first_home[1]-sj
                # 열쇠의 돌기와 자물쇠 홈이 만나는 부분 개수
                cnt = 0
                for i, j in k:
                    # 모든 열쇠 돌기 좌표들 조정
                    ni, nj = i+a, j+b
                    # 열쇠 돌기와 자물쇠 돌기가 만날 Eo를 대비한 flag
                    flag = True
                    if 0<=ni<N and 0<=nj<N:
                        # 열쇠 돌기와 자물쇠 홈이 만날 때
                        if not lock[ni][nj]:
                            cnt += 1
                        # 열쇠 돌기와 자물쇠 돌기가 만날 때
                        else:
                            flag = False
                            break
                # 열쇠 돌기와 자물쇠 돌기가 만난 적이 없고, 모든 자물쇠의 홈을 채웠을 때
                if cnt==homes and flag:
                    answer = True
                    break
            if answer:
                break
    # 열쇠가 이미 모두 채워져 있을 떄
    elif not homes:
        answer = True
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 0, 1], [1, 0, 1]]    # result = true

print(solution(key, lock))