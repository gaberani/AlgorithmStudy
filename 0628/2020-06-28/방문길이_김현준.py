def solution(dirs):
    answer = 0
    # 가로, 세로 경계 각각 배열 만들기
    garo = [[0]*10 for _ in range(11)]
    sero = [[0]*11 for _ in range(10)]
    # 캐릭터 출발점을 [5, 5]로 임의지정
    i, j = 5, 5
    for d in dirs:
        # 각 방향에 맞춰 경계 배열 자리 찾기 (범위 조심!!)
        # 캐릭터 이동
        if d=='U':
            if 0<=i-1<11 and 0<=j<11:
                sero[i-1][j] = 1
                i -= 1
        elif d=='D':
            if 0<=i+1<11 and 0<=j<11:
                sero[i][j] = 1
                i += 1
        elif d=='R':
            if 0<=i<11 and 0<=j+1<11:
                garo[i][j] = 1
                j += 1
        elif d=='L':
            if 0<=i<11 and 0<=j-1<11:
                garo[i][j-1] = 1
                j -= 1
    # 갔던 길 카운트
    for i in range(10):
        for j in range(11):
            if garo[j][i]:
                answer += 1
            if sero[i][j]:
                answer += 1
    return answer

# dirs = "ULURRDLLU"
# # result = 7

# dirs = "LULLLLLLU"
# # result = 7

dirs = 'RRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUULU'
print(solution(dirs))