"""
단어 찾기

현수는 영어로 시는 쓰는 것을 좋아합니다.
현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다.
이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다.
여러분이 찾아 주세요.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에
쓰인 N-1개의 단어가 주어진다.

▣ 출력설명
첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.

▣ 입력예제 1
5
big
good
sky
blue
mouse
sky
good
mouse
big

▣ 출력예제 1
blue
"""
import sys
# sys.stdin = open("in1.txt", "rt")

word_num = int(input())
table = dict()
words = []
used = []
for _ in range(word_num):
    words.append(input())

for _ in range(word_num-1):
    used.append(input())

for i in words:
    table[i] = 0

for i in used:
    table[i] = 1

for i in list(table.keys()):
    if table[i] == 0:
        print(i)
        break


