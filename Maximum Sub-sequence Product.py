from sys import stdin

INF = float('inf')

def fill_column(lo,sequence):
	global memo, ans
	n = len(sequence)
	

def solve(sequence):
	global memo, ans
	n = len(sequence)
	memo = [[0 for _ in range(n)] for _ in range(n)]
	ans = sequence[0]
	memo[0][0] = sequence[0]
	if len(sequence) > 1:
		for i in range(1,n):
			memo[0][i] = memo[0][i-1]*sequence[i]
			if memo[0][i] > ans: ans = memo[0][i]

		for lo in range(1,n):
			if sequence[lo-1] != 0:
				for hi in range(lo,n):
					memo[lo][hi] = memo[lo-1][hi]//sequence[lo-1]
					if memo[lo][hi] > ans: ans = memo[lo][hi]
			else:
				memo[lo][lo] = sequence[lo]
				for i in range(lo+1,n):
					memo[lo][i] = memo[lo][i-1]*sequence[i]
					if memo[lo][i] > ans: ans = memo[lo][i]
	return ans

def main():
	line = stdin.readline().split()
	while len(line):
		sequence = [int(x) for x in line]
		sequence.pop()
		ans = solve(sequence)
		print(ans)
		line = stdin.readline().split()
main()