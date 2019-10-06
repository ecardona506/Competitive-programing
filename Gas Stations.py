from sys import stdin

def solve(gas,L):
	n = len(gas)
	ans = n
	low,i,flag = 0,0,1
	while low < L and i < n and flag:
		if low < gas[i][0]: flag = 0
		best,i = i,i+1
		while i < n and gas[i][0] <= low and flag:
			if gas[i][1] > gas[best][1]:
				best = i
			i+=1
		if flag: ans-=1
		low = gas[best][1]
	if low < L or not flag: ans = -1
	return ans

def main():
	L,G = map(int,stdin.readline().split())
	while L!= 0 and G != 0:
		gas = list()
		for _  in range(G):
			x,r = map(int,stdin.readline().split())
			gas.append((x-r,x+r))
		gas.sort()
		ans = solve(gas,L)
		print(ans)
		L,G = map(int,stdin.readline().split())
main()