"""
인접 행렬에서 본 그래프와 같은 모양의 그래프를 예로 들 것.
입력: 그래프의 인접 리스트
출력: 위상 정렬의 순서(같은 순서일 경우 아무거나 뽑음)
알고리즘
    1. 모든 정점의 진입 차수를 계산
    2. 진입 차수가 0인 정점을 스택에 삽입
    3. 위상 순서를 생성
"""
adj_list = {0: [2, 3], 1: [3, 4], 2: [3, 5], 3: [5], 4: [5], 5: []}


def topological_sort_stack(adj_list):
    stack = []
    in_degree = [0] * len(adj_list)
    answer = []

    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            temp = adj_list[j]
            for k in range(len(temp)):
                if temp[k] == i:
                    in_degree[i] += 1

    print("in_degree 배열: ", in_degree)

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            stack.append(i)

    print("초기 스택: ", stack)
    while stack:
        node = stack.pop()
        answer.append(node)
        print("pop 된 노드: ", node)

        for i in range(len(adj_list[node])):
            idx = adj_list[node][i]
            in_degree[idx] -= 1
            if in_degree[idx] == 0:
                stack.append(idx)

    print("answer: ", answer)


print(topological_sort_stack(adj_list))

"""
이 아래에는 스택이 아닌 큐를 이용해서 위상 정렬을 해보겠다. 
"""

def topological_sort_queue(adj_list):
    import queue

    myQue = queue.Queue()
    in_degree = [0] * len(adj_list)
    answer = []

    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            temp = adj_list[j]
            for k in range(len(temp)):
                if temp[k] == i:
                    in_degree[i] += 1
    print("in_degree 배열: ", in_degree)

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            myQue.put(i)

    print("초기 큐: ", myQue)
    while not myQue.empty():
        node = myQue.get()
        answer.append(node)
        print("pop 된 노드: ", node)

        for i in range(len(adj_list[node])):
            idx = adj_list[node][i]
            in_degree[idx] -= 1
            if in_degree[idx] == 0:
                myQue.put(idx)

    print("answer: ", answer)


print(topological_sort_queue(adj_list))


def queue_topo_sort(adj_list):
    queue = []
    in_degree = [0] * len(adj_list)
    answer = []

    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            temp = adj_list[j]
            for k in range(len(temp)):
                if temp[k] == i:
                    in_degree[i] += 1
    print("in_degree 배열: ", in_degree)

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)

    print("초기 큐: ", queue, "에서 반복 시작")
    while queue:
        print("\nqueue: ", queue)
        node = queue.pop(0)
        answer.append(node)
        print("pop 된 노드: ", node)

        for i in range(len(adj_list[node])):
            idx = adj_list[node][i]
            in_degree[idx] -= 1
            if in_degree[idx] == 0:
                queue.append(idx)

    print("answer: ", answer)

queue_topo_sort(adj_list)
