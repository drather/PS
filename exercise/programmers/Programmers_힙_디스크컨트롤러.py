"""
shorted job first 를 구현한다.

1. heap을 하나 선언한다.
2. jobs를 힙으로 만든다.
3. 제일 처음에 들어온거를 뺀다.
4.

jobs의 각 원소의 모양
[걸리는 시간, 요청 시간, 대기 시간]

고려할 사항
1. 일단 cpu가 있다.
2. cpu가 비어있으면, 다음에 어떤 걸 가져올 지를 정한다. 이거 정하는 알고리즘이 필요
3. cpu가 차있으면, 별다른 행동을 하지 않는다. 그냥 대기 시간을 1씩 증가시킨다.
    그리고, time이 1씩 증가하는데, time이 jobs[i][0]과 같다면, 그걸 waiting_process로 옮긴다.
4. 그리고, waiting_process가 힙이다. 최소힙으로, 1번째 원소를 기준으로 정렬할 것이다.

"""

import heapq as hq


def solution_(jobs):
    time = 0
    waiting_process = []
    finished_process = []
    cpu = None

    for i in range(len(jobs)):
        temp = jobs[i][0]
        jobs[i][0] = jobs[i][1]
        jobs[i][1] = temp
        jobs[i].append(0)

    while jobs:
        # 현재 처리중인 프로세스 없음
        print("\n현재 cpu: ", cpu)
        print("현재 time: ", time)
        print("현재 대기중인 프로세스: ", waiting_process)

        # 처리중인 프로세스 없음
        if not cpu:
            # 처리중인 프로세스 없고, 대기중인 프로세스 없음
            if not waiting_process:
                cpu = jobs.pop(0)

            # 처리중인 프로세스 없고, 대기중인 프로세스 있음
            else:
                cpu = hq.heappop(waiting_process)

        # 처리중인 프로세스 있음
        else:
            cpu[-1] += 1
            if time - cpu[1] == cpu[0]:
                print(cpu, "프로세스 완료")
                finished_process.append(cpu)
                cpu = None

        time += 1

        for i in range(len(jobs)):
            try:
                if time == jobs[i][1]:
                    waiting_process.append(jobs[i])
                    print("대기열에 추가: ", jobs[i])
                    del jobs[i]

                if time < jobs[i][1]:
                    break
            except(IndexError):
                continue

    finished_process.append(cpu)
    cpu = None
    answer = time + finished_process[-1][0]

    print("finished: ", finished_process)
    print("cpu: ", cpu)
    print("jobs: ", jobs)


"""
jobs의 각 원소의 모양
[걸리는 시간, 요청 시간, 대기 시간, 진행 시간]
"""


def solution(jobs):
    time = 0
    waiting_process = []
    finisied_process = []
    cpu = None
    process_num = len(jobs)

    for i in range(len(jobs)):
        temp = jobs[i][0]
        jobs[i][0] = jobs[i][1]
        jobs[i][1] = temp
        jobs[i].append(0)
        jobs[i].append(0)

    print("걸리는 시간, 요청 시각, 대기 시간, 진행 시간")
    jobs.sort(key=lambda x:x[1])
    print("jobs: ", jobs)

    while len(finisied_process) != process_num:
        print("\n현재 time: ", time, "초")

        # 1). jobs -> waiting 으로 프로세스 옮기는 과정
        for i in range(len(jobs)):
            if time == jobs[i][1]:
                hq.heappush(waiting_process, jobs[i])
                print("대기열에 추가: ", jobs[i])
                print("waiting_process: ", waiting_process)

            elif time < jobs[i][1]:
                break

        # 2). waiting -> cpu로 옮기는 과정
        if not cpu:
            if waiting_process:
                cpu = hq.heappop(waiting_process)
                print("cpu에 프로세스 추가, ", cpu)

        # 3). cpu -> finish로 옮기는 과정
        else:
            print("cpu가 process 처리중")
            cpu[-1] += 1
            print("cpu: ", cpu)
            if cpu[0] == cpu[-1]:
                cpu[2] = time - cpu[1]
                finisied_process.append(cpu)
                print("cpu가 프로세스 마침")
                print("마친 프로세스: ", cpu)
                cpu = None
                print("마치고 난 cpu: ", cpu)
                if waiting_process:
                    cpu = hq.heappop(waiting_process)
                    print("마치고 들어온 프로세스: ", cpu)

        time += 1

    print("finished: ", finisied_process)
    answer = 0
    for i in finisied_process:
        answer += i[2]

    answer = answer // process_num
    print("answer: ", answer)
    return answer


jobs = [[0, 3], [1, 9], [2, 6]]
jobs = [[0, 3], [1, 9], [500, 6]]
jobs = [[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]
jobs = [[0,3],[0,1],[4,7]]
print(solution(jobs))