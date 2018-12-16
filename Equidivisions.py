"""
modificar para que acepte el caso en que cada grupo
no tenga exactamente n-1 elementos
"""
from sys import stdin

board,aux,visited = None,None,None
size,n = 0,0
deltaf = [1,-1,0,0]
deltac = [0,0,1,-1]

def dfs(fila,col):
	global visited, aux, board, deltaf, deltac,size, ans, n
	#numero del grupo
	tag = board[fila][col]
	#adyacentes es la lista de nodos adyacentes del mismo grupo
	adyacentes = []
	stack = [(fila,col)] ; visited[fila][col] = 1
	while (len(stack) != 0):
		f,c = stack.pop()
		for i in range(len(deltaf)):
			df,dc = f + deltaf[i], c + deltac[i]
			#pos valida, es uno, y no esta visitado
			if(0 <=df<size and 0<=dc<size and board[df][dc] == tag and visited[df][dc] == 0):
				stack.append((df,dc)); visited[df][dc] = 1
				adyacentes.append((df,dc)) 
		visited[f][c] = 2
	adyacentes = list(set(adyacentes))
	if(len(adyacentes) != size - 1):
		return 'wrong'
	else:
		return 'good'

def solve():
	global board,size,aux, visited
	visited = [[0 for _ in range(size)] for _ in range(size)]
	ans = 'good'
	len_aux = len(aux)
	i = 0
	#ciclo para hacer bfs sobre cada grupo
	while(i < len_aux):
		#si un grupo no ha sido recorrido
		if (ans == 'good' and visited[aux[i]][aux[i+1]] == 0):
			ans = dfs(aux[i],aux[i+1])
		i+=2
	return ans

def build(n,lista,tag):
	global board
	lenl = 2*n
	m = n-1
	i = 0
	while(i < lenl):
		board[int(lista[i]) - 1][int(lista[i+1]) - 1] = tag
		i += 2

def main():
	global board,size, aux, n
	ok = 1
	aux = []
	#lista de posiciones de grupos diferentes
	while(ok):
		#dimension del equidivision
		size = int(stdin.readline())
		if(size == 0):
			ok = 0
		else:
			#inicializacion del equidivision
			board = [[(size - 1) for _ in range(size)] for _ in range(size)]
			#construccion de grupos
			for i in range(size - 1):
				source_list = stdin.readline().strip().split()
				aux.append(int(source_list[0]) - 1 )
				aux.append(int(source_list[1]) - 1 )
				#construccion del equidivision
				build(size,source_list,i)
			print(solve())
			aux.clear()

main()