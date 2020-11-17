# 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시

# 노래를 수록하는 기준은 다음과 같습니다.
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

def solution(genres, plays):
    # 노래의 장르를 나타내는 문자열 배열 genres
    # 노래별 재생 횟수를 나타내는 정수 배열 plays
    # 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return
    # 장르에 속한 곡이 하나라면, 하나의 곡만 선택
    answer = []
    genre_dict = {}
    idx = 0
    for genre, val in zip(genres, plays):
        if genre_dict.get(genre) == None:
            genre_dict[genre] = [val, [idx, val]]
        else:
            genre_dict[genre][0] += val
            genre_dict[genre].append([idx, val])
        idx += 1
    print(genre_dict)
    genre_lsts = sorted(genre_dict.values(), key = lambda x: (-x[0], x[1]))
    sorted_lst = []
    for genre_lst in genre_lsts:
        val, lst = genre_lst[0], list(genre_lst[1:])
        sorted_lst.append([val, sorted(lst, key = lambda x: -x[-1])])
    # print(sorted_lst)

    for one_genre in sorted_lst:
        play_musics = one_genre[1][:2]
        for play_music in play_musics:
            answer.append(play_music[0])

    return answer

print(solution(['classic', 'classic', 'classic', 'pop'], [500, 150, 800, 2500]))