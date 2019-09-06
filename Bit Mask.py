from sys import stdin
import math

def solve(n,low,hi):
	ans = None
	binary = bin(n)[2:]
	complement = [1 for _ in range(32)]
	m,j = len(binary),0
	powers = [2147483648]
	for _ in range(31):
		powers.append(powers[-1]>>1)
	for i in range(m-1,-1,-1):
		if int(binary[i]): complement[31-j] = 0
		j+=1
	accum,flag = 0,1
	if hi:
		i = 32 - math.ceil(math.log2(hi))
		while i < 32 and flag:
			if complement[i]:
				if accum + powers[i] <= hi: accum += powers[i]
			else:
				if accum + powers[i] <= low: accum += powers[i]
			i+=1
	return accum

def main():
	line = stdin.readline().split()
	while len(line):
		n,low,hi = map(int,line)
		ans = solve(n,low,hi)
		print(ans)
		line = stdin.readline().split()
		
main()