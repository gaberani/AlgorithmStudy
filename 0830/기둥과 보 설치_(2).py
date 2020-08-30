# 2차원 벽면은 n x n 크기 정사각 격자 형태이며, 각 격자는 1 x 1 크기
# n은 5 이상 100 이하
# build_frame의 세로(행) 길이는 1이상 1000이하, 가로(열) 길이는 4

# build_frame의 원소는 [x, y, a, b]형태
# x, y는 [가로 좌표, 세로 좌표] / a: 0은 기둥, 1은 보 / b는 0은 삭제, 1은 설치

import pprint
def check(ans):
    for x, y, frame in ans:
        # 기둥
        if frame == 0:
            # 바닥 위 / 보의 한쪽 끝 부분 위 /다른 기둥 위
            if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                continue
            else:
                return False
        # 보
        elif frame == 1:
            # 한쪽 끝 부분이 기둥 위 / 양쪽 끝 부분이 다른 보와 동시에 연결
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for info in build_frame:
        x, y, frame, work = info
        # 설치
        if work == 1:
            # 미리 설치하고 체크하러 가기
            answer.append([x, y, frame])
            if check(answer) == False:
                answer.remove([x, y, frame])
        # 삭제
        else:
            # 미리 제거하고 체크하러 가기
            answer.remove([x, y, frame])
            if check(answer) == False:
                answer.append([x, y, frame])

    answer.sort()
    return answer


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))

# [[1,0,0]
# ,[1,1,1]
# ,[2,1,0]
# ,[2,2,1]
# ,[3,2,1]
# ,[4,2,1]
# ,[5,0,0]
# ,[5,1,0]]