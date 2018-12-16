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
	global ans, visited, topo, campo
	ans += 1
	stack = []
	stack.append(src); visited[src] == 1
	while (len(stack)!=0):
		next_v = stack.pop()
		for i in campo[next_v]:
			if(visited[i] == 0):
				stack.append(i)
				visited[i] = 1
		visited[next_v] == 2
	return visited

def solve():
	global campo, ans, visited, luces
	ans = 0
	visited = [0 for _ in range(luces)]
	topo = toposort(campo)
	for i in topo:
		if(visited[i] == 0):
			dfs(i)
	return ans

def main():
	global campo, luces
	tc = int(stdin.readline())
	case = 1
	while(tc !=0):
		luces, lines = map(int,stdin.readline().split())
		campo = [[] for _ in range(luces)]
		while (lines != 0):
			vertices = stdin.readline().strip().split()
			u,v = int(vertices[0]) -1,int(vertices[1]) - 1
			campo[u].append(v)
			lines -= 1
		stdin.readline()
		print('Case {0}: {1}'.format(case,solve()))
		solve()
		case += 1
		tc -= 1
		
main()