from sys import stdin
from collections import deque

def bfs(G,src,dst):
	queue = deque()
	queue.append(src)
	n = len(G)
	visited = [0 for _ in range(n)]
	prev = [-1 for _ in range(n)]
	while len(queue):
		u = queue.popleft()
		for v in G[u]:
			if not visited[v]:
				queue.append(v)
				prev[v] = u
		visited[u] = 1
	x = dst
	road = list()
	while x != -1:
		road.append(x)
		x = prev[x]
	ans = ''
	i =len(road)-1
	while i >= 0:
		ans+= chr(road[i]+65)
		i-=1
	return ans

def main():
	tc = int(stdin.readline().strip())
	while tc:
		space = stdin.readline()
		n,m = map(int,stdin.readline().split())
		i = 0
		G=[[] for _ in range(26)]
		for _ in range(n):
			x,y = map(str,stdin.readline().split())
			u,v = x[0],y[0]
			G[ord(u)-65].append(ord(v)-65)
			G[ord(v)-65].append(ord(u)-65)
		#print(G)
		for _ in range(m):
			x,y = map(str,stdin.readline().split())
			u,v = x[0],y[0]
			ans = bfs(G,ord(u)-65,ord(v)-65)
			print(ans)
		if tc-1:
			print()
		tc -= 1

main()