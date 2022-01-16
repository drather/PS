n, m = map(int, input().split())

table = {}
answer = []
num = 0
for i in range(n):
    temp = input()
    table[temp] = 1

for j in range(m):
    temp = input()
    try:
        table[temp]
        num += 1
        answer.append(temp)
    except:
        continue

print(num)
answer.sort()
for i in answer:
    print(i)

"""
이 아래 코드는 실행 시간이 훌씬 낮은 답안. 꼭 참고해라. 
"""
import sys

N, M = map(int, sys.stdin.readline().split())
N_list = [sys.stdin.readline().strip() for i in range(N)]
M_list = [sys.stdin.readline().strip() for i in range(M)]

# 교차하는 이름들을 찾는다
duplicate = list(set(N_list) & set(M_list))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)