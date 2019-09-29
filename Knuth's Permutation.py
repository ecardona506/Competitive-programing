from sys import stdin

def solve(ans,i):
	global word,n
	if i == n-1:
		for j in range(n):
			tmp = ans[:]
			ans.insert(j,word[i])
			for k in ans:
				print(k,end='')
			ans = tmp[:]
			print()
	else:
		for j in range(i+1):
			tmp = ans[:]
			ans.insert(j,word[i])
			solve(ans,i+1)
			ans = tmp

def main():
	global word,n
	word = stdin.readline().strip()
	while len(word):
		n = len(word)
		solve(list(),0)
		word = stdin.readline().strip()
		if len(word): print()

main()