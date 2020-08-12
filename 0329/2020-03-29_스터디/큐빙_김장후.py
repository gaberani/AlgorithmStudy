import sys
input = sys.stdin.readline
def changeplus(x):
    global cn, U, D, F, B, L, R
    tmp = [[0] * cn for _ in range(cn)]
    for i in range(cn):
        for j in range(cn):
            tmp[j][cn - i - 1] = x[i][j]
    x = tmp
    return x
def changeminus(x):
    global cn, U, D, F, B, L, R
    tmp = [[0] * cn for _ in range(cn)]
    for i in range(cn):
        for j in range(cn):
            tmp[cn - j - 1][i] = x[i][j]
    x = tmp
    return x

def plus(x):
    global cn, U, D, F, B, L, R

    if x == 'U':
        # F, R, B, L
        U = changeplus(U)
        atmp = F[0][0], F[0][1], F[0][2]
        F[0][0], F[0][1], F[0][2] = R[0][0], R[0][1], R[0][2]
        R[0][0], R[0][1], R[0][2] = B[2][2], B[2][1], B[2][0]
        B[2][2], B[2][1], B[2][0] = L[0][0], L[0][1], L[0][2]
        L[0][0], L[0][1], L[0][2] = atmp
    elif x == 'F':
        # U, L, D, R
        F = changeplus(F)
        atmp = U[2][2], U[2][1], U[2][0]
        U[2][2], U[2][1], U[2][0] = L[0][2], L[1][2], L[2][2]
        L[0][2], L[1][2], L[2][2] = D[0][0], D[0][1], D[0][2]
        D[0][0], D[0][1], D[0][2] = R[2][0], R[1][0], R[0][0]
        R[2][0], R[1][0], R[0][0] = atmp
    elif x == 'D':
        # F, L, B, R
        D = changeplus(D)
        atmp = F[2][2], F[2][1], F[2][0]
        F[2][2], F[2][1], F[2][0] = L[2][2], L[2][1], L[2][0]
        L[2][2], L[2][1], L[2][0] = B[0][0], B[0][1], B[0][2]
        B[0][0], B[0][1], B[0][2] = R[2][2], R[2][1], R[2][0]
        R[2][2], R[2][1], R[2][0] = atmp
    elif x == 'B':
        # U, R, D, L
        B = changeplus(B)
        atmp = U[0][0], U[0][1], U[0][2]
        U[0][0], U[0][1], U[0][2] = R[0][2], R[1][2], R[2][2]
        R[0][2], R[1][2], R[2][2] = D[2][2], D[2][1], D[2][0]
        D[2][2], D[2][1], D[2][0] = L[2][0], L[1][0], L[0][0]
        L[2][0], L[1][0], L[0][0] = atmp
    elif x == 'L':
        # U, B, D, F
        L = changeplus(L)
        atmp = U[2][0], U[1][0], U[0][0]
        U[2][0], U[1][0], U[0][0] = B[2][0], B[1][0], B[0][0]
        B[2][0], B[1][0], B[0][0] = D[2][0], D[1][0], D[0][0]
        D[2][0], D[1][0], D[0][0] = F[2][0], F[1][0], F[0][0]
        F[2][0], F[1][0], F[0][0] = atmp
    else:
        # U, F, D, B
        R = changeplus(R)
        atmp = U[0][2], U[1][2], U[2][2]
        U[0][2], U[1][2], U[2][2] = F[0][2], F[1][2], F[2][2]
        F[0][2], F[1][2], F[2][2] = D[0][2], D[1][2], D[2][2]
        D[0][2], D[1][2], D[2][2] = B[0][2], B[1][2], B[2][2]
        B[0][2], B[1][2], B[2][2] = atmp


def minus(x):
    global cn, U, D, F, B, L, R
    if x == 'U':
        U = changeminus(U)
        atmp = F[0][2], F[0][1], F[0][0]
        F[0][2], F[0][1], F[0][0] = L[0][2], L[0][1], L[0][0]
        L[0][2], L[0][1], L[0][0] = B[2][0], B[2][1], B[2][2]
        B[2][0], B[2][1], B[2][2] = R[0][2], R[0][1], R[0][0]
        R[0][2], R[0][1], R[0][0] = atmp
    elif x == 'F':
        F = changeminus(F)
        atmp = U[2][0], U[2][1], U[2][2]
        U[2][0], U[2][1], U[2][2] = R[0][0], R[1][0], R[2][0]
        R[0][0], R[1][0], R[2][0] = D[0][2], D[0][1], D[0][0]
        D[0][2], D[0][1], D[0][0] = L[2][2], L[1][2], L[0][2]
        L[2][2], L[1][2], L[0][2] = atmp
    elif x == 'D':
        D = changeminus(D)
        atmp = F[2][0], F[2][1], F[2][2]
        F[2][0], F[2][1], F[2][2] = R[2][0], R[2][1], R[2][2]
        R[2][0], R[2][1], R[2][2] = B[0][2], B[0][1], B[0][0]
        B[0][2], B[0][1], B[0][0] = L[2][0], L[2][1], L[2][2]
        L[2][0], L[2][1], L[2][2] = atmp
    elif x == 'B':
        B = changeminus(B)
        atmp = U[0][2], U[0][1], U[0][0]
        U[0][2], U[0][1], U[0][0] = L[0][0], L[1][0], L[2][0]
        L[0][0], L[1][0], L[2][0] = D[2][0], D[2][1], D[2][2]
        D[2][0], D[2][1], D[2][2] = R[2][2], R[1][2], R[0][2]
        R[2][2], R[1][2], R[0][2] = atmp
    elif x == 'L':
        L = changeminus(L)
        atmp = U[0][0], U[1][0], U[2][0]
        U[0][0], U[1][0], U[2][0] = F[0][0], F[1][0], F[2][0]
        F[0][0], F[1][0], F[2][0] = D[0][0], D[1][0], D[2][0]
        D[0][0], D[1][0], D[2][0] = B[0][0], B[1][0], B[2][0]
        B[0][0], B[1][0], B[2][0] = atmp
    else:
        R = changeminus(R)
        atmp = U[2][2], U[1][2], U[0][2]
        U[2][2], U[1][2], U[0][2] = B[2][2], B[1][2], B[0][2]
        B[2][2], B[1][2], B[0][2] = D[2][2], D[1][2], D[0][2]
        D[2][2], D[1][2], D[0][2] = F[2][2], F[1][2], F[0][2]
        F[2][2], F[1][2], F[0][2] = atmp


def turning(p, d):
    if d == '+':
        plus(p)
    else:
        minus(p)

cn = 3
n = int(input())
for _ in range(n):
    U = [['w'] * cn for _ in range(cn)]
    D = [['y'] * cn for _ in range(cn)]
    F = [['r'] * cn for _ in range(cn)]
    B = [['o'] * cn for _ in range(cn)]
    L = [['g'] * cn for _ in range(cn)]
    R = [['b'] * cn for _ in range(cn)]
    turn = int(input())
    planedir = list(input().split())
    for i in range(turn):
        plane = planedir[i][0]
        d = planedir[i][1]
        turning(plane, d)
    for i in range(cn):
        for j in range(cn):
            print(U[i][j], end='')
        print()