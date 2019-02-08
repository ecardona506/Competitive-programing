from sys import stdin

def solve(rungs, n):
  ans = 0
  if(n == 1):
  	ans = rungs[0]
  else:
	  for i in range(n):
	  	if(i < n-1):
	  		if((rungs[i+1] - rungs[i]) > ans):
	  			ans = rungs[i+1] - rungs[i]
  return ans

def main():
  tcnt = int(stdin.readline())
  for tc in range(1, tcnt+1):
    n = int(stdin.readline())
    rungs = [ int(x) for x in stdin.readline().split() ]
    print('Case {0}: {1}'.format(tc, solve(rungs, n)))

main()
