"""
가장 큰 수
선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하
여 가장 큰 수를 만들라고 했습니다. 여러분이 현수를 도와주세요.(단 숫자의 순서는
유지해야 합니다)

만약 5276823 이 주어지고 3개의 자릿수를 제거한다면
7823이 가장 큰 숫자가 됩니다.

▣ 입력설명
첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.

▣ 출력설명
가장 큰 수를 출력합니다.

▣ 입력예제 1
5276823 3

▣ 출력예제 1
7823

▣ 입력예제 2
9977252641 5

▣ 출력예제 2
99776
"""
import sys
sys.stdin = open("in3.txt", "rt")

num, count = map(int, input().split())

stack = []
str_num = str(num)
answer = ""

for s in str_num:
    num_int = int(s)

    while stack and count > 0 and stack[-1] < num_int:
        stack.pop()
        count -= 1

    stack.append(num_int)

while count > 0:
    stack.pop()
    count -= 1

res = ''.join(map(str, stack))
print(res)







# !!!!!!!!!!!! 첫번째 풀이 !!!!!!!!!!!!
# for s in str_num:
#     int_num = int(s)
#     stack.append(int_num)
#
#     if len(stack) < 2:
#         continue
#
#     while count > 0:
#         if len(stack) >= 2:
#             if stack[-1] > stack[-2]:
#                 stack[-1], stack[-2] = stack[-2], stack[-1]
#                 temp = stack.pop()
#                 count -= 1
#             else:
#                 break
#         else:
#             break
#
# while count > 0:
#     stack.pop(-1)
#     count -= 1
#
# for i in stack:
#     answer += str(i)
#
# print(answer)










