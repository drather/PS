n = int(input())
temp = ''
answer = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            temp = str(h) + str(m) + str(s)
            if '3' in temp:
                answer += 1

print(answer)

