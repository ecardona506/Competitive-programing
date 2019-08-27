from sys import stdin
import sys

sys.setrecursionlimit(10000)

INF = float('inf')

def phi(a,e,h):
	global expected,n,m,memo
	ans = None
	if (a,e,h) in memo: ans = memo[(a,e,h)]
	elif a == 0: ans = 0
	elif e == 0: ans = -INF
	elif expected[a-1][e-1] < 5: ans = phi(a,e-1,h)
	else:
		ans = phi(a,e-1,h)
		if h >= e: ans = max(ans,phi(a-1,m,h-e)+expected[a-1][e-1])
	memo[(a,e,h)] = ans
	return ans

def main():
	global expected,n,m,memo
	tc = int(stdin.readline().strip())
	while tc:
		n,m = map(int,stdin.readline().split())
		expected,memo = list(),{}
		for _ in range(n):
			line = [int(x) for x in stdin.readline().split()]
			expected.append(line)
		ans = (phi(n,m,m)/n)
		if (ans>=5):print("Maximal possible average mark - {0:.2f}.".format(ans))
		else: print("Peter, you shouldn't have played billiard that much.")
		tc-=1

main()