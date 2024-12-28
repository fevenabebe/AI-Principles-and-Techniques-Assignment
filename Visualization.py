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

def bfs_path_finder(roads, start_city, goal_city):
    queue = deque([(start_city, [start_city])])
    visited = set()

    while queue:
        current_city, path = queue.popleft()
        if current_city == goal_city:
            return path  # Return the path found
        visited.add(current_city)

        for neighbor, _ in roads[current_city]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found

# Example usage
start_city = 'Addis Ababa'
goal_city = 'Mekelle'
path = bfs_path_finder(roads, start_city, goal_city)

print("Path found:", path)

# Visualization using NetworkX
def visualize_graph(roads, path=None):
    G = nx.Graph()
    
    # Add edges to the graph
    for city, connections in roads.items():
        for connected_city, distance in connections:
            G.add_edge(city, connected_city, weight=distance)

    pos = nx.spring_layout(G)  # Positioning nodes
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')

    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Ethiopia Road Network")
    plt.show()

# Visualize the graph and highlight the path
visualize_graph(roads, path)