answer = []
while True:
    temp = list(input())
    print("temp: ", temp)
    if temp == ['E', 'N', 'D']:
        break
    else:
        temp.reverse()
        answer.append(temp)

res = []
for i in range(len(answer)):
    temp = ""
    for j in range(len(answer[i])):
        temp += answer[i][j]

    res.append(temp)

for i in res:
    print(i)

