from sys import stdin

dict_bin = {0:'000',1:'001',2:'010',3:'011',4:'100',5:'101',6:'110',7:'111'}

def solve(state,i,ans):
	global digits,flag,n
	if i == 0:
		for j in digits[int(state[i])]:
			if not flag:
				ans[0:2],ans[-1] = dict_bin[j][1:3],dict_bin[j][0]
				solve(state,i+1,ans)
	elif i == n-2:
		for j in digits[int(state[i])]:
			if not flag and dict_bin[j] == ans[i-1] + ans[i] + ans[i+1]:
				for k in digits[int(state[i+1])]:
					if not flag and dict_bin[k][0:2] == ans[n-2] + ans[n-1] and ans[0] == dict_bin[k][2]:
						flag = 1	
	else:
		for j in digits[int(state[i])]:
			if not flag and dict_bin[j][0:2] == ans[i-1] + ans[i]:
				ans[i+1] = dict_bin[j][2]
				solve(state,i+1,ans)

def main():
	global digits,flag,n
	line = stdin.readline().split()
	while len(line):
		x,n,init = map(str,line)
		x,n = int(x),int(n)
		binary = bin(x)[2:]
		if len(binary) < 8: binary = '0'*(8-len(binary)) + binary
		digits = [[],[]]
		for i in range(8):
			if binary[i] == '0': digits[0].append(7-i)
			else: digits[1].append(7-i)
		tmp = [-1 for _ in range(n)]
		flag = 0
		solve(init,0,tmp)
		print('REACHABLE') if flag else print('GARDEN OF EDEN')
		flag = 0
		line = stdin.readline().split()

main()