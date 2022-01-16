import heapq as hq


def solution(jobs):
    time = 0
    waiting_process = []
    finisied_process = []
    cpu = None
    process_num = len(jobs)
    idx = 0

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
        for i in range(idx, len(jobs)):
            print("idx: ", idx)
            if time == jobs[i][1]:
                temp = jobs[i]
                hq.heappush(waiting_process, temp)
                print("대기열에 추가: ", temp)
                print("waiting_process: ", waiting_process)
                i += 1
            elif time < jobs[i][1]:
                idx = i
                break

        # 2). waiting -> cpu로 옮기는 과정
        if not cpu:
            if waiting_process:
                cpu = hq.heappop(waiting_process)
                print("cpu에 프로세스 추가, ", cpu)

        # 3). cpu -> finish로 옮기는 과정
        else:
            print("cpu가 process 처리중")
            print("cpu: ", cpu)
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