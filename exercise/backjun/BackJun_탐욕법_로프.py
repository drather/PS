rope_num = 2
ropes = [10, 15, 21, 19, 17, 20, 1, 3, 4, 5, 7]
ropes = [5, 1, 2, 3, 4, 5]
# ropes = [2, 1, 1]
# ropes = [2, 10, 100]
# ropes = [1, 1]
# ropes = [3, 11, 5, 4]
#
rope_num = int(input())

ropes = []

for i in range(rope_num):
    ropes.append(int(input()))

ropes.sort(reverse=True)
print(ropes)

used_rope = []

weight_max = 0
weight_sum = 0
weight_temp = 0

for i in range(len(ropes)):
    print("\nropes 의 원소: ", ropes[i])
    if i == 0:
        weight_max += ropes[i]
        weight_sum += ropes[i]
        used_rope.append(ropes[i])

    else:
        # print("이번꺼 포함한 밧줄 갯수: ", i)
        weight_temp = ropes[i] * (i+1)
        print("weight_temp: ", weight_temp)
        print("weight_max: ", weight_max)
        if weight_max < weight_temp:
            used_rope.append(ropes[i])
            weight_max = weight_temp
            print("밧줄 사용함")

        else:
            print("밧줄 사용안함")

    print("사용한 로프: ", used_rope)

print(weight_max)
