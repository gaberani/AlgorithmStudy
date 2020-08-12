def solution(nodeinfo):
    answer = [[]]
    N = len(nodeinfo)
    for n in range(N):
        nodeinfo[n] += [n+1]
    sorted_nodeinfo = sorted(nodeinfo, key=lambda x:(x[0], x[1], x[2]))
    print(sorted_nodeinfo)
    top = sorted_nodeinfo[0]
    preorder = []
    for n in range(N):
        preorder.append(sorted_nodeinfo[n][2])
    print(preorder)
    sorted_nodeinfo = sorted(nodeinfo, key=lambda x:(x[0], x[1]), reverse=True)

    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))