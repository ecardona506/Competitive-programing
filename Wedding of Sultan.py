from sys import stdin

def solve(path):
	global n, int_to_str, str_to_int
	sprinkles = list(set(path))
	tmp = [ord(i) for i in sprinkles]
	tmp.sort()
	n = len(sprinkles)
	for i in range(n):
		sprinkles[i] = chr(tmp[i])
	str_to_int, int_to_str, acum, G = {}, {}, {}, [[] for _ in range(n)]
	for i in range(n):
		acum[sprinkles[i]] = 0
		int_to_str[i] = sprinkles[i]
		str_to_int[sprinkles[i]] = i
	stack, u = [], 1
	stack.append(path[0])
	acum[path[0]] = 1
	while len(stack):
		if u < len(path):
			if acum[path[u]] == 0:
				acum[path[u]] += 1
				stack.append(path[u])
				u+=1
			elif acum[path[u]] == 0:
				acum[path[u]] += 1
				u+=1
			else:
				v = stack.pop()
				j = u
				if len(stack):
					G[str_to_int[stack[-1]]].append(v)
					G[str_to_int[v]].append(stack[-1])
				u+=1
	return G

def main():
	global n, str_to_int, int_to_str
	cases = int(stdin.readline().strip())
	for i in range(cases):
		path = list(stdin.readline().strip())
		ans = solve(path)
		print("Case {0}".format(i+1))
		for u in range(n):
			print("{0} = {1}".format(int_to_str[u],len(ans[u])))

main()