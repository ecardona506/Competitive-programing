from sys import stdin

MAX = 10010
bet = [None for i in range(10010)]

def solve(A, low, hi):
  assert 0 <= low < hi <= len(A)
  ans = None
  if low+1==hi: ans = A[low]
  else:
    mid = low+((hi-low)>>1)   # (low+hi)//2
    ans = max(solve(A, low, mid), solve(A, mid, hi))
    ans = max(ans, max_crossing(A, low, mid, hi))
  return ans

def max_crossing(A, low, mid, hi):
  bestl,accl,l = A[mid-1],A[mid-1],mid-2
  while l>=low:
    accl += A[l]
    if accl>bestl: bestl = accl
    l -= 1
  bestr,accr,r = A[mid],A[mid],mid+1
  while r!=hi:
    accr += A[r]
    if accr>bestr: bestr = accr
    r += 1
  return bestl+bestr

def main():
  global bet
  inp = stdin
  n = int(inp.readline().strip())
  while n!=0:
    tok = inp.readline().strip().split()
    for i in range(n): bet[i] = int(tok[i])
    ans = solve(bet,0,n)
    if ans<=0: print('Losing streak.')
    else: print('The maximum winning streak is {0}.'.format(ans))
    n = int(inp.readline().strip())

main()
