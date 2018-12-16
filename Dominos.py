from sys import stdin

def toposort(G):
  ans = list()
  indeg = [ 0 for _ in range(len(G)) ]
  vis = [ 0 for _ in range(len(G)) ]
  for u in range(len(G)):
    for v in G[u]:
      indeg[v] += 1
      vis[v] = 2
  pending = list()
  min_deg = 0
  while (len(ans) != len(G)):
	  for u in range(len(G)):
	    if indeg[u]==min_deg:
	      pending.append(u)
	      vis[u] = 2
	  while len(pending)!=0:
	    u = pending.pop()
	    ans.append(u)
	    for v in G[u]:
	      indeg[v] -= 1
	      if indeg[v]==min_deg:
	        pending.append(v)
	        vis[v] = 2
	  min_deg += 1
  return ans

def dfs(src):
	global ans, visited, topo, fichas
	ans += 1
	stack = []
	stack.append(src); visited[src] == 1
	while (len(stack)!=0):
		next_v = stack.pop()
		for i in fichas[next_v]:
			if(visited[i] == 0):
				stack.append(i)
				visited[i] = 1
		visited[next_v] == 2
	return visited

#list(map(int,stdin.readline().strip())

def solve():
	global fichas, ans, visited, dominos
	ans = 0
	visited = [0 for _ in range(dominos)]
	topo = toposort(fichas)
	for i in topo:
		if(visited[i] == 0):
			dfs(i)
	return ans

def main():
	global fichas, dominos
	tc = int(stdin.readline())
	while(tc !=0):
		nm = stdin.readline().strip().split()
		dominos = int(nm[0])
		lines =  int(nm[1])
		fichas = [[] for _ in range(dominos)]
		while (lines != 0):
			vertices = stdin.readline().strip().split()
			u,v = int(vertices[0]) -1,int(vertices[1]) - 1
			fichas[u].append(v)
			lines -= 1
		print(solve())
		tc -= 1
		

main()