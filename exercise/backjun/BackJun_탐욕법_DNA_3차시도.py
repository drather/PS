N, M = map(int, input().split())
dna = []
result = ''
hd = 0
for i in range(N):
    dna.append(input())

alphas = ["A", "C", "G", "T"]
ham_dist = 0
for i in range(M):
    counts = [0, 0, 0, 0]
    for j in range(N):
        if dna[j][i] == 'A':
            counts[0] += 1
        elif dna[j][i] == 'C':
            counts[1] += 1
        elif dna[j][i] == 'G':
            counts[2] += 1
        else:
            counts[3] += 1

    max_count = max(counts)
    max_idx = counts.index(max_count)
    result += alphas[max_idx]
    ham_dist += N - max_count

print(result)
print(ham_dist)

