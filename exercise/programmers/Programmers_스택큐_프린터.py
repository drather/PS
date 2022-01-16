def solution(priorities, location):
    answer = 0
    d2_prior = []

    # 인덱스와 값을 따로 저장하기 위해서, 주어진 데이터를 2차원 배열의 형태로 바꾼다.
    # 각 원소는 [처음에 주어진 인덱스, 값] 이러한 형태로 저장된다.
    for i in range(len(priorities)):
        d2_prior.append([i, priorities[i]])

    # d2_prior 배열의 원소가 더이상 없을 때까지 순회한다.
    i = 0
    while d2_prior:
        # d2_prior 배열의 0번째 원소를 꺼낸다.
        temp = d2_prior.pop(0)

        # 나머지 d2_prior 배열의 1번째 값과 temp의 1번째 값을 비교한다.
        for i in range(len(d2_prior)):
            # 만약 d2_prior배열의 i번째 원소의 1번째 값이 더 크다면, 더 중요한 문서가 뒤에 있다는 뜻이다.
            # 그러므로 출력하지 않고 d2_prior배열의 맨 뒤로 보낸다.
            if temp[1] < d2_prior[i][1]:
                d2_prior.append(temp)
                print(temp, "출력 대기, 뒤로감")
                break

            # 그렇지 않고, 현재 temp의 1번쨰 값이 가장 크다면, temp문서가 가장 중요하다는 뜻이므로 출력한다.
            else:
                print(temp, "출력")
                # 그리고, 문제에서 주어진 location과 temp의 0번쨰 값이 일치한다면, 그때 멈춘다.
                if temp[0] == location:
                    break
                # 그렇지 않다면, answer의 값을 1 증가시킨다.
                else:
                    answer += 1
    return answer + 1

def solution3(priorities, location):
    answer = 0
    d2_prior = []

    # 인덱스와 값을 따로 저장하기 위해서, 주어진 데이터를 2차원 배열의 형태로 바꾼다.
    # 각 원소는 [처음에 주어진 인덱스, 값] 이러한 형태로 저장된다.
    for i in range(len(priorities)):
        d2_prior.append([i, priorities[i]])
    i = 0

    # d2_prior 배열의 원소가 더이상 없을 때까지 순회한다.

    while priorities:
        # d2_prior 배열의 0번째 원소를 꺼낸다.
        temp = d2_prior.pop(0)

        # 나머지 d2_prior 배열의 1번째 값과 temp의 1번째 값을 비교한다.
        for i in range(len(d2_prior)):
            # 만약 d2_prior배열의 i번째 원소의 1번째 값이 더 크다면, 더 중요한 문서가 뒤에 있다는 뜻이다.
            # 그러므로 출력하지 않고 d2_prior배열의 맨 뒤로 보낸다.
            print(temp[1], d2_prior[i][1])

            if temp[1] <= d2_prior[i][1]:
                d2_prior.append(temp)
                continue

            # 그렇지 않고, 현재 temp의 1번쨰 값이 가장 크다면, temp문서가 가장 중요하다는 뜻이므로 출력한다.
            else:
                # 문제에서 주어진 location과 temp의 0번쨰 값이 일치한다면, 그때 멈춘다.
                if temp[0] == location:
                    print(temp[0], location)
                    return answer + 1
                else:
                    # 그렇지 않다면, answer의 값을 1 증가시킨다.
                    answer += 1
    return answer + 1


def solution2(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans

priorities = [2, 1, 3, 2]
location = 2

priorities = [1,1,9,1,1,1]
location = 0


print("정답: ", solution3(priorities, location))

