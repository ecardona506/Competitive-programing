from sys import stdin
from collections import deque

INF = float('inf')

def to_num(t):
	return t[0]*1000+t[1]*100+t[2]*10+t[3]

def next_states(t):
	ans = []
	t = [int(x) for x in str(t)]
	n = len(t)
	if n != 4:
		aux = list()
		for i in range(4-n):
			aux.append(0)
		for i in range(n):
			aux.append(t[i])
		t = aux
	tmp = t.copy()
	for i in range(4):
		tmp[i] += 1
		if tmp[i] == 10:
			tmp[i] = 0
		ans.append(to_num(tmp))
		tmp = t.copy()
		tmp[i] -= 1
		if tmp[i] == -1:
			tmp[i] = 9
		ans.append(to_num(tmp))
		tmp = t.copy()
	return ans

def bfs(source, target):
	global visited
	dist = [INF for _ in range(10000)]
	queue = deque()
	queue.append(source); visited[source] = 1
	top,flag,dist = source, 0, 1
	while len(queue):
		u = queue.popleft()
		for v in next_states(u):
			if not flag:
				if(visited[v] == 0):
					queue.append(v); visited[v] = 1
				if target == v:
					queue.clear()
					flag = 1
		if u == top and len(queue):
			dist+=1
			top = queue[-1]
		visited[u] = 2
	if flag:
		return dist
	else:
		return -1

def main():
	global visited
	case = int(stdin.readline().strip())
	for k in range(case):
		line = stdin.readline().strip()
		flag = 1
		if len(line): 
			source = [int(x) for x in line.split()]
		else:
			source = [int(x) for x in stdin.readline().strip().split()]
		target = [int(x) for x in stdin.readline().strip().split()]
		if target == source:
			ans = 0
			flag = 0
		cnt = int(stdin.readline().strip())
		visited = [0 for _ in range(10000)]
		for i in range(cnt):
			forbidden = [int(x) for x in stdin.readline().strip().split()]
			visited[to_num(forbidden)] = 1
			if forbidden == target and flag: 
				flag = 0
				ans = -1
		if flag:
			ans = bfs(to_num(source),to_num(target))
		print(ans)

main()
