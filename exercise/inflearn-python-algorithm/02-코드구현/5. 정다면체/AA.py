import sys
# sys.stdin = open("in1.txt", "rt")

n, m = map(int, input().split())

n_arr = range(1, n+1)
m_arr = range(1, m+1)
cnt = [0] * (n+m+1)
# print("cnt: ", cnt)

for i in n_arr:
    for j in m_arr:
        cnt[i+j] += 1

# print("cnt: ", cnt)

answer = []
max_val = max(cnt)
for i in range(len(cnt)):
    if max_val == cnt[i]:
        answer.append(i)

print(*answer)

