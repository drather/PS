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

def change_one_ch(idx):
    # 한 글자를 바꾸는 함수
    pass


def find_next_idx():
    # 다음 글자를 찾는 함수
    pass


def solution(name):
    answer = 0
    origin = ""
    a_asc = 65
    num_alpha = 26
    ans_str = ""
    for i in range(len(name)):
        origin += "A"

    idx = 0
    while ans_str != name:
        # if origin[idx] != name[idx]:
        #     name_asc = ord(name[idx])
        #     diff = name_asc - a_asc
        #     print("diff: ", diff)
        #     added = 0
        #     if diff <= 13:
        #         added = diff
        #     else:
        #         added = num_alpha - diff
        #     print("added: ", added)
        #
        # else:
        #     print(idx, "번째 같음")
        #     ans_str += name[idx]
        #     idx += 1
        #     continue
        #
        # ans_str += name[idx]
        # answer += added
        # print("\norigin: ", origin)
        # print("name: ", name)
        # print("ans_str: ", ans_str)
        # print("answer: ", answer)

        # 지금은 idx += 1 로만 했는데, 이제 1번을 구현해야 함.
        # 그러고 다음 수정할 위치의 인덱스를 정해서, idx의 값을 정해야 함
        right_count = 0
        left_count = 0
        ans_str += name[idx]

        left_idx = 0
        right_idx = 0
        # 시계방향으로 다른 문자 탐색
        for i in range(idx, idx + len(name)):
            j = i % len(name)
            print("시계방향으로 다음 문자 탐색하는 i: ", i)
            print("찾은 원소: ", name[j])

            if name[j] != 'A':
                right_idx = j
                break
            else:
                right_count += 1

        # 반시계방향으로 다른 문자 탐색
        for i in range(idx, len(name) - 1, -1):
            j = i % len(name)
            print("반시계방향으로 탐색하는 i: ", i)
            print("찾은 원소: ", name[j])

            if name[j] != 'A':
                left_idx = j
                break
            else:
                left_count += 1

        if left_count > right_count:
            idx += right_idx
            answer += right_count
        else:
            idx += left_idx
            answer += left_count


    print("answer: ", answer)


    return answer


name = "JAZ"

print(solution(name))