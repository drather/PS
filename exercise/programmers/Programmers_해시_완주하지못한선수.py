def solution(participants, completion):
    # 해쉬 테이블을 이용하기 위해 딕셔너리 선언
    hash_table = dict()

    # participants 배열을 순회하면서, 각 원소를 hash_table의 key로 선언한다.
    # 한 이름이 나올 때마다, 그 이름에 해당하는 value를 1 증가시킨다.
    for i in range(len(participants)):
        # key가 이미 존재하고, 그 key에 해당하는 값을 1 증가시키는 try문. 동명이인인 경우를 처리하기 위함이다.
        try:
            hash_table[participants[i]] += 1

        # 해당하는 key가 없을 경우, 새로 만들어 주기 위한 except문
        except:
            hash_table[participants[i]] = 1

    # completion 배열을 순회하면서, 각 원소를 key로써 hash_table에 접근한다. key에 해당하는 value의 값을 1씩 감소시킨다.
    for i in range(len(completion)):
        hash_table[completion[i]] -= 1

    # hash_table의 key들을 순회하면서, value가 0이 아닌 key를 리턴한다.
    # 즉, 참가자 명단에는 이름이 나왔지만 완주하지는 못한 선수의 이름을 리턴한다.
    for i in hash_table.keys():
        if hash_table[i] != 0:
            return i


participants = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participants, completion))