"""
위상정렬을 사용한다. -> 오답, 그냥 위상정렬 연습이라 생각하자
위상 정렬을 하는데, 같은 위상값을 가진 애들을 배열로 나타낸 것.
즉, 기존의 위상정렬은 DFS 기반인데, 여기선 BFS기반으로 한 것.
이것 또한 엄청난 소득이니, 잊지 말 것.
"""
import pprint

def solution(n, results):
    import copy
    real_answer = 0
    answer = []

    adj_list = {}
    in_degrees = [0] * (n+1)
    in_degrees[0] = -1

    for i in range(1, n+1):
        adj_list[i] = []

    for res in results:
        adj_list[res[0]].append(res[1])
        in_degrees[res[1]] += 1

    print("adj_list: ", adj_list)
    print("in_degrees: ", in_degrees)

    queue = []
    for i in range(len(in_degrees)):
        if in_degrees[i] == 0:
            queue.append(i)

    while queue:
        if len(queue) >= 2:
            real_answer += len(queue)
        print("\n\n-----반복 시작할 때 queue: ", queue, "-----")
        temp = []

        for i in queue:
            node = i
            print("탐색할 node: ", node)
            answer.append(node)

            print("node에서 갈 수 있는 노드들", adj_list[node])
            for j in adj_list[node]:
                print("\n진입차수 깎일 노드 :", j)
                in_degrees[j] -= 1
                if in_degrees[j] == 0:
                    print("큐에 추가될 노드: ", j)
                    temp.append(j)

        queue = temp
        print("temp: ", temp)

        if len(temp) >= 2:
            real_answer += len(temp)


    print("answer: ", answer)
    print("real_answer: ", real_answer)
    return real_answer


results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
n = 5

print("\n\n찐 answer: ", solution(n, results))

