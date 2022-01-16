"""
num 을 1부터 쭉 증가시키면서, num이 false가 되는 순간의 값을 return한다
동적 계획법을 사용할 것이다
num = 1 일때, 1이 weights에 있는지 확인한다.
    있으면 dp[1]을 true로 하고, 없다면 dp[1]을 false로 한다.
    dp[1]이 false라면, 1을 리턴한다.
    그렇지 않다면, num을 1 증가시킨다

num = 2 일 때, 2이 weight에 있는 지 확인한다.
    있으면 dp[2]를 true로 하고,없다면 dp[1]로 num을 만들 수 있는 지를 확인한다.
    근데 추가 있으므로, dp[2]를 true로 하고 num을 1 증가시킨다.

num = 3 일 때, 3이 weight에 있는 지 확인한다.
    있으니까 dp[3] = true

num = 4 일 때, 4가 weight에 있는지 확인한다.
    없다 -> dp[3] 과 dp[1]이 참인지 확인한다.
    둘다 참 -> dp[4]도 참

num = 5 일 때, 이건 weight에 없다
    dp[4], dp[1]이 참인지 본다.
    참 -> dp[5] 도 true

num = 6 , dp[6] = true

num = 7, 있음, dp[7] = true

num = 8, 없음
    dp[7] = true, dp[1] = true -> true

num = 9, 없음
    dp[8] = true, dp[1] = true

num = 10, 없음
    dp[9] = true, dp[1] = true
----------------------------------------
생각을 해보자
11을 맞춰야 한다. 11이 weight에 있는지 보자. 이 반복은, 인덱스가 0 이상인 동안만 반복한다.
    있으면 끝, dp[11] = true, break
    없다면, 11보다 작으면서 가장 큰 추를 놓는다. a라 하자.
        11 - a = b 라 하자. b가 0이 아니라면, b를 맞춰야 한다.
        b가 weight에 있다면 끝, dp[11] = True, break
        없다면, b보다 작으면서 가장 큰 수를 c라 하자.
            b - c = d 라 하자. d가 0이라면 끝, dp[11] = true
b - c

다시 생각해보자. num을 맞춰야 한다.
num은 1부터 계속 증가한다. (while문 사용)
    dp[num] = False
    num이 weight에 있는가?
        있으면,
            dp[num] = true,
            num += 1
            continue
        없으면, weight배열을 순회하는 인덱스가 0보다 큰 동안
            temp = num보다 작은 제일 큰 추
            a = num - temp
            dp[a]가 true인가?
                true면,
                    dp[num] = true
                아니면,
                    num = temp
                    temp = a보다 작으면서 가장 큰 추

    if dp[num] == False:
        return num


이런식으로 dp배열을 1부터 하다가, false가 되는 순간에 num을 리턴
고려할 점: graph를 deepcopy하던가 해서, 갯수에 대한 정보까지 가져야 한다.
존내 어렵넹 ㅋ
"""


# 아이디어는 좋았으나 실패 ㅋ
def solution(weights):
    weights.sort()
    print("weights: ", weights)
    graph = {}
    for w in weights:
        if w not in list(graph.keys()):
            graph[w] = 1
        else:
            graph[w] += 1
    print("graph: ", graph)

    dp = [-1]
    num = 1

    while True:
        dp.append(False)
        print("\nnum: ", num)
        if num in weights:
            print("num만큼의 무게 가진 추 있음")
            dp[num] = True
            num += 1
            print("dp: ", dp)
            continue

        else:
            temp = -1
            for i in range(num-1, 0, -1):
                if i in weights:
                    temp = i
                    print("처음 정해진 temp: ", temp)
                    break

            if temp == -1:
                print(num, "만큼의 추도 없고, 그보다 작은 추도 없음, 만들수 없다")
                return num

            origin = num
            while True:
                print("--반복 시작할 것--")
                print("num: ", origin)
                print("temp: ", temp)
                rest = origin - temp
                print("Rest: ", rest)
                print("Test: ", dp[temp], dp[rest])
                print("dp: ", dp)
                if dp[temp] == True and dp[rest] == True:
                    dp[num] = True
                    break
                else:
                    print(temp, rest, "로는 ", origin, "만들 수 없음, 다시 반복")
                    origin = temp
                    temp = rest

        print("test, num: ", num)
        if dp[num] == False:
            print("num 찾음, 정답: ", num)
            return num

        else:
            print("num 만들 수 있음, num 1 증가")

        num += 1
    print("dp: ", dp)


# dp배열이 각 num을 맞추는데 필요한 동전에 대한 정보를 가지면 어떨까
"""
다시 생각을 해보자.
dp = [-1, ]이다. 이 뒤로, 각 인덱스마다 그 인덱스값 만큼을 구성하기 위한 조합이 배열로 들어갈 것이다. 

num = 1 
while문을 통해 반복한다. 일단은 무한히 반복한다.
    dp.append([]) 
    만약 num만큼의 추가 weights에 있다면, 
        dp[num].append(num)
        num += 1
        continue
    
    그렇지 않다면, 
        아래를 반복한다. 
            0. sub_graph = copy.deepcopy(graph)
            1. num보다 작은 최대의 추를 찾아서, largest에 저장한다.
            2. num - largest를 rest에 저장한다. 
            이제, dp[rest]를 확인한다. (이 만큼만 채우면 된다)
                dp[rest]
"""

