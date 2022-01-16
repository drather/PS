"""
알파벳   A  B  C  D  E  F  G  H  I  J  K  L  M    N    O  P  Q  R  S  T  U  V  W  X  Y  Z
아스키  65 66 67 68 69 70 71 72 73 74 75 76 77   78   79 80 81 82 83 84 85 86 87 88 89 90
diff    0  1  2  3  4  5  6  7  8  9  10 11 12   13   14 15 16 17 18 19 20 21 22 23 24 25
실제거리 0  1  2  3  4  5  6  7  8  9  10 11 12   13   12 11 10 9  8  7  6  5  4  3  2  1

ABCDEFGHIJKLM N OPQRSTUVWXYZ

중간값은 A + Z // 2 = 65 + 90 // 2 = 77
즉, 오른쪽으로 돌지 왼 쪽으로 돌 지를 결정해야 한다.
타겟 문자의 아스키 값과 A의 아스키 값을 뺀 값이 12이하라면
A는 65
B는 66
...
Z는 90

구현할 것
1. 하나의 문자를 바꾸는 기능(위, 아래로)
2. 하나의 문자를 완성하고, 다른 문자로 이동하는 경우(오른, 왼으로)

1번 구현
알파벳은 총 26개
최대 13번까지 움직일 수 있다.
N이 중간인데, N이면 무조건 13번 움직여야 바꿀 수 있음
그게 아니라면, B ~ M 은 오른쪽으로 움직이고, O ~ Z 는 왼쪽으로 움직여야 함
반대방향으로 움직이는 경우는
    diff가 24라 하자
    그럼, 26에서 24를 나눈 나머지를 더한다.
    그럼 2이다.
    diff가 18이라 하자
    26에서 18을 나눈 나머지는 8이다.

2번 구현
방향을 정해야 한다. 왼쪽 OR 오른쪽
왼쪽이나 오른쪽 중, A가 없는 쪽으로 간다.
둘다 A라면, 그냥 한쪽방향으로 간다?

AAAAAAAAZAA
바꿀 문자를 찾는다.
왼쪽으로 찾은 거리, 오른쪽으로 찾은 거리 거리가 가까운 곳으로 이동?
"""


# 다른 걸 찾아서, 한 글자를 바꾸는 함수
# 입력: name, A가 아닌 글자의 인덱스
def change_one_ch(name, idx):
    print("찾은 위치 글자 바꾸기 함수 진입")
    print("바꾸려는 index: ", idx)
    print("바꾸려는 글자: ", name[idx])

    a_asc = 65
    num_alpha = 26

    if name[idx] != 'A':
        name_asc = ord(name[idx])
        diff = name_asc - a_asc
        added = 0
        if diff <= 13:
            added = diff
        else:
            added = num_alpha - diff
    print("한글자 바꾸면서 더할 added: ", added)
    return added


# 현재 idx 로부터, A가 아닌 다른 글자의 인덱스를 찾는 함수
# 입력: name, 현재 인덱스
# 출력: 'A'가 아닌 인덱스
def find_next_idx(name, origin, idx):
    print("\n다음 위치 찾기 함수")
    result = []
    left_idx = 0
    right_idx = 0

    left_count = 0
    right_count = 0

    # 시계방향으로 다른 문자 탐색
    for i in range(idx + 1, idx + len(name)):
        j = i % len(name)
        # print("시계 j: ", j)

        right_count += 1

        if name[j] != origin[j]:
            right_idx = j
            break

    # 반시계방향으로 다른 문자 탐색
    for i in range(idx - 1, -(idx + len(name)), -1):
        j = i % len(name)
        # print("반시계 j: ", j)
        left_count += 1

        if name[j] != origin[j]:
            left_idx = j
            break

    if left_count > right_count:
        idx = right_idx
        added = right_count
        print("오른쪽으로 감")

    elif left_count == right_count:
        idx = right_idx
        added = right_count
        print("오른쪽으로 감")

    else:
        idx = left_idx
        added = left_count
        print("왼쪽으로 감")

    print("lc, rc: ", left_count, right_count)
    print("lx, rx: ", left_idx, right_idx)
    print("next_idx: ", idx)
    print("다음 글자 찾으면서 더하는 added: ", added)
    return [idx, added]


def solution(name):
    print("\n\n----------"+str(name)+"-----------")
    origin = []
    arr_name = []
    want_change = []
    for i in range(len(name)):
        origin.append("A")
        arr_name.append(name[i])
        if origin[i] != name[i]:
            want_change.append(i)

    print("초기 origin: \t", origin)
    print("초기 arr_name: \t", arr_name)
    print("바꿔야 될 인덱스: \t", want_change)

    answer = 0
    a_asc = 65
    num_alpha = 26

    idx = 0
    iter_num = 0
    while True:
        print("\n")
        print("idx: ", idx)
        if name[idx] != origin[idx]:
            answer += change_one_ch(arr_name, idx)



        origin[idx] = name[idx]
        temp = find_next_idx(arr_name, origin, idx)
        if origin == arr_name:
            break

        idx = temp[0]
        answer += temp[1]

        print("origin: \t", origin)
        print("arr_name: \t", arr_name)

    print("answer: ", answer)
    return answer

# names = ["BBABA", "BBBAAB", "BBAABAA", "BBAABBB", "BBAABAAAA", "BBAABAAAAB"]
# answers = []
# for name in names:
#     answers.append(solution(name))

print(solution("BBABAAAB"))

# print("answers: ", answers)
# 정답: 6, 8, 7, 10, 7, 10
test = "ZBC"
# solution("JAN")

# name = "JEROEN"
# change_one_ch(name, 2)
# find_next_idx(name, 0)
# change_one_ch(idx)
