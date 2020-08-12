# X
def solution(m, musicinfos):
    answer = ''
    max_T = 0
    for music in musicinfos:
        flag = 0
        info = music.split(',')
        num1, num2 = info[0].split(':'), info[1].split(':')
        time = (int(num2[0])-int(num1[0]))*60 + int(num2[1])-int(num1[1])
        um = ''
        um += info[3]*(time//len(info[3]))
        um += info[3][:time%len(info[3])]
        info[3] = um
        if m in info[3]:
            if m+'#' in info[3]:
                flag = 1
            if flag == 0 and max_T < time:
                max_T = time
                answer = info[2]
            # break
        print(info)
    return answer

# print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
# print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))
print(solution('ABC',['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))