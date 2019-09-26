from sys import stdin

def solve(diccionario,rule,n,i,ans):
	if i == n-1:
		if rule[i] == '0':
			for k in range(10):
				ans.append('{}'.format(k))
				for i in ans:
					print(i,end='')
				ans.pop()
				print()
		else:
			m = len(diccionario)
			for i in diccionario:
				ans.append('{}'.format(i))
				for j in ans:
					print(j,end='')
				ans.pop()
				print()
	else:
		if rule[i] == '0':
			for k in range(10):
				ans.append('{}'.format(k))
				solve(diccionario,rule,n,i+1,ans)
				ans.pop()
		else:
			m = len(diccionario)
			for k in diccionario:
				ans.append('{}'.format(k))
				solve(diccionario,rule,n,i+1,ans)
				ans.pop()

def main():
	line = stdin.readline().strip()
	while len(line):
		n = int(line)
		diccionario = list()
		for _ in range(n):
			diccionario.append(stdin.readline().strip())
		m = int(stdin.readline().strip())
		rules =list()
		for _ in range(m):
			rules.append(stdin.readline().strip())
		print('--')
		for i in range(m):
			ans = solve(diccionario,rules[i],len(rules[i]),0,list())	
		line = stdin.readline().strip()
main()