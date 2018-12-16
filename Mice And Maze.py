from sys import stdin
from heapq import heappop, heappush

INF = float('inf')

def dijkstra(G, s):
	ans = [INF for _ in G]; ans[s] = 0
	#prev = [None for _ in G]
	visited = [False for _ in G]
	heap = [(0,s)]
	while (len(heap)): # O (|E|)
		d,u = heappop(heap) # O (log |E|)
		if visited[u] == False:
			for v,dv in G[u]:
				if d+dv< ans[v]:
					ans[v] = d+dv
					heappush(heap, (ans[v],v))
			visited[u] = True
	return ans

def main():
	cnt = 0
	cases = int(stdin.readline().strip())
	for i in range(cases):
		stdin.readline()
		celdas = int(stdin.readline().strip())
		goal = int(stdin.readline().strip())
		limit = int(stdin.readline().strip())
		grafo = [[] for _ in range(celdas)]
		lines = int(stdin.readline().strip())
		for i in range(lines):
			u,v,d = map(int,stdin.readline().split())
			grafo[v-1].append((u-1,d))
		paths = dijkstra(grafo,goal-1)
		ans= 0
		for i in paths:
			if i<=limit:
				ans+=1		
		print(ans)
		cnt += 1	
		if cnt<cases:
			print()

main()