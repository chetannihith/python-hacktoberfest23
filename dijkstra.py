import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

def create_graph():
    graph = {}
    nodes = int(input("Enter the number of nodes in the graph: "))
    for i in range(nodes):
        node = input(f"Enter the label of node {i + 1}: ")
        graph[node] = {}
        while True:
            try:
                edges = int(input(f"Enter the number of edges for node {node}: "))
                break
            except ValueError:
                print("Please enter a valid integer.")
        for j in range(edges):
            while True:
                try:
                    neighbor, weight = input(f"Enter the neighbor and weight for edge {j + 1} (format: neighbor weight): ").split()
                    graph[node][neighbor] = int(weight)
                    break
                except ValueError:
                    print("Please enter valid neighbor and weight values.")
    return graph

if __name__ == "__main__":
    graph = create_graph()
    source_node = input("Enter the source node: ")
    result = dijkstra(graph, source_node)
    print(f"Shortest distances from source node {source_node}: {result}")
