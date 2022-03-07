import heapq


arr_input = list(map(str, input()))
arr_str = []
num_sum = 0
res = ""

for i in arr_input:
    print(i)
    if i.isalpha():
        heapq.heappush(arr_str, i)

    if i.isdecimal():
        num_sum += int(i)

while arr_str:
    res += heapq.heappop(arr_str)

print(res + str(num_sum))