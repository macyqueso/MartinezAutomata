#SHORTEST PATH IN A WEIGHTED GRAPH

import heapq

def astar_graph(graph, heuristic, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph.get(current, []):
            tentative_g = g_score[current] + cost
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic.get(neighbor, 0)
                heapq.heappush(open_set, (f, neighbor))
                came_from[neighbor] = current
    return None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}
heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

path = astar_graph(graph, heuristic, 'A', 'D')
print("Path:", path)