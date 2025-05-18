"""
Maximum Flow Algorithms in Python
------------------------------
This implementation includes the Ford-Fulkerson algorithm with Edmonds-Karp
optimization for finding the maximum flow in a network. The algorithm uses
BFS to find augmenting paths, ensuring polynomial time complexity.
"""

from collections import defaultdict, deque

class MaxFlow:
    def __init__(self, graph):
        """
        Initialize with a graph.
        Args:
            graph: Graph object with vertices and edges
        """
        self.graph = graph
        self.vertices = graph.get_vertices()
        self.adj_list = graph.adj_list
        self.residual_graph = defaultdict(dict)
        self.initialize_residual_graph()
    
    def initialize_residual_graph(self):
        """
        Initialize the residual graph with forward and backward edges.
        """
        # Add forward edges
        for vertex in self.vertices:
            for neighbor, capacity in self.adj_list[vertex]:
                self.residual_graph[vertex][neighbor] = capacity
                # Initialize backward edge with 0 capacity
                if neighbor not in self.residual_graph:
                    self.residual_graph[neighbor] = {}
                self.residual_graph[neighbor][vertex] = 0
    
    def bfs_augmenting_path(self, source, sink):
        """
        Find an augmenting path using BFS.
        Returns:
            Tuple of (path, min_capacity) or (None, 0) if no path exists
        """
        parent = {source: None}
        min_capacity = {source: float('inf')}
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            
            for neighbor, capacity in self.residual_graph[current].items():
                if capacity > 0 and neighbor not in parent:
                    parent[neighbor] = current
                    min_capacity[neighbor] = min(min_capacity[current], capacity)
                    
                    if neighbor == sink:
                        # Reconstruct path
                        path = []
                        current = sink
                        while current is not None:
                            path.append(current)
                            current = parent[current]
                        return path[::-1], min_capacity[sink]
                    
                    queue.append(neighbor)
        
        return None, 0
    
    def ford_fulkerson(self, source, sink):
        """
        Find maximum flow using Ford-Fulkerson algorithm with Edmonds-Karp optimization.
        Time Complexity: O(VE²) where V is vertices and E is edges
        Args:
            source: Source vertex
            sink: Sink vertex
        Returns:
            Maximum flow value and flow network
        """
        max_flow = 0
        flow_network = defaultdict(dict)
        
        # Initialize flow network
        for vertex in self.vertices:
            for neighbor in self.residual_graph[vertex]:
                flow_network[vertex][neighbor] = 0
        
        while True:
            # Find augmenting path
            path, min_capacity = self.bfs_augmenting_path(source, sink)
            
            if path is None:
                break
            
            # Update residual graph and flow network
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                # Update residual capacities
                self.residual_graph[u][v] -= min_capacity
                self.residual_graph[v][u] += min_capacity
                # Update flow network
                flow_network[u][v] += min_capacity
            
            max_flow += min_capacity
        
        return max_flow, flow_network

def main():
    # Create a directed graph
    from graphs import Graph
    graph = Graph(directed=True)
    
    # Example 1: Simple flow network
    print("Example 1: Simple Flow Network")
    print("-" * 50)
    edges1 = [
        ('S', 'A', 10),
        ('S', 'B', 8),
        ('A', 'C', 4),
        ('A', 'D', 2),
        ('B', 'C', 9),
        ('B', 'D', 9),
        ('C', 'T', 10),
        ('D', 'T', 10)
    ]
    
    graph1 = Graph(directed=True)
    for from_vertex, to_vertex, capacity in edges1:
        graph1.add_edge(from_vertex, to_vertex, capacity)
    
    max_flow1 = MaxFlow(graph1)
    flow_value1, flow_network1 = max_flow1.ford_fulkerson('S', 'T')
    
    print(f"Maximum Flow: {flow_value1}")
    print("\nFlow Network:")
    for vertex in sorted(flow_network1.keys()):
        for neighbor, flow in flow_network1[vertex].items():
            if flow > 0:
                print(f"{vertex} -> {neighbor}: {flow}")
    
    # Example 2: More complex flow network
    print("\nExample 2: Complex Flow Network")
    print("-" * 50)
    edges2 = [
        ('S', 'A', 16),
        ('S', 'B', 13),
        ('A', 'B', 10),
        ('A', 'C', 12),
        ('B', 'A', 4),
        ('B', 'C', 14),
        ('B', 'D', 9),
        ('C', 'D', 7),
        ('C', 'T', 20),
        ('D', 'C', 6),
        ('D', 'T', 4)
    ]
    
    graph2 = Graph(directed=True)
    for from_vertex, to_vertex, capacity in edges2:
        graph2.add_edge(from_vertex, to_vertex, capacity)
    
    max_flow2 = MaxFlow(graph2)
    flow_value2, flow_network2 = max_flow2.ford_fulkerson('S', 'T')
    
    print(f"Maximum Flow: {flow_value2}")
    print("\nFlow Network:")
    for vertex in sorted(flow_network2.keys()):
        for neighbor, flow in flow_network2[vertex].items():
            if flow > 0:
                print(f"{vertex} -> {neighbor}: {flow}")

if __name__ == "__main__":
    main() 