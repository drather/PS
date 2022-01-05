#n, m, k = map(int, input().split())
#data = list(map(int, input().split()))

n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]
cnt = [k] * n
data.sort()

first_val = data[-1]
second_val = data[-2]

answer = 0

while True:
    for i in range(k):
        answer += first_val
    
    if m == 0:
        break
    else:
        answer += second_val

    m -= 1


print(answer)


