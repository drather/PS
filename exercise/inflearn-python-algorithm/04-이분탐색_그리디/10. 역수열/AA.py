"""
역수열(그리디)
1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때, 1부터 n까지 각각의 수 앞
에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라 한다.

예를 들어 다음과 같은 수열의 경우
4 8 6 2 5 1 3 7
1앞에 놓인 1보다 큰 수는 4, 8, 6, 2, 5. 이렇게 5개이고,
2앞에 놓인 2보다 큰 수는 4, 8, 6. 이렇게 3개,
3앞에 놓인 3보다 큰 수는 4, 8, 6, 5 이렇게 4개......
따라서 4 8 6 2 5 1 3 7의 역수열은 5 3 4 0 2 1 1 0 이 된다.

n과 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 원래의 수열을 출
력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<100)이 주어지고, 두 번째 줄에는 역수열이 숫자 사이에 한
칸의 공백을 두고 주어진다.

▣ 출력설명
원래 수열을 출력합니다.

▣ 입력예제 1
8
5 3 4 0 2 1 1 0

▣ 출력예제 1
4 8 6 2 5 1 3 7
"""
import sys
sys.stdin = open("in1.txt", "rt")

num = int(input())
rev_arr = list(map(int, input().split()))


num = 8
# origin= [4, 8, 6, 2, 5, 1, 3, 7]
rev_arr = [5, 3, 4, 0, 2, 1, 1, 0]

answer = [0] * num
print("초기 answer: ", answer)
for i in range(num):
    print("\n위치를 찾고자 하는 수: ", i+1)
    for j in range(num):
        print("위치 찾기위한 인덱스: ", j)
        if rev_arr[i] == 0 and answer[j] == 0:
            print("자리 찾음")
            answer[j] = i+1
            break

        elif answer[j] == 0:
            print("\t0의 갯수 감소해줌")
            rev_arr[i] -= 1

    print("answer: ", answer)
print(*answer)





# !!!!!!!!!!!! 첫 번째 풀이 !!!!!!!!!!!!
# answer = [0] * num
# for i in range(num):
#     target_value = i+1
#     count = rev_arr[i]
#     pos = 0
#
#     # print("\nanswer 배열에 넣으려는 원소의 값: ", target_value)
#     # print("answer 배열에서 target_value 앞에 위치해야 하는 0의 갯수: ", count)
#
#     for j in range(num):
#         # print("위치 찾는 인덱스 j: ", j)
#         if count == 0:
#             break
#
#         if answer[j] == 0:
#             count -= 1
#         pos += 1
#
#     while answer[pos] != 0:
#         pos += 1
#
#     # print("위치: ", pos)
#     answer[pos] = target_value



print(*answer)

