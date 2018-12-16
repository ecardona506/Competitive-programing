from sys import *

setrecursionlimit(1000000)

INPUT,I = stdin.buffer.read(),0
SPACE,CR,LPAR,RPAR,ZERO,NINE,MINUS = ord(' '),ord('\n'),ord('('),ord(')'),ord('0'),ord('9'),ord('-')

def has_next(): return I<len(INPUT)

def is_par() : return LPAR==INPUT[I] or RPAR==INPUT[I]

def is_digit(): return ZERO <= INPUT[I] <= NINE

def is_minus(): return MINUS==INPUT[I]

def read_blanks():
  global INPUT,I
  while has_next() and not(is_digit()) and not(is_par()) and not(is_minus()): I += 1

def read_par():
  global INPUT,I
  ans,I = chr(INPUT[I]),I+1
  return ans

def signed_num():
  global INPUT,I
  I += 1
  read_blanks()
  return read_num()*-1

def read_num():
  global INPUT,I
  ans = 0
  while has_next() and is_digit(): ans,I = int(chr(INPUT[I]))+ans*10,I+1
  return ans

def next_token():
  global INPUT,I
  ans = None
  read_blanks()
  if I!=len(INPUT):
    if is_digit():
      ans = read_num()
    elif is_minus():
      ans = signed_num()
    else: ans = read_par()
  return ans

def parse_tree():
  ans = list()
  next_token()
  tk = next_token()
  if tk!=')':
    ans.append(tk)
    ans.append(parse_tree())
    ans.append(parse_tree())
    next_token()
  return ans

def solve(tree):
  global ans,answers
  if(type(tree) != 'int' and (len(tree) !=0)):
    if(type(tree[1]) != 'int' and type(tree[2]) != 'int' and len(tree[1]) == 0 and len(tree[2]) == 0):
      ans += tree[0]
      answers.append(ans)
      ans -= tree[0]
      return
    if(type(tree[1]) != 'int' and len(tree[1]) == 0):
      ans+= tree[0]
      solve(tree[2])
      ans-= tree[0]
      return
    if(type(tree[2]) != 'int' and len(tree[2]) == 0):
      ans+= tree[0]
      solve(tree[1])
      ans-= tree[0]
      return
    else:
      ans += tree[0]
      solve(tree[1])
      solve(tree[2])
      ans -= tree[0]
      return
  else:
    return

def main():
  global ans,answers
  i = 0
  tkn= next_token()
  while(tkn!=None):
    answers = []
    tree = parse_tree()
    ans = 0
    summing = 'no'
    if(len(tree) == 0):
      print(summing)
    else:
      solve(tree)
      for i in range(len(answers)):
        if(answers[i] == tkn):
          summing = 'yes'
      print(summing)
    tkn= next_token()

main()