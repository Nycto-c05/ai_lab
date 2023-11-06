# Define a graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  # Create a set to keep track of visited nodes

def dfs(node):
    if node not in visited:
        print(node)  # Process the current node
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)  # Recursively visit unvisited neighbors

# Start DFS from an initial node (e.g., 'A')
initial_node = 'A'
dfs(initial_node)
