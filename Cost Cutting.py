from sys import stdin

def main():
	tc = int(stdin.readline().strip())
	for i in range(tc):
		a,b,c = map(int,stdin.readline().split())
		ans = None
		if (a >= b and a <= c) or (a <= b and a >= c): ans = a
		elif (b >= a and b <= c) or (b <= a and b >= c): ans = b
		elif (c >= a and c <= b) or (c <= a and c >= b): ans = c
		print('Case {}: {}'.format(i+1,ans))

main()