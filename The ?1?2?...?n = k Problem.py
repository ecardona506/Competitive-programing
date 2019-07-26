
from sys import stdin
import math,sys

def sequence_lenght(n,ans):
	global acum
	if n <= 9:
		return ans + (int(n)*(int(n)+1))>>1
	exp = int(math.log(n,10))
	x = int(n-(10**exp) + 1)
	ans += int(exp*((x*(x+1))>>1))
	return sequence_lenght(x,ans)

def binary_search(low,hi,i):
	mid = (low+hi)>>1
	if low + 1 == hi:
		length = sequence_lenght(low,0)
		exp = int(math.log(low,10))
		string = ""
		for i in range(1,low+1):
			string += str(i)
		ans = string[length-i-2]
		print(ans)
	else:
		length = sequence_lenght(mid,0)
		if i > length: binary_search(mid,hi,i)
		elif i <= length: binary_search(low,mid,i)

def main():
	global string
	cases = int(stdin.readline().strip())
	string = ""
	for i in range(1,8977):
		string += str(i)
	"""
	while cases:
		i = int(stdin.readline().strip())
		binary_search(1,8977,i)
		cases-=1
	"""
main()
