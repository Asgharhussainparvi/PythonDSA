"""
Graph Implementation in Python
----------------------------
A graph is a data structure that consists of a set of vertices (nodes) and a set of edges
connecting these vertices. This implementation includes both adjacency list and adjacency
matrix representations, along with common graph algorithms.
"""

from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self, directed=False):
        """
        Initialize a graph.
        Args:
            directed (bool): If True, the graph is directed
        """
        self.directed = directed
        self.adj_list = defaultdict(list)  # Adjacency list representation
        self.vertices = set()
        self.edges = []
    
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        Time Complexity: O(1)
        """
        self.vertices.add(vertex)
    
    def add_edge(self, from_vertex, to_vertex, weight=1):
        """
        Add an edge to the graph.
        Time Complexity: O(1)
        """
        self.vertices.add(from_vertex)
        self.vertices.add(to_vertex)
        self.adj_list[from_vertex].append((to_vertex, weight))
        self.edges.append((from_vertex, to_vertex, weight))
        
        if not self.directed:
            self.adj_list[to_vertex].append((from_vertex, weight))
    
    def get_vertices(self):
        """
        Get all vertices in the graph.
        Time Complexity: O(1)
        """
        return list(self.vertices)
    
    def get_edges(self):
        """
        Get all edges in the graph.
        Time Complexity: O(1)
        """
        return self.edges
    
    def get_adjacency_matrix(self):
        """
        Get the adjacency matrix representation of the graph.
        Time Complexity: O(V^2) where V is the number of vertices
        """
        vertices = sorted(list(self.vertices))
        n = len(vertices)
        matrix = [[0] * n for _ in range(n)]
        
        # Create vertex to index mapping
        vertex_to_index = {vertex: i for i, vertex in enumerate(vertices)}
        
        # Fill the matrix
        for from_vertex, to_vertex, weight in self.edges:
            i = vertex_to_index[from_vertex]
            j = vertex_to_index[to_vertex]
            matrix[i][j] = weight
            if not self.directed:
                matrix[j][i] = weight
        
        return matrix, vertices
    
    def bfs(self, start_vertex):
        """
        Perform Breadth-First Search starting from a vertex.
        Time Complexity: O(V + E) where V is vertices and E is edges
        Returns:
            List of vertices in BFS order
        """
        if start_vertex not in self.vertices:
            return []
        
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        bfs_order = []
        
        while queue:
            vertex = queue.popleft()
            bfs_order.append(vertex)
            
            for neighbor, _ in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return bfs_order
    
    def dfs(self, start_vertex):
        """
        Perform Depth-First Search starting from a vertex.
        Time Complexity: O(V + E) where V is vertices and E is edges
        Returns:
            List of vertices in DFS order
        """
        if start_vertex not in self.vertices:
            return []
        
        visited = set()
        dfs_order = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            dfs_order.append(vertex)
            
            for neighbor, _ in self.adj_list[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_vertex)
        return dfs_order
    
    def dijkstra(self, start_vertex):
        """
        Find shortest paths from start_vertex to all other vertices using Dijkstra's algorithm.
        Time Complexity: O((V + E)logV) where V is vertices and E is edges
        Returns:
            Dictionary of shortest distances and paths
        """
        if start_vertex not in self.vertices:
            return {}
        
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0
        paths = {vertex: [] for vertex in self.vertices}
        paths[start_vertex] = [start_vertex]
        
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[current_vertex] + [neighbor]
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances, paths

def main():
    # Create a graph
    graph = Graph(directed=True)
    
    # Add vertices and edges
    print("Creating a directed graph...")
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('E', 'D', 7)
    ]
    
    for from_vertex, to_vertex, weight in edges:
        graph.add_edge(from_vertex, to_vertex, weight)
    
    # Get graph information
    print("\nGraph Information:")
    print(f"Vertices: {graph.get_vertices()}")
    print(f"Edges: {graph.get_edges()}")
    
    # Get adjacency matrix
    matrix, vertices = graph.get_adjacency_matrix()
    print("\nAdjacency Matrix:")
    print("  " + " ".join(vertices))
    for i, row in enumerate(matrix):
        print(f"{vertices[i]} {' '.join(map(str, row))}")
    
    # Perform BFS
    print("\nBFS starting from vertex 'A':")
    bfs_order = graph.bfs('A')
    print(" -> ".join(bfs_order))
    
    # Perform DFS
    print("\nDFS starting from vertex 'A':")
    dfs_order = graph.dfs('A')
    print(" -> ".join(dfs_order))
    
    # Perform Dijkstra's algorithm
    print("\nDijkstra's Shortest Paths from vertex 'A':")
    distances, paths = graph.dijkstra('A')
    for vertex in sorted(distances.keys()):
        if distances[vertex] != float('infinity'):
            print(f"To {vertex}: Distance = {distances[vertex]}, Path = {' -> '.join(paths[vertex])}")
        else:
            print(f"To {vertex}: No path exists")

if __name__ == "__main__":
    main() 