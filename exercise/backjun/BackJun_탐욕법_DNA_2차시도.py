N, M = map(int, input().split())
dna = []
result = ''
hd = 0
for i in range(N):
    dna.append(input())

for i in range(M):
    cnt = [0, 0, 0, 0]
    for j in range(N):
        if dna[j][i] == 'A':
            cnt[0] += 1
        elif dna[j][i] == 'C':
            cnt[1] += 1
        elif dna[j][i] == 'G':
            cnt[2] += 1
        elif dna[j][i] == 'T':
            cnt[3] += 1

    print("\n반복이 끝난 후 cnt 배열: ", cnt)

    max_cnt = max(cnt)
    idx = cnt.index(max_cnt)
    print("가장 많이 나온 DNA 값: ", max_cnt)
    print("그 값의 idx: ", idx)

    if idx == 0:
        result += 'A'
    elif idx == 1:
        result += 'C'
    elif idx == 2:
        result += 'G'
    elif idx == 3:
        result += 'T'

    hd += N - max_cnt
    print("hd: ", hd)

print(result)

print(hd)
