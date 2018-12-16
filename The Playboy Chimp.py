from sys import stdin 

def solve(altura,n,ladys_h):
	small,tall,lo = 0,0,0
	hi = n - 1
	ok = 1
	mid = (hi+lo) >> 1
	while(lo!=hi and ok):
		if(int(ladys_h[mid]) < int(altura)):
			small = ladys_h[mid]
			tall = ladys_h[mid +1]
			lo = mid + 1
			mid = (hi+lo) >> 1
		elif(int(ladys_h[mid]) > int(altura)):
			tall = ladys_h[mid]
			small = ladys_h[mid - 1]
			hi =  mid
			mid = (hi+lo) >> 1
		elif(int(ladys_h[mid]) == int(altura)):
			i = mid
			#igual tall
			flag = 1
			if(mid + 1 < n):
				while(flag and int(ladys_h[i]) == int(altura)):
					i += 1
					if(i > n or i == n):
						tall = 'X'
						flag = 0
					else:
						tall = ladys_h[i]
				ok = 0
			else:
				tall = 'X'
			#igual small
			if(mid - 1 >= 0):
				i = mid
				small = ladys_h[mid - 1]
				while (int(ladys_h[i]) == int(altura) and flag):
					i -= 1
					if(i < 0):
						small = 'X'
						flag = 0
					else:
						small = ladys_h[i]
				ok = 0
			else:
				small = 'X'
				ok = 0
	if (int(ladys_h[0]) > int(altura) and small != 'X'):
		small = 'X'
		tall = ladys_h[0]
	if (int(ladys_h[-1]) < int(altura) and tall != 'X'):
		tall = 'X'
		small = ladys_h[-1]
	elif (int(ladys_h[-1]) == int(altura) and tall != 'X'):
		tall = 'X'
	return small,tall
			
def main():
	n = int(stdin.readline())
	ladys_h = (stdin.readline().strip().split())
	h = int(stdin.readline())
	luchu_h = (stdin.readline().strip().split())
	for i in range(h):
		altura = luchu_h[i]
		ans = solve(altura,n,ladys_h)
		print(ans[0] + " " + ans[1])
main()
