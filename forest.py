from sys import stdin

n,m = None,None
deltaf = [-1,-1,-1,0,0,1,1,1]
deltac = [-1,0,1,-1,1,-1,0,1]

def dfs(G,pos,ans):
	global n, m, deltaf, deltac, visited, cnt, size
	stack = []
	stack.append(pos)
	visited[pos[0]][pos[1]] = 1
	cnt += 1
	ans[pos[0]][pos[1]] = cnt
	tmp = len("{0}".format(cnt))
	if tmp > size[pos[1]]:
		size[pos[1]] = tmp
	while len(stack):
		u = stack.pop()
		for i in range(len(deltaf)):
			fil = u[0]+deltaf[i]
			col = u[1]+deltac[i]
			if (0<=fil<n) and (0<=col<m):
				if G[pos[0]][pos[1]] == G[fil][col] and (visited[fil][col] == 0):
					stack.append([fil,col])
					ans[fil][col] = cnt
					tmp = len("{0}".format(cnt))
					if tmp > size[col]:
						size[col] = tmp
			visited[u[0]][u[1]] = 1
	return ans

def solve(G):
	global n, m, visited, cnt, size
	n = len(G)
	m = len(G[0])
	if n == m:
		ok = 1
	size = [1 for _ in range(m)]
	ans = [[0 for _ in range(m)] for _ in range(n)]
	visited = [[0 for _ in range(m)] for _ in range(n)]
	cnt = 0
	for i in range(n):
		for j in range(m):
			if visited[i][j] == 0:
				dfs(G,[i,j],ans)
	return ans

def print_ans(G):
	global n, m, cnt, size
	for i in range(n):
		res = str(G[i][0])
		spaces = (size[0] - len(res))
		ans = spaces*" " + res
		if m == 1:
			pass
		elif m > 2:
			for j in range(1,m):
				res = "{0}".format(G[i][j])
				if size[j] == len(res):
					spaces = 1
				else:
					spaces = (size[j] - len(res)+1)
				ans += " "*spaces + res
		elif m == 2:
			res = str(G[i][0])
			spaces = size[0] - len(res)
			ans = spaces*" " + res
			spaces = (size[1] - len(res)+1)
			ans += " "*spaces + "{0}".format(G[i][1])
		print(ans)

def main():
	line = stdin.readline().strip().split()
	G = []
	while len(line):
		if line[0] == "%":
			ans = solve(G)
			print_ans(ans)
			print("%")
			G.clear()
		elif len(line) >= 1:
			G.append(line)
		line = stdin.readline().strip().split()
	ans = solve(G)
	print_ans(ans)
	print("%")	

main()