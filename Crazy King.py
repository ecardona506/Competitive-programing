from sys import stdin
from collections import deque

"""
m: numero de filas
n: numero de columnas
----
Tablero
0: en blanco
1: caballo
2: reino A
3: reino B
----
Visitados
0: no visitado
1: caballo/visitado  
"""

n,m,visited = None,None,None
king_f = [-1,-1,-1,0,0,1,1,1]
king_c = [-1,0,1,-1,1,-1,0,1]
horse_f = [1,2,1,2,-1,-2,-1,-2]
horse_c = [-2,-1,2,1,2,1,-2,-1]

def bfs(G,src):
	global n,m, visited, king_c, king_f
	cola = deque()
	cola.append(src)
	flag = 0
	cnt = 1
	top = src
	while len(cola):
		u = cola.popleft()
		for i in range(len(king_f)):
			if not flag:
				kfil,kcol = u[0] + king_f[i], u[1] + king_c[i]
				if 0<=kfil<m and 0<=kcol<n:
					if visited[kfil][kcol] == 0:
						cola.append([kfil,kcol])
						visited[kfil][kcol] = 1
					if G[kfil][kcol] == 3:
						cola.clear()
						flag = 1
		visited[u[0]][u[1]] = 2
		if u == top and len(cola):
			cnt+=1
			top = cola[-1]
		#print(u,cnt)
	if flag:
		ans = "Minimal possible length of a trip is {0}".format(cnt)
	else:
		ans = "King Peter, you can't go now!"
	return ans

def main():
	global n,m, visited, goal, horse_c, horse_f
	tc = int(stdin.readline().strip())
	S = {".":0,"Z":1,"A":2,"B":3}
	for i in range(tc):
		m,n = map(int,stdin.readline().strip().split())
		board = [[] for _ in range(m)]
		visited = [[0 for _ in range(n)] for _ in range(m)]
		horses = deque()
		for fil in range(m):
			line = list(stdin.readline().strip())
			for col in range(n):
				board[fil].append(S[line[col]])
				if S[line[col]] == 1:
					visited[fil][col] = 1
					horses.append([fil,col])
				elif S[line[col]] == 2:
					src = [fil,col]
				elif S[line[col]] == 3:
					goal = [fil,col]
		for u in range(len(horses)):
			for j in range(8):
				hfil,hcol = horses[u][0] + horse_f[j], horses[u][1] + horse_c[j]
				if 0<=hfil<m and 0<=hcol<n and board[hfil][hcol] != 3:
					visited[hfil][hcol] = 1
		#print(visited)
		ans = bfs(board,src)
		print(ans)

main()