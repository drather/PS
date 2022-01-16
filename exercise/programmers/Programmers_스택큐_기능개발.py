def solution(progresses, speeds):
    # 정답을 담을 배열
    answer = []

    # 선입선출을 활용하기 위한 자료구조 Queue
    queue = []

    # progresses배열을 순회하면서, 각 원소를 배포까지 며칠이 남았는지를 나타내게끔 바꾼다.
    for i in range(len(progresses)):
        progresses[i] = (progresses[i] - 100) * -1
        progresses[i] = progresses[i] / speeds[i]
        if progresses[i] % 1 != 0:
            progresses[i] = int(progresses[i]) + 1

    # progress배열을 하나씩 queue에 집어넣는다.
    for i in range(len(progresses)):
        # queue에 원소가 하나도 없다면, progress[i]를 집어넣고 continue한다.
        if len(queue) == 0:
            queue.append(progresses[i])
            continue

        # queue에 원소가 2개 이상 있다면, 원소들 중 가장 큰 값을 temp_max에 저장한다.
        temp_max = max(queue)

        # queue에 progresses[i]를 집어넣는다.
        queue.append(progresses[i])

        # 만약 새로 들어온 원소가 기존의 최대값인 temp_max보다 크다면,
        if temp_max < progresses[i]:
            # 방금 들어온 원소를 제외한 나머지를 arr에 복사한다.
            arr = queue[0:-1]
            # arr의 원소의 갯수를 answer배열에 append한다.
            answer.append(len(arr))

            # 방금 들어온 원소를 제외하고 나머지 원소는 없애준다.
            while len(queue) != 1:
                queue.pop(0)

    # queue에 남아있는 원소들의 갯수를 answer에 append한다.
    answer.append(len(queue))
    return answer

progresses = [93,30,55]
speeds =  [1,30,5]
print(solution(progresses, speeds))