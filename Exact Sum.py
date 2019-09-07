from sys import stdin

def bs(A,low,hi,n):
	if low+1==hi:
		ans = [low,0]
	else:
		mid = (low+hi)>>1
		if A[mid] > n: ans = bs(A,low,mid,n)
		elif A[mid] < n: ans = bs(A,mid,hi,n)
		else: ans = [mid,1]
	return ans

def solve(books,budget):
	n = len(books)
	if n == 2:
		ans = books
	else:
		books.sort()
		i,f = bs(books,0,n,budget>>1)
		j,flag = i+1,1
		if f:
			if i+1 < n and books[i] == books[i+1]: j = i+1;flag = 0
			elif i-1 >= 0 and books[i] == books[i-1]: j = i-1; flag = 0
		while i >= 0 and j < n and flag:
			if books[j] + books[i] == budget: flag = 0
			elif books[j] + books[i] > budget: i-=1
			elif books[j] + books[i] < budget: j+=1
		ans = [books[i],books[j]]
	ans.sort()
	return ans

def main():
	line = stdin.readline().strip()
	while len(line):
		books = [int(x) for x in stdin.readline().split()]
		budget = int(stdin.readline().strip())
		ans = solve(books,budget)
		print('Peter should buy books whose prices are {} and {}.'.format(ans[0],ans[1]))
		space = stdin.readline()
		line = stdin.readline().strip()
		print()

main()