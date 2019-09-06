from sys import stdin

def solve(n):
	ans = None
	if n == 0:ans = 0
	elif n == 3: ans = 3
	else:
		if n%2:
			if ((n+1)>>1)%2:ans = solve(n-1) + 1
			else: ans = solve(n+1) + 1
		else: ans = solve(n>>1) + 1
	return ans

def main():
	line = stdin.readline().strip()
	while len(line):
		n = int(line)
		ans = solve(n)
		print(ans)
		line = stdin.readline().strip()

main()