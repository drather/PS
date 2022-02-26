"""
모험가 N명이 있다. 각 모험가를 대상으로 공포도를 측정했다.
공포도가 X인 모험가는 반드시 X명 이상으로 구성해야 여행을 떠날 수 있을 때, 최대 몇개의 모험가 그룹을 만들 수 있는지를 구하시오

입력
5
2 3 1 2 2

출력
2
"""
person_cnt = int(input())
array = list(map(int, input().split()))
# person_cnt = 5
# array = [2, 3, 1, 2, 2]


if __name__ == '__main__':
    array.sort()

    start_idx = 0
    end_idx = 0
    answer = 0

    while start_idx < person_cnt and end_idx < person_cnt:
        start_horror = array[start_idx]
        end_idx = start_idx + start_horror
        print(f"start_idx, end_idx : {start_idx}, {end_idx}")

        for horror in array[start_idx:end_idx]:
            if horror > start_horror:
                break

        else:
            answer += 1
            start_idx = end_idx
            end_idx += array[start_idx]

    print(answer)

