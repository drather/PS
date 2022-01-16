def solution(operations):
    import heapq as hq
    heap = []
    heap2 = []
    for i in range(len(operations)):
        operations[i] = operations[i].split(" ")
        operations[i][1] = int(operations[i][1])

    for op in operations:
        print("\nop: ", op)
        # 삽입
        if op[0] == 'I':
            hq.heappush(heap, op[1])
            print("삽입")
            print("heap : ", heap)

            hq.heappush(heap2, (-op[1], op[1]))

        elif op[0] == 'D' and heap:
            # 최대값 제거
            if op[1] == 1:
                print("최대값 제거")
                print("제거된 값: ", hq.heappop(heap2))

            # 최소값 제거
            else:
                print("최소값 제거")
                print("제거된 값: ", hq.heappop(heap))

    print("heap: ", heap)
    print("heap2: ", heap2)

    answer = []
    while heap and heap2:
        pass

def solution2(operations):
    from _collections import deque

    for i in range(len(operations)):
        operations[i] = operations[i].split(" ")
        operations[i][1] = int(operations[i][1])

    dq = []
    dq = deque(dq)

    for op in operations:
        print("\nop: ", op)
        if op[0] == 'I':
            print("삽입")
            dq.append(op[1])
            print("정렬 전 dq: ", dq)
            print("정렬")
            dq = deque(sorted(dq))
            print("정렬 후 dq: ", dq)

        if op[0] == 'D' and dq:
            if op[1] == 1:
                print("최대값 삭제")
                dq.pop()
                print("dq: ", dq)

            else:
                print("최솟값 삭제")
                dq.popleft()
                print("dq: ", dq)

    print("dq: ", dq)
    if not dq:
        return [0, 0]
    else:
        return [dq[-1], dq[0]]
    print(dq)


operations = ["I -45", "I 653", "D 1", "I -642", "I 97", "I 45", "D 1", "D -1", "I 333"]
print(solution2(operations))