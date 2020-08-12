from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    visited = []

    q = deque()
    q.append((0, 0, 0, 1, 0, 1))
    visited.append({(0, 0), (0, 1)})

    while q:
        rxo, ryo, rxt, ryt, cnt, shape = q.popleft()
        if rxo == ryo == N-1 or rxt == ryt == N-1:
            answer = cnt
            break

        for k in range(4):
            nxo, nyo = rxo + di[k], ryo + dj[k]
            nxt, nyt = rxt + di[k], ryt + dj[k]

            if 0 <= nxo < N and 0 <= nyo < N and 0 <= nxt < N and 0 <= nyt < N and \
                    not board[nxo][nyo] and not board[nxt][nyt]:
                if {(nxo, nyo), (nxt, nyt)} not in visited:
                    visited.append({(nxo, nyo), (nxt, nyt)})
                    if shape:
                        q.append((nxo, nyo, nxt, nyt, cnt+1, 1))
                    elif not shape:
                        q.append((nxo, nyo, nxt, nyt, cnt + 1, 0))
                if shape:
                    if k == 2 or k == 3:
                        if {(rxo, ryo), (nxo, nyo)} not in visited:
                            visited.append({(rxo, ryo), (nxo, nyo)})
                            q.append((rxo, ryo, nxo, nyo, cnt + 1, 0))

                        if {(nxt, nyt), (rxt, ryt)} not in visited:
                            visited.append({(nxt, nyt), (rxt, ryt)})
                            q.append((nxt, nyt, rxt, ryt, cnt + 1, 0))
                else:
                    if k == 0 or k == 1:
                        if {(rxo, ryo), (nxo, nyo)} not in visited:
                            visited.append({(rxo, ryo), (nxo, nyo)})
                            q.append((rxo, ryo, nxo, nyo, cnt + 1, 1))

                        if {(nxt, nyt), (rxt, ryt)} not in visited:
                            visited.append({(nxt, nyt), (rxt, ryt)})
                            q.append((nxt, nyt, rxt, ryt, cnt + 1, 1))
    return answer





board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))