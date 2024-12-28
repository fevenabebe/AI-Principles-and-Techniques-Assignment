import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# City data
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    if strategy == 'bfs':
        return bfs_path_finder(roads, start_city, goal_city)
    elif strategy == 'dfs':
        return dfs_path_finder(roads, start_city, goal_city)
    else:
        raise ValueError("Strategy must be 'bfs' or 'dfs'.")

def bfs_path_finder(roads, start_city, goal_city):
    queue = deque([(start_city, [start_city])])
    visited = set()

    while queue:
        current_city, path = queue.popleft()
        if current_city == goal_city:
            return path, len(path) - 1  # cost is the number of steps
        visited.add(current_city)

        for neighbor, _ in roads[current_city]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, 0  # No path found

def dfs_path_finder(roads, start_city, goal_city):
    stack = [(start_city, [start_city])]
    visited = set()

    while stack:
        current_city, path = stack.pop()
        if current_city == goal_city:
            return path, len(path) - 1  # cost is the number of steps
        visited.add(current_city)

        for neighbor, _ in roads[current_city]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None, 0  # No path found

# Example usage
start_city = 'Addis Ababa'
goal_city = 'Mekelle'
bfs_path, bfs_cost = uninformed_path_finder(cities, roads, start_city, goal_city, 'bfs')
dfs_path, dfs_cost = uninformed_path_finder(cities, roads, start_city, goal_city, 'dfs')

print("BFS Path:", bfs_path, "Cost:", bfs_cost)
print("DFS Path:", dfs_path, "Cost:", dfs_cost)

# Visualization using NetworkX
def visualize_graph(roads, path=None):
    G = nx.Graph()
    
    for city, connections in roads.items():
        for connected_city, distance in connections:
            G.add_edge(city, connected_city, weight=distance)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')

    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Ethiopia Road Network")
    plt.show()

# Visualize the BFS path
visualize_graph(roads, bfs_path)