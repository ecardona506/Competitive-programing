from sys import stdin
from collections import deque

INF = float('inf')

def phi(i,j):
	global INF,matrix,n,memo
	ans = None
	if (i,j) in memo: ans = memo[(i,j)]
	elif j == 0:
		if i == 0: ans = 0
		else: ans = INF
	elif i == 0: ans = min(30 + phi(i,j-1) - matrix[i][j-1],20 + phi(i+1,j-1) - matrix[i+1][j-1])
	elif i == 9: ans = min(60 + phi(i-1,j-1) - matrix[i-1][j-1],30 + phi(i,j-1) - matrix[i][j-1])
	elif 0<i<10 and 0<j<n: ans = min(60 + phi(i-1,j-1) - matrix[i-1][j-1],30 + phi(i,j-1) - matrix[i][j-1],20 + phi(i+1,j-1) - matrix[i+1][j-1])
	else: ans = INF
	memo[(i,j)] = ans
	return ans

def main():
	global matrix,n,memo
	tc = int(stdin.readline().strip())
	while tc:
		line = stdin.readline().strip()
		while not len(line):
			line = stdin.readline().strip()
		n = int(line) // 100
		matrix,memo = deque(),{}
		for _ in range(10):
			x = [int(x) for x in stdin.readline().split()]
			matrix.appendleft(x)
		ans = phi(0,n)
		print(ans)
		if tc: print()
		tc-=1

main()