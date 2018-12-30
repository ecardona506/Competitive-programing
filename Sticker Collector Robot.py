from sys import stdin

"""
0 = . (Normal)
1 = * (Sticker)
2 = # (Pilar)
3 = NSLO (Orientacion)
"""
posX, posY = None, None

def graphify(arr):
	global posY, orientacion
	res = []
	flag = 0
	for i in range(len(arr)):
		if(arr[i] == "."):
			res.append(0)
		elif(arr[i] == "*"):
			res.append(1)
		elif(arr[i] == "#"):
			res.append(2)
		elif(arr[i] == "N"):
			res.append(0)
			posY = len(res) - 1
			orientacion = 0
			flag = 1
		elif(arr[i] == "O"):
			res.append(0)
			posY = len(res) - 1
			orientacion = 3
			flag = 1
		elif(arr[i] == "S"):
			res.append(0)
			posY = len(res) - 1
			orientacion = 2
			flag = 1
		elif(arr[i] == "L"):
			res.append(0)
			posY = len(res) - 1
			orientacion = 1
			flag = 1
	if flag:
		return True, res
	else:
		return False, res

def solve(graph,instrucciones):
	global N,M,orientacion,posX,posY,orientacion
	#aumenta indice, gira derecha
	deltac,deltaf = [-1,0,1,0], [0,1,0,-1]
	ans = 0
	for i in range(len(instrucciones)):
		if(instrucciones[i] == 'F'):
			if((0<=posX + deltac[orientacion] < N) and (0<=posY + deltaf[orientacion]<M)):
				if(graph[posX + deltac[orientacion]][posY + deltaf[orientacion]] == 0):
					posX = posX + deltac[orientacion]
					posY = posY + deltaf[orientacion]
				elif(graph[posX + deltac[orientacion]][posY + deltaf[orientacion]] == 1):
					posX = posX + deltac[orientacion]
					posY = posY + deltaf[orientacion]
					graph[posX][posY] = 0
					ans += 1
				elif(graph[posX + deltac[orientacion]][posY + deltaf[orientacion]] == 2):
					pass
		elif(instrucciones[i] == 'D'):
			if(orientacion == 3):
				orientacion = 0
			else:
				orientacion +=1
		elif(instrucciones[i] == 'E'):
			if(orientacion == 0):
				orientacion = 3
			else:
				orientacion -=1
	return ans

def main():
	global N,M, posX
	N,M,S = map(int,stdin.readline().strip().split())
	while ((0==N==M==S) == False):
		graph = []
		for i in range(N):
			arr = stdin.readline().strip()
			tmp = graphify(arr)
			graph.append(tmp[1])
			if(tmp[0] == True):
				posX = i
		instrucciones = stdin.readline().strip()
		ans = solve(graph,instrucciones)
		print(ans)
		N,M,S = map(int,stdin.readline().strip().split())

main()