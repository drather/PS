import sys

# sys.stdin = open("in2.txt", "rt")

stu_num = int(input())
score_list = list(map(float, input().split()))

# print(stu_num, score_list)

avg = round(sum(score_list) / len(score_list))
# print("avg: ", avg)

ans = tuple()
abs_val = 9999
for i in range(len(score_list)):
    cand = abs(score_list[i] - avg)
    if cand < abs_val:
        abs_val = cand
        ans = (score_list[i], i+1)

    elif cand == abs_val:
        if ans[0] < score_list[i]:
            ans = (score_list[i], i+1)

    # print("ans: ", ans)

print(int(avg), ans[1])