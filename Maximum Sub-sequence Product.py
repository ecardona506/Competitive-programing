from sys import stdin

def solve(sequence,n):
	best_product,worst_product,ans = sequence[0],sequence[0],sequence[0]
	tmp_max,tmp_min = None,None
	for i in range(1,n):
		tmp_max,tmp_min = best_product,worst_product 
		worst_product = min(sequence[i],tmp_max*sequence[i],tmp_min*sequence[i])
		best_product = max(sequence[i],tmp_max*sequence[i],tmp_min*sequence[i])
		ans = max(ans,best_product,worst_product)
	return ans

def main():
	line = stdin.readline().split()
	while len(line):
		sequence = [int(x) for x in line]
		line = sequence
		while line[-1] != -999999:
			line = [int(x) for x in stdin.readline().split()]
			sequence.extend(line)
		sequence.pop()
		ans = solve(sequence,len(sequence))
		print(ans)
		line = stdin.readline().split()

main()