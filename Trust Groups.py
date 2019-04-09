from sys import stdin

def dfs1(G,src):
	global visited, order
	visited[src] = 1
	for v in G[src]:
		if not visited[v]: dfs1(G,v)
	order.append(src)
	return

def dfs2(G,src):
	global visited
	stack = list()
	stack.append(src)
	while len(stack):
		u = stack.pop()
		for v in G[u]:
			if visited[v] == 0:
				stack.append(v)
		visited[u] = 1
	return

def kosaraju(G):
	global p, order, visited
	order = list()
	R = [[] for _ in range(p)]
	for u in range(p):
		for v in G[u]:
			R[v].append(u)
	visited = [0 for _ in range(p)]
	for u in range(p):
		if visited[u] == 0:
			dfs1(G, u)
	ans = 0
	visited = [0 for _ in range(p)]
	while (len(order)):
		u = order.pop()
		if not visited[u]:
			ans+=1
			dfs2(R, u)
	return ans

def main():
	global p, G
	line = stdin.readline().strip()
	p,t = map(int,line.split())
	while line != "0 0":
		name_to_id = {}
		for i in range(p):
			name = stdin.readline().strip()
			name_to_id[name] = i
		G = [[] for _ in range(p)]
		for i in range(t):
			u = stdin.readline().strip()
			v = stdin.readline().strip()
			G[name_to_id[u]].append(name_to_id[v])
		ans = kosaraju(G)
		print(ans)
		line = stdin.readline().strip()
		p,t = map(int,line.split())

main()