"""
다시다시, 생각해보자 
num = 1 부터 증가할 것
while을 통해 반복한다.
    dp.append([]) 
    만약 num만큼의 추가 weights에 있다면, 
        dp[num].append(num)
        num += 1
        continue
        
    아니라면, num보다 작은 가장 큰 추를 찾는다
    거기부터 역순으로 순회하면서, largest보다 작은 원소를 찾아서 더해본다. 
        largest의 인덱스를 i라 하자. largest + weight[i-1]를 더해서 sum에 저장한다.
        sum이 num보다 크다면, 그냥 넘어간다.
        sum이 num과 같다면, num을 1 증가시키고 새로운 반복을 시행한다.
        sum이 num보다 작다면, 또 더한다. 
            
        # sum += weights[i]
        # if sum > num:
        #    return num
        # elif sum == num:
        #     num += 1
        #     break

"""


def solution2(weights):
    weights.sort()
    print("weights: ", weights)

    num = 1
    while True:
        print("\nnum: ", num)
        if num in weights:
            print("num만큼의 값을 가진 추가 있음")
            num += 1
            continue

        # 다른 조합 찾는 부분
        else:
            # largest를 찾아야 한다.
            largest = 0
            for i in range(num-1, 0, -1):
                if i in weights:
                    largest = i
                    break
            print("largest: ", largest)

            # 이제, largest의 인덱스를 구한다
            largest_index = weights.index(largest)
            print("largest_index: ", largest_index)

            total = largest
            temp_weight = weights[:largest_index]
            print("temp_weight: ", temp_weight)
            for i in range(len(temp_weight)-1, -1, -1):
                print("\ni: ", i)
                print("더하기 전 total: ", total)
                print("temp_weight[i]: ", temp_weight[i])
                if total + temp_weight[i] > num:
                    print("total + temp_weight[i]가 num보다 큼, 합산 안함")
                elif total + temp_weight[i] == num:
                    print("total + temp_weight[i]이 num과 같음, 다음 반복 진행")
                    total += temp_weight[i]
                    break
                else:
                    print("total + temp_weight[i]가 num보다 작음, 합산 함")
                    total += temp_weight[i]

            print("total, num: ", total, num)
            if total != num:
                return num
        num += 1


def solution2(weights):
    weights.sort()
    sum_set = set()
    sum_list = []
    temp = 0
    for i in range(len(weights)):
        added_list = []
        print("\ni: ", i, ", weights[i]: ", weights[i])
        print("1회 반복 전 sum_set: ", sum_set)

        if i == 0:
            sum_set.add(weights[i])
            continue

        else:
            sum_list = list(sum_set)
            previous_sum_list_max = sum_list[-1]

            for j in range(len(sum_list)):
                added_list.append(sum_list[j] + weights[i])

        sum_list = list(sum_set)
        print("1회 반복 후 sum_set: ", sum_set)
        print("1회 반복 후 sum_list: ", sum_list)
        print("1회 반복 후 added_list: ", added_list)

        print("previous_sum_list_max: ", previous_sum_list_max)
        print("added_list[0]: ", added_list[0])
        if len(sum_list) >= 2 and previous_sum_list_max + 1 < added_list[0]:
            return previous_sum_list_max + 1


def sol3(weights):
    weights.sort()
    sum_set = set()
    temp1 = -1
    temp2 = -1
    for i in range(len(weights)):
        print("\ni: ", i)
        added_list = [weights[i]]
        if i == 0:
            sum_set.add(weights[i])
            continue

        else:
            sum_list = list(sum_set)
            print("sum_list: ", sum_list)
            temp1 = sum_list[-1]

            for j in range(len(sum_list)):
                added_list.append(sum_list[j] + weights[i])
            sum_set.add(weights[i])
            sum_set.update(added_list)
            temp2 = added_list[0]

            print("added_list: ", added_list)
            print("Temp1: ", temp1)
            print("temp2: ", temp2)

            if temp2 > temp1 + 1:
                return temp1 + 1

    return added_list[-1]+1


def sol4(weights):
    weights.sort()
    sum_set = set()
    temp1 = -1
    temp2 = -1
    
    for i in range(len(weights)):
        print("\ni: ", i)
        added_list = [weights[i]]
        if i == 0:
            sum_set.add(weights[i])
            continue

        else:
            sum_list = list(sum_set)
            print("sum_list: ", sum_list)
            temp1 = sum_list[-1]

            for j in range(len(sum_list)):
                added_list.append(sum_list[j] + weights[i])
            sum_set.add(weights[i])
            sum_set.update(added_list)
            temp2 = added_list[0]

            print("added_list: ", added_list)
            print("Temp1: ", temp1)
            print("temp2: ", temp2)

            if temp2 > temp1 + 1:
                return temp1 + 1

    return added_list[-1]+1


def sol5(weights):
    weights.sort()
    print("weights: ", weights)
    temp = weights[0]
    for i in range(1, len(weights)):
        if weights[i] - temp > 1:
            return temp+1
        else:
            temp += weights[i]

weights = [3, 1, 6, 2, 7, 30, 1]
print("정답: ", sol5(weights))