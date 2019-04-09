from sys import stdin
INPUT = stdin.read()

def toposort(G):
	global ind
	n = len(G)
	pending = list()
	topo = list()
	for u in range(n):
		if indeg[u] == 0: pending.append(u) 
	while len(pending):
		u = pending.pop()
		topo.append(u)
		for v in G[u]:
			indeg[v] -= 1
			if indeg[v] == 0: pending.append(v)
	return topo

def solve(L):
	global indeg, ok
	tmp = list(set(L))
	n = len(tmp)
	m = len(L)
	to_id = {}
	for u in range(n):
		to_id[tmp[u]] = u
	G = [[] for _ in range(n)]
	childs = [0 for _ in range(n)]
	parent = [[] for _ in range(n)]
	indeg = [0 for _ in range(n)]
	ok,i = 1,0
	while ok and i < m:
		G[to_id[L[i]]].append(to_id[L[i+1]])
		parent[to_id[L[i+1]]].append(to_id[L[i]])
		indeg[to_id[L[i+1]]] += 1
		if indeg[to_id[L[i+1]]] > 1:
			ok = 0
		i+= 2
	indeg_zero = 0
	for i in range(n):
		if indeg[i] == 0:
			indeg_zero += 1
	if indeg_zero > 1: ok = 0
	if ok:
		topo = toposort(G)
		if len(topo) != n: ok = 0
	return "is" if ok else "is not"

def next_number():
	global index, INPUT
	while not INPUT[index].isdigit() and INPUT[index] != '-':
		index += 1
	j = index+1
	while j < len(INPUT) and INPUT[j].isdigit():
		j+=1
	ans = int(INPUT[index:j])
	index = j
	return ans

def main():
	global index, INPUT
	ok = 1
	L = list()
	index, cnt_zero,k = 0,0,1
	while(ok):
		bit = INPUT[index]
		if bit.isdigit():
			number = next_number()
			if number == 0:
				cnt_zero += 1
				if cnt_zero == 2:
					ans = solve(L)
					print("Case {} {} a tree.".format(k,ans))
					k+=1
					L.clear()
					cnt_zero = 0
			else:
				L.append(number)
		elif bit == "-":
			ok = 0
		elif bit == '\n' or bit == '\r' or bit == " ":
			pass
		index+=1

"""
def main():
	ok = 1
	L = list()
	k = 1
	while(ok):
		bit = stdin.read(1)
		if bit == "0":
			if len(L):
				ans = solve(L)
				print("Case {} {} a tree.".format(k,ans))
				k+=1
				L.clear()
		elif bit == "-":
			ok = 0
		elif bit == '\n' or bit == '\r' or bit == " ":
			pass
		else:
			L.append(bit)
"""
main()