import heapq
import time

class NetworkAnalyzer:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight)) 

    def find_shortest_path(self, start, target):
        start_time = time.time()
        
  
        pq = [(0, start)]
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        
        while pq:
            current_dist, current_node = heapq.heappop(pq)
            
            if current_node == target:
                break
                
            if current_dist > distances[current_node]:
                continue
                
            for neighbor, weight in self.graph.get(current_node, []):
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
                    
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        
        return distances.get(target, float('inf')), execution_time_ms


if __name__ == "__main__":
    analyzer = NetworkAnalyzer()
    

    analyzer.add_edge("Server_A", "Server_B", 4)
    analyzer.add_edge("Server_A", "Server_C", 2)
    analyzer.add_edge("Server_C", "Server_B", 1)
    analyzer.add_edge("Server_B", "Server_D", 5)
    analyzer.add_edge("Server_C", "Server_D", 8)
    
    target_distance, latency = analyzer.find_shortest_path("Server_A", "Server_D")
    
    print(f"Optimal Path Cost: {target_distance}")
    print(f"Query Latency: {latency:.4f} ms")