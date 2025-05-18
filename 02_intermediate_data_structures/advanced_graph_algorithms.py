"""
Advanced Graph Algorithms in Python
--------------------------------
This implementation includes:
1. Kosaraju's algorithm for finding Strongly Connected Components (SCC)
2. Topological Sort using DFS
These algorithms are fundamental for analyzing directed graphs and their properties.
"""

from collections import defaultdict, deque

class AdvancedGraphAlgorithms:
    def __init__(self, graph):
        """
        Initialize with a graph.
        Args:
            graph: Graph object with vertices and edges
        """
        self.graph = graph
        self.vertices = graph.get_vertices()
        self.adj_list = graph.adj_list
    
    def _reverse_graph(self):
        """
        Create a reversed version of the graph.
        Returns:
            Dictionary representing the reversed adjacency list
        """
        reversed_adj = defaultdict(list)
        for vertex in self.vertices:
            for neighbor, weight in self.adj_list[vertex]:
                reversed_adj[neighbor].append((vertex, weight))
        return reversed_adj
    
    def _dfs_first_pass(self, vertex, visited, order):
        """
        First DFS pass for Kosaraju's algorithm.
        Fills the order stack with vertices in order of finishing times.
        """
        visited.add(vertex)
        for neighbor, _ in self.adj_list[vertex]:
            if neighbor not in visited:
                self._dfs_first_pass(neighbor, visited, order)
        order.append(vertex)
    
    def _dfs_second_pass(self, vertex, visited, component, reversed_adj):
        """
        Second DFS pass for Kosaraju's algorithm.
        Finds all vertices in the current strongly connected component.
        """
        visited.add(vertex)
        component.append(vertex)
        for neighbor, _ in reversed_adj[vertex]:
            if neighbor not in visited:
                self._dfs_second_pass(neighbor, visited, component, reversed_adj)
    
    def find_scc(self):
        """
        Find all strongly connected components using Kosaraju's algorithm.
        Time Complexity: O(V + E) where V is vertices and E is edges
        Returns:
            List of lists, where each inner list represents a strongly connected component
        """
        # First DFS pass to get the order
        visited = set()
        order = []
        for vertex in self.vertices:
            if vertex not in visited:
                self._dfs_first_pass(vertex, visited, order)
        
        # Second DFS pass on reversed graph
        reversed_adj = self._reverse_graph()
        visited = set()
        scc_list = []
        
        # Process vertices in reverse order of finishing times
        for vertex in reversed(order):
            if vertex not in visited:
                component = []
                self._dfs_second_pass(vertex, visited, component, reversed_adj)
                scc_list.append(component)
        
        return scc_list
    
    def _dfs_topological(self, vertex, visited, temp_visited, order):
        """
        Helper function for topological sort using DFS.
        Returns True if a cycle is detected.
        """
        visited.add(vertex)
        temp_visited.add(vertex)
        
        for neighbor, _ in self.adj_list[vertex]:
            if neighbor not in visited:
                if self._dfs_topological(neighbor, visited, temp_visited, order):
                    return True
            elif neighbor in temp_visited:
                return True
        
        temp_visited.remove(vertex)
        order.appendleft(vertex)
        return False
    
    def topological_sort(self):
        """
        Perform topological sort using DFS.
        Time Complexity: O(V + E) where V is vertices and E is edges
        Returns:
            List of vertices in topological order, or None if graph has cycles
        """
        visited = set()
        temp_visited = set()
        order = deque()
        
        for vertex in self.vertices:
            if vertex not in visited:
                if self._dfs_topological(vertex, visited, temp_visited, order):
                    return None  # Graph has cycles
        
        return list(order)

def main():
    # Create a directed graph
    from graphs import Graph
    graph = Graph(directed=True)
    
    # Example 1: Graph with SCCs
    print("Example 1: Finding Strongly Connected Components")
    print("-" * 50)
    edges1 = [
        ('A', 'B', 1),
        ('B', 'C', 1),
        ('C', 'A', 1),
        ('B', 'D', 1),
        ('D', 'E', 1),
        ('E', 'F', 1),
        ('F', 'D', 1),
        ('G', 'F', 1),
        ('G', 'H', 1),
        ('H', 'I', 1),
        ('I', 'J', 1),
        ('J', 'G', 1)
    ]
    
    graph1 = Graph(directed=True)
    for from_vertex, to_vertex, weight in edges1:
        graph1.add_edge(from_vertex, to_vertex, weight)
    
    scc = AdvancedGraphAlgorithms(graph1)
    scc_components = scc.find_scc()
    
    print("Strongly Connected Components:")
    for i, component in enumerate(scc_components, 1):
        print(f"Component {i}: {' -> '.join(component)}")
    
    # Example 2: DAG for Topological Sort
    print("\nExample 2: Topological Sort")
    print("-" * 50)
    edges2 = [
        ('A', 'B', 1),
        ('A', 'C', 1),
        ('B', 'D', 1),
        ('C', 'D', 1),
        ('D', 'E', 1),
        ('E', 'F', 1),
        ('G', 'E', 1)
    ]
    
    graph2 = Graph(directed=True)
    for from_vertex, to_vertex, weight in edges2:
        graph2.add_edge(from_vertex, to_vertex, weight)
    
    topo = AdvancedGraphAlgorithms(graph2)
    topo_order = topo.topological_sort()
    
    if topo_order:
        print("Topological Order:")
        print(" -> ".join(topo_order))
    else:
        print("Graph contains cycles, topological sort not possible")
    
    # Example 3: Graph with cycles (should fail topological sort)
    print("\nExample 3: Graph with Cycles")
    print("-" * 50)
    edges3 = [
        ('A', 'B', 1),
        ('B', 'C', 1),
        ('C', 'A', 1)  # Creates a cycle
    ]
    
    graph3 = Graph(directed=True)
    for from_vertex, to_vertex, weight in edges3:
        graph3.add_edge(from_vertex, to_vertex, weight)
    
    topo_cycle = AdvancedGraphAlgorithms(graph3)
    topo_order_cycle = topo_cycle.topological_sort()
    
    if topo_order_cycle:
        print("Topological Order:")
        print(" -> ".join(topo_order_cycle))
    else:
        print("Graph contains cycles, topological sort not possible")

if __name__ == "__main__":
    main()