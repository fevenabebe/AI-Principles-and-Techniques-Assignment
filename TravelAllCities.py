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

def traverse_all_cities(cities, roads, start_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').
    
    Returns:
    - path: List of cities representing the traversal path.
    - cost: Total cost (distance) of the traversal.
    """
    if strategy == 'bfs':
        return bfs_traverse(roads, start_city)
    elif strategy == 'dfs':
        return dfs_traverse(roads, start_city)
    else:
        raise ValueError("Strategy must be 'bfs' or 'dfs'.")

def bfs_traverse(roads, start_city):
    queue = deque([start_city])
    visited = set([start_city])
    path = []
    total_cost = 0

    while queue:
        current_city = queue.popleft()
        path.append(current_city)

        for neighbor, distance in roads[current_city]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                total_cost += distance  # Add distance for each edge traversed

    return path, total_cost

def dfs_traverse(roads, start_city):
    stack = [start_city]
    visited = set([start_city])
    path = []
    total_cost = 0

    def dfs(city):
        nonlocal total_cost
        path.append(city)

        for neighbor, distance in roads[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                total_cost += distance
                dfs(neighbor)  # Recursive DFS call

    dfs(start_city)
    return path, total_cost

# Example usage
start_city = 'Addis Ababa'
bfs_path, bfs_cost = traverse_all_cities(cities, roads, start_city, 'bfs')

print("BFS Path:", bfs_path, "with cost:", bfs_cost)