from sys import stdin

def prefix(string):
	n = len(string)
	border = [0 for _ in range(n)]
	i = 0
	for j in range(1,n):
		while i>0 and string[j] != string[i]:
			#encuentra el indice del border mas largo dentro del prefijo analizado
			i = border[i-1]
		if string[i] == string[j]:
			#si encuentra un match en el siguiente caracter del border más largo analizado, aumenta
			i += 1
		else:
			#significa que no encontro un match, entonces el border mas largo dentro de la subcadena es ""
			i = 0
		border[j] = i
	return border

def kmp(string,pattern, limit):
	global index
	n,m = len(string),len(pattern)
	pattern += "|" + string
	border = prefix(pattern)
	ans = list()
	if limit > 1: p = index + m + 1 + limit
	else: p = index + m + 2
	first_value = 0
	if p < m+n+1:
		for i in range(p,m+n+1):
			if border[i] == m:
				ans.append(i - 2*m)
				if not first_value and i-2*m >= index + limit:
					index = i - 2*m
					first_value = 1
	return ans, first_value

def solve(string,pattern):
	global index
	ans = []
	tmp = ""
	flag,index,m = 1,-1,0
	n = len(string)
	for p in pattern:
		if p != '*':
			tmp += p
		else:
			if len(tmp) and flag:
				indices, flag = kmp(string,tmp,m)
				m = len(tmp)
				ans.append(indices)
				#print(tmp,indices)
				if not len(indices): flag = 0
				tmp = ""
	if len(tmp) and flag:
		indices, flag = kmp(string,tmp,m)
		ans.append(indices)
		m = len(tmp)
		#print(tmp,indices)
		if not len(indices): flag = 0
	if flag:
		return "yes"
	else:
		return "no"
	
def main():
	n_patterns = stdin.readline().strip()
	while len(n_patterns):
		string = stdin.readline().strip()
		for i in range(int(n_patterns)):
			pattern = stdin.readline().strip()
			ans = solve(string,pattern)
			print(ans)
		n_patterns = stdin.readline().strip()

main()