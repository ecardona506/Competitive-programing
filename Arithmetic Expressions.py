from sys import stdin

def operate():
	global acum, operation, numbers, parenthesis
	parenthesis.pop()
	b = float(numbers.pop())
	a = float(numbers.pop())
	op = operation.pop()
	if(op == '+'):
		result = a + b
	if(op == '-'):
		result = a - b
	if(op == '*'):
		result = a * b
	if(op == '/'):
		result = a / b
	numbers.append(result)

def solve(tree):
	global acum,operation, numbers, parenthesis
	parenthesis, numbers, operation = [], [], []
	acum = 0
	if(len(tree) == 1):
		numbers.append(float(tree[0]))
	else:
		for i in tree:
			if(i == '('):
				parenthesis.append(i)
			elif(i == '+' or i == '-' or i == '*' or i == '/'):
				operation.append(i)
			elif(i != ')'):
				numbers.append(i)
			else:
				operate()
	ans = str(round(numbers[0],2))
	dot = ans.index('.')
	if(dot +1 == len(ans)-1):
		ans += '0'
	print(ans)

def main():
	cases = int(stdin.readline())
	while(cases):
		arith = stdin.readline().strip().split()
		solve(arith)
		cases-=1 

main()