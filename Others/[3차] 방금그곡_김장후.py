def change(m, music):
    tone = ['C#', 'D#', 'F#', 'G#', 'A#']
    change_tone = ['c', 'd', 'f', 'g', 'a']
    for i in range(len(tone)):
        m = m.replace(tone[i], change_tone[i])
        music = music.replace(tone[i], change_tone[i])
    return m, music

def arr_sort(tmp, N):
    for i in range(N-1):
        max_idx = i
        for j in range(i+1, N):
            if tmp[max_idx][0] < tmp[j][0]:
                max_idx = j
        tmp[i], tmp[max_idx] = tmp[max_idx], tmp[i]
    return tmp

def solution(m, musicinfos):
    answer = ''
    N = len(musicinfos)
    tmp = []
    for music in musicinfos:
        # time
        start = int(music[:2]) * 60 + int(music[3:5])
        end = int(music[6:8]) * 60 + int(music[9:11])
        play = end - start
        # title and content
        tit_content = music[12:]
        idx = tit_content.index(',')
        title = tit_content[:idx]
        content = tit_content[idx+1:]
        # play content
        m, content = change(m, content)
        quo = play // len(content)
        remain = play % len(content)
        content = content * quo + content[:remain+1]
        # save playtime, title and music content
        tmp.append((play, title, content))
    # sort
    tmp = arr_sort(tmp, N)
    # check music
    flag = 0
    for i in range(N):
        if m in tmp[i][2]:
            answer = tmp[i][1]
            flag = 1
            break
    if not flag:
        answer = '(None)'
    return answer