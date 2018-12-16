from sys import stdin

INF = float('inf')

def floyd_warshall(G):
    n = len(G)
    dp = [[INF for i in range(n)] for j in range(n)]
    path = [[None for i in range(n)] for j in range(n)]
    for u in range(n):
        for v,d in G[u]:
            if d < dp[u][v]:
                dp[u][v] = d
                path[u][v] = u
    for i in range(n):
        dp[i][i] = 0
        path[i][i] = None
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(dp[i][k] + dp[k][j] < dp[i][j]):
                    dp[i][j] = dp[i][k] + dp[k][j]
                    path[i][j] = path[k][j]
    return dp  

def main():
	intersections = int(stdin.readline().strip()) 
	while(intersections != 0):
		#cada intersección es un nodo del grafo DIRIGIDO
		old = [[] for _ in range(intersections)]
		new = [[] for _ in range(intersections)]
		for i in range(intersections):
			#crea la representación antigua de edgetown como un grafo
			old_streets = list(map(int,stdin.readline().strip().split()))
			for j in range(1,len(old_streets)):
				old[old_streets[0]-1].append((old_streets[j] - 1,1))
		for i in range(intersections):
			#crea la nueva representación de edgetown como un grafo	
			new_streets = list(map(int,stdin.readline().strip().split()))
			for j in range(1,len(new_streets)):
				new[new_streets[0]-1].append((new_streets[j] - 1,1))
		A,B = map(int,stdin.readline().strip().split())
		old_map=floyd_warshall(old)
		new_map = floyd_warshall(new)
		#print(old_map)
		#print(new_map)
		ans,i=1,0
		while(ans and (i < intersections)):
			j = 0
			while(ans and (j < intersections)):
				if(new_map[i][j] > (A * old_map[i][j]) + B):
					ans = 0
				j+=1
			i+=1
		if(ans):
			print("Yes")
		else:
			print("No")
		intersections = int(stdin.readline().strip())

main()
