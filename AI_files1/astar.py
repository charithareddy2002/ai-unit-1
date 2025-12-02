# A* Search Algorithm Implementation

from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 7)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 3,
    'F': 2,
    'G': 0
}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    cost = {start: 0}

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            print("Goal Reached:", goal)
            return

        print(current, end=" ")

        for next_node, weight in graph[current]:
            new_cost = cost[current] + weight
            if next_node not in cost or new_cost < cost[next_node]:
                cost[next_node] = new_cost
                priority = new_cost + heuristic[next_node]
                pq.put((priority, next_node))

# Driver Code
print("A* Path:")
astar('A', 'G')
