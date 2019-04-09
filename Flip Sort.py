from sys import stdin

def solve(num, low, hi):
  r = 0
  if hi <= low+1:
    return 0
  mid = low + ((hi-low)>>1)
  i,j =low,mid
  r = solve(num,low,mid)
  r+= solve(num,mid,hi)
  tmp = []
  while (i < mid and j < hi):
    if num[i] <= num [j]:
      tmp.append(num[i])
      i+=1
    else:
      tmp.append(num[j])
      j+=1
      r+=mid-i
  while i < mid:
    tmp.append(num[i])
    i+=1
  while j < hi:
    tmp.append(num[j])
    j+=1
  num[low:hi] = tmp
  return r

def main():
  inp = stdin
  s = inp.readline()
  lab = "Minimum exchange operations : {0}"
  while len(s)>0:
    n = int(s)
    num = [int(x) for x in stdin.readline().strip().split()]
    print(lab.format(solve(num, 0, n)))
    s = inp.readline().strip()

main()
