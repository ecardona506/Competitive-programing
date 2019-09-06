from sys import stdin

def solve(S,G):
	tmp = list()
	n = len(G)
	for i in range(n):
		tmp.append((S[i],G[i]))
	left,right = list(),list()
	for i in range(n):
		if tmp[i][0] <= tmp[i][1]: left.append(tmp[i])
		else: right.append(tmp[i])
	left.sort(),right.sort(key = lambda x:x[1])
	accum_left,accum_right = 0,0
	m,p = len(left),len(right)
	for i in range(m):
		accum_left += left[i][0]
		if accum_left >= accum_right: accum_right = accum_left + left[i][1]
		else: accum_right += left[i][1]
	for i in range(p-1,-1,-1):
		accum_left += right[i][0]
		if accum_left >= accum_right: accum_right = accum_left + right[i][1]
		else: accum_right += right[i][1]
	return max(accum_left,accum_right)

def main():
	line = stdin.readline().strip()
	while len(line):
		n = int(line)
		S = [int(x) for x in stdin.readline().split()]
		G = [int(x) for x in stdin.readline().split()]
		ans = solve(S,G)
		print(ans)
		line = stdin.readline().strip()

main()