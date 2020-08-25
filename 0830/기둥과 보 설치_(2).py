# 2차원 벽면은 n x n 크기 정사각 격자 형태이며, 각 격자는 1 x 1 크기
# n은 5 이상 100 이하
# build_frame의 세로(행) 길이는 1이상 1000이하, 가로(열) 길이는 4

# build_frame의 원소는 [x, y, a, b]형태
# x, y는 [가로 좌표, 세로 좌표] / a: 0은 기둥, 1은 보 / b는 0은 삭제, 1은 설치

import pprint
def solution(n, build_frame):
    # 기둥과 보가 설치 가능한지 검사
    def check(ci, cj, a):
        if not a:  # 기둥(위로)
            # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야함.
            if ci == 0 or build_Map[5-ci][cj][abs(a-1)] == 1 or build_Map[5-ci][cj][a] == 1:  # 기둥 아래부분
                return True
            return False
        else:       # 보(오른쪽으로)
            # 연결된 보의 끝 부분 찾기
            left, right = cj, cj+1
            while left == 1 and right == 1:
                if build_Map[5-ci][left][a]:    # 1 or 2
                    left -= 1
                if build_Map[5-ci][right][a]:   # 1 or 2
                    right += 1
            # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되있어야함.
            if build_Map[5-ci][left+1][abs(a-1)] == 1 or build_Map[5-ci][right-1][abs(a-1)] == 1 or (build_Map[5-ci][left+1][a] == 1 and build_Map[5-ci][right-1][a] == 1):
                return True
            return False

    answer = [[]]
    build_Map = [[[0, 0] for _ in range(n+1)] for _ in range(n+1)] # 왼쪽은 기둥, 오른쪽은 보
    for build_info in build_frame:
        bi, bj, a, b = build_info[1], build_info[0], build_info[2], build_info[3]
        # 기둥을 1로 보를 2로 생각해서 더해주면 어떨까?
        if not a:   # 기둥(위로)
            if check(bi, bj, a):
                build_Map[5-bi][bj][a] += 1 if b else 0
                build_Map[5-bi-1][bj][a] += 1 if b else 0
        else:       # 보(오른쪽으로)
            # 보는 더해서 1과 2도 구별하는 식으로 할까?(기둥 연결된 곳은 1, 보 끼리는 2)
            if check(bi, bj, a):
                build_Map[5-bi][bj][a] += 1 if b else 0
                build_Map[5-bi][bj+1][a] += 1 if b else 0
        pprint.pprint(build_Map)
        print('---------')

    # return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표
    # x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬
    # x, y좌표가 모두 같은 경우 기둥이 보보다 앞 -> sorted lambda 쓰자.

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