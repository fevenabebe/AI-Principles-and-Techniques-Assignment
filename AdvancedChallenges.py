import heapq
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

def block_road(roads, city1, city2):
    """Blocks the road between city1 and city2."""
    if city1 in roads and city2 in roads[city1]:
        roads[city1] = [(c, d) for c, d in roads[city1] if c != city2]
    if city2 in roads and city1 in roads[city2]:
        roads[city2] = [(c, d) for c, d in roads[city2] if c != city1]

def unblock_road(roads, city1, city2, distance):
    """Unblocks the road between city1 and city2."""
    roads[city1].append((city2, distance))
    roads[city2].append((city1, distance))

def k_shortest_paths(roads, start_city, goal_city, k):
    """Finds the k shortest paths from start_city to goal_city."""
    # Using a priority queue to store paths
    pq = []
    heapq.heappush(pq, (0, [start_city]))  # (cost, path)
    paths = []

    while pq and len(paths) < k:
        cost, path = heapq.heappop(pq)
        current_city = path[-1]

        if current_city == goal_city:
            paths.append((path, cost))
            continue

        for neighbor, distance in roads[current_city]:
            if neighbor not in path:  # Avoid cycles
                heapq.heappush(pq, (cost + distance, path + [neighbor]))

    return paths

# Example usage
start_city = 'Addis Ababa'
bfs_path, bfs_cost = traverse_all_cities(cities, roads, start_city, 'bfs')
print("BFS Path:", bfs_path, "with cost:", bfs_cost)

# Block a road and show how it affects traversal
block_road(roads, 'Addis Ababa', 'Hawassa')
bfs_path_after_block, bfs_cost_after_block = traverse_all_cities(cities, roads, start_city, 'bfs')
print("BFS Path after blocking road:", bfs_path_after_block, "with cost:", bfs_cost_after_block)

# Find k shortest paths from Addis Ababa to Mekelle
k = 2
shortest_paths = k_shortest_paths(roads, 'Addis Ababa', 'Mekelle', k)
for idx, (path, cost) in enumerate(shortest_paths):
    print(f"Path {idx + 1}: {path} with cost: {cost}")