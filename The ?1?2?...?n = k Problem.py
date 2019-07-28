from sys import stdin

def binary_search(n,low,hi):
	mid = (low+hi)>>1
	if low+1 == hi:
		value = (low*(low+1))>>1
		if value == n:
			ans = low
		else:
			low+=1
			value = (low*(low+1))>>1
			#Si se resta algun valor, el nuevo valor es value - 2 veces el valor a restar
			while (value - n)%2:
				low+=1
				value = (low*(low+1))>>1
			ans = low
		return ans 
	value = (mid*(mid+1))>>1
	if value > n: return binary_search(n,low,mid)
	else: return binary_search(n,mid,hi)

def main():
	cases = int(stdin.readline().strip())
	while cases != 1:
		stdin.readline()
		n = int(stdin.readline().strip())
		ans = binary_search(abs(n),1,44721)
		print(ans)
		print()
		cases -=1
	stdin.readline()
	n = int(stdin.readline().strip())
	ans = binary_search(abs(n),1,44721)
	print(ans)

main()
