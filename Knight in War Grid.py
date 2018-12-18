from sys import stdin
from collections import deque

"""
visited = 0 "No visitado"
visited = 1 "No visitado, cola"
visited = 2 "visitado"
visited = 3 "Charco"
"""

charcos = []

visited = None
deltac, deltaf = None,None
pares, impares = None, None

#vertex es la posicion en una tupla.

def next_states(vertex):
	global deltac, f,c, deltaf, pares, impares
	ans = list()
	for i in range(8):
		fil, col = vertex[0] + deltaf[i],vertex[1] + deltac[i]
		if(0<=fil<f and 0<=col<c):
			if(visited[fil][col] != 3):
				ans.append((fil,col))
	ans = list(set(ans))
	reach = len(ans)
	if(reach == 0 or reach % 2 == 0):
		pares += 1
		return pares
	else:
		impares+= 1
		return impares

def bfs(source):
	global visited, pares, impares, water, c, f
	cola = deque()
	cola.append(source); visited[0][0] = 2
	next_states(source)
	while (len(cola) != 0):
		u = cola.popleft()
		for i in range(8):
			fil, col = u[0] + deltaf[i],u[1] + deltac[i]
			if((0<=fil<f and 0<=col<c) and (visited[fil][col] == 0)):
				cola.append((fil,col))
				next_states((fil,col))
				visited[fil][col] = 1
			visited[u[0]][u[1]] = 2
	return pares, impares

def solve(board):
	global charcos,pares,impares, water, deltac, deltaf, m, n
	pares, impares = 0,0
	deltaf = [0-m,0-n,0-n,0-m,m,n,m,n]
	deltac = [n,m,0-m,0-n,0-n,0-m,n,m]
	bfs((0,0))
	return pares, impares

def main():
	global f,c,n,m, water, charcos, visited
	tc = 1
	casos = int(stdin.readline())
	while(casos):
		f,c,m,n = map(int,stdin.readline().strip().split())
		waterhole = int(stdin.readline().replace(" ",""))
		water = waterhole
		visited = [[0 for _ in range(c)] for _ in range(f)]
		while (waterhole):
			wf,wc = map(int,stdin.readline().strip().split())
			visited[wf][wc] = 3
			waterhole -= 1
		answer = solve(visited)
		print('Case {0}: {1} {2}'.format(tc,answer[0],answer[1]))
		casos -= 1
		tc += 1

main()
