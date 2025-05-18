"""
Minimum Spanning Tree (MST) Algorithms in Python
--------------------------------------------
This implementation includes both Kruskal's and Prim's algorithms for finding
the minimum spanning tree of a graph. A minimum spanning tree is a subset of
edges that connects all vertices with the minimum possible total edge weight.
"""

from collections import defaultdict
import heapq

class DisjointSet:
    """
    Disjoint Set data structure for Kruskal's algorithm.
    Used to efficiently manage connected components.
    """
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}
    
    def find(self, vertex):
        """
        Find the root of the set containing vertex.
        Uses path compression for efficiency.
        """
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, vertex1, vertex2):
        """
        Union the sets containing vertex1 and vertex2.
        Uses union by rank for efficiency.
        """
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if root1 == root2:
            return
        
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

class MST:
    def __init__(self, graph):
        """
        Initialize MST algorithms with a graph.
        Args:
            graph: Graph object with vertices and edges
        """
        self.graph = graph
        self.vertices = graph.get_vertices()
        self.edges = graph.get_edges()
    
    def kruskal(self):
        """
        Find MST using Kruskal's algorithm.
        Time Complexity: O(E log E) where E is the number of edges
        Returns:
            List of edges in the MST and total weight
        """
        # Sort edges by weight
        sorted_edges = sorted(self.edges, key=lambda x: x[2])
        
        # Initialize disjoint set
        ds = DisjointSet(self.vertices)
        
        mst_edges = []
        total_weight = 0
        
        for from_vertex, to_vertex, weight in sorted_edges:
            # Check if adding this edge creates a cycle
            if ds.find(from_vertex) != ds.find(to_vertex):
                mst_edges.append((from_vertex, to_vertex, weight))
                total_weight += weight
                ds.union(from_vertex, to_vertex)
        
        return mst_edges, total_weight
    
    def prim(self, start_vertex=None):
        """
        Find MST using Prim's algorithm.
        Time Complexity: O((V + E) log V) where V is vertices and E is edges
        Args:
            start_vertex: Optional starting vertex. If None, uses first vertex
        Returns:
            List of edges in the MST and total weight
        """
        if not self.vertices:
            return [], 0
        
        if start_vertex is None:
            start_vertex = self.vertices[0]
        
        # Initialize data structures
        visited = set([start_vertex])
        mst_edges = []
        total_weight = 0
        
        # Priority queue for edges (weight, from_vertex, to_vertex)
        edges = []
        for neighbor, weight in self.graph.adj_list[start_vertex]:
            heapq.heappush(edges, (weight, start_vertex, neighbor))
        
        while edges and len(visited) < len(self.vertices):
            weight, from_vertex, to_vertex = heapq.heappop(edges)
            
            if to_vertex not in visited:
                visited.add(to_vertex)
                mst_edges.append((from_vertex, to_vertex, weight))
                total_weight += weight
                
                # Add new edges to priority queue
                for neighbor, weight in self.graph.adj_list[to_vertex]:
                    if neighbor not in visited:
                        heapq.heappush(edges, (weight, to_vertex, neighbor))
        
        return mst_edges, total_weight

def main():
    # Create a graph
    from graphs import Graph
    graph = Graph(directed=False)
    
    # Add vertices and edges (example from a common MST problem)
    print("Creating an undirected graph...")
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('E', 'F', 5),
        ('D', 'F', 6),
        ('B', 'F', 2)
    ]
    
    for from_vertex, to_vertex, weight in edges:
        graph.add_edge(from_vertex, to_vertex, weight)
    
    # Create MST object
    mst = MST(graph)
    
    # Find MST using Kruskal's algorithm
    print("\nKruskal's Algorithm:")
    print("-" * 30)
    kruskal_edges, kruskal_weight = mst.kruskal()
    print("MST Edges:")
    for from_vertex, to_vertex, weight in kruskal_edges:
        print(f"{from_vertex} -- {weight} -- {to_vertex}")
    print(f"Total Weight: {kruskal_weight}")
    
    # Find MST using Prim's algorithm
    print("\nPrim's Algorithm:")
    print("-" * 30)
    prim_edges, prim_weight = mst.prim()
    print("MST Edges:")
    for from_vertex, to_vertex, weight in prim_edges:
        print(f"{from_vertex} -- {weight} -- {to_vertex}")
    print(f"Total Weight: {prim_weight}")
    
    # Verify that both algorithms give the same total weight
    print("\nVerification:")
    print(f"Kruskal's total weight: {kruskal_weight}")
    print(f"Prim's total weight: {prim_weight}")
    print(f"Algorithms agree: {kruskal_weight == prim_weight}")

if __name__ == "__main__":
    main() 