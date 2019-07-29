from sys import stdin

#Solving 2(n(n+1)//2) = 2**31 we get 46341 aprox.

def binary_search(low,hi,n):
	mid = (low+hi)>>1
	if n == 0:
		return 0
	elif low+1 == hi:
		ans = 2*low-1
		value = low*(low+1) - low
		dif = n - value
		while dif > 0:
			dif -= low
			ans+=1
		return ans
	else:
		if mid*(mid+1) - mid > n: return binary_search(low,mid,n)
		else: return binary_search(mid,hi,n)

def main():
	n = int(stdin.readline().strip())
	for _ in range(n):
		x,y = map(int,stdin.readline().split())
		ans = binary_search(0,46341,y-x)
		print(ans)

main()