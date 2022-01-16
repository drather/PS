# dna_num = 5
# dna_length = 8
# dnas = ['TATGATAC', 'TAAGCTAC', 'AAAGATCC', 'TGAGATAC', 'TAAGATGT']
#
# # dna_num, dna_length = 6, 10
# # dnas = [
# # "ATGTTACCAT",
# # "AAGTTACGAT",
# # "AACAAAGCAA",
# # "AAGTTACCTT",
# # "AAGTTACCAA",
# # "TACTTACCAA"]
# #
# dna_num, dna_length = 4, 10
# dnas = [
# # "ACGTACGTAC",
# # "CCGTACGTAG",
# # "GCGTACGTAT",
# # "TCGTACGTAA",
# # ]
dna_num, dna_length = input().split()
dna_num = int(dna_num)

dnas = []
for i in range(dna_num):
    dnas.append(input())
answers = []
answer_mat = [[0] * dna_num for i in range(dna_num)]

print(answer_mat)


def check(s1, s2, length):
    result = 0

    for q in range(length):
        if s1[q] != s2[q]:
            result += 1

    return result


for i in range(dna_num):
    str1 = dnas[i]
    print("i: ", i)
    for j in range(i+1, dna_num):

        idx = j % dna_num
        print("idx: ", idx)
        str2 = dnas[idx]
        temp = check(str1, str2, int(dna_length))
        answer_mat[i][idx] = temp
        answer_mat[idx][i] = temp


for i in answer_mat:
    print(i)
    answers.append(sum(i))

print(dnas[answers.index(min(answers))])
print("answer: ", answers)
print(min(answers))


