G = int(input())
airport = dict()
flag = 0
for _ in range(int(input())):
    val = int(input())
    idx = val-1
    if val in airport:
        tmp = airport[val]
        while tmp not in airport:
            try:
                tmp = airport[tmp]
            except KeyError:    # 앞 공항이 비어있는 경우
                break
        if tmp in airport:
            flag = 1
        airport[tmp] = tmp-1
    else:
        airport[val] = idx
    # print(airport)
    if -1 in airport.values():
        print(len(airport.values())-1)
        break
    if flag:
        print(len(airport.values()))
        break