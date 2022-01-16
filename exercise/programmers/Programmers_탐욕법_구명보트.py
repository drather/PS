# 시간 초과
def solution(people, limit):
    answer = 0
    min_weight = 40

    people.sort()

    while people:
        i = 0

        if limit - people[0] < min_weight:
            answer += 1
            people.pop(i)

        else:
            pop_num = 1
            temp_sum = people[i]
            if len(people) > 1:
                j = i + 1
                while temp_sum <= limit and j < len(people):
                    if temp_sum + people[j] <= limit:
                        pop_num += 1
                        temp_sum += people[j]
                    else:
                        j += 1

                answer += 1

                while pop_num > 0 and people:
                    people.pop(0)
                    pop_num -= 1

            else:
                answer += 1

    return answer

def solution2(people, limit):
    answer = 0
    boat = [0]
    min_weight = 40

    # 사람들의 몸무게의 최소값이 40이므로, 한 보트에 최대 limit // 40의 결과값만큼 사람을 태울 수 있다.
    capacity = (limit // min_weight)

    while people:
        i = 0
        print("i, people[i]: ", i, people[i])

        if limit - people[0] < min_weight:
            print("뚱땡이 발견, 더 못태우니까 바로 태워서 보냄")
            answer += 1
            people.pop(i)

        else:
            print("날씬이 발견, 더 태울 수 있음")
            stack = [people[i]]
            j = i + 1
            if len(people) > 1:
                while sum(stack) + people[j] <= limit:
                    print("j, people[j]: ", j, people[j])
                    print("더 태울 수 있는 사람 발견")
                    stack.append(people[j])
                    print("stack: ", stack)

                print("이제 그만 태움, stack: ", stack)
                answer += 1
                people.pop(i)
                people.pop(j)
            else:
                answer += 1
                people.pop(i)

    return answer


def solution3(people, limit):
    answer = 0
    min_weight = 40

    people.sort()
    # 사람들의 몸무게의 최소값이 40이므로, 한 보트에 최대 limit // 40의 결과값만큼 사람을 태울 수 있다.
    capacity = (limit // min_weight)

    while people:
        print("answer: ", answer)
        i = 0
        print("people: ", people)
        print("i, people[i]: ", i, people[i])

        if limit - people[0] < min_weight:
            print("뚱땡이 발견, 더 못태우니까 바로 태워서 보냄")
            answer += 1
            people.pop(i)

        else:
            print("날씬이 발견, 더 태울 수 있음")
            pop_num = 1
            temp_sum = people[i]
            if len(people) > 1:
                j = i + 1
                if temp_sum + people[j] <= limit:
                    print("\t더 태울 수 있는 사람 발견")
                    print("\t\tj, people[j]: ", j, people[j])
                    pop_num += 1
                    print("\t\tpop 할 횟수: ", pop_num)
                    temp_sum += people[j]
                    print("\t\ttemp_sum: ", temp_sum)

                print("보트 무게 초과, 이제 그만 태움 몇번 pop? : ", pop_num)
                answer += 1

                while pop_num > 0 and people:
                    print("pop")
                    people.pop(0)
                    pop_num -= 1

            else:
                answer += 1
                print("마지막넘: ", people.pop(i))

        print("\n")

    return answer


def solution4(people, limit):
    from _collections import deque

    answer = 0
    people.sort()

    # dq는 배열의 양 끝에서 삽입, 삭제가 가능한 자료구조이다.
    dq = deque(people)

    while dq:
        length = len(dq)
        # dq에 원소가 2개 이상 있으면 삭제할 원소를 찾는다.
        if length >= 2:
            # 배열의 맨 처음과, 맨 끝의 원소를 더한 값이 limit보다 작다면, 맨 처음 원소와 맨 끝 원소를 pop한다.
            # 맨 끝 원소는 그냥 pop()으로 빼면 되지만,
            # 0번째 원소는 pop(0)으로 꺼낼 경우, people의 길이만큼의 시간복잡도를 갖는다.
            # 따라서, dq.popleft()로 꺼낸다. 이 경우, 시간 복잡도가 현저히 줄어든다.
            if dq[0] + dq[-1] <= limit:
                dq.popleft()
                dq.pop()
                answer += 1
            # 배열의 맨 처음과 맨 끝 원소의 합이 limit을 넘긴다면, 맨 끝 원소를 pop한다.
            else:
                dq.pop()
                answer += 1

        # dq에 원소가 1개밖에 없다면, answer에 1을 더해서 리턴한다
        elif length == 1:
            return answer + 1

        # dq에 원소가 없다면, answer를 리턴한다.
        else:
            return answer
    return answer



# people = [40, 50, 40, 40, 70, 90, 150, 140, 130, 120, 90, 55, 46, 78, 95, 101]
# limit = 150
# people = [40, 50, 40, 50, 60, 50, 40, 60, 50]
# limit = 240
# people = [70, 50, 80, 50]
# limit = 100
people = [10, 20, 30, 40, 50, 60, 70, 80, 90]
limit = 100

# print("정답: ", solution(people, limit))
print("정답2: ", solution4(people, limit))