from sys import stdin
from heapq import heappop, heappush
INF = float('inf')
graph, lenv,source,target = None,None,None,None

def solve():
	global graph,lenv,source, target
	visited = [0 for _ in range(lenv)]
	distance = [INF for _ in range(lenv)]
	heap,distance[source] = [(0,source)],0
	while len(heap) and not visited[target]:
		d,u = heappop(heap)
		if not visited[u]:
			visited[u] = 1
			for v,w in graph[u]:
				#duv = distancia de u a v
				duv = d + w
				if not visited[v] and distance[v] > duv:
					#si puedo mejorar la distancia, entonces
					#actualiza el mejor camino con la distancia minima
					distance[v] = duv
					heappush(heap, (duv,v))
	return distance[target]

def main():
	global graph,lenv,source, target
	tcnt = int(stdin.readline().strip()) 
	for tc in range(1,tcnt+1):
		lenv,lene,source,target = map(int, stdin.readline().split())
		graph = [list() for _ in range(lenv)]
		for _ in range(lene):
			u,v,w = map(int,stdin.readline().split())
			if u != v:
				graph[u].append((v,w))
				graph[v].append((u,w))
		ans = solve()
		print("Case #{}: {}".format(tc,ans if ans != INF else "unreachable"))

main()