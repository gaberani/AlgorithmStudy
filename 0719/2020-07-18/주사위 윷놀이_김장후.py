import sys; input = sys.stdin.readline
from collections import deque


# 2.
import sys; input = sys.stdin.readline
from collections import deque


def dfs():
    global maxV, movie_info, score_info
    turn = 10
    end = 32
    stack = deque()
    stack.append((0, 0, 0, [0, 0, 0, 0]))
    while stack:
        idx, cnt, total, horses = stack.pop()
        if cnt == turn:
            maxV = max(total, maxV)
        else:
            horses[idx] = move[horses[idx]][move_info[cnt]-1]
            total += score_info[horses[idx]]
            for i in range(4):
                if horses[i] == end: continue
                if cnt+1 < turn:
                    next_move = move[horses[i]][move_info[cnt+1]-1]
                    if next_move != end and next_move in horses: continue
                stack.append((i, cnt+1, total, horses[:]))



score_info = {}
for i in range(20):
    score_info[i] = i*2
tmp = [13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 40, 0]
for i in range(13):
    score_info[i+20] = tmp[i]

move = {
    0: [1, 2, 3, 4, 5],
    1: [2, 3, 4, 5, 6],
    2: [3, 4, 5, 6, 7],
    3: [4, 5, 6, 7, 8],
    4: [5, 6, 7, 8, 9],
    5: [20, 21, 22, 28, 29],
    6: [7, 8, 9, 10, 11],
    7: [8, 9, 10, 11, 12],
    8: [9, 10, 11, 12, 13],
    9: [10, 11, 12, 13, 14],
    10: [23, 24, 28, 29, 30],
    11: [12, 13, 14, 15, 16],
    12: [13, 14, 15, 16, 17],
    13: [14, 15, 16, 17, 18],
    14: [15, 16, 17, 18, 19],
    15: [25, 26, 27, 28, 29],
    16: [17, 18, 19, 31, 32],
    17: [18, 19, 31, 32, 32],
    18: [19, 31, 32, 32, 32],
    19: [31, 32, 32, 32, 32],
    20: [21, 22, 28, 29, 30],
    21: [22, 28, 29, 30, 31],
    22: [28, 29, 30, 31, 32],
    23: [24, 28, 29, 30, 31],
    24: [28, 29, 30, 31, 32],
    25: [26, 27, 28, 29, 30],
    26: [27, 28, 29, 30, 31],
    27: [28, 29, 30, 31, 32],
    28: [29, 30, 31, 32, 32],
    29: [30, 31, 32, 32, 32],
    30: [31, 32, 32, 32, 32],
    31: [32, 32, 32, 32, 32]
}

move_info = list(map(int, input().split()))
maxV = 0
dfs()
print(maxV)


# 1.
def dfs_recursion(idx, cnt, total, horses):
    global maxV, turn, end
    if cnt == turn:
        maxV = max(total, maxV)
        return
    else:
        h_tmp = horses[:]
        h_tmp[idx] = move[h_tmp[idx]][move_info[cnt]-1]
        total += score_info[h_tmp[idx]]
        for i in range(4):
            if h_tmp[i] == end: continue
            if cnt+1 < turn:
                next_move = move_info[cnt+1]-1
                if move[h_tmp[i]][next_move] != end and move[h_tmp[i]][next_move] in h_tmp: continue
            dfs(i, cnt+1, total, h_tmp)


score_info = {}
for i in range(20):
    score_info[i] = i*2
tmp = [13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 40, 0]
for i in range(13):
    score_info[i+20] = tmp[i]

move = {
    0: [1, 2, 3, 4, 5],
    1: [2, 3, 4, 5, 6],
    2: [3, 4, 5, 6, 7],
    3: [4, 5, 6, 7, 8],
    4: [5, 6, 7, 8, 9],
    5: [20, 21, 22, 28, 29],
    6: [7, 8, 9, 10, 11],
    7: [8, 9, 10, 11, 12],
    8: [9, 10, 11, 12, 13],
    9: [10, 11, 12, 13, 14],
    10: [23, 24, 28, 29, 30],
    11: [12, 13, 14, 15, 16],
    12: [13, 14, 15, 16, 17],
    13: [14, 15, 16, 17, 18],
    14: [15, 16, 17, 18, 19],
    15: [25, 26, 27, 28, 29],
    16: [17, 18, 19, 31, 32],
    17: [18, 19, 31, 32, 32],
    18: [19, 31, 32, 32, 32],
    19: [31, 32, 32, 32, 32],
    20: [21, 22, 28, 29, 30],
    21: [22, 28, 29, 30, 31],
    22: [28, 29, 30, 31, 32],
    23: [24, 28, 29, 30, 31],
    24: [28, 29, 30, 31, 32],
    25: [26, 27, 28, 29, 30],
    26: [27, 28, 29, 30, 31],
    27: [28, 29, 30, 31, 32],
    28: [29, 30, 31, 32, 32],
    29: [30, 31, 32, 32, 32],
    30: [31, 32, 32, 32, 32],
    31: [32, 32, 32, 32, 32]
}

move_info = list(map(int, input().split()))
horses = [0, 0, 0, 0]
turn = 10
end = 32
maxV = 0
dfs_recursion(0, 0, 0, horses)
print(maxV)


# 5: 10
# score_info[20] = 13
# score_info[21] = 16
# score_info[22] = 19
# 10: 20
# score_info[23] = 22
# score_info[24] = 24
# 15: 30
# score_info[25] = 28
# score_info[26] = 27
# score_info[27] = 26
# 28 :25
# score_info[28] = 25
# score_info[29] = 30
# score_info[30] = 35
# end
# score_info[31] = 40
# score_info[32] = 0