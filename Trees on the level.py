from sys import *

coma,right_par = ord(','),ord(')') 

def parse_elements(string):
	global arbol, tmp, numero_de_raices
	if(len(string) != 2):
		parse= []
		number = ""
		position = ""
		for i in range(len(string)):
			parse.append(ord(string[i]))
		for num in range(1,parse.index(coma)):
			number += string[num]
		if(parse.index(coma) + 1 == parse.index(right_par)):
			position = 0
			numero_de_raices +=1
		else:
			for pos in range(parse.index(coma) + 1,parse.index(right_par)):
				if(string[pos] == 'L'):
					position += '1'
				else:
					position += '2'
			tmp.append(int(position))
		arbol[int(position)] = number

def solve():
	global entrada, arbol, level, tmp,ans, numero_de_raices
	arbol = {0:""}
	ans = ""
	tmp = [0]
	ok = 1
	j = 0
	numero_de_raices = 0
	for i in range(len(entrada)):
		parse_elements(entrada[i])
	tmp.sort()
	tmp2 = list(set(tmp))
	tree = []
	for i in tmp:
		tree.append(str(i))
	ans += arbol[0]
	tmp2 = list(set(tmp))
	if((arbol[0] == "") or (len(tmp) != len(tmp2))):
		ok = 0
	if(ok):
		if(numero_de_raices != 1):
			ok = 0
	if(ok):
		for i in tree:
			padre = ""
			for j in range(len(i)-1):
				padre += i[j]
			if(padre!= ""):
				try:
					tree.index(padre)
				except ValueError:
					ok = 0
	if(ok):
		for level in range(1,len(tmp)):
			ans+= " " + arbol[tmp[level]]
		print(ans)
	else:
		print('not complete')

def main():
	global entrada
	flag = 1 
	while (flag):
		entrada = stdin.readline().strip().split()
		if(len(entrada) == 0):
			flag = 0
		else:
			solve()

main()