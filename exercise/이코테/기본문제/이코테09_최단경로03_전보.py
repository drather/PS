import heapq

city_num, link_num, start_city = map(int, input().split())

graph = [[] for _ in range(city_num+1)]


for _ in range(link_num):
    src, trg, wgt = map(int, input().split())

    graph[src].append((trg, wgt))

INF = int(1e9)
distances = [INF] * (city_num+1)
distances[start_city] = 0

def dijkstra(start):
    pq = []
    
    heapq.heappush(pq, (0, start))
    
    while pq:
        distance, current_node = heapq.heappop(pq)
        print(f"current_node, weight : {current_node}, {distance}")

        if distances[current_node] < distance:
            print("이미 처리된 노드")
            continue

        for adj_city, adj_weight in graph[current_node]:
            new_weight = distances[current_node] + adj_weight
            print(f"new_weight, 기존 distance: {new_weight}, {distances[adj_city]}")

            if new_weight < distances[adj_city]:
                distances[adj_city] = new_weight

                heapq.heappush(pq, (new_weight, adj_city))


dijkstra(start_city)

num_of_cities = len([d for d in distances[1:] if 0 < d < INF])
time = (max(distances[1:]))

print(num_of_cities, time)
