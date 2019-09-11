from sys import stdin
import math

def solve(sprinklers,hi):
	ans = 0
	n = len(sprinklers)
	low,i,flag = 0,0,1
	while low < hi and i < n and flag:
		if low < sprinklers[i][0]: flag = 0
		best,i = i,i+1
		while i < n and sprinklers[i][0] <= low and flag:
			if sprinklers[i][1] > sprinklers[best][1]:
				best = i
			i+=1
		if flag: ans+=1
		low = sprinklers[best][1]
	if low < hi or not flag or ans == 0: ans = -1
	return ans

def main():
	line = stdin.readline().split()
	while len(line):
		n,l,w = map(int,line)
		sprinklers = list()
		for _ in range(n):
			i,r = map(int,stdin.readline().split())
			if r > w/2:
				x = math.sqrt((r**2)-((w/2)**2))
				array = [i-x,i+x]
				sprinklers.append(array)
		sprinklers.sort()
		#print(sprinklers)
		ans = solve(sprinklers,l)
		print(ans)
		line = stdin.readline().split()

main()