from sys import stdin
import sys

sys.setrecursionlimit(100000)

def solve(tree,low,hi):
	global post
	if(low >= hi):
		return
	elif((low+1 == hi)):
		post.append(tree[low])
		return
	else:
		mid = low+1
		while(mid < hi and tree[low] > tree[mid]):
			mid+=1
		solve(tree,low+1,mid) 
		solve(tree,mid,hi)
		post.append(tree[low])
	return

def main():
	global post
	arbol = []
	post = []

	nodo = stdin.readline()
	while (len(nodo) != 0):
		arbol.append(int(nodo))
		nodo = stdin.readline()
	solve(arbol,0,len(arbol))
	for i in range(len(post)):
		print(post[i])

main()