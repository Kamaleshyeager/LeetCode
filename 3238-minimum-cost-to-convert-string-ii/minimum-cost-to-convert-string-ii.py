from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], 
                    changed: List[str], cost: List[int]) -> int:
        # Build graph
        graph = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            graph[o].append((w, c))
        
        # Memoized Dijkstra
        shortest_cache = {}
        
        def get_shortest_path(start):
            if start in shortest_cache:
                return shortest_cache[start]
            
            dist = {start: 0}
            pq = [(0, start)]
            visited = set()
            
            while pq:
                d, u = heapq.heappop(pq)
                if u in visited:
                    continue
                visited.add(u)
                
                for w, v in graph[u]:
                    new_dist = d + w
                    if v not in visited and (v not in dist or new_dist < dist[v]):
                        dist[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))
            
            shortest_cache[start] = dist
            return dist
        
        # DP
        n = len(source)
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        # Valid lengths
        all_strings = set(original) | set(changed)
        valid_lengths = {len(s) for s in all_strings}
        
        for i in range(n):
            if dp[i] >= INF:
                continue
            
            # No transformation
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            
            # Try transformations
            for L in valid_lengths:
                j = i + L
                if j > n:
                    continue
                
                s_sub = source[i:j]
                t_sub = target[i:j]
                
                # Lazy Dijkstra computation
                if s_sub in all_strings:
                    dist = get_shortest_path(s_sub)
                    if t_sub in dist:
                        dp[j] = min(dp[j], dp[i] + dist[t_sub])
        
        return dp[n] if dp[n] < INF else -1