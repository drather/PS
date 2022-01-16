"""
이 경우는 DFS로 푸는 것이 맞을 것 같다. 목적지로 가는 최단 거리를 구하는 경우이므로, 모든 경우를 고려할 필요가 없기 때문이다.
즉, begin에서 출발해서, stack에다가 begin과 1개만 차이나는 단어들을 append한다.
그러고 stack이 빌 때까지 원소를 하나씩 pop하고, pop한 원소와 1개 차이나는 원소들을 찾는다.
찾은 원소를 다시 죽 살펴보면서 target과 일치하는지 확인한다.
pop하고 확인할 때마다, target과 같아지면 answer를 리턴한다.


떙, 너비우선으로 푸시오
"""

# 이 함수는 두 문자열을 비교한다.
# 길이가 같은 두개의 문자열이 서로 한 문자만 다른지를 확인하고, 그렇다면 True, 아니면 False를 반환한다.
def comparison(str1, str2):
    answer = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            answer += 1
    if answer == len(str1)-1:
        return True
    else:
        return False


def dfs_iterative_solution(begin, target, words):
    if target not in words:
        return 0

    visited = []
    answer = 0
    stack = [begin]

    while stack:
        temp = stack.pop()
        visited.append(temp)
        print("temp: ", temp)
        for i in range(len(words)):
            if comparison(temp, words[i]) and words[i] not in stack and words[i]not in visited:
                stack.append(words[i])

        print("stack: ", stack)
        print("visited: ", visited, "\n")
        if target in stack:
            print("찾음")
            return answer + 1
        else:
            print("못찾음")
            answer += 1

    return 0


def solution(begin, target, words):
    queue = [begin]
    answer = 0

    if target not in words:
        return 0

    temp = queue.pop(0)
    for i in range(len(words)):
        if comparison(temp, words[i]):
            queue.append(words[i])

        if target in queue:
            print("찾음")

        else:
            print("못찾음")
            answer += 1


def bfs_solution(begin, target, words):
    # target이 words안에 없다면 단어 변환을 할 수 없으므로 0을 리턴한다.
    if target not in words:
        return 0

    # 딕셔너리를 선언한다.
    # 이 딕셔너리의 key는 각 단계를 나타내는 정수이고, value는 그 단계에서 만들수 있는 모든 단어의 배열이다.
    graph = dict()
    graph[0] = [begin]

    # i는 graph의 key로 들어갈 값이다. 즉, 각 단계를 나타낸다. 그리고 temp배열을 만들어놓는다.
    for i in range(1, len(words)):
        # print("i: ", i)
        temp = []

        # j라는 인덱스는 i-1번째 단계의 value, 즉 i-1번 변환해서 만들 수 있는 단어들의 배열을 순회한다.
        # 각 원소를 comp로 지정한다.
        for j in range(len(graph[i-1])):
            # print("j:", j)
            comp = graph[i-1][j]

            # k라는 인덱스는 words배열의 다른 단어들을 순회한다.
            for k in range(len(words)):
                # print("k: ", k)

                # words의 단어들을 순회하면ㅅ, comp와 comparison했을 때 True인 원소들을 temp에 append한다.
                if comparison(comp, words[k]):
                    temp.append(words[k])

        # temp 안에 target이 있다면, i를 리턴한다
        if target in temp:
            graph[i] = temp
            print(graph)
            return i

        # 그렇지 않다면, graph의 key인 i에 value로써 temp를 지정한다.
        graph[i] = temp
        print(graph)




begin = "hit"
target = "cog"
words = ["cog", "hot", "log", "hqt",  "dog", "dot", "lot"]
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(bfs_solution(begin, target, words))