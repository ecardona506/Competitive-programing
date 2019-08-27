from sys import stdin
from collections import deque

def LIS(A,n):
	lis,lds = [None for _ in range(n)],[None for _ in range(n)]
	ans = 0
	best_lis,best_lds = 0,0
	for i in range(n):
		lds[i],lis[i] = 1,1
		for j in range(i):
			if A[j]<=A[i] and lis[j]>=lis[i]: lis[i] = lis[j] + 1
			if A[j]>=A[i] and lds[j]>=lds[i]: lds[i] = lds[j] + 1
		ans = max(lis[i]+lds[i]-1,ans)
	return ans 

def main():
	tc = int(stdin.readline().strip())
	while tc:
		n = int(stdin.readline().strip())
		train = deque()
		for _ in range(n):
			x = int(stdin.readline().strip())
			train.appendleft(x)
		ans = LIS(train,n)
		print(ans)
		tc-=1

main()