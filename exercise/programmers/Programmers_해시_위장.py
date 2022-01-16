def solution(clothes):
    answer = 1
    # 해쉬 테이블을 사용하기 위해 딕셔너리 선언
    table = dict()

    # clothes의 각 원소들을 읽어서, 옷의 종류가 key이고,
    # {옷의 종류1 : 종류1 의 출현 빈도, 옷의 종류2: 종류2 의 출현 빈도}
    # 이런 형태의 딕셔너리를 만들것이다.

    for i in range(len(clothes)):
        # clothes[i][1]은 옷의 종류를 말한다.
        # 즉, headgear라는 키에 해당하는 value가 있으면 그 값을 1 증가시킨다.
        try:
            table[clothes[i][1]] += 1
        # headgear라는 key가 딕셔너리에 들어와있지 않으면, 새로 추가하고 그 value를 1로 한다.
        except:
            table[clothes[i][1]] = 1

    # 딕셔너리에서 value들을 뽑아서, 리스트로 만든다.
    values = list(table.values())

    # 각 원소들을 1 증가시킨 후, 모두 곱한다.
    for i in range(len(values)):
        values[i] += 1
        answer *= values[i]

    # 1을 빼주고 리턴한다.
    answer -= 1
    return answer


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],
           ["oldbe", "bottom"], ["oltus", "top"]]
print(solution(clothes))
