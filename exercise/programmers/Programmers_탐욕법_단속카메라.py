"""
sections 배열은, 2차원 배열로, 구간의 시작과 끝을 같는 배열을 원소로 갖는다.
또한, sections 는 stack이다. 원소가 들어오면

다음을 반복한다.
    1. sections 배열을 선언한다.
    2. sections 배열에 routes를 하나씩 넣을 것이다.
    3. sections 배열에 원소가 없다면, 그냥 집어넣는다
    4. sections 배열에 원소가 있다면, routes에서 하나를 꺼내서, 둘을 비교해서, 교집합 구간을 만들어서, 집어넣는다.
        1).
"""


def make_intersection(r1, r2):
    print("r1, r2: ", r1, r2)

    lower = max(r1[0], r2[0])
    upper = min(r1[1], r2[1])

    temp = []
    if upper < lower:
        print("교집합 없음")
        return None

    elif upper == lower:
        print("교집합이 한 점")
        temp.append([upper, upper])

    else:
        print("교집합 있음")
        temp.append([lower, upper])

    print("----새롭게 만들어진 교집합 temp: ", temp)
    return temp


def solution(routes):
    answer = 0
    # routes.sort(key=lambda x:abs(x[1]-x[0]), reverse=True)
    routes.sort(key=lambda x:x[1])
    sections = []
    print(routes)

    for i in routes:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]

        mid = []
        print("\n추가할 routes: ", i)

        if not sections:
            sections.append(i)
            continue

        else:
            while sections:
                section_popped = sections.pop()
                print("비교할 sections: ", section_popped)
                temp = make_intersection(i, section_popped)

                for k in temp:
                    if k not in mid:
                        mid.append(k)

            sections = mid
            print("중간 결과물: ", sections)

    print("sections: ", sections)
    answer = len(sections)
    print("이번 케이스 정답: ", answer, "\n\n")
    return answer

my_answers = []
print(my_answers.append(solution([[-2, -1], [1, 2], [-3, 0]]))) #2
print(my_answers.append(solution([[0, 0], ]))) #1
print(my_answers.append(solution([[1, 2], [0, 1], [0, 1], ]))) #1
print(my_answers.append(solution([[0, 1], [2, 3], [4, 5], [6, 7]]))) #4
print(my_answers.append(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))) #2
print(my_answers.append(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))) #2
print(my_answers.append(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))) #2
answers = [2, 1, 1, 4, 2, 2, 2]
print("cor_answers: \t", answers)
print("my_answers: \t", my_answers)


