people_num = int(input())
times = list(map(int, input().split()))
answer = []
times.sort()
res = 0
for i in range(len(times)):
    res += times[i]
    answer.append(res)

print(sum(answer))