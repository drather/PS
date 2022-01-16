def solution(genres, plays):
    answer = []
    dict_genres = dict()
    dict_table = dict()

    # dict_genres는 각 장르에 속한 노래들의 정보를 담은 딕셔너리이다
    # { classic: [[노래번호, 재생횟수], ... , [노래번호, 재생횟수]], pop: [[노래번호, 재생횟수], ... , [노래번호, 재생횟수]] }

    for i in range(len(genres)):
        dict_genres[genres[i]] = []

    for i in range(len(genres)):
        dict_genres[genres[i]].append([i, plays[i]])

    # 딕셔너리의 value에 해당하는 2차원 배열을, 각 원소의 1번째 원소를 기준으로 정렬한다.
    for i in list(dict_genres.keys()):
        dict_genres[i].sort(key=lambda x: x[1], reverse=True)

    print("장르별 노래정보(dict_genres): ", dict_genres)

    # dict_table은 장르별 재생횟수 총합을 구하기 위한 딕셔너리이다.
    # {장르: 재생횟수, 장르: 재생횟수, ... , 장르: 재생횟수}
    for i in range(len(genres)):
        dict_table[genres[i]] = 0

    for i in range(len(genres)):
        dict_table[genres[i]] += plays[i]

    dict_table = list(dict_table.items())
    dict_table = sorted(dict_table, key=lambda x:x[1], reverse=True)
    print("정렬된 dict_table: ", dict_table)

    # 각 장르별 재생횟수를 담고있는 딕셔너리를 순회한다.
    for i in range(len(dict_table)):
        key = dict_table[i][0]

        # 해당 장르의 노래가 1개밖에 없다면, 1개의 곡의 고유번호만 answer배열에 append한다.
        if len(dict_genres[key]) == 1:
            answer.append(dict_genres[key][0][0])

        # 해당 장르의 노래가 2개 이상이라면, 2개의 곡의 고유번호를 answer배열에 append한다.
        # dict_genres 딕셔너리의 value에 해당하는 2차원 배열을 재생횟수를 기준으로 내림차순 정렬했기 때문에,
        # 0번째 원소와 1번쨰 원소의 고유번호를 append하면 된다.
        else:
            answer.append(dict_genres[key][0][0])
            answer.append(dict_genres[key][1][0])

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))