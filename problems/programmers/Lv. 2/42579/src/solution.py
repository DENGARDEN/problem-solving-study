from collections import Counter, defaultdict, OrderedDict

def solution(genres, plays):

    song_info = defaultdict(list)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        song_info[genre].append((play, idx))
    
    for genre in song_info:
        song_info[genre].sort(key=lambda x: x[0], reverse=True)

    sorted_genre_counts = sorted(song_info.items(), key=lambda x: sum(play for play, idx in x[1]), reverse=True)

    answer = []
    for genre, _ in sorted_genre_counts:
        answer.append(song_info[genre][0][1])
        if len(song_info[genre]) > 1:
            answer.append(song_info[genre][1][1])
    return answer