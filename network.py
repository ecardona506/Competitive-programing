from sys import stdin

def dfs(G,u):
	global visited,low,discovery,cnt,ap,parent
	low[u] = discovery[u] = cnt ; visited[u] = 1
	cnt += 1
	for v in G[u]:
		if(visited[v] == 0):
			parent[v] = u
			dfs(G,v)
			low[u] = min(low[u],low[v])
			if(discovery[u] <= low[v] and parent[u] != -1 ):
				ap.append(u)
		else:
			low[u] = min(low[u],discovery[v])

def solve(G):
	global visited, ans, low, back, tree ,parent, discovery, cnt, ap
	n = len(G)
	cnt = 0
	back,tree = list(), list()
	visited = [0 for _ in range(n)]
	discovery = [-1 for _ in range(n)]
	low = [0 for _ in range(n)]
	parent = [-1 for _ in range(n)]
	ans = 0
	ap = list()
	children = 0
	for i in range(n):
		if not visited[i]: dfs(G,i)
	
	for i in range(n):
		if parent[i] == 0:
			children+=1
	if children > 1:
		ap.append(0)
	ap = list(set(ap))
	ans = len(ap)
	return ans

def main():
	n = int(stdin.readline().strip())
	while n != 0:
		edges = [int(x) for x in stdin.readline().strip().split()]
		m = len(edges)
		G = [[] for _ in range(n)]
		while m > 1:
			for v in range(1,m):
				G[edges[0] - 1].append(edges[v]-1)
				G[edges[v] - 1].append(edges[0] - 1)
			edges = [int(x) for x in stdin.readline().strip().split()]
			m = len(edges)
		#print(G)
		answer = solve(G)
		print(answer)
		n = int(stdin.readline().strip())

main()