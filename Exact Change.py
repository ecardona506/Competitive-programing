from sys import stdin

INF = float('inf')
"""

def phi(coins,price,i,ammount):
	global INF,budget,memo
	ans = None
	if (i,ammount) in memo: ans = memo[(i,ammount)]
	elif i == 0:
		if price > 0: ans = (INF,INF)
		else: ans = (ammount,coins)
	else:
		ans = min(phi(coins,price,i-1,ammount),phi(coins+1,price - budget[i-1],i-1,ammount + budget[i-1]))	
	memo[(i,ammount)] = ans
	return ans

def main():
	global budget,memo
	tc = int(stdin.readline().strip())
	while tc:
		price = int(stdin.readline().strip())
		n = int(stdin.readline().strip()) 
		budget = list()
		memo = {}
		for _ in range(n):
			x = int(stdin.readline().strip())
			budget.append(x)
		ans = phi(0,price,n,0)
		print(ans[0],ans[1])
		tc -=1
"""

def phi(price,i):
	global INF,budget
	if (price,i) in memo: ans = memo[(price,i)]
	elif i == 0:
		if price <= 0: ans = (0,0)
		else: ans = (INF,INF)
	else:
		tmp = phi(price-budget[i-1],i-1)
		ans = min(phi(price,i-1),(budget[i-1]+tmp[0],1+tmp[1]))
	memo[(price,i)] = ans
	return ans


def main():
	global budget,memo
	tc = int(stdin.readline().strip())
	while tc:
		price = int(stdin.readline().strip())
		n = int(stdin.readline().strip()) 
		budget = list()
		memo = {}
		for _ in range(n):
			x = int(stdin.readline().strip())
			budget.append(x)
		ans = phi(price,n)
		print(ans[0],ans[1])
		tc -=1

main()