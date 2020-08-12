def solution(n, build_frame):
    answer = []
    # 기둥 위치 좌표
    pillar = [[0]*(n+1) for _ in range(n)]
    # 보 위치 좌표
    beam = [[0]*(n) for _ in range(n+1)]
    # 기둥 혹은 보를 설치할 수 있는지 확인
    def check(i, j, a):
        # 보를 설치할 때
        if a:
            # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결될 때
            if pillar[i][j] or pillar[i][j+1] or ((j-1!=-1 and beam[i][j-1]) and (j+1!=n and beam[i][j+1])):
                return True
        # 기둥을 설치할 때
        else:
            # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 할 때
            if i+1==n or pillar[i+1][j] or (j-1!=-1 and beam[i+1][j-1]) or (j!=n and beam[i+1][j]):
                return True
        return False

    # 편의를 위해 x,y 좌표를 j, i로 바꿈
    for j, i, a, b in build_frame:
        # 편의상 아래위 뒤집기
        i = n-i
        # 설치할 때
        if b:
            # 보
            if a:
                if check(i, j, a):
                    beam[i][j] = 1
            # 기둥
            else:
                if check(i-1, j, a):
                    pillar[i-1][j] = 1
        # 삭제할 때
        else:
            # 보
            if a:
                # 미리 보를 없앤다
                beam[i][j] = 0
                # 없앤 보의 양쪽 보가 존재할 수 있는지 확인, 없앤 보의 서있는 양쪽 기둥이 존재할 수 있는지 확인
                if not((j-1==-1 or not beam[i][j-1] or check(i, j-1, 1)) and (j+1==n or not beam[i][j+1] or check(i, j+1, 1))\
                        and (not pillar[i-1][j] or check(i-1, j, 0)) and (not pillar[i-1][j+1] or check(i-1, j+1, 0))):
                    beam[i][j] = 1
            # 기둥
            else:
                # 미리 기둥을 없앤다.
                pillar[i-1][j] = 0
                # 없앤 기둥 위에 양쪽 보가 존재할 수 있는지 확인, 없앤 기둥 위의 기둥이 존재할 수 있는지 확인
                if not((j-1==-1 or not beam[i-1][j-1] or check(i-1, j-1, 1)) and (j==n or not beam[i-1][j] or check(i-1, j, 1))\
                        and (i-2==-1 or not pillar[i-2][j] or check(i-2, j, 0))):
                    pillar[i-1][j] = 1
    # 기둥 정보 취합
    for i in range(n):
        for j in range(n+1):
            if pillar[i][j]:
                answer.append([j, n-i-1, 0])
    # 보 정보 취합
    for i in range(n+1):
        for j in range(n):
            if beam[i][j]:
                answer.append([j, n-i, 1])
    # x, y, 기둥, 보 순으로 정렬
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer

# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# # result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

print(solution(n, build_frame))