edges = []
adj_list = {}
students, comp_num = map(int, input().split())

in_degrees = [0] * (students+1)
in_degrees[0] = -1

# 인접 리스트 생성
for i in range(1, students+1):
    adj_list[i] = []

for i in range(comp_num):
    temp = list(map(int, input().split()))
    adj_list[temp[0]].append(temp[1])

    in_degrees[temp[1]] += 1


print("adj_list: ", adj_list)
print("in_degrees: ", in_degrees, "\n")

# 원래 배열 구하는 부분
# for i in list(adj_list.keys()):
#     for j in list(adj_list.keys()):
#         if i in adj_list[j]:
#             in_degrees[i] += 1


# stack 자료구조를 이용해, 진입 차수가 0인 노드부터 answer 배열에 담을 것
stack = []
answer = []
for i in range(1, len(in_degrees)):
    if in_degrees[i] == 0:
        stack.append(i)
print("Stack: ", stack)

while stack:
    node = stack.pop()
    answer.append(node)

    for i in adj_list[node]:
        in_degrees[i] -= 1
        if in_degrees[i] == 0:
            stack.append(i)

print("answer: ", answer)