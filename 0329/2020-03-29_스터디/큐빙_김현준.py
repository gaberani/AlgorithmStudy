change = ['U', 'D', 'F', 'B', 'L', 'R']

def rotate(direc):
    a, b = direc[0], direc[1]       # 면, 방향
    for i in range(6):
        if a==change[i]:        # 돌리는 면을 숫자로 바꿈
            a = i
            break
    rotate1(a, b)       # 기준면 돌리기
    Q1 = [[['']*3 for _ in range(3)] for _ in range(6)]     # 돌린 후 정보 저장할 빈 배열 생성
    for i in range(6):
        for j in range(3):
            for k in range(3):
                Q1[i][j][k] = Q[i][j][k]        # 원래 면 색깔 복사
    if a==0:                                                                                                                # 윗면
        for i in range(3):
            if b=='+':                                                                                                      # 시계방향
                Q1[4][0][i], Q1[5][0][i], Q1[3][0][i], Q1[2][0][i] = Q[2][0][i], Q[3][0][i], Q[4][0][i], Q[5][0][i]
            elif b=='-':                                                                                                    # 반시계방향
                Q1[5][0][i], Q1[4][0][i], Q1[2][0][i], Q1[3][0][i] = Q[2][0][i], Q[3][0][i], Q[4][0][i], Q[5][0][i]
    elif a==1:
        for i in range(3):
            if b=='+':
                Q1[5][2][i], Q1[4][2][i], Q1[2][2][i], Q1[3][2][i] = Q[2][2][i], Q[3][2][i], Q[4][2][i], Q[5][2][i]
            elif b=='-':
                Q1[4][2][i], Q1[5][2][i], Q1[3][2][i], Q1[2][2][i] = Q[2][2][i], Q[3][2][i], Q[4][2][i], Q[5][2][i]
    elif a==2:
        for i in range(3):
            if b=='+':
                Q1[5][i][0], Q1[1][0][2-i], Q1[4][i][2], Q1[0][2][2-i] = Q[0][2][i], Q[5][i][0], Q[1][0][i], Q[4][i][2]
            elif b=='-':
                Q1[4][2-i][2], Q1[0][2][i], Q1[5][2-i][0], Q1[1][0][i] = Q[0][2][i], Q[5][i][0], Q[1][0][i], Q[4][i][2]
    elif a==3:
        for i in range(3):
            if b=='+':
                Q1[4][2-i][0], Q1[1][2][i], Q1[5][2-i][2], Q1[0][0][i] = Q[0][0][i], Q[4][i][0], Q[1][2][i], Q[5][i][2]
            elif b=='-':
                Q1[5][i][2], Q1[0][0][2-i], Q1[4][i][0], Q1[1][2][2-i] = Q[0][0][i], Q[4][i][0], Q[1][2][i], Q[5][i][2]
    elif a==4:
        for i in range(3):
            if b=='+':
                Q1[2][i][0], Q1[1][i][0], Q1[3][2-i][2], Q1[0][2-i][0] = Q[0][i][0], Q[2][i][0], Q[1][i][0], Q[3][i][2]
            elif b=='-':
                Q1[3][2-i][2], Q1[0][i][0], Q1[2][i][0], Q1[1][2-i][0] = Q[0][i][0], Q[2][i][0], Q[1][i][0], Q[3][i][2]
    elif a==5:
        for i in range(3):
            if b=='+':
                Q1[3][2-i][0], Q1[1][2-i][2], Q1[2][i][2], Q1[0][i][2] = Q[0][i][2], Q[3][i][0], Q[1][i][2], Q[2][i][2]
            elif b=='-':
                Q1[2][i][2], Q1[0][2-i][2], Q1[3][2-i][0], Q1[1][i][2] = Q[0][i][2], Q[3][i][0], Q[1][i][2], Q[2][i][2]

    for i in range(6):
        for j in range(3):
            for k in range(3):
                Q[i][j][k] = Q1[i][j][k]

def rotate1(a, b):                          # 기준면 돌리기
    arr = [['']*3 for _ in range(3)]
    if b=='+':
        for i in range(3):
            for j in range(3):
                arr[j][2-i] = Q[a][i][j]        # 90도
    elif b=='-':
        for i in range(3):
            for j in range(3):
                arr[i][j] = Q[a][j][2-i]        # -90도
    for i in range(3):
        for j in range(3):
            Q[a][i][j] = arr[i][j]

N = int(input())
for _ in range(N):
    T = int(input())
    direcs = list(input().split())
    Q = [[['w']*3 for _ in range(3)],       # 각 면 색깔 저장
         [['y']*3 for _ in range(3)],
         [['r']*3 for _ in range(3)],
         [['o']*3 for _ in range(3)],
         [['g']*3 for _ in range(3)],
         [['b']*3 for _ in range(3)]]
    for direc in direcs:    # 돌리기
        rotate(direc)
    for i in range(3):
        print(''.join(Q[0][i]))