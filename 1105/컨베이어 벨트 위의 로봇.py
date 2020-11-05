N, K = map(int, input().split())
belt = list(map(int, input().split()))
visit = [0]*N
answer = 0
while 1:
    answer += 1
    # 내려가는 위치에 로봇이 있는 경우 로봇은 반드시 땅으로 내려가야 한다.


    # 1. 벨트가 한 칸 회전한다.(로봇도 같이감)
    belt = [belt[-1]] + belt[:2*N-1]
    visit = [visit[-1]] + visit[:N-1]
    if visit[-1] == 1: visit[-1] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    #    만약 이동할 수 없다면 가만히 있는다.
    for i in range(N-2, -1, -1):
        # 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 이어야 한다.
        if visit[i] == 1 and visit[i+1] == 0 and belt[i+1] >= 1:
            belt[i+1] -= 1
            visit[i], visit[i+1] = visit[i+1], visit[i]
    if visit[-1] == 1: visit[-1] = 0

    # 3. 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    # 로봇이 어떤 칸에 올라가거나 이동하면 그 칸의 내구도는 즉시 1만큼 감소
    if visit[0] == 0 and belt[0] >= 1:
        belt[0] -= 1
        visit[0] = 1

    # print(belt)
    # print(visit)
    # print('----------')
    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if belt.count(0) >= K:
        break

print(answer